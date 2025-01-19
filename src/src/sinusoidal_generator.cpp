#include "sinusoidal_generator.h"
#include <cmath>

SinusoidalGenerator::SinusoidalGenerator(double amplitude, double frequency, double phase)
    : amplitude(amplitude), frequency(frequency), phase(phase)
{
}

double SinusoidalGenerator::calculateVoltage(double time) const
{
    return amplitude * std::sin(2 * M_PI * frequency * time + phase);
}