"""Check the multiplier reduction and interval counting without floating point."""

from math import isqrt


def ceil_sqrt(n):
    root = isqrt(n)
    return root + (root * root != n)


def fits(n, d, s, t, limit):
    if s * s - t * t != 4 * d * n or d > limit:
        return False
    # Equivalent to sqrt(d)*s <= 2*d*sqrt(n) + sqrt(limit).
    difference = d * t * t - limit
    return difference <= 0 or difference**2 <= 16 * d * d * n * limit


def primes_of(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def from_entries(x, length, limit):
    hits = set()
    reductions = 0
    for n in range(x + 1, x + length + 1):
        for d in range(1, limit + 1):
            first = ceil_sqrt(4 * d * n)
            for s in range(first, first + isqrt(limit // d) + 2):
                t = isqrt(s * s - 4 * d * n)
                if not fits(n, d, s, t, limit):
                    continue
                hits.add(n)
                rd, rs, rt = d, s, t
                for p in primes_of(d):
                    while rd % (p*p) == 0 and rs % p == 0:
                        assert rt % p == 0
                        rd, rs, rt = rd // (p*p), rs // p, rt // p
                        assert fits(n, rd, rs, rt, limit)
                        reductions += 1
    return hits, reductions


def from_square_ranges(x, length, limit, check_spacing):
    hits = set()
    for d in range(1, limit + 1):
        first = ceil_sqrt(4 * d * x)
        last = ceil_sqrt(4 * d * (x + length)) + isqrt(limit // d) + 1
        primes = primes_of(d)
        for s in range(first, last + 1):
            if any(d % (p*p) == 0 and s % p == 0 for p in primes):
                continue
            roots = [r for r in range(d) if (r*r - s*s) % d == 0]
            assert len(roots) <= 2 * 2**len(primes)
            lower = ceil_sqrt(max(0, s*s - 4*d*(x + length)))
            upper = isqrt(s*s - 4*d*x)
            if check_spacing and s > first:
                assert upper - lower < 1
            for r in roots:
                for t in range(lower + (r - lower) % d, upper + 1, d):
                    n, remainder = divmod(s*s - t*t, 4*d)
                    if remainder == 0 and n > x and fits(n, d, s, t, limit):
                        hits.add(n)
    return hits


reductions = 0
for start, length, limit in [(1, 80, 16), (110, 67, 24), (31**2-20, 27, 20),
                             (10**24-150, 150, 30), (10**27+79, 93, 32)]:
    hits, count = from_entries(start, length, limit)
    assert hits == from_square_ranges(start, length, limit, start > 10**20)
    reductions += count
assert reductions > 0
print('Matched entry-wise and reduced multiplier counts, including square endpoints.')
print(f'Checked {reductions} common-square reductions with exact integer arithmetic.')
