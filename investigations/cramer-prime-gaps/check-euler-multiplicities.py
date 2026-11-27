"""Exact finite checks for the rounding and Euler-factor identities."""
from fractions import Fraction
from itertools import product
from math import comb, prod


def moments(x, nodes):
    return [sum(w * t**k for w, t in zip(x, nodes)) for k in range(2)]


def check_rounding():
    nodes = (1, 2, 4, 6, 8, 10)
    x = [Fraction(i, 8) for i in (-7, 2, 6, -5, 0, 3)]
    goal = moments(x, nodes)
    while True:
        free = [i for i, w in enumerate(x) if abs(w) < 1]
        if len(free) <= 2:
            break
        i, j, k = free[:3]
        # Null direction for the two rows 1 and t.
        direction = [(i, nodes[j]-nodes[k]), (j, nodes[k]-nodes[i]),
                     (k, nodes[i]-nodes[j])]
        step = min(((1 if d > 0 else -1) - x[idx])/d for idx, d in direction)
        for idx, d in direction:
            x[idx] += step*d
        assert all(abs(w) <= 1 for w in x)
        assert moments(x, nodes) == goal
    rounded = [w if abs(w) == 1 else 0 for w in x]
    for k, value in enumerate(moments(rounded, nodes)):
        assert abs(goal[k] - value) <= sum(nodes[i]**k for i in free)


def check_recenter():
    # Rational values stand in for log(p^m) and log X; the identity is polynomial.
    locations = (Fraction(3, 2), Fraction(8, 3), Fraction(13, 4))
    weights = (Fraction(2, 3), Fraction(-1, 5), Fraction(1, 7))
    center, shift, scale = Fraction(5, 4), Fraction(7, 3), 64
    def centered(c, factor, k):
        return factor * sum(w*(t-c)**k for t, w in zip(locations, weights))
    for k in range(7):
        transformed = 16 * sum(comb(k, i)*(-shift)**(k-i)*centered(center, scale, i)
                               for i in range(k+1))
        assert centered(center+shift, 16*scale, k) == transformed


def local_a(b, e):
    if e == 0:
        return 1
    return comb(b+e-1, e) if b else 0


def local_g(b, e):
    if e == 0 or b == 2:
        return 1
    return -1 if b == 0 and e == 1 else 0


def check_divisors():
    primes = (2, 3, 5)
    for bs in product(range(3), repeat=3):
        def factor(n, coefficient):
            value = 1
            for p, b in zip(primes, bs):
                e = 0
                while n % p == 0:
                    n //= p
                    e += 1
                value *= coefficient(b, e)
            return value
        # Unlisted ordinary primes keep multiplicity one: a has no extra
        # factor there, whereas g vanishes if any unlisted prime divides d.
        for exps in product(range(4), repeat=3):
            n = prod(p**e for p, e in zip(primes, exps))
            for p, b, e in zip(primes, bs, exps):
                # Compare the coefficient of log p in the divisor identity.
                assert factor(n, local_a)*e == b*sum(factor(n//p**i, local_a)
                                                     for i in range(1, e+1))
        for cutoff in (19, 40, 101):
            floors = 0
            for exps in product(range(cutoff.bit_length()), repeat=3):
                d = prod(p**e for p, e in zip(primes, exps))
                if d <= cutoff:
                    floors += factor(d, local_g)*(cutoff//d)
            assert floors == sum(factor(n, local_a) for n in range(1, cutoff+1))


if __name__ == "__main__":
    check_rounding()
    check_recenter()
    check_divisors()
    print("Passed exact checks for rounding, centered moments, prime multiplicities and divisor sums.")
