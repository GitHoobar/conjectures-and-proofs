"""Exact arithmetic checks for interior support and the two congruence tests."""

from fractions import Fraction
from math import gcd, isqrt, prod


def is_prime(n):
    return n > 1 and all(n % k for k in range(2, isqrt(n) + 1))


def check_dual():
    radius, power = 3, 8
    counts = {0: 1}
    for _ in range(power):
        new = {}
        for j, value in counts.items():
            for i in range(-radius, radius + 1):
                new[j+i] = new.get(j+i, 0) + value
        counts = new
    scale = (2*radius + 1)**power
    assert Fraction(counts[0], scale) >= Fraction(1, power*radius + 1)
    block = {40: -4, 41: 3, 42: 5, 43: 2}
    for t in block:
        def coefficient(j):
            mask = prod(1 - Fraction(j, u-t) for u in block if u != t)
            return counts[j] * (-1 if j % 2 else 1) * mask
        assert sum(coefficient(j) * block.get(t+j, 0) for j in counts) == counts[0]*block[t]


def check_shell(x, h, q, r):
    assert is_prime(q) and is_prime(r) and q != r and h < min(q, r)
    d = q*r
    starts = range(x+1, 2*x+1)
    assert d > x
    # Use prime counts with unit weights to check selection; the identity is
    # linear in the prime weights. The model factors are checked separately.
    actual = {m: sum(is_prime(m+i) for i in range(1, h+1)) for m in starts}
    c_by_residue = [sum(gcd(b+i, d) == 1 for i in range(1, h+1)) for b in range(d)]
    phi = (q-1)*(r-1)
    represented = {m % d for m in starts}
    assert any(c_by_residue[b] == h for b in range(d) if b not in represented)
    for b in range(d):
        us = [int((m-b) % q == 0) for m in starts]
        ws = [int((m-b) % r == 0) for m in starts]
        selected = sum(actual[m]*u*w for m, u, w in zip(starts, us, ws))
        assert sum(u*w for u, w in zip(us, ws)) == int(b in represented)
        assert selected == sum(actual[m] for m in starts if m % d == b)
        assert 4*selected == sum(actual[m]*((u+w)**2-(u-w)**2)
                                 for m, u, w in zip(starts, us, ws))
        c = c_by_residue[b]
        assert h-2 <= c <= h
        assert h-2 <= Fraction(d*c, phi) <= Fraction(d*h, phi)


check_dual()
check_shell(100, 5, 17, 19)
check_shell(400, 8, 31, 37)
print('Verified dual coefficient masks and congruence selection, polarization, and residue counts on two shells.')
