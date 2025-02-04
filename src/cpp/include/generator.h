#ifndef GENERATOR_H
#define GENERATOR_H

/**
 * @class IGenerator
 * @brief An interface for signal generators.
 *
 * This interface defines the common behavior for all signal generator classes.
 * Any class implementing this interface must provide the `calculateVoltage` method.
 */
class IGenerator
{
public:
    /**
     * @brief Calculates the voltage at a given time.
     *
     * This pure virtual function must be implemented by derived classes to return
     * the voltage value of the generated signal at a specific time.
     * @param time The time (in seconds) at which to evaluate the signal.
     * @return The voltage value at the given time.
     */
    virtual double calculateVoltage(double time) const = 0;

    /**
     * @brief Default virtual destructor.
     *
     * The destructor is marked virtual to ensure proper cleanup of derived classes.
     */
    virtual ~IGenerator() = default;
};

#endif // GENERATOR_H
