"""Exact finite checks for rough-intervals.md and vacancy-test.md."""

from fractions import Fraction
from itertools import combinations
from math import comb, perm, prod


def subsets(items):
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def check_congruences():
    offsets = (0, 2, 4, 6)
    primes = (7, 11, 13)
    period = prod(primes)
    hits = [
        {i: {p for p in primes if (1 + 5 * t + i) % p == 0} for i in offsets}
        for t in range(period)
    ]
    prefix = [hits[t % period] for t in range(93, 93 + 1793)]
    survival = prod(Fraction(p - 1, p) for p in primes)
    for selected in subsets(offsets):
        size = len(selected)
        survivors = sum(all(not row[i] for i in selected) for row in hits)
        assert Fraction(survivors, period) == prod(Fraction(p - size, p) for p in primes)
        all_hit = sum(all(row[i] for i in selected) for row in hits)
        assert Fraction(all_hit, period) <= (1 - survival) ** size
        for prime_subset in subsets(primes):
            mod = prod(prime_subset)
            classes = size ** len(prime_subset)
            count = sum(all(any(p in row[i] for i in selected) for p in prime_subset)
                        for row in prefix)
            assert abs(count - Fraction(len(prefix) * classes, mod)) <= classes
        for sample in (hits, prefix):
            distinct_hits = [len(set().union(*(row[i] for i in selected))) for row in sample]
            empty = distinct_hits.count(0)
            partial = 0
            for order in range(len(primes) + 1):
                partial += (-1) ** order * sum(comb(value, order) for value in distinct_hits)
                assert (-1) ** order * (partial - empty) >= 0

    count = [sum(not hit for hit in row.values()) for row in hits]
    half = Fraction(1, 2)
    assert sum(half ** u for u in count) / period <= (1 - survival / 2) ** len(offsets)
    for u in range(32):
        for order in range(0, u + 2, 2):
            upper = sum((-half) ** j * comb(u, j) for j in range(order + 1))
            assert 0 <= upper - half ** u <= half ** (order + 1) * comb(u, order + 1)


def check_polynomial():
    for m, r, rho in [(48, 3, Fraction(1, 4)), (100, 8, Fraction(1, 3))]:
        t = rho / (1 - rho)
        zero = sum(comb(m, j) * t ** j for j in range(r + 1))
        one = comb(m - 1, r) * t ** r
        assert 2 * one >= zero
        for y in range(1, m + 1):
            coefficients = sum(
                (-1) ** i * comb(y, i) * comb(m - y, j - i) * t ** (j - i)
                for j in range(r + 1) for i in range(min(y, j) + 1)
            )
            identity = sum(
                (-1) ** i * comb(y - 1, i) * Fraction(perm(r, i), perm(m - 1, i))
                / rho ** i for i in range(min(y - 1, r) + 1)
            )
            assert coefficients == one * identity


if __name__ == "__main__":
    check_congruences()
    check_polynomial()
    print("Passed exact CRT, hit-probability, Bonferroni, and polynomial checks.")
