#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/chrono.h>
#include "../include/sinusoidal_generator.h"
#include "../include/square_wave_generator.h"
#include "../include/circuit_rl.h"

namespace py = pybind11;

PYBIND11_MODULE(electriccircuitsim, m)
{
    py::class_<IGenerator, std::shared_ptr<IGenerator>>(m, "IGenerator")
        .def("calculateVoltage", &IGenerator::calculateVoltage);

    py::class_<SinusoidalGenerator, std::shared_ptr<SinusoidalGenerator>, IGenerator>(m, "SinusoidalGenerator")
        .def(py::init<double, double, double>(), py::arg("amplitude"), py::arg("frequency"), py::arg("phase") = 0.0)
        .def("calculateVoltage", &SinusoidalGenerator::calculateVoltage);

    py::class_<SquareWaveGenerator, std::shared_ptr<SquareWaveGenerator>, IGenerator>(m, "SquareWaveGenerator")
        .def(py::init<double, double>(), py::arg("amplitude"), py::arg("frequency"))
        .def("calculateVoltage", &SquareWaveGenerator::calculateVoltage);

    py::class_<CircuitRL>(m, "CircuitRL")
        .def(py::init<double, double, double>(), py::arg("resistance"), py::arg("inductance"), py::arg("initialCurrent") = 0.0)
        .def("simulate", &CircuitRL::simulate);
}