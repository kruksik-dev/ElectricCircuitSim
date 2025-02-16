class Generator:
    def calculateVoltage(self, time: float) -> float: ...

class Circuit:
    def simulate(
        self, generator: Generator, t_end: float, dt: float
    ) -> list[tuple[float, float, float]]: ...

class SinusoidalGenerator(Generator):
    def __init__(
        self, frequency: float, amplitude: float, phase: float = 0.0
    ) -> None: ...
    def calculateVoltage(self, time: float) -> float: ...

class SquareWaveGenerator(Generator):
    def __init__(self, frequency: float, amplitude: float) -> None: ...
    def calculateVoltage(self, time: float) -> float: ...

class CircuitRL(Circuit):
    def __init__(
        self, resistance: float, inductance: float, initialCurrent: float = 0.0
    ) -> None: ...
    def simulate(
        self, generator: Generator, t_end: float, dt: float
    ) -> list[tuple[float, float, float]]: ...
