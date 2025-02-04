#ifndef CIRCUIT_H
#define CIRCUIT_H

#include "generator.h"
#include <vector>
#include <tuple>

/**
 * @class ICircuit
 * @brief An interface for simulating electrical circuits.
 *
 * This interface defines the common behavior for all circuit simulation classes.
 * Any class implementing this interface must provide the `simulate` method
 * to simulate the circuit's behavior with a given signal generator.
 */
class ICircuit
{
public:
    /**
     * @brief Simulates the circuit's behavior over time.
     *
     * This pure virtual function must be implemented by derived classes to simulate
     * the circuit's response to a given signal generator over a specified period.
     * The result is a series of time-voltage-current triplets.
     *
     * @param generator The signal generator used to provide input to the circuit.
     * @param t_end The final time (in seconds) for the simulation.
     * @param dt The time step (in seconds) used for the simulation.
     * @return A vector of tuples, each containing a time, voltage, and current.
     */
    virtual std::vector<std::tuple<double, double, double>> simulate(
        const IGenerator &generator, double t_end, double dt) = 0;

    /**
     * @brief Default virtual destructor.
     *
     * The destructor is marked virtual to ensure proper cleanup of derived classes.
     */
    virtual ~ICircuit() = default;
};

#endif // CIRCUIT_H
