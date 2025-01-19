#include <pybind11/pybind11.h>
#include "sinusoidal_generator.h"
#include "square_wave_generator.h"
#include "circuit_rl.h"

namespace py = pybind11;

PYBIND11_MODULE(electrical_sim, m)
{
    py::class_<SinusoidalGenerator>(m, "SinusoidalGenerator")
        .def(py::init<double, double, double>(), py::arg("amplitude"), py::arg("frequency"), py::arg("phase") = 0.0)
        .def("calculateVoltage", &SinusoidalGenerator::calculateVoltage);

    py::class_<SquareWaveGenerator>(m, "SquareWaveGenerator")
        .def(py::init<double, double>(),
             py::arg("amplitude"), py::arg("frequency"))
        .def("calculateVoltage", &SquareWaveGenerator::calculateVoltage);

    py::class_<CircuitRL>(m, "CircuitRL")
        .def(py::init<double, double, double>(),
             py::arg("resistance"), py::arg("inductance"), py::arg("initialCurrent") = 0.0)
        .def("simulate", &CircuitRL::simulate);
}