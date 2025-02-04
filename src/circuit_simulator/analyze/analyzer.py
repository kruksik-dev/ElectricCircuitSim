from abc import ABC, abstractmethod
from os import path
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from circuit_simulator.core import CircuitRL, SinusoidalGenerator, SquareWaveGenerator

GeneratorType = SquareWaveGenerator | SinusoidalGenerator


class AbstractAnalyzer(ABC):
    """Abstract base class for analyzers."""

    @abstractmethod
    def plot_results(self) -> None:
        """Plots the analysis results."""
        pass

    @abstractmethod
    def analyze(self) -> None:
        """Performs the analysis."""
        pass


class CircuitRLAnalyzer(AbstractAnalyzer):
    """Analyzer for RL circuits."""

    def __init__(
        self,
        generators: dict[str, GeneratorType] | None = None,
        circuit: CircuitRL | None = None,
    ) -> None:
        """Initializes the CircuitRLAnalyzer.

        Args:
            generators (dict[str, GeneratorType] | None, optional): Generators for the circuit. Defaults to None.
            circuit (CircuitRL | None, optional): Circuit to be analyzed. Defaults to None.
        """
        self._generators: dict[str, GeneratorType] = (
            generators if generators is not None else {}
        )
        self._circuit: CircuitRL | None = circuit
        self._results: dict[str, list[tuple[float, float, float]]] = {}

    @property
    def generators(self) -> dict[str, GeneratorType]:
        """Returns the generators.

        Returns:
            dict[str, GeneratorType]: Dictionary of generators.
        """
        return self._generators

    @property
    def results(self) -> dict[str, list[tuple[float, float, float]]]:
        """Returns the analysis results.

        Returns:
            dict[str, list[tuple[float, float, float]]]: Analysis results.
        """
        return self._results

    @property
    def circuit(self) -> CircuitRL | None:
        """Returns the circuit.

        Returns:
            CircuitRL | None: The RL circuit.
        """
        return self._circuit

    @circuit.setter
    def circuit(self, value: CircuitRL) -> None:
        """Sets the circuit.

        Args:
            value (CircuitRL): The RL circuit to be set.
        """
        self._circuit = value
        print("Circuit set")

    def add_generator(self, name: str, generator: GeneratorType) -> None:
        """Adds a generator to the analyzer.

        Args:
            name (str): Name of the generator.
            generator (GeneratorType): The generator instance.
        """
        self._generators[name] = generator
        print(f"Generator {name} added")

    def remove_generator(self, name: str) -> None:
        """Removes a generator from the analyzer.

        Args:
            name (str): Name of the generator.

        Raises:
            ValueError: If the generator is not found.
        """
        if name not in self._generators:
            raise ValueError(f"Generator {name} not found")
        del self._generators[name]
        print(f"Generator {name} removed")

    def analyze(
        self, end_time: float, step: float, name: str | list[str] | None = None
    ) -> None:
        """Performs the circuit analysis.

        Args:
            end_time (float): The end time of the simulation.
            step (float): The time step for the simulation.
            name (str | list[str] | None, optional): Specific generator(s) to analyze.
            Defaults to None (analyzes all generators).
        """
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
        """Plots the analysis results.

        Args:
            show (bool, optional): Whether to display the plot. Defaults to True.
            save_fig (Path | None, optional): Path to save the figure. Defaults to None.
        """
        if not self._results:
            print("No results to plot. Please analyze first.")
            return
        fig = self._create_plot()
        if save_fig:
            self._save_figure(fig, save_fig)
        if show:
            plt.show()

    def _create_plot(self) -> Figure:
        """Creates a plot of the results.

        Returns:
            Figure: The generated matplotlib figure.
        """
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
        """Saves the plot to a file.

        Args:
            fig (Figure): The matplotlib figure to save.
            save_fig (Path): The file path to save the figure.
        """
        if not path.exists(save_fig.parent):
            save_fig.mkdir(parents=True, exist_ok=True)
        if save_fig.suffix == "":
            save_fig = save_fig / "plot.png"
            save_fig = save_fig / "plot.png"
        fig.savefig(save_fig)
        print(f"Plot saved to {save_fig}")
