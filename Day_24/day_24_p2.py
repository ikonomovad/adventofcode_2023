import re
from z3 import Solver, Real, sat

# This problem was too hard for me and it is fully solved thanks to comments on Reddit:
# https://www.reddit.com/r/adventofcode/comments/18pnycy/2023_day_24_solutions/?utm_source=share&utm_medium=web2x&context=3

"""
Z3 is a high-performance theorem prover developed at Microsoft Research. 
It is designed to solve logical formulas, particularly those involving integer and real arithmetic. 
Z3 is widely used in formal verification, symbolic execution, and constraint solving.

In our case we will be using z3 to solve system of equations.
"""

with open('input.txt') as file:
    lines = [list(map(int, re.findall(r'-?\d+', line.replace(' @ ', ', '))))
             for line in file.read().split('\n')]

    # Creating a solver for system of equation
    solver = Solver()

    # Define symbolic variables
    rx, ry, rz = Real('rx'), Real('ry'), Real('rz')  # Rock position
    rvx, rvy, rvz = Real('rvx'), Real('rvy'), Real('rvz')  # Rock velocity
    time = [Real(f't{i}') for i in range(3)]  # Times

    # - We add 3 equations on each iteration;
    # - We want to find 9 unknowns x, y, z, vx, vy, vz, t0, t1, t2;
    # - If we iterate each hailstone the system will be over-constrained because there will be more equations than unknowns;
    # - So we can create system of 9 equations, that means we can iterate 3 times only;
    # - A solution, if it exists, should satisfy all equations.

    print('Processing...')

    for i in range(3):
        px, py, pz, pvx, pvy, pvz = lines[i]

        # Time cannot be negative
        solver.add(time[i] >= 0)

        # Add the equation for the rock's x-coordinate based on time[i]
        solver.add(rx + rvx * time[i] == px + pvx * time[i])

        # Add the equation for the rock's y-coordinate based on time[i]
        solver.add(ry + rvy * time[i] == py + pvy * time[i])

        # Add the equation for the rock's z-coordinate based on time[i]
        solver.add(rz + rvz * time[i] == pz + pvz * time[i])

    if solver.check() == sat:
        model = solver.model()
        solution = model.eval(rx + ry + rz)
        print(solution)
