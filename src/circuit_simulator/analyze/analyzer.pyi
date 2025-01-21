from abc import ABC
from pathlib import Path
from circuit_simulator.core import SquareWaveGenerator, SinusoidalGenerator, CircuitRL

GeneratorType = SquareWaveGenerator | SinusoidalGenerator


class AbstractAnalyzer(ABC):
    def plot_results(self) -> None: ...
    def analyze(self) -> None: ...


class CircuitRLAnalyzer(AbstractAnalyzer):
    def __init__(
        self,
        generators: dict[str, GeneratorType] | None = None,
        circuit: CircuitRL | None = None,
    ) -> None: ...
    def add_generator(self, name: str, generator: GeneratorType) -> None: ...
    def remove_generator(self, name: str) -> None: ...
    def set_circuit(self, circuit: CircuitRL) -> None: ...
    def analyze(self, end_time: float, step: float, name: str | list[str] | None = None) -> None: ...
    def plot_results(self, show: bool = True, save_fig: Path | None = None) -> None: ...
