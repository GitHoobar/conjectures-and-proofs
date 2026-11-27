"""Exact arithmetic checks for the Cramér research notes. Run with python3."""
from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


# Index zero is unused in Wang's notation.
p = [0] + [n for n in range(2, 98) if prime(n)]


def gap(n):
    return p[n + 1] - p[n]


def average(n):
    return Fraction(p[n + 1] - 2, n)


for n in (9, 24):
    a, b, c = average(n - 1), gap(n - 1), gap(n)
    assert a < b < c and b * b / a > c
    print(f"Lemma 2.4, n={n}, primes={p[n-1:n+2]}, A={a}, {b*b/a} > {c}")

n = 6
assert gap(n - 1) < average(n - 1) and average(n - 2) < average(n) < gap(n)
ratio = Fraction(n - 2, n) * (gap(n) - average(n - 1)) / (average(n - 1) - gap(n - 1))
assert ratio == 6 and ratio > Fraction(7, 2)
print(f"Equation (2.11), n={n}, left side = {ratio} > 7/2")

offsets = [2**j for j in range(64)]
assert all(0 < b-a < c-b for a, b, c in combinations(offsets, 3))
print("All ordered triples from the 64 offsets have strictly increasing jumps.")

for y in range(16):
    for r in range(0, 14, 2):
        bound = sum((-1)**j * comb(y, j) for j in range(r + 1))
        assert bound == (comb(y - 1, r) if y else 1)
        assert bound >= int(y == 0)

# Uniform affine polynomials over F_5, tested at four distinct coordinates.
rows = [tuple((a*x + b) % 5 == 0 for x in range(4)) for a, b in product(range(5), repeat=2)]
for i, j in combinations(range(4), 2):
    assert sum(row[i] for row in rows) == 5
    assert sum(row[i] and row[j] for row in rows) == 1
assert sum(not any(row) for row in rows) >= 4
print("Bonferroni identities and the pairwise-independent example passed.")
