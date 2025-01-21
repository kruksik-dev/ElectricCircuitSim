from abc import ABC, abstractmethod
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from circuit_simulator.core import CircuitRL, SinusoidalGenerator, SquareWaveGenerator

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

    def plot(self, show: bool = True, save_fig: Path | None = None) -> None:
        if not self._results:
            print("No results to plot. Please analyze first.")
            return
        fig = self._create_plot()
        if save_fig:
            self._save_figure(fig, save_fig)
        if show:
            plt.show()

    def _create_plot(self) -> Figure:
        fig, ax = plt.subplots(figsize=(10, 6))
        for gen_name, data in self._results.items():
            time, voltage, current = zip(*data)
            ax.plot(time, voltage, label=f"{gen_name} - Voltage", linestyle="-")
            ax.plot(time, current, label=f"{gen_name} - Current", linestyle="--")

        ax.set_title("Circuit RL Analysis Results")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Magnitude (V or A)")
        ax.legend()
        return fig

    def _save_figure(self, fig: Figure, save_fig: Path) -> None:
        save_fig.mkdir(parents=True, exist_ok=True)
        if save_fig.suffix == "":
            save_fig = save_fig / "plot.jpg"
        fig.savefig(save_fig)
        print(f"Plot saved to {save_fig}")
