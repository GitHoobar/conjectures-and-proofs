"""Exact finite checks for the divisor-preserving translation criteria."""

from itertools import combinations
from math import gcd, isqrt, prod


def prime_factors(n):
    remaining = n
    factors = set()
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.add(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.add(remaining)
    return factors


def subsets(values):
    for size in range(len(values) + 1):
        yield from combinations(values, size)


def check_window(x, h):
    values = list(range(x + 1, x + h + 1))
    factors = [prime_factors(n) for n in values]
    radicals = [prod(primes) for primes in factors]
    # Enumerate the possible surviving positions over every squarefree period
    # made from original divisors, independently of the radical criterion.
    possible = set()
    for chosen in subsets(sorted(set.union(*factors))):
        modulus = prod(chosen)
        possible.add(tuple(i for i, n in enumerate(values) if gcd(n, modulus) == 1))

    for target in subsets(range(h)):
        target_product = prod(values[i] for i in target)
        obstructing = [j for j in range(h) if j not in target and target_product % radicals[j] == 0]
        assert (target in possible) == (not obstructing)
        for j in obstructing:
            assert prod(abs(j - i) for i in target) % radicals[j] == 0

    exceptional = [i for i, rad in enumerate(radicals) if rad <= h]
    if len(exceptional) == 1:
        e, = exceptional
        blocked = {i for i in range(h) if (i,) not in possible}
        assert blocked == {i for i in range(h) if i != e and (i - e) % radicals[e] == 0}
        assert len(blocked) <= (h - 1) // 2
    if not exceptional:
        assert all((i,) in possible for i in range(h))


for start in range(1, 101):
    check_window(start, 6)

start, length = 2**16 - 1, 15
radicals = [prod(prime_factors(n)) for n in range(start + 1, start + length + 1)]
assert [i for i, rad in enumerate(radicals) if rad <= length] == [0]
blocked = [i for i in range(length) if any((start + i + 1) % rad == 0
           for j, rad in enumerate(radicals) if j != i)]
assert blocked == list(range(2, length, 2)) and len(blocked) == (length - 1) // 2


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


before = range(114, 126)
assert not any(is_prime(n) for n in before)
assert [n + 210 for n in before if is_prime(n + 210)] == [331]
assert [n for n in before if gcd(n, n + 210) == 1] == [121]
print('Checked all subsets at 100 starts, a sharp singleton count, and the translate containing 331.')
