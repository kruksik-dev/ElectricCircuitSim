#include "../include/square_wave_generator.h"
#include <cmath>

SquareWaveGenerator::SquareWaveGenerator(double amplitude, double frequency)
    : amplitude(amplitude), frequency(frequency)
{
}

double SquareWaveGenerator::calculateVoltage(double time) const
{
    double period = 1.0 / frequency;
    return (fmod(time, period) < period / 2) ? amplitude : -amplitude;
}