import electriccircuitsim as el

sim_gen = el.SinusoidalGenerator(1, 1)

circ = el.CircuitRL(1, 1)

sim = circ.simulate(sim_gen, 1000, 0.1)
print(sim)
