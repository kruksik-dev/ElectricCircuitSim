#include <gtest/gtest.h>
#include "../src/cpp/include/sinusoidal_generator.h"
#include "../src/cpp/include/square_wave_generator.h"
#include "../src/cpp/include/circuit_rl.h"

TEST(SinusoidalGeneratorTest, CalculateVoltage)
{
    SinusoidalGenerator generator(1.0, 1.0, 0.0);
    EXPECT_NEAR(generator.calculateVoltage(0.0), 0.0, 1e-6);
    EXPECT_NEAR(generator.calculateVoltage(0.25), 1.0, 1e-6);
    EXPECT_NEAR(generator.calculateVoltage(0.5), 0.0, 1e-6);
    EXPECT_NEAR(generator.calculateVoltage(0.75), -1.0, 1e-6);
    EXPECT_NEAR(generator.calculateVoltage(1.0), 0.0, 1e-6);
}

TEST(SquareWaveGeneratorTest, CalculateVoltage)
{
    SquareWaveGenerator generator(1.0, 1.0);
    EXPECT_EQ(generator.calculateVoltage(0.0), 1.0);
    EXPECT_EQ(generator.calculateVoltage(0.25), 1.0);
    EXPECT_EQ(generator.calculateVoltage(0.5), -1.0);
    EXPECT_EQ(generator.calculateVoltage(0.75), -1.0);
    EXPECT_EQ(generator.calculateVoltage(1.0), 1.0);
}

TEST(CircuitRLTest, Simulate)
{
    SinusoidalGenerator sin_gen(1.0, 1.0, 0.0);
    CircuitRL circuit(1.0, 1.0, 0.0);
    auto result = circuit.simulate(sin_gen, 1.0, 0.25);
    std::vector<std::tuple<double, double, double>> expected = {
        {0.0, 0.0, 0.0},
        {0.25, 1.0, 0.25},
        {0.5, 1.22e-16, 0.187},
        {0.75, -1.0, -0.109},
        {1.0, -2.44e-16, -0.082},
    };
    ASSERT_EQ(result.size(), expected.size());
    for (size_t i = 0; i < result.size(); ++i)
    {
        EXPECT_NEAR(std::get<0>(result[i]), std::get<0>(expected[i]), 1e-3);
        EXPECT_NEAR(std::get<1>(result[i]), std::get<1>(expected[i]), 1e-3);
        EXPECT_NEAR(std::get<2>(result[i]), std::get<2>(expected[i]), 1e-3);
    }
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}