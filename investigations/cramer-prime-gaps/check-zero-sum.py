#!/usr/bin/env python3
"""Small replay of the smoothed explicit-formula kernel.

Usage: python3 check-zero-sum.py ODLYZKO_ZEROS

Supply the Odlyzko table from the first positive ordinate onward, with one
ordinate per line in increasing order. The script reads the local file.
"""

from __future__ import annotations

import cmath
import math
import pathlib
import sys
from decimal import Decimal, getcontext

B = 1.0 / 8.0
getcontext().prec = 70


def primes_and_von_mangoldt(limit: int):
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    primes = [n for n in range(2, limit + 1) if is_prime[n]]
    lam = {}
    for p in primes:
        q = p
        while q <= limit:
            lam[q] = math.log(p)
            q *= p
    return primes, lam


def irwin_hall_cdf(y: float, k: int) -> float:
    """CDF of a sum of k U[0,1] variables, with endpoint stabilization."""
    if y <= 0.0:
        return 0.0
    if y >= k:
        return 1.0
    # Decimal avoids catastrophic cancellation in the alternating Irwin-Hall
    # sum near its centre (K is about 8 log x even in this tiny replay).
    yd = Decimal(str(y))
    jmax = min(k, int(yd))
    total = Decimal(0)
    denom = Decimal(math.factorial(k))
    for j in range(jmax + 1):
        term = Decimal(math.comb(k, j)) * (yd - j) ** k / denom
        total += -term if j % 2 else term
    return min(1.0, max(0.0, float(total)))


def kernel(u: float, b: float, k: int) -> float:
    """f = 1_[b,1-b] convolved with k uniforms on [-b/k,b/k]."""
    a = b / k
    def cdf_s(s: float) -> float:
        return irwin_hall_cdf((s + k * a) / (2.0 * a), k)
    return max(0.0, min(1.0, cdf_s(u - b) - cdf_s(u - (1.0 - b))))


def F(s: complex, b: float, k: int) -> complex:
    """Mellin-side transform of the kernel."""
    if abs(s) < 1e-12:
        box = 1.0 - 2.0 * b
        taper = 1.0
    else:
        box = (cmath.exp(s * (1.0 - b)) - cmath.exp(s * b)) / s
        z = b * s / k
        taper = cmath.sinh(z) / z if abs(z) > 1e-14 else 1.0
        taper = taper ** k
    return box * taper


def read_ordinates(path: str):
    values = []
    for line in pathlib.Path(path).read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        value = float(line)
        if not math.isfinite(value) or value <= 0 or (values and value <= values[-1]):
            raise ValueError(f"expected strictly increasing positive ordinates, found {line!r}")
        values.append(value)
    return values


def replay(x: int, right: int, ordinates: list[float], expect_above_one: bool, cells=False):
    h = right - x
    anchor = x + 0.5 if cells else x
    b = 1 / (16 * h) if cells else B
    delta = math.log1p(h / anchor)
    log_anchor = math.log(anchor)
    k = math.ceil(8.0 * log_anchor)
    primes, lam = primes_and_von_mangoldt(right)
    prime_set = set(primes)
    contributions = {
        n: weight * kernel(math.log1p((n - anchor) / anchor) / delta, b, k)
        for n, weight in lam.items() if x < n <= right
    }
    direct = math.fsum(weight for n, weight in contributions.items() if n in prime_set)
    proper_powers = math.fsum(weight for n, weight in contributions.items() if n not in prime_set)

    if cells:
        assert all(contributions[n] == lam[n] for n in contributions)
    cutoff = 4.0 * k / (b * delta)
    if not ordinates or ordinates[-1] < cutoff:
        raise ValueError(f"zero file does not reach T={cutoff:.6g} for ({x},{right}]")
    used = [t for t in ordinates if t <= cutoff]
    # The tabulated zeros at these heights have real part 1/2. Pair conjugates.
    zero_sum = 2.0 / math.sqrt(anchor) * math.fsum(
        (cmath.exp(1j * t * log_anchor) * F(delta * (0.5 + 1j * t), b, k)).real
        for t in used
    )
    trivial_zeros = 0.0
    for j in range(1, 10000):
        term = anchor ** (-2.0 * j) * F(-2.0 * j * delta, b, k).real
        trivial_zeros += delta * term
        if abs(term) < 1e-18:
            break
    statistic = delta * anchor * (F(delta, b, k).real - zero_sum) - trivial_zeros - proper_powers
    error = statistic - direct
    mode = "integer cells" if cells else "tapered"
    print(f"({x},{right}]  {mode}  T={cutoff:.2f}  ordinates={len(used)}  Z_T={zero_sum:.10g}")
    print(f"  prime weight={direct:.12g}  proper-power weight={proper_powers:.12g}"
          f"  A={statistic:.12g}  discrepancy={error:.3g}")
    if abs(error) > 1e-7 or (statistic > 1.0) != expect_above_one:
        raise AssertionError(f"finite prime statistic mismatch on ({x},{right}]")


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: check-zero-sum.py ODLYZKO_ZEROS")
    ordinates = read_ordinates(sys.argv[1])
    if not ordinates:
        raise SystemExit("zero file contained no positive ordinates")
    print(f"read {len(ordinates)} positive ordinates from {sys.argv[1]}")
    # (113,126] is composite; the next two windows contain 127, with 121 and
    # 125 also present in the longer one as proper prime powers.
    replay(113, 126, ordinates, False)
    replay(113, 127, ordinates, False)
    replay(113, 130, ordinates, True)
    replay(7, 10, ordinates, False, cells=True)
    replay(7, 11, ordinates, True, cells=True)


if __name__ == "__main__":
    main()
