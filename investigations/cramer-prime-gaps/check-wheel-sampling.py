#!/usr/bin/env python3
"""Check residue-class interpolation and replay the finite zero formula."""
import cmath
import math
import sys
from bisect import bisect_right
from pathlib import Path


def residues(q):
    return [s for s in range(q) if math.gcd(s, q) == 1]


def kernel(u, r, q):
    omega = math.pi / q
    t = omega * u
    value = (math.sin(t) / t if t else 1.0)**10
    for s in residues(q):
        if s != r:
            value *= (math.sin(omega * (u + r - s)) / math.sin(omega * (r - s)))**2
    return value


def coefficients(r, q):
    # Fourier coefficients of the product of sine squares.
    values = {0: 1}
    for s in residues(q):
        if s == r:
            continue
        angle = math.pi * (r - s) / q
        scale = 1 / (4 * math.sin(angle)**2)
        plus = -scale * cmath.exp(2j * angle)
        updated = {}
        for index, value in values.items():
            for shift, weight in [(-1, plus.conjugate()), (0, 2*scale), (1, plus)]:
                key = index + shift
                updated[key] = updated.get(key, 0) + weight * value
        values = updated
    return values


def transform_sinc(t):
    # Density of the sum of ten uniforms on [-1,1], using the nearer endpoint.
    z = 10 - abs(t)
    if z <= 0:
        return 0.0
    return math.fsum((-1)**k * math.comb(10, k) * (z - 2*k)**9
                     for k in range(5) if 2*k < z) / (1024 * math.factorial(9))


def transform(y, coeff, q):
    omega = math.pi / q
    return 2*q * sum(value * transform_sinc(y / omega + 2*k)
                     for k, value in coeff.items())


def excluded_powers(j, r, q):
    total = 0.0
    for p in range(2, q+1):
        if q % p or any(p % k == 0 for k in range(2, math.isqrt(p)+1)):
            continue
        n = p
        while n <= 2*j:
            if 2*n >= j:
                total += math.log(p) * kernel(n-j, r, q)
            n *= p
    return total


def replay(j, q, expected, ordinates):
    r = j % q
    coeff = coefficients(r, q)
    height = (8 + 2 * len(residues(q))) * math.pi * j / q
    assert height < ordinates[-1]
    end = bisect_right(ordinates, height)
    zeros = math.fsum((cmath.exp(1j*g*math.log(j)) * transform(g/j, coeff, q)).real
                      for g in ordinates[:end])
    value = transform(0, coeff, q).real - 2 * zeros / math.sqrt(j) - excluded_powers(j, r, q)
    print(f"q={q}, j={j}, reconstructed {value:.7f}, expected {expected:.7f}")
    assert abs(value - expected) < 0.04
    return value > 0.75 * math.log(j)


if __name__ == "__main__":
    for q in [2, 6, 30]:
        for r in residues(q):
            for d in range(-3*q, 3*q+1):
                if math.gcd(r+d, q) == 1:
                    assert abs(kernel(d, r, q) - (d == 0)) < 1e-12
    print("Cardinal weights passed for moduli 2, 6 and 30.")
    if len(sys.argv) == 2:
        ordinates = [float(v) for v in Path(sys.argv[1]).read_text().split()]
        if len(ordinates) != 100000 or not all(0 < a < b for a,b in zip(ordinates, ordinates[1:])):
            raise ValueError("expected the ordered Odlyzko table of 100,000 ordinates")
        for q, j, base in [(6, 121, 11), (6, 125, 5), (6, 127, 127),
                           (30, 961, 31), (30, 1001, 1), (30, 1021, 1021)]:
            assert replay(j, q, math.log(base), ordinates) == (base == j)
    elif len(sys.argv) > 2:
        raise SystemExit("usage: check-wheel-sampling.py [ODLYZKO_ZEROS]")
