#ifndef SQUARE_WAVE_GENERATOR_H
#define SQUARE_WAVE_GENERATOR_H

#include "generator.h"

/**
 * @class SquareWaveGenerator
 * @brief A class representing a square wave signal generator.
 *
 * This class implements the `IGenerator` interface and generates a square wave
 * signal with a specified amplitude and frequency.
 */
class SquareWaveGenerator : public IGenerator
{
private:
    double amplitude; ///< Amplitude of the square wave.
    double frequency; ///< Frequency of the square wave.

public:
    /**
     * @brief Constructs a SquareWaveGenerator with given amplitude and frequency.
     * @param amplitude The peak amplitude of the square wave.
     * @param frequency The frequency of the square wave in Hz.
     */
    SquareWaveGenerator(double amplitude, double frequency);

    /**
     * @brief Calculates the voltage at a given time.
     *
     * This function returns the voltage value of the square wave at a specific time.
     * @param time The time (in seconds) at which to evaluate the wave.
     * @return The voltage value at the given time.
     */
    double calculateVoltage(double time) const override;

    /**
     * @brief Default destructor.
     */
    ~SquareWaveGenerator() override = default;
};

#endif // SQUARE_WAVE_GENERATOR_H
