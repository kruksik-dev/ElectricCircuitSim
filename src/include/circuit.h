#ifndef CIRCUIT_H
#define CIRCUIT_H

#include "generator.h"
#include <vector>
#include <tuple>

class ICircuit
{
public:
    virtual std::vector<std::tuple<double, double, double>> simulate(
        const IGenerator &generator, double t_end, double dt) = 0;
    virtual ~ICircuit() = default;
};
#endif // CIRCUIT_H