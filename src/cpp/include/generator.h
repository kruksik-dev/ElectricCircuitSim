#ifndef GENERATOR_H
#define GENERATOR_H

class IGenerator
{
public:
    virtual double calculateVoltage(double time) const = 0;
    virtual ~IGenerator() = default;
};
#endif // GENERATOR_H