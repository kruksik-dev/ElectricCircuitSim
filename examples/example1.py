from ElectricCircuitSim.core import CircuitRL, SquareWaveGenerator

# Create generator
square_gen = SquareWaveGenerator(frequency=0.5, amplitude=0.5)

# Create RL circuit
circuit = CircuitRL(resistance=1, inductance=5)

# Simulate Circuit
result = circuit.simulate(generator=square_gen, t_end=1, dt=0.1)

# Print result
print(result)
