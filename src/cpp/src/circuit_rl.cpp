#include "../include/circuit_rl.h"
#include <cmath>

CircuitRL::CircuitRL(double resistance, double inductance, double current)
    : resistance(resistance), inductance(inductance), current(current)
{
}

std::vector<std::tuple<double, double, double>> CircuitRL::simulate(
    const IGenerator &generator, double t_end, double dt)
{
    std::vector<std::tuple<double, double, double>> result;
    double time = 0.0;

    while (time <= t_end)
    {
        double voltage = generator.calculateVoltage(time);
        double current_change = (voltage - resistance * current) / inductance * dt;
        current += current_change;
        result.push_back(std::make_tuple(time, voltage, current));
        time += dt;
    }

    return result;
}
