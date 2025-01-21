#ifndef CIRCUIT_RL_H
#define CIRCUIT_RL_H

#include "circuit.h"

class CircuitRL : public ICircuit
{
private:
    double resistance;
    double inductance;
    double current;

public:
    CircuitRL(double resistance, double inductance, double current = 0.0);
    std::vector<std::tuple<double, double, double>> simulate(
        const IGenerator &generator, double t_end, double dt) override;
    ~CircuitRL() override = default;
};

#endif // CIRCUIT_RL_H