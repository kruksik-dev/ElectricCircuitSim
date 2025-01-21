#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/chrono.h>
#include "../include/sinusoidal_generator.h"
#include "../include/square_wave_generator.h"
#include "../include/circuit_rl.h"

namespace py = pybind11;

PYBIND11_MODULE(_electric_sim, m)
{
    m.doc() = R"pbdoc(
        Electric Simulation Module

        This module provides tools for simulating electrical circuits and generators.
        It includes sinusoidal and square wave generators, as well as RL circuit simulation.
    )pbdoc";

    py::class_<IGenerator, std::shared_ptr<IGenerator>>(m, "Generator")
        .def("calculateVoltage", &IGenerator::calculateVoltage,
             R"pbdoc(
                Calculate the voltage generated at a specific time.

                Parameters:
                    t (float): The time at which to calculate the voltage.

                Returns:
                    float: The voltage at the given time.
            )pbdoc")
        .def("__repr__", [](const IGenerator &gen)
             { return "<Generator (interface)>"; });

    py::class_<ICircuit, std::shared_ptr<ICircuit>>(m, "Circuit")
        .def("simulate", &ICircuit::simulate, py::arg("generator"), py::arg("t_end"), py::arg("dt"),
             R"pbdoc(
                Simulate the circuit response to a generator over time.

                Parameters:
                    generator (Generator): The generator driving the circuit.
                    t_end (float): The simulation end time.
                    dt (float): The time step for the simulation.

                Returns:
                    list[float]: The simulation results as a list of currents over time.
            )pbdoc")
        .def("__repr__", [](const ICircuit &circuit)
             { return "<Circuit (interface)>"; });

    py::class_<SinusoidalGenerator, std::shared_ptr<SinusoidalGenerator>, IGenerator>(m, "SinusoidalGenerator")
        .def(py::init<double, double, double>(), py::arg("amplitude"), py::arg("frequency"), py::arg("phase") = 0.0,
             R"pbdoc(
                Create a sinusoidal generator.

                Parameters:
                    amplitude (float): The amplitude of the sinusoidal wave.
                    frequency (float): The frequency of the sinusoidal wave.
                    phase (float, optional): The initial phase of the sinusoidal wave (default is 0.0).
            )pbdoc")
        .def("calculateVoltage", &SinusoidalGenerator::calculateVoltage,
             R"pbdoc(
                Calculate the voltage of the sinusoidal generator at a specific time.

                Parameters:
                    t (float): The time at which to calculate the voltage.

                Returns:
                    float: The voltage at the given time.
            )pbdoc")
        .def("__repr__", [](const SinusoidalGenerator &gen)
             { return "<SinusoidalGenerator>"; });

    py::class_<SquareWaveGenerator, std::shared_ptr<SquareWaveGenerator>, IGenerator>(m, "SquareWaveGenerator")
        .def(py::init<double, double>(), py::arg("amplitude"), py::arg("frequency"),
             R"pbdoc(
                Create a square wave generator.

                Parameters:
                    amplitude (float): The amplitude of the square wave.
                    frequency (float): The frequency of the square wave.
            )pbdoc")
        .def("calculateVoltage", &SquareWaveGenerator::calculateVoltage,
             R"pbdoc(
                Calculate the voltage of the square wave generator at a specific time.

                Parameters:
                    t (float): The time at which to calculate the voltage.

                Returns:
                    float: The voltage at the given time.
            )pbdoc")
        .def("__repr__", [](const SquareWaveGenerator &gen)
             { return "<SquareWaveGenerator>"; });

    py::class_<CircuitRL>(m, "CircuitRL")
        .def(py::init<double, double, double>(), py::arg("resistance"), py::arg("inductance"), py::arg("initialCurrent") = 0.0,
             R"pbdoc(
                Create an RL circuit simulation.

                Parameters:
                    resistance (float): The resistance of the circuit in ohms.
                    inductance (float): The inductance of the circuit in henries.
                    initialCurrent (float, optional): The initial current in the circuit (default is 0.0).
            )pbdoc")
        .def("simulate", &CircuitRL::simulate, py::arg("generator"), py::arg("t_end"), py::arg("dt"),
             R"pbdoc(
                Simulate the RL circuit response to a generator over time.

                Parameters:
                    generator (Generator): The generator driving the circuit.
                    t_end (float): The simulation end time.
                    dt (float): The time step for the simulation.

                Returns:
                    list[float]: The simulation results as a list of currents over time.
            )pbdoc")
        .def("__repr__", [](const CircuitRL &circuit)
             { return "<CircuitRL>"; });
}
