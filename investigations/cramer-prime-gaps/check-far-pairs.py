"""Finite identities for the signed-pair notes. Optionally replay tabulated zeta zeros."""

import cmath
import math
import sys
from fractions import Fraction
from pathlib import Path


def cutoff_cdf(s):
    """CDF of a density proportional to (s-1)(2-s) on [1,2]."""
    t = min(1, max(0, s - 1))
    return 3 * t**2 - 2 * t**3


def check_cutoff_complement():
    ordinates = [Fraction(t, 2) for t in (-11, -6, -4, -4, 4, 4, 6, 11)]
    coeffs = [2, -1, 1, -3, -3, 1, -1, 2]
    pairs = [(abs(s - t), a * b) for s, a in zip(ordinates, coeffs)
             for t, b in zip(ordinates, coeffs)]
    for q in range(1, 9):
        breaks = {Fraction(1), Fraction(2)}
        breaks.update(d / q for d, _ in pairs if q < d < 2 * q)
        ordered = sorted(breaks)
        hard_average = 0
        for left, right in zip(ordered, ordered[1:]):
            cutoff = q * (left + right) / 2
            far = sum(weight for d, weight in pairs if d > cutoff)
            hard_average += (cutoff_cdf(right) - cutoff_cdf(left)) * far
        near = sum(weight * (1 - cutoff_cdf(d / q)) for d, weight in pairs)
        assert hard_average + near == sum(coeffs)**2


def check_riesz_curvature():
    # Arbitrary nonnegative arithmetic weights include support on both boundaries.
    atoms = {7: 3, 8: 2, 9: 1, 12: 4, 16: 5, 17: 8}
    def value(t):
        return sum(weight * max(t / n - 1, 0) for n, weight in atoms.items())
    for x in range(3, 18):
        for h in range(1, 12):
            left = Fraction(2 * x + 1, 2)
            right = left + h
            curvature = value(left) - 2 * value((left + right) / 2) + value(right)
            expected = sum(Fraction(weight, n) * min(n - left, right - n)
                           for n, weight in atoms.items() if x < n <= x + h)
            assert curvature == expected


def spline_and_derivative(u, order):
    """Density of a sum of uniforms on [-1/order,1/order] and its derivative."""
    if abs(u) >= 1:
        return 0.0, 0.0
    # Evaluate the lower half of the symmetric spline for numerical stability.
    z = (1 - abs(u)) * order / 2
    def power_sum(power):
        return math.fsum((-1)**j * math.comb(order, j) * (z - j)**power
                         for j in range(math.floor(z) + 1))
    density = order * power_sum(order - 1) / (2 * math.factorial(order - 1))
    derivative = order**2 * power_sum(order - 2) / (4 * math.factorial(order - 2))
    if u == 0:
        derivative = 0.0
    return density, -derivative if u > 0 else derivative


def replay_ordinates(path):
    # This finite B-spline has the same support and pole cancellation as the
    # smooth test. Use all 100,000 ordinates to check normalization at small x.
    ordinates = [float(line) for line in Path(path).read_text().splitlines() if line.strip()]
    if len(ordinates) != 100000 or not all(a < b for a, b in zip(ordinates, ordinates[1:])):
        raise ValueError("expected the ordered 100,000-entry Odlyzko table")
    a, order = 1 / (16 * 31), 16
    coefficients = []
    for gamma in ordinates:
        y = a * gamma
        sinc = math.sin(y / order) / (y / order)
        coefficients.append((a / 2 - 1j * y) * sinc**order)

    # The parent (31,37] includes the power 32 and right endpoint prime 37.
    worst = 0.0
    for n, mangoldt in [(32, math.log(2)), (34, 0.0), (37, math.log(37))]:
        for u in (-0.29, 0.0, 0.26):
            t = math.log(n) - a * u
            density, derivative = spline_and_derivative(u, order)
            direct = mangoldt / math.sqrt(n) * (derivative + a * density / 2)
            predicted = -2 * a * math.fsum(
                (z * cmath.exp(1j * gamma * t)).real
                for z, gamma in zip(coefficients, ordinates))
            # Trivial zero -2j has transform (a/2-s) (sinh(s/k)/(s/k))^k
            # with real s=a*(-2j-1/2). At these centers 8 terms suffice.
            for j in range(1, 9):
                s = a * (-2 * j - 0.5)
                transform = (a / 2 - s) * (math.sinh(s / order) / (s / order))**order
                predicted -= a * math.exp((-2 * j - 0.5) * t) * transform
            worst = max(worst, abs(predicted - direct))
    assert worst < 2e-7, worst
    print(f"Prime, composite, and proper-power pulse replay: maximum discrepancy {worst:.3g}.")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise SystemExit("usage: check-far-pairs.py [ODLYZKO_ZEROS]")
    check_cutoff_complement()
    check_riesz_curvature()
    print("Passed exact cutoff-complement and Riesz curvature checks.")
    if len(sys.argv) == 2:
        replay_ordinates(sys.argv[1])
