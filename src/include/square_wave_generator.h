#ifndef SQUARE_WAVE_GENERATOR_H
#define SQUARE_WAVE_GENERATOR_H

#include "generator.h"

class SquareWaveGenerator : public IGenerator
{
private:
    double amplitude;
    double frequency;

public:
    SquareWaveGenerator(double amplitude, double frequency);
    double calculateVoltage(double time) const override;
    ~SquareWaveGenerator() override = default;
};
#endif // SQUARE_WAVE_GENERATOR_H