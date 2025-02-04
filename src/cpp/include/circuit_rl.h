#ifndef CIRCUIT_RL_H
#define CIRCUIT_RL_H

#include "circuit.h"

/**
 * @class CircuitRL
 * @brief A class representing an RL (resistor-inductor) circuit.
 *
 * This class implements the `ICircuit` interface and simulates the behavior of
 * an RL circuit, which consists of a resistor and an inductor, under the influence
 * of an input signal generator.
 */
class CircuitRL : public ICircuit
{
private:
    double resistance; ///< The resistance of the resistor in the RL circuit (in ohms).
    double inductance; ///< The inductance of the inductor in the RL circuit (in henrys).
    double current;    ///< The initial current in the RL circuit (in amperes).

public:
    /**
     * @brief Constructs a CircuitRL object with the given resistance, inductance, and initial current.
     * @param resistance The resistance value of the resistor in ohms.
     * @param inductance The inductance value of the inductor in henrys.
     * @param current The initial current in the circuit (default is 0.0).
     */
    CircuitRL(double resistance, double inductance, double current = 0.0);

    /**
     * @brief Simulates the behavior of the RL circuit over time.
     *
     * This function simulates the current, voltage, and time values of the RL circuit
     * under the influence of a specified signal generator. The simulation is run over
     * the time interval [0, t_end] with the given time step `dt`.
     *
     * @param generator The signal generator used to provide input to the circuit.
     * @param t_end The final time (in seconds) for the simulation.
     * @param dt The time step (in seconds) used for the simulation.
     * @return A vector of tuples, each containing time, voltage, and current values for the circuit.
     */
    std::vector<std::tuple<double, double, double>> simulate(
        const IGenerator &generator, double t_end, double dt) override;

    /**
     * @brief Default destructor.
     *
     * The destructor is marked virtual to ensure proper cleanup of derived classes.
     */
    ~CircuitRL() override = default;
};

#endif // CIRCUIT_RL_H
