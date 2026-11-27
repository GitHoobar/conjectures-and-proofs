"""Exact finite checks for primes-in-residue-classes.md."""
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt


def primes_up_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = 0
    return {n for n in range(2, limit + 1) if sieve[n]}


def check_rows():
    left, right, width = 200, 600, 11
    primes = primes_up_to(right + width)
    removed = {p for p in primes if 330 < p <= 344}
    assert removed
    for modulus in (30, 35, 105):
        assert modulus > width + 14
        for residue in range(modulus):
            starts = list(range(left + (residue - left) % modulus, right, modulus))
            eligible = [i for i in range(1, width + 1) if gcd(residue + i, modulus) == 1]
            original = [{i for i in eligible if x + i in primes} for x in starts]
            thinned = [{i for i in row if x + i not in removed}
                       for x, row in zip(starts, original)]
            assert sum(a != b for a, b in zip(original, thinned)) <= 1
            for size in range(len(eligible) + 1):
                for offsets in combinations(eligible, size):
                    counts = [len(row.intersection(offsets)) for row in original]
                    column_total = sum(
                        left + i <= p < right + i and (p - i) % modulus == residue
                        for i in offsets for p in primes
                    )
                    assert sum(counts) == column_total
                    hits = sum(bool(n) for n in counts)
                    assert sum(counts) ** 2 <= hits * sum(n * n for n in counts)
                    thinned_hits = sum(not row.isdisjoint(offsets) for row in thinned)
                    assert 0 <= hits - thinned_hits <= 1


def check_vacancies():
    primes = primes_up_to(320)
    for marks in (primes, {p for p in primes if not 120 < p <= 190}):
        ordered = sorted(marks)
        for left, right in [(100, 202), (135, 165), (119, 191), (121, 205)]:
            for width in (1, 7, 20):
                values = [sum(x < p <= x + width for p in marks) for x in range(left, right)]
                empty = values.count(0)
                by_gaps = sum(max(0, min(right, b - width) - max(left, a))
                              for a, b in zip(ordered, ordered[1:]))
                assert empty == by_gaps
                q = Fraction(width, right - left)
                assert empty <= sum(q ** n for n in values) <= empty + width


if __name__ == "__main__":
    check_rows()
    check_vacancies()
    print("Passed column, subset, one-start deletion, clipped gap, and vacancy checks.")
