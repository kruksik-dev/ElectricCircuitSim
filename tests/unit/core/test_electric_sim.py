import pytest

from circuit_simulator.core import CircuitRL, SinusoidalGenerator, SquareWaveGenerator


@pytest.mark.parametrize(
    "frequency, amplitude, phase, time, expected_voltage",
    [
        (1.0, 1.0, 0.0, 0.0, 0.0),  # sin(0) = 0
        (1.0, 1.0, 0.0, 0.25, 1.0),  # sin(pi/2) = 1
        (1.0, 1.0, 0.0, 0.5, 0.0),  # sin(pi) = 0
        (1.0, 1.0, 0.0, 0.75, -1.0),  # sin(3pi/2) = -1
        (1.0, 1.0, 0.0, 1.0, 0.0),  # sin(2pi) = 0
    ],
)
def test_sinusoidal_generator(
    frequency: float,
    amplitude: float,
    phase: float,
    time: float,
    expected_voltage: float,
) -> None:
    generator = SinusoidalGenerator(frequency=frequency, amplitude=amplitude, phase=phase)
    voltage = generator.calculateVoltage(time)
    assert pytest.approx(voltage, 0.01) == expected_voltage


@pytest.mark.parametrize(
    "frequency, amplitude, time, expected_voltage",
    [
        (1.0, 1.0, 0.0, 1.0),  # square wave at t=0
        (1.0, 1.0, 0.25, 1.0),  # square wave at t=T/4
        (1.0, 1.0, 0.5, -1.0),  # square wave at t=T/2
        (1.0, 1.0, 0.75, -1.0),  # square wave at t=3T/4
        (1.0, 1.0, 1.0, 1.0),  # square wave at t=T
    ],
)
def test_square_wave_generator(
    frequency: float, amplitude: float, time: float, expected_voltage: float
) -> None:
    generator = SquareWaveGenerator(frequency=frequency, amplitude=amplitude)
    voltage = generator.calculateVoltage(time)
    assert pytest.approx(voltage, 0.01) == expected_voltage


@pytest.mark.parametrize(
    "resistance, inductance, current, generator, t_end, dt, expected_simulation",
    [
        (
            1.0,
            1.0,
            0.0,
            SinusoidalGenerator(frequency=1.0, amplitude=1.0),
            1.0,
            0.25,
            [
                (0.0, 0.0, 0.0),
                (0.25, 1.0, 0.25),
                (0.5, 1e-16, 0.187),
                (0.75, -1.0, -0.109),
                (1.0, -2e-16, -0.082),
            ],
        ),
        (
            1.0,
            1.0,
            0.0,
            SquareWaveGenerator(frequency=1.0, amplitude=1.0),
            1.0,
            0.25,
            [
                (0.0, 1.0, 0.25),
                (0.25, 1.0, 0.437),
                (0.5, -1.0, 0.078),
                (0.75, -1.0, -0.191),
                (1.0, 1.0, 0.106),
            ],
        ),
    ],
)
def test_circuit_rl(
    resistance: float,
    inductance: float,
    current: float,
    generator: SinusoidalGenerator,
    t_end: float,
    dt: float,
    expected_simulation: list[tuple[float, float, float]],
) -> None:
    circuit = CircuitRL(
        resistance=resistance, inductance=inductance, initialCurrent=current
    )
    simulation = circuit.simulate(generator=generator, t_end=t_end, dt=dt)
    for sim, expected in zip(simulation, expected_simulation):
        for i in range(3):
            assert sim[i] == pytest.approx(expected[i], rel=1e-2)
