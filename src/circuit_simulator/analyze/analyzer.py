from abc import ABC, abstractmethod
from pathlib import Path
import matplotlib.pyplot as plt
from circuit_simulator.core import SinusoidalGenerator, SquareWaveGenerator, CircuitRL

GeneratorType = SquareWaveGenerator | SinusoidalGenerator


class AbstractAnalyzer(ABC):
    @abstractmethod
    def plot_results(self) -> None:
        pass

    @abstractmethod
    def analyze(self) -> None:
        pass


class CircuitRLAnalyzer(AbstractAnalyzer):

    def __init__(
        self,
        generators: dict[str, GeneratorType] | None = None,
        circuit: CircuitRL | None = None,
    ) -> None:
        self._generators: dict[str, GeneratorType] = (
            generators if generators is not None else {}
        )
        self._circuit: CircuitRL | None = circuit
        self._results: dict[str, list[tuple[float, float, float]]] = {}

    def add_generator(self, name: str, generator: GeneratorType) -> None:
        self._generators[name] = generator
        print(f"Generator {name} added")

    def remove_generator(self, name: str) -> None:
        if name not in self._generators:
            raise ValueError(f"Generator {name} not found")
        del self._generators[name]
        print(f"Generator {name} removed")

    def set_circuit(self, circuit: CircuitRL) -> None:
        self._circuit = circuit
        print("Circuit set")

    def analyze(
        self, end_time: float, step: float, name: str | list[str] | None = None
    ) -> None:
        if self._circuit is None:
            print("No circuit set. Please set a circuit before analyzing.")
            self._results = {}
            return

        names_to_analyze = [name] if isinstance(name, str) else name
        if names_to_analyze is None:
            names_to_analyze = list(self._generators.keys())

        result: dict[str, list[tuple[float, float, float]]] = {}
        for gen_name in names_to_analyze:
            if gen_name not in self._generators:
                print(f"Generator {gen_name} not found")
                continue

            generator = self._generators[gen_name]
            result[gen_name] = self._circuit.simulate(generator, end_time, step)
        self._results = result

    def plot_results(self, show: bool = True, save_fig: Path | None = None) -> None:
        if not self._results:
            print("No results to plot. Please analyze first.")
            return

        plt.figure(figsize=(10, 6))
        for gen_name, data in self._results.items():
            time, voltage, current = zip(*data)
            plt.plot(time, voltage, label=f'{gen_name} - Voltage', linestyle='-')
            plt.plot(time, current, label=f'{gen_name} - Current', linestyle='--')

        plt.title("Circuit RL Analysis Results")
        plt.xlabel("Time (s)")
        plt.ylabel("Magnitude (V or A)")
        plt.legend()

        if save_fig:
            plt.savefig(save_fig)
            print(f"Plot saved to {save_fig}")

        if show:
            plt.show()
