from pathlib import Path
import tempfile
from unittest.mock import MagicMock
import pytest
from ElectricCircuitSim.analyze.analyzer import CircuitRLAnalyzer
from ElectricCircuitSim.core import CircuitRL, SinusoidalGenerator, SquareWaveGenerator


@pytest.fixture
def circuit() -> CircuitRL:
    return CircuitRL(resistance=1.0, inductance=1.0, initialCurrent=0.0)


@pytest.fixture
def sinusoidal_generator() -> SinusoidalGenerator:
    return SinusoidalGenerator(frequency=1.0, amplitude=1.0, phase=0.0)


@pytest.fixture
def square_wave_generator() -> SquareWaveGenerator:
    return SquareWaveGenerator(frequency=1.0, amplitude=1.0)


@pytest.mark.parametrize(
    "generator_name, generator_fixture",
    [
        ("sinusoidal", "sinusoidal_generator"),
        ("square_wave", "square_wave_generator"),
    ],
)
def test_add_generator(generator_name: str, generator_fixture: str, request: pytest.FixtureRequest) -> None:
    generator = request.getfixturevalue(generator_fixture)
    analyzer = CircuitRLAnalyzer()
    analyzer.add_generator(generator_name, generator)
    assert generator_name in analyzer.generators
    assert analyzer.generators[generator_name] == generator


def test_remove_generator(sinusoidal_generator: SinusoidalGenerator) -> None:
    analyzer = CircuitRLAnalyzer(generators={"sinusoidal": sinusoidal_generator})
    analyzer.remove_generator("sinusoidal")
    assert "sinusoidal" not in analyzer.generators


def test_set_circuit(circuit: CircuitRL) -> None:
    analyzer = CircuitRLAnalyzer()
    analyzer.circuit = circuit
    assert analyzer.circuit == circuit


def test_analyze(circuit, sinusoidal_generator: SinusoidalGenerator) -> None:
    analyzer = CircuitRLAnalyzer(
        generators={"sinusoidal": sinusoidal_generator}, circuit=circuit
    )
    analyzer.analyze(1.0, 0.25)
    assert "sinusoidal" in analyzer.results
    assert len(analyzer.results["sinusoidal"]) > 0


def test_analyze_no_circuit(sinusoidal_generator: SinusoidalGenerator) -> None:
    analyzer = CircuitRLAnalyzer(generators={"sinusoidal": sinusoidal_generator})
    analyzer.analyze(end_time=1.0, step=0.25)
    assert analyzer.results == {}


def test_plot_results(circuit: CircuitRL, sinusoidal_generator: SinusoidalGenerator, mocker: MagicMock) -> None:
    analyzer = CircuitRLAnalyzer(
        generators={"sinusoidal": sinusoidal_generator}, circuit=circuit
    )
    analyzer.analyze(end_time=1.0, step=0.25)
    mock_show = mocker.patch("matplotlib.pyplot.show")
    analyzer.plot_results(show=True)
    mock_show.assert_called_once()


def test_save_figure(circuit: CircuitRL, sinusoidal_generator: SinusoidalGenerator) -> None:
    analyzer = CircuitRLAnalyzer(
        generators={"sinusoidal": sinusoidal_generator}, circuit=circuit
    )
    analyzer.analyze(end_time=1.0, step=0.25)
    with tempfile.TemporaryDirectory() as tmp_dir:
        save_path_1 = Path(tmp_dir) / "results.png"
        analyzer.plot_results(show=False, save_fig=save_path_1)
        assert save_path_1.exists()
        save_path_2 = Path(tmp_dir)
        analyzer.plot_results(show=False, save_fig=save_path_2)
        assert (save_path_2 / "plot.png").exists()
