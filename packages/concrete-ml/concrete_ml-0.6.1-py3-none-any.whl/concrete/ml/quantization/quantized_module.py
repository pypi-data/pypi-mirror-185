"""QuantizedModule API."""
import copy
from typing import Any, Dict, Generator, Iterable, List, Optional, Tuple, Union

import numpy
from concrete.numpy.compilation.artifacts import DebugArtifacts
from concrete.numpy.compilation.circuit import Circuit
from concrete.numpy.compilation.compiler import Compiler
from concrete.numpy.compilation.configuration import Configuration

from ..common.debugging import assert_true
from ..common.utils import (
    check_there_is_no_p_error_options_in_configuration,
    generate_proxy_function,
    manage_parameters_for_pbs_errors,
)
from .base_quantized_op import QuantizedOp
from .quantizers import QuantizedArray, UniformQuantizer


def _raise_qat_import_error(bad_qat_ops: List[Tuple[str, str]]):
    """Raise a descriptive error if any invalid ops are present in the ONNX graph.

    Args:
        bad_qat_ops (List[Tuple[str, str]]): list of tensor names and operation types

    Raises:
        ValueError: if there were any invalid, non-quantized, tensors as inputs to non-fusable ops
    """

    raise ValueError(
        "Error occurred during quantization aware training (QAT) import: "
        "The following tensors were expected to be quantized, but the values "
        "found during calibration do not appear to be quantized. \n\n"
        + "\n".join(
            map(
                lambda info: f"* Tensor {info[0]}, input of an {info[1]} operation",
                bad_qat_ops,
            )
        )
        + "\n\nCould not determine a unique scale for the quantization! "
        "Please check the ONNX graph of this model."
    )


def _get_inputset_generator(
    q_inputs: Tuple[numpy.ndarray, ...], input_quantizers: List[UniformQuantizer]
) -> Generator:
    """Create an input set generator with proper dimensions.

    Args:
        q_inputs (numpy.ndarray): The quantized inputs
        input_quantizers (List[UniformQuantizer]): The input quantizers used on the input set

    Returns:
        Generator: The input set generator with proper dimensions.
    """
    if len(input_quantizers) > 1:
        return (
            tuple(numpy.expand_dims(q_input[idx], 0) for q_input in q_inputs)
            for idx in range(q_inputs[0].shape[0])
        )
    return (numpy.expand_dims(arr, 0) for arr in q_inputs[0])


