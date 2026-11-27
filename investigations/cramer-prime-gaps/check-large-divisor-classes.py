"""Exact checks of the local sieve and prime-weight identities."""

from fractions import Fraction
from itertools import product
from math import gcd, prod


def factors(n):
    primes = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            primes.append(p)
            n //= p
        p += 1
    if n > 1:
        primes.append(n)
    return primes


# Check the Fourier energy with integer Ramanujan sums on squarefree d.
small = (2, 3, 5)
for forbidden in product(*(range(p) for p in small)):
    for step in (7, 11, 31, 257):
        for residue in (0, 1, step - 1):
            transformed = [(a - residue) * pow(step, -1, q) % q
                           for q, a in zip(small, forbidden)]
            coordinates = range(-4, 34)
            survivors = [t for t in coordinates if all(
                (residue + step * t) % q != a for q, a in zip(small, forbidden))]
            assert survivors == [t for t in coordinates if all(
                t % q != b for q, b in zip(small, transformed))]
            for d in (1, 2, 3, 5, 6, 10, 15, 30):
                primes = factors(d)
                phi = prod(q - 1 for q in primes)
                a_d = next(a for a in range(d) if all(a % q == b
                           for q, b in zip(small, transformed) if d % q == 0))
                assert all(gcd(t - a_d, d) == 1 for t in survivors)
                energy = sum(prod(q - 1 if (t - u) % q == 0 else -1 for q in primes)
                             for t in survivors for u in survivors)
                assert energy * phi >= len(survivors) ** 2

# These weights cancel every semiprime, including squares.
r = Fraction(1, 32)
for x in range(4, 350):
    survivors = [n for n in range(x + 1, x + 21) if gcd(n, 6) == 1]
    counts = [len(factors(n)) for n in survivors]
    prime_count = counts.count(1)
    test = sum(2 * r ** (j - 1) - (2 * r) ** (j - 1) for j in counts)
    assert 0 <= prime_count - test <= 4 * len(counts) * r**2
    assert (test > 0) == (prime_count > 0)

print('Verified progression residues and Fourier energy for all 30 small-prime patterns.')
print('Verified the signed prime-weight test on 346 integer intervals.')
