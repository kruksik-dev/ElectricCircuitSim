
# Electric Circuit Simulator

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📚 Overview

**Electric Circuit Simulator** is a powerful Python package for simulating **electrical circuits** and **generators**. It supports both **sinusoidal** and **square wave generators**, as well as **RL circuit simulations**. The core calculations are written in **C++** for optimal performance, and Python bindings are provided using `pybind11` for easy integration.

This tool allows you to simulate, analyze, and visualize the behavior of **resistive-inductive (RL) circuits** powered by different signal generators.



## 🧮 Mathematical Explanation

### Sinusoidal Generator

The voltage $V(t)$ generated by a sinusoidal generator is given by the equation:

$$
V(t) = A \sin(2 \pi f t + \phi)
$$

Where:
- $ A $ is the **amplitude**
- $ f $ is the **frequency**
- $ \phi $ is the **phase**
- $ t $ is **time**

### Square Wave Generator

The voltage $ V(t) $ produced by a square wave generator is:

$$V(t) = \begin{cases} A & \text{if } \mod(t, T) < \frac{T}{2} \\ -A & \text{otherwise} \end{cases}$$

Where:
- $ A $ is the **amplitude**
- $ T $ is the **period** (with $ T = \frac{1}{f} $)
- $ f $ is the **frequency**
- $ t $ is **time**

### RL Circuit Simulation

The RL circuit's behavior is governed by the differential equation:

$$
V(t) = L \frac{dI(t)}{dt} + R I(t)
$$

Where:
- $ V(t) $ is the **voltage** from the generator
- $ I(t) $ is the **current** flowing through the circuit
- $ L $ is the **inductance**
- $ R $ is the **resistance**

This equation is solved iteratively using the **Euler method** for simulation.



## 🛠 Package Contents

- **core**: C++ bindings for generators and circuit simulation.
- **analyze**: Tools for analyzing and visualizing simulation results.



## 📦 Installation

### From PyPI

Install the package directly from PyPI:

```bash
pip install XXXXXX
```

### From Source

To install from the source, follow these steps:

```bash
git clone https://github.com/yourusername/electric-circuit-simulator.git
cd electric-circuit-simulator
python -m venv .venv
source .venv/bin/activate
pip install .
```

---

## 🧑‍💻 Usage Example

Here’s how you can use the Electric Circuit Simulator to analyze an RL circuit with different generators.

#Example 1
```python

from circuit_simulator.core import CircuitRL, SquareWaveGenerator

# Create generator
square_gen = SquareWaveGenerator(frequency=0.5, amplitude=0.5)

# Create RL circuit
circuit = CircuitRL(resistance=1, inductance=5)

# Simulate Circuit
result = circuit.simulate(generator=square_gen, t_end=1, dt=0.1)

# Print result
print(result) # [(0.0, 0.5, 0.010000000000000002), (0.1, 0.5, 0.019800000000000005), (0.2, 0.5, 0.029404000000000007), ...]

```
#Example 2
```python


from circuit_simulator.analyze import CircuitRLAnalyzer
from circuit_simulator.core import CircuitRL, SinusoidalGenerator, SquareWaveGenerator

# Create generators
sin_gen = SinusoidalGenerator(frequency=0.25, amplitude=0.5)
square_gen = SquareWaveGenerator(frequency=0.2, amplitude=0.2)

# Create RL circuit
circuit = CircuitRL(resistance=0.5, inductance=15)

# Create analyzer
analyzer = CircuitRLAnalyzer(generators={"sin": sin_gen, "square": square_gen}, circuit=circuit)

# Analyze the circuit
analyzer.analyze(end_time=10.0, step=0.1)

# Plot the results
analyzer.plot_results()
```



## 🚀 Features

- **High Performance**: Core computations are implemented in C++ for maximum performance.
- **Python Bindings**: Seamless Python API provided by `pybind11`.
- **Flexible Generators**: Includes both **sinusoidal** and **square wave** generators for different testing conditions.
- **RL Circuit Simulation**: Simulate the response of an **RL circuit** under varying conditions.
- **Analysis Tools**: Built-in functionality for analyzing and plotting the simulation results.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🤝 Contributing

We welcome contributions! If you'd like to contribute to **Electric Circuit Simulator**, please feel free to:

1. Fork the repository
2. Make your changes
3. Submit a **pull request**

For any issues or feature requests, please open an issue in the repository.

---

## 💡 Additional Information

The **Electric Circuit Simulator** is ideal for educational purposes, research, and testing different electrical circuits using realistic signal generators. It provides a robust and easy-to-use platform for simulating real-world electrical systems.