class QuantizedModule:
    """Inference for a quantized model."""

    ordered_module_input_names: Tuple[str, ...]
    ordered_module_output_names: Tuple[str, ...]
    quant_layers_dict: Dict[str, Tuple[Tuple[str, ...], QuantizedOp]]
    input_quantizers: List[UniformQuantizer]
    output_quantizers: List[UniformQuantizer]
    forward_fhe: Union[None, Circuit]

    def __init__(
        self,
        ordered_module_input_names: Iterable[str] = None,
        ordered_module_output_names: Iterable[str] = None,
        quant_layers_dict: Dict[str, Tuple[Tuple[str, ...], QuantizedOp]] = None,
    ):
        # If any of the arguments are not provided, skip the init
        if not all([ordered_module_input_names, ordered_module_output_names, quant_layers_dict]):
            return

        # for mypy
        assert isinstance(ordered_module_input_names, Iterable)
        assert isinstance(ordered_module_output_names, Iterable)
        assert all([ordered_module_input_names, ordered_module_output_names, quant_layers_dict])
        self.ordered_module_input_names = tuple(ordered_module_input_names)
        self.ordered_module_output_names = tuple(ordered_module_output_names)

        num_outputs = len(self.ordered_module_output_names)
        assert_true(
            (num_outputs) == 1,
            f"{QuantizedModule.__class__.__name__} only supports a single output for now, "
            f"got {num_outputs}",
        )

        assert quant_layers_dict is not None
        self.quant_layers_dict = copy.deepcopy(quant_layers_dict)
        self._is_compiled = False
        self.forward_fhe = None
        self.input_quantizers = []
        self.output_quantizers = self._set_output_quantizers()
        self._onnx_model = None
        self._post_processing_params: Dict[str, Any] = {}

    @property
    def is_compiled(self) -> bool:
        """Return the compiled status of the module.

        Returns:
            bool: the compiled status of the module.
        """
        return self._is_compiled

    @property
    def fhe_circuit(self) -> Circuit:
        """Get the FHE circuit.

        Returns:
            Circuit: the FHE circuit
        """
        return self.forward_fhe

    @fhe_circuit.setter
    def fhe_circuit(self, fhe_circuit: Circuit):
        """Set the FHE circuit.

        Args:
            fhe_circuit (Circuit): the FHE circuit
        """
        self.forward_fhe = fhe_circuit
        self._is_compiled = True

    @property
    def post_processing_params(self) -> Dict[str, Any]:
        """Get the post-processing parameters.

        Returns:
            Dict[str, Any]: the post-processing parameters
        """
        return self._post_processing_params

    @post_processing_params.setter
    def post_processing_params(self, post_processing_params: Dict[str, Any]):
        """Set the post-processing parameters.

        Args:
            post_processing_params (dict): the post-processing parameters
        """
        self._post_processing_params = post_processing_params

    def post_processing(self, qvalues: numpy.ndarray) -> numpy.ndarray:
        """Post-processing of the quantized output.

        Args:
            qvalues (numpy.ndarray): numpy.ndarray containing the quantized input values.

        Returns:
            (numpy.ndarray): Predictions of the quantized model
        """
        return self.dequantize_output(qvalues)

    def _set_output_quantizers(self) -> List[UniformQuantizer]:
        """Get the output quantizers.

        Returns:
            List[UniformQuantizer]: List of output quantizers.
        """
        output_layers = (
            self.quant_layers_dict[output_name][1]
            for output_name in self.ordered_module_output_names
        )
        output_quantizers = list(
            QuantizedArray(
                output_layer.n_bits,
                values=None,
                value_is_float=False,
                stats=output_layer.output_quant_stats,
                params=output_layer.output_quant_params,
            ).quantizer
            for output_layer in output_layers
        )
        return output_quantizers

    @property
    def onnx_model(self):
        """Get the ONNX model.

        .. # noqa: DAR201

        Returns:
           _onnx_model (onnx.ModelProto): the ONNX model
        """
        return self._onnx_model

    @onnx_model.setter
    def onnx_model(self, value):
        self._onnx_model = value

    def __call__(self, *x: numpy.ndarray):
        return self.forward(*x)

    def forward(
        self, *qvalues: numpy.ndarray, debug: bool = False
    ) -> Union[numpy.ndarray, Tuple[numpy.ndarray, Dict[str, numpy.ndarray]]]:
        """Forward pass with numpy function only.

        Args:
            *qvalues (numpy.ndarray): numpy.array containing the quantized values.
            debug (bool): In debug mode, returns quantized intermediary values of the computation.
                          This is useful when a model's intermediary values in Concrete-ML need
                          to be compared with the intermediary values obtained in pytorch/onnx.
                          When set, the second return value is a dictionary containing ONNX
                          operation names as keys and, as values, their input QuantizedArray or
                          ndarray. The use can thus extract the quantized or float values of
                          quantized inputs.

        Returns:
            (numpy.ndarray): Predictions of the quantized model
        """
        # Make sure that the input is quantized
        invalid_inputs = tuple(
            (idx, qvalue)
            for idx, qvalue in enumerate(qvalues)
            if not issubclass(qvalue.dtype.type, numpy.integer)
        )
        assert_true(
            len(invalid_inputs) == 0,
            f"Inputs: {', '.join(f'#{val[0]} ({val[1].dtype})' for val in invalid_inputs)} are not "
            "integer types. Make sure you quantize your input before calling forward.",
            ValueError,
        )

        if debug:
            debug_value_tracker: Dict[str, Any] = {}
            for (_, layer) in self.quant_layers_dict.values():
                layer.debug_value_tracker = debug_value_tracker
            result = self._forward(*qvalues)
            for (_, layer) in self.quant_layers_dict.values():
                layer.debug_value_tracker = None
            return result, debug_value_tracker

        return self._forward(*qvalues)

    def _forward(self, *qvalues: numpy.ndarray) -> numpy.ndarray:
        """Forward function for the FHE circuit.

        Args:
            *qvalues (numpy.ndarray): numpy.array containing the quantized values.

        Returns:
            (numpy.ndarray): Predictions of the quantized model

        """

        n_qinputs = len(self.input_quantizers)
        n_qvalues = len(qvalues) == n_qinputs
        assert_true(
            n_qvalues,
            f"Got {n_qvalues} inputs, expected {n_qinputs}",
            TypeError,
        )

        q_inputs = [
            QuantizedArray(
                self.input_quantizers[idx].n_bits,
                qvalues[idx],
                value_is_float=False,
                options=self.input_quantizers[idx].quant_options,
                stats=self.input_quantizers[idx].quant_stats,
                params=self.input_quantizers[idx].quant_params,
            )
            for idx in range(len(self.input_quantizers))
        ]

        # Init layer_results with the inputs
        layer_results = dict(zip(self.ordered_module_input_names, q_inputs))

        bad_qat_ops: List[Tuple[str, str]] = []
        for output_name, (input_names, layer) in self.quant_layers_dict.items():
            inputs = (layer_results[input_name] for input_name in input_names)

            error_tracker: List[int] = []
            layer.error_tracker = error_tracker
            output = layer(*inputs)
            layer.error_tracker = None

            if len(error_tracker) > 0:
                # The error message contains the ONNX tensor name that
                # triggered this error
                for input_idx in error_tracker:
                    bad_qat_ops.append((input_names[input_idx], layer.__class__.op_type()))

            layer_results[output_name] = output

        if len(bad_qat_ops) > 0:
            _raise_qat_import_error(bad_qat_ops)

        outputs = tuple(
            layer_results[output_name] for output_name in self.ordered_module_output_names
        )

        assert_true(len(outputs) == 1)

        return outputs[0].qvalues

    def forward_and_dequant(self, *q_x: numpy.ndarray) -> numpy.ndarray:
        """Forward pass with numpy function only plus dequantization.

        Args:
            *q_x (numpy.ndarray): numpy.ndarray containing the quantized input values. Requires the
                input dtype to be int64.

        Returns:
            (numpy.ndarray): Predictions of the quantized model
        """
        q_out = self.forward(*q_x)
        return self.dequantize_output(q_out)  # type: ignore

    def quantize_input(
        self, *values: numpy.ndarray
    ) -> Union[numpy.ndarray, Tuple[numpy.ndarray, ...]]:
        """Take the inputs in fp32 and quantize it using the learned quantization parameters.

        Args:
            *values (numpy.ndarray): Floating point values.

        Returns:
            Union[numpy.ndarray, Tuple[numpy.ndarray, ...]]: Quantized (numpy.int64) values.
        """
        n_qinputs = len(self.input_quantizers)
        n_values = len(values) == n_qinputs
        assert_true(
            n_values,
            f"Got {n_values} inputs, expected {n_qinputs}",
            TypeError,
        )

        qvalues = tuple(self.input_quantizers[idx].quant(values[idx]) for idx in range(len(values)))

        return qvalues[0] if len(qvalues) == 1 else qvalues

    def dequantize_output(self, qvalues: numpy.ndarray) -> numpy.ndarray:
        """Take the last layer q_out and use its dequant function.

        Args:
            qvalues (numpy.ndarray): Quantized values of the last layer.

        Returns:
            numpy.ndarray: Dequantized values of the last layer.
        """
        real_values = tuple(
            output_quantizer.dequant(qvalues) for output_quantizer in self.output_quantizers
        )

        assert_true(len(real_values) == 1)

        return real_values[0]

    def set_inputs_quantization_parameters(self, *input_q_params: UniformQuantizer):
        """Set the quantization parameters for the module's inputs.

        Args:
            *input_q_params (UniformQuantizer): The quantizer(s) for the module.
        """
        n_inputs = len(self.ordered_module_input_names)
        n_values = len(input_q_params)
        assert_true(
            n_values == n_inputs,
            f"Got {n_values} inputs, expected {n_inputs}",
            TypeError,
        )

        self.input_quantizers.clear()
        self.input_quantizers.extend(copy.deepcopy(q_params) for q_params in input_q_params)

    def compile(
        self,
        q_inputs: Union[Tuple[numpy.ndarray, ...], numpy.ndarray],
        configuration: Optional[Configuration] = None,
        compilation_artifacts: Optional[DebugArtifacts] = None,
        show_mlir: bool = False,
        use_virtual_lib: bool = False,
        p_error: Optional[float] = None,
        global_p_error: Optional[float] = None,
        verbose_compilation: bool = False,
    ) -> Circuit:
        """Compile the forward function of the module.

        Args:
            q_inputs (Union[Tuple[numpy.ndarray, ...], numpy.ndarray]): Needed for tracing and
                building the boundaries.
            configuration (Optional[Configuration]): Configuration object to use during compilation
            compilation_artifacts (Optional[DebugArtifacts]): Artifacts object to fill during
            show_mlir (bool): if set, the MLIR produced by the converter and which is
                going to be sent to the compiler backend is shown on the screen, e.g., for debugging
                or demo. Defaults to False.
            use_virtual_lib (bool): set to use the so called virtual lib simulating FHE computation.
                Defaults to False.
            p_error (Optional[float]): probability of error of a single PBS.
            global_p_error (Optional[float]): probability of error of the full circuit. Not
                simulated by the VL, i.e., taken as 0
            verbose_compilation (bool): whether to show compilation information

        Returns:
            Circuit: the compiled Circuit.
        """

        if not isinstance(q_inputs, tuple):
            q_inputs = (q_inputs,)
        else:
            ref_len = q_inputs[0].shape[0]
            assert_true(
                all(q_input.shape[0] == ref_len for q_input in q_inputs),
                "Mismatched dataset lengths",
            )

        # concrete-numpy does not support variable *args-style functions, so compile a proxy
        # function dynamically with a suitable number of arguments
        forward_proxy, orig_args_to_proxy_func_args = generate_proxy_function(
            self._forward, self.ordered_module_input_names
        )

        compiler = Compiler(
            forward_proxy,
            {arg_name: "encrypted" for arg_name in orig_args_to_proxy_func_args.values()},
        )

        inputset = _get_inputset_generator(q_inputs, self.input_quantizers)

        # Don't let the user shoot in her foot, by having p_error or global_p_error set in both
        # configuration and in direct arguments
        check_there_is_no_p_error_options_in_configuration(configuration)

        # Find the right way to set parameters for compiler, depending on the way we want to default
        p_error, global_p_error = manage_parameters_for_pbs_errors(p_error, global_p_error)

        self.forward_fhe = compiler.compile(
            inputset,
            configuration,
            compilation_artifacts,
            show_mlir=show_mlir,
            virtual=use_virtual_lib,
            p_error=p_error,
            global_p_error=global_p_error,
            verbose=verbose_compilation,
        )

        self._is_compiled = True

        return self.forward_fhe
