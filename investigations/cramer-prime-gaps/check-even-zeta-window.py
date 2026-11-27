"""Certify small window tests by rational enclosures of the ordinary even zeta values."""
from fractions import Fraction as Q
from math import comb, factorial, isqrt, prod


def atan_interval(q, terms):
    partial = sum(Q((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(terms))
    following = partial + Q((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(partial, following), max(partial, following)


def pi_interval():
    a, b = atan_interval(5, 70)
    c, d = atan_interval(239, 70)
    scale = 1 << 300
    lower = (16*a - 4*d)*scale
    upper = (16*b - 4*c)*scale
    return Q(lower.__floor__(), scale), Q(upper.__ceil__(), scale)


def bernoullis(limit):
    values = [Q(1)]
    for n in range(1, limit+1):
        values.append(-sum(comb(n+1, j)*v for j, v in enumerate(values))/(n+1))
    return values


def square(poly):
    result = [0] * (2*len(poly)-1)
    for i, a in enumerate(poly):
        for j, b in enumerate(poly):
            result[i+j] += a*b
    return result


def coefficients(m):
    u = [0]*m
    for j in range((m-1)//2+1):
        exponent = m-1-2*j
        u[exponent] = (-1)**j*comb(m-1-j, j)*2**exponent
    fourth = square(square(u))
    assert not any(fourth[1::2])
    return [Q(0)] + [Q(a, m**4) for a in fourth[::2]]


def value(poly, t):
    return sum(c*t**k for k, c in enumerate(poly))


def prime(n):
    return n >= 2 and all(n % p != 0 for p in range(2, isqrt(n)+1))


def score_interval(y, b, g, m, argument_scale=Q(1)):
    # The computation of the score uses primes only through y.
    initial = [p for p in range(2, y+1) if prime(p)]
    poly = coefficients(m)
    assert value(poly, Q(1)) == 1
    normal = value(poly, Q(b, b-g)**2)
    lo_pi, hi_pi = pi_interval()
    assert hi_pi**2*b*b/(6*m**4*normal) < Q(1, 4)
    bern = bernoullis(2*(len(poly)-1))
    lower = upper = Q(0)
    for k, c in enumerate(poly[1:], 1):
        s = 2*k
        rational = abs(bern[s])*2**(s-1)/factorial(s)
        rational *= prod(1-Q(1, p**s) for p in initial)
        factor = c*b**s/normal
        endpoints = [factor*(rational*argument_scale**k*pival**s-1)
                     for pival in (lo_pi, hi_pi)]
        lower += min(endpoints)
        upper += max(endpoints)
    assert upper-lower < Q(1, 1000)
    return lower, upper


for y, b, g, m in ((13, 16, 0, 8), (13, 17, 0, 9), (13, 19, 0, 9),
                   (13, 20, 2, 6), (19, 22, 1, 7)):
    lo, hi = score_interval(y, b, g, m)
    actual = [n for n in range(y+1, b+1) if prime(n)]
    if not actual:
        assert hi < Q(1, 4)
    if any(n <= b-g for n in actual):
        assert lo >= 1
    assert not (lo > Q(1, 4) and not actual)
    if g == 0:
        poly = coefficients(m)
        eta = 4*(1+(b-y)*value(poly, Q(b, y)**2))/value(poly, b**2)
        assert (1-eta)*b**2 > 1
        assert score_interval(y, b, g, m, 1-eta)[1] < Q(1, 2)
        assert score_interval(y, b, g, m, 1+eta)[0] > Q(1, 2)
print("Certified empty and occupied windows, guarded tests, and both sides of the nearby polynomial threshold.")
