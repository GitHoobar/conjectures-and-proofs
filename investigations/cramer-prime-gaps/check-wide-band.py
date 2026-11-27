#!/usr/bin/env python3
"""Replay the single-zero side of the wide-band transfer on Odlyzko's table."""

import math
import runpy
import sys
from pathlib import Path

primes_and_von_mangoldt = runpy.run_path(
    str(Path(__file__).with_name("check-zero-sum.py"))
)["primes_and_von_mangoldt"]


def density_derivative(y, order):
    """Derivative of the density of a sum of eight U[-1,1] variables."""
    if abs(y) >= 8:
        return 0.0
    # Evaluate on the negative half to avoid large canceling terms.
    power = 7 - order
    total = math.fsum(
        (-1)**j * math.comb(8, j) * (8 - abs(y) - 2*j)**power
        for j in range(5) if 2*j < 8 - abs(y)
    )
    sign = -1 if y > 0 and order % 2 else 1
    return sign * total / (256 * math.factorial(power))


def transform(y, order):
    # f(u) = (1-u²) sinc(u)^8. Multiplying by -u² differentiates twice.
    return 2 * math.pi * (density_derivative(y, order) +
                          density_derivative(y, order + 2))


def minorant(u):
    if u == 0:
        return 1.0
    return (1 - u*u) * (math.sin(u) / u)**8


def replay(x, h, expected_primes, ordinates):
    left, right = math.log(x + 0.5), math.log(x + h + 0.5)
    center, delta = (left + right) / 2, (right - left) / 2
    assert ordinates[-1] >= 8 / delta
    primes, mangoldt = primes_and_von_mangoldt(math.ceil(math.exp(center + 0.5)))
    prime_set = set(primes)

    def spatial(scale):
        square_terms, powers = [], []
        inside_upper = 0.0
        for n, lam in mangoldt.items():
            v = math.log(n) - center
            if abs(v) > 0.5:
                continue
            weight = minorant(v / scale) / (scale * n)
            square_terms.append(lam**2 * weight)
            if n not in prime_set:
                powers.append(lam * (math.log(n) - lam) * weight)
            if x < n <= x + h:
                inside_upper += lam**2 / (delta * n)
        mass = math.fsum(square_terms)
        if scale == delta:
            assert mass <= inside_upper + 1e-10
        return mass, math.fsum(powers)

    def zeros(scale):
        terms = []
        for gamma in ordinates:
            y = scale * gamma
            if y >= 8:
                break
            # Quadratic Taylor correction for (center+v) exp(-v/2).
            real = (center * transform(y, 0)
                    - (center/8 - 0.5) * scale**2 * transform(y, 2))
            imag = -(1 - center/2) * scale * transform(y, 1)
            phase = center * gamma
            terms.append(real * math.cos(phase) - imag * math.sin(phase))
        return 2 * math.exp(-center/2) * math.fsum(terms)

    narrow_mass, narrow_powers = spatial(delta)
    broad_mass, broad_powers = spatial(2 * delta)
    # The two transforms have the same mass at zero, so the pole cancels.
    residual = (narrow_mass - broad_mass + narrow_powers - broad_powers
                + zeros(delta) - zeros(2 * delta))
    prime_count = sum(x < p <= x+h for p in primes)
    assert prime_count == expected_primes
    print(f"({x},{x+h}]: prime count {prime_count}, "
          f"power correction {narrow_powers - broad_powers:+.5f}, "
          f"residual {residual:+.3g}")
    assert abs(residual) < 2e-6, residual


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check-wide-band.py ODLYZKO_ZEROS")
    ordinates = [float(v) for v in Path(sys.argv[1]).read_text().split()]
    if len(ordinates) != 100000 or not all(0 < a < b for a, b in zip(ordinates, ordinates[1:])):
        raise ValueError("expected the ordered 100,000-entry Odlyzko table")
    for start, length, count in [(9973, 33, 0), (10193, 17, 0),
                                 (10193, 18, 1), (16381, 30, 1)]:
        replay(start, length, count, ordinates)
