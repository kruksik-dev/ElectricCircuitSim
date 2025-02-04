Examples
========

Example 1: Creating Generators
------------------------------
This section demonstrates how to create different types of generators and call their functions.

.. code-block:: python

    from ElectricCircuitSim.core import SinusoidalGenerator, SquareWaveGenerator

    # Create a sinusoidal generator
    sinusoidal_gen = SinusoidalGenerator(frequency=50, amplitude=10)
    voltage_at_t1 = sinusoidal_gen.calculateVoltage(time=1.0)
    print(f"Sinusoidal Generator Voltage at t=1.0s: {voltage_at_t1:.2f}V")

    # Create a square wave generator
    square_wave_gen = SquareWaveGenerator(frequency=50, amplitude=10)
    voltage_at_t1 = square_wave_gen.calculateVoltage(time=1.0)
    print(f"Square Wave Generator Voltage at t=1.0s: {voltage_at_t1:.2f}V")

Example 2: Simple RL Circuit with Sinusoidal Generator and Square Wave Generator
--------------------------------------------------------------------------------
This example demonstrates a simple RL circuit with a sinusoidal generator.

.. code-block:: python

    from ElectricCircuitSim.core import CircuitRL, SinusoidalGenerator

    # Create a sinusoidal generator
    generator_sin = SinusoidalGenerator(frequency=50, amplitude=10)

    # Create an RL circuit
    circuit = CircuitRL(resistance=10, inductance=0.1)

    # Simulate the circuit
    results = circuit.simulate(generator_sin, t_end=1.0, dt=0.01)

    # Print the results
    for time, voltage, current in results:
        print(f"Time: {time:.2f}s, Voltage: {voltage:.2f}V, Current: {current:.2f}A")

    # Create a square wave generator
    generator_square = SquareWaveGenerator(frequency=50, amplitude=10)

    # Simulate the circuit
    results = circuit.simulate(generator_square, t_end=1.0, dt=0.01)

    # Print the results
    for time, voltage, current in results:
        print(f"Time: {time:.2f}s, Voltage: {voltage:.2f}V, Current: {current:.2f}A")

Example 3: Using CircuitRLAnalyzer
----------------------------------
This section demonstrates how to use the `CircuitRLAnalyzer` to analyze and plot results, and save the plot to a file.

.. code-block:: python

    from ElectricCircuitSim.analyze import CircuitRLAnalyzer
    from ElectricCircuitSim.core import CircuitRL, SinusoidalGenerator, SquareWaveGenerator
    from pathlib import Path

    # Create generators
    sinusoidal_gen = SinusoidalGenerator(frequency=50, amplitude=10)
    square_wave_gen = SquareWaveGenerator(frequency=50, amplitude=10)

    # Create an RL circuit
    circuit = CircuitRL(resistance=10, inductance=0.1)

    # Initialize the analyzer with the circuit and generators
    analyzer = CircuitRLAnalyzer(
        generators={"sinusoidal": sinusoidal_gen, "square_wave": square_wave_gen},
        circuit=circuit
    )

    # Perform the analysis
    analyzer.analyze(end_time=1.0, step=0.01)

    # Plot the results
    analyzer.plot_results(show=True)

    # Save the plot to a file
    save_path = Path("analysis_results/plot.png")
    analyzer.plot_results(show=False, save_fig=save_path)
