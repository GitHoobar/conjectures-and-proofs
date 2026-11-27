"""Exact finite checks of the block crossing and extrapolation steps."""
from fractions import Fraction
from itertools import product
from math import factorial, prod


def check_crossings():
    for marks in product(range(2), repeat=9):
        for length in range(1, len(marks) + 1):
            counts = [sum(marks[i:i+length]) for i in range(len(marks) - length + 1)]
            high = max(counts[j] for j in range(0, len(counts), length))
            # Stop at the partition window witnessing the maximum.
            end = next(j for j in range(0, len(counts), length) if counts[j] == high)
            assert set(range(counts[0], high + 1)).issubset(counts[:end + 1])


def check_extrapolation():
    for low, high in [(3, 14), (19, 42), (101, 129)]:
        for degree in range(1, min(9, high - low) + 1):
            step = (high-low) // degree
            nodes = [low + i*step for i in range(degree + 1)]
            coeff = [prod(Fraction(-y, x-y) for y in nodes if y != x) for x in nodes]
            # Verification on monomials checks all polynomials of this degree.
            for power in range(degree + 1):
                assert sum(c*x**power for c, x in zip(coeff, nodes)) == (power == 0)
            bound = Fraction((2*high)**degree, step**degree * factorial(degree))
            assert sum(abs(c) for c in coeff) <= bound


def check_perturbed_nodes():
    for jump in range(1, 4):
        step, low, degree = 2*jump + 1, 19, 3
        for overshoots in product(range(jump + 1), repeat=degree + 1):
            nodes = [low + i*step + v for i, v in enumerate(overshoots)]
            for i, x in enumerate(nodes):
                for j, y in enumerate(nodes[:i]):
                    assert 2*(x-y) >= (i-j)*step
            coeff = [prod(Fraction(-y, x-y) for y in nodes if y != x) for x in nodes]
            bound = Fraction((4*max(nodes))**degree, step**degree * factorial(degree))
            assert sum(abs(c) for c in coeff) <= bound
            for power in range(degree + 1):
                assert sum(c*x**power for c, x in zip(coeff, nodes)) == (power == 0)


if __name__ == "__main__":
    check_crossings()
    check_extrapolation()
    check_perturbed_nodes()
    print("Verified block crossings, extrapolation weights, and perturbed interpolation nodes.")
