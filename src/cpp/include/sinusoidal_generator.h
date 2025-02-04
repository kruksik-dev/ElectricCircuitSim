#ifndef SINUSOIDAL_GENERATOR_H
#define SINUSOIDAL_GENERATOR_H

#include "generator.h"

/**
 * @class SinusoidalGenerator
 * @brief A class representing a sinusoidal wave signal generator.
 *
 * This class implements the `IGenerator` interface and generates a sinusoidal
 * wave signal with a specified amplitude, frequency, and phase.
 */
class SinusoidalGenerator : public IGenerator
{
private:
    double amplitude; ///< Amplitude of the sinusoidal wave.
    double frequency; ///< Frequency of the sinusoidal wave in Hz.
    double phase;     ///< Phase shift of the sinusoidal wave in radians.

public:
    /**
     * @brief Constructs a SinusoidalGenerator with given amplitude, frequency, and phase.
     * @param amplitude The peak amplitude of the sinusoidal wave.
     * @param frequency The frequency of the sinusoidal wave in Hz.
     * @param phase The phase shift of the sinusoidal wave in radians (default is 0.0).
     */
    SinusoidalGenerator(double amplitude, double frequency, double phase = 0.0);

    /**
     * @brief Calculates the voltage at a given time.
     *
     * This function returns the voltage value of the sinusoidal wave at a specific time.
     * @param time The time (in seconds) at which to evaluate the wave.
     * @return The voltage value at the given time.
     */
    double calculateVoltage(double time) const override;

    /**
     * @brief Default destructor.
     */
    ~SinusoidalGenerator() override = default;
};

#endif // SINUSOIDAL_GENERATOR_H
