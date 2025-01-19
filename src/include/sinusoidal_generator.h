#ifndef SINUSOIDAL_GENERATOR_H
#define SINUSOIDAL_GENERATOR_H

#include "generator.h"

class SinusoidalGenerator : public IGenerator
{
private:
    double amplitude;
    double frequency;
    double phase;

public:
    SinusoidalGenerator(double amplitude, double frequency, double phase = 0.0);
    double calculateVoltage(double time) const override;
    ~SinusoidalGenerator() override = default;
};

#endif // SINUSOIDAL_GENERATOR_H