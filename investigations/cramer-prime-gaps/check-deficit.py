"""Finite checks for the local zero-pair expansion and the prime-power bound."""

import cmath
import math
from fractions import Fraction
from itertools import combinations


def triangular_transform(s, width):
    if s == 0:
        return 1
    return ((cmath.exp(width * s) - 1) / (width * s)) ** 2


def check_pair_identity():
    # Include conjugate exponents, off-line parameters and a repeated ordinate.
    positive = [
        (-0.5 + 3j, 0.4 + 0.1j),
        (-0.5 + 3j, 0.4 + 0.1j),
        (-0.3 + 3.4j, -0.8 + 0.4j),
        (-0.7 + 3.4j, 0.1 - 0.6j),
        (-0.5 + 12j, -0.25 + 0.3j),
    ]
    terms = positive + [(s.conjugate(), a.conjugate()) for s, a in positive]
    width = 0.19
    cutoff = 1
    close = []
    far = []
    for s, a in terms:
        for t, b in terms:
            kernel = triangular_transform(s + t.conjugate(), width)
            pair = a * b.conjugate() * kernel
            group = close if abs(s.imag - t.imag) <= cutoff else far
            group.append(pair)
    expanded = sum(close) + sum(far)
    assert abs(expanded.imag) < 1e-13

    # Integrate the two linear pieces of the triangular density independently
    # of the transform formula. Composite Simpson quadrature includes the peak.
    panels = 256
    pieces = []
    for start in (0, width):
        for j in range(panels + 1):
            v = start + width * j / panels
            signal = sum(a * cmath.exp(s * v) for s, a in terms)
            density = max(0, width - abs(v - width)) / width**2
            weight = 1 if j in (0, panels) else 4 if j % 2 else 2
            pieces.append(weight * density * abs(signal) ** 2)
    integral = math.fsum(pieces) * width / (3 * panels)
    assert abs(integral - expanded.real) < 1e-8

    neighbors = max(sum(abs(s.imag - t.imag) <= cutoff for t, _ in terms)
                    for s, _ in terms)
    squared_mass = sum(abs(a) ** 2 for _, a in terms)
    assert sum(map(abs, close)) <= neighbors * squared_mass + 1e-12


def check_extended_pair_identity():
    # This synthetic list checks signs, symmetric height truncation and multiplicity.
    ordinates = (-11, -5, -5, -2, 2, 5, 5, 11)
    log_center, tau = math.log(31), 0.13
    pairs = sum(cmath.exp(1j * (a - b) * log_center) * 4 / (4 + (tau * (a - b)) ** 2)
                for a in ordinates for b in ordinates)

    # Direct integration with respect to the two-sided Laplace probability law.
    panels = 4096
    step = 20 * tau / panels
    samples = []
    for j in range(panels + 1):
        v = j * step
        squared = sum(abs(sum(cmath.exp(1j * g * (log_center + sign * v))
                              for g in ordinates)) ** 2 for sign in (-1, 1))
        factor = 1 if j in (0, panels) else 4 if j % 2 else 2
        samples.append(factor * squared * math.exp(-2 * v / tau) / tau)
    assert abs(pairs - math.fsum(samples) * step / 3) < 1e-7

    # Abel summation for a decaying even transform, integrating its derivative
    # exactly between successive ordinates, including the final infinite tail.
    heights = sorted(set(map(abs, ordinates)))
    weights = [math.exp(-(tau * t) ** 2) for t in heights] + [0.0]
    direct = sum(cmath.exp(1j * g * log_center) * math.exp(-(tau * g) ** 2)
                 for g in ordinates)
    integrated = 0j
    for j, t in enumerate(heights):
        partial = sum(cmath.exp(1j * g * log_center) for g in ordinates if abs(g) <= t)
        integrated += (weights[j] - weights[j + 1]) * partial
    assert abs(direct - integrated) < 1e-12


def check_proper_powers():
    limit = 4000
    primes = [n for n in range(2, limit + 1)
              if all(n % d for d in range(2, math.isqrt(n) + 1))]
    powers = []
    for p in primes:
        value, exponent = p * p, 2
        while value <= limit:
            powers.append((value, exponent))
            value *= p
            exponent += 1
    for x in range(2, limit):
        # The largest integer h strictly below 2 sqrt(x).
        h = min(math.isqrt(4 * x - 1), limit - x)
        exponents = [e for n, e in powers if x < n <= x + h]
        assert all(math.gcd(a, b) == 1 for a, b in combinations(exponents, 2))
        assigned = [next(p for p in primes if e % p == 0) for e in exponents]
        assert len(assigned) == len(set(assigned))
        assert sum(Fraction(1, e) for e in exponents) <= sum(Fraction(1, p) for p in assigned)


def check_containment():
    for lam in (Fraction(1, 100), Fraction(1, 16), Fraction(1, 9)):
        # Work in units of log(1+h/x), so the parent's exact endpoints are 0, 1.
        delta = 1 / (1 + 2 * lam)
        width = lam * delta
        for i in range(11):
            for j in range(11):
                v = width * Fraction(i + j, 10)
                assert 0 <= v < v + delta <= 1


if __name__ == "__main__":
    check_pair_identity()
    check_extended_pair_identity()
    check_proper_powers()
    check_containment()
    print("Passed local and extended pair identities, Abel summation, exponent checks and containment.")
