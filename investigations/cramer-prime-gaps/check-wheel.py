"""Check the finite interpolation and wheel identities exactly with rational masses."""
from fractions import Fraction
from math import comb, gcd, lcm, prod


def modified_binomial(m, rho, k):
    """Return reference and perturbed count laws for m eligible positions."""
    mu = m * rho
    assert 0 < rho <= Fraction(1, 2) and 1 <= k <= mu / 4
    masses = [comb(m, y) * rho**y * (1 - rho)**(m - y) for y in range(m + 1)]
    start = int(mu)
    nodes = list(range(start, start + k + 1))
    weights = [
        prod(Fraction(-b, a - b) for b in nodes if b != a)
        for a in nodes
    ]
    for degree in range(k + 1):
        expected = int(degree == 0)
        assert sum(w * a**degree for w, a in zip(weights, nodes)) == expected

    delta = min(masses[a] / w for a, w in zip(nodes, weights) if w > 0)
    changed = masses.copy()
    changed[0] += delta
    for a, w in zip(nodes, weights):
        changed[a] -= delta * w
    assert min(changed) >= 0 and sum(changed) == 1 and changed[0] > masses[0]
    return masses, changed


def pattern_probability(masses, hits, misses):
    """Probability of a specified binary pattern under uniform sampling at fixed count."""
    m = len(masses) - 1
    return sum(
        masses[y] * Fraction(comb(m - hits - misses, y - hits), comb(m, y))
        for y in range(hits, m - misses + 1)
    )


def check_interpolation():
    for m, rho, k in [(24, Fraction(1, 3), 2), (40, Fraction(2, 5), 4),
                       (48, Fraction(7, 24), 3), (31, Fraction(2, 7), 2)]:
        reference, changed = modified_binomial(m, rho, k)
        for s in range(k + 1):
            for hits in range(s + 1):
                misses = s - hits
                expected = rho**hits * (1 - rho)**misses
                assert pattern_probability(reference, hits, misses) == expected
                assert pattern_probability(changed, hits, misses) == expected
        print(f"m={m}, rho={rho}, k={k}: every mixed pattern agrees. "
              f"Empty probability increases by a factor of {float(changed[0] / reference[0]):.2f}.")


def phi(n):
    return sum(gcd(i, n) == 1 for i in range(n))


def check_wheel():
    w = 2 * 3 * 5 * 7
    for q in [1, 4, 9, 10, 14, 21, 35]:
        period = lcm(w, q)
        for a in range(q):
            if gcd(a, q) == 1:
                count = sum(gcd(n, w) == 1 and n % q == a for n in range(period))
                assert Fraction(count, period) == Fraction(phi(w), w * phi(q))
    print("The progression density agrees over each full wheel period.")


if __name__ == "__main__":
    check_interpolation()
    check_wheel()
