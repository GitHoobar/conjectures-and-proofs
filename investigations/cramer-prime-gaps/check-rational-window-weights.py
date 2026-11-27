"""Exact checks for switching prime-power coordinates and for the residue form."""

from fractions import Fraction
from itertools import combinations, product
from math import gcd, prod


offsets = (1, 7, 13)
coordinates = ((5, 25), (7, 7), (11, 11))
subsets = [set(s) for size in range(4) for s in combinations(offsets, size)]


def weight(v):
    # Periods 25, 35 and 11. Each summand sees at most two groups of switches.
    return v[0] - 8 + (v[0] % 5 - 2) * (v[1] - 3) - 2 * v[2]


def good(v, i):
    return all((a + i) % p for a, (p, _) in zip(v, coordinates))


# Conditional on the small primes 2 and 3 being at residue zero, all T are eligible.
for p, modulus in coordinates:
    assert len({i % p for i in offsets}) == len(offsets)
    escape = [a for a in range(modulus) if all((a + i) % p for i in offsets)]
    for selected in subsets:
        mass = [Fraction(0)] * modulus
        for a in range(modulus):
            if any((a + i) % p == 0 for i in selected):
                for b in escape:
                    mass[b] += Fraction(1, modulus * len(escape))
            else:
                mass[a] += Fraction(1, modulus)
        assert sum(mass) == 1
        assert max(mass) * modulus == 1 + Fraction(len(selected), p - len(offsets))

full_energy = good_energy = 0
for original in product(*(range(q) for _, q in coordinates)):
    # Zero is a legal escape for each prime here. The mixed difference vanishes
    # for every fixed escape draw. Distinct example choices exercise that identity.
    alternatives = []
    for a, (p, q) in zip(original, coordinates):
        escape = [b for b in range(q) if all((b + i) % p for i in offsets)]
        alternatives.append(escape[a % len(escape)])
    mixed_difference = 0
    for selected in subsets:
        changed = [alt if any((a + i) % p == 0 for i in selected) else a
                   for a, alt, (p, _) in zip(original, alternatives, coordinates)]
        assert all(good(changed, i) for i in selected)
        mixed_difference += (-1)**len(selected) * weight(changed)
    assert mixed_difference == 0
    energy = weight(original)**2
    full_energy += energy
    if any(good(original, i) for i in offsets):
        good_energy += energy

density_bound = prod(Fraction(p, p-len(offsets)) for p, _ in coordinates)
assert 0 < good_energy < full_energy <= 4**len(offsets) * density_bound * good_energy

# The normalized main matrix is positive as a whole. Evaluate Ramanujan sums
# with integer identities on a finite period including nonsquarefree frequencies.
period = 60
phi = lambda q: sum(gcd(a, q) == 1 for a in range(q))


def mobius(n):
    count = 0
    for p in range(2, n + 1):
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            count += 1
    return (-1)**count


def ramanujan(q, v):
    return sum(d * mobius(q // d) for d in range(1, q + 1) if gcd(q, v) % d == 0)


for q in range(1, period + 1):
    if period % q:
        continue
    for i in range(1, 8):
        unit_sum = sum(ramanujan(q, v) for v in range(period) if gcd(v + i, period) == 1)
        assert Fraction(unit_sum, phi(period)) == Fraction(mobius(q)*ramanujan(q, i), phi(q))

print('Verified switch identities on 1,925 original states, all subset density bounds, and residue averages.')
