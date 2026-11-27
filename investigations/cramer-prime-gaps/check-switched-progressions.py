"""Exact finite checks of divisor switching, signed shifts and the local mean."""

from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod


def is_prime(n):
    return n >= 2 and all(n % j for j in range(2, isqrt(n) + 1))


def phi(n):
    return sum(gcd(i, n) == 1 for i in range(1, n + 1))


def weight(t, x):
    # Compact rational test with the theorem's support and unit central weight.
    return max(0, 1 - Fraction(4 * abs(t), x)) ** 3


def check_switch(x, y, h, qs, ts):
    primes = [p for p in range(y-x//4, y+h+x//4+1) if is_prime(p)]
    prime_set = set(primes)
    deleted = [p for p in primes if y < p <= y + 3*h]
    assert 3*h < min(qs)*min(ts)
    direct = switched = 0
    directions = set()
    for q, r, i in product(qs, ts, range(1, h+1)):
        a, d = y+i, q*r
        direct += sum(weight(p-a, x) for p in primes if (p-a) % d == 0)
        removed = sum(weight(p-a, x) for p in deleted if (p-a) % d == 0)
        assert removed == int(a in prime_set)
    for q in qs:
        for k in range(-x//(4*q*min(ts))-1, x//(4*q*min(ts))+2):
            if k == 0:
                continue
            for i in range(1, h+1):
                a = y+i
                for r in ts:
                    p = a+k*q*r
                    if p in prime_set and weight(k*q*r, x):
                        assert gcd(a, abs(k)*q) == 1
                        directions.add(1 if k > 0 else -1)
                        switched += weight(k*q*r, x)
    center = sum(is_prime(y+i) for i in range(1, h+1))
    assert directions == {-1, 1}
    assert direct - switched == len(qs)*len(ts)*center
    return center


qs, ts = (5, 7), range(8, 16)  # Includes pairs where q divides r.
centers = [check_switch(6000, y, 7, qs, ts) for y in (6000, 6020, 6100, 6110)]
assert 0 in centers and max(centers) > 0

# Average of the exact multiplicative local factors on a complete period.
small = (2, 3, 5, 7)
period = prod(small)
c0 = prod(1 + Fraction(1, p*(p-1)) for p in small)
v = {p: Fraction(p, p*p-p+1) for p in small}
means = [c0 * prod(1-v[p] for p in small if a % p == 0) for a in range(period)]
assert sum(means) == period
for a in range(1, 71):
    # This is the sieve truncated to the four displayed primes.
    terms = [prod(Fraction(p, p-1) for p in small if r % p == 0)
             for r in range(1, period+1) if not any(a % p == r % p == 0 for p in small)]
    assert sum(terms)/period == means[a]
    assert Fraction(a, phi(a)) == prod(Fraction(p, p-1) for p in range(2, a+1)
                                        if is_prime(p) and a % p == 0)
print('Checked both shift directions, targeted deletions, empty and occupied windows, and the full-period local factors.')
