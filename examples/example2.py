from ElectricCircuitSim.analyze import CircuitRLAnalyzer
from ElectricCircuitSim.core import CircuitRL, SinusoidalGenerator, SquareWaveGenerator

# Create generators
sin_gen = SinusoidalGenerator(frequency=0.25, amplitude=0.5)
square_gen = SquareWaveGenerator(frequency=0.2, amplitude=0.2)

# Create RL circuit
circuit = CircuitRL(resistance=0.5, inductance=15)

# Create analyzer
analyzer = CircuitRLAnalyzer(
    generators={"sin": sin_gen, "square": square_gen}, circuit=circuit
)

# Analyze the circuit
analyzer.analyze(end_time=10.0, step=0.1)

# Plot the results
analyzer.plot_results()
