"""Exhaustive finite checks of the alignment lemmas on marking patterns."""
from fractions import Fraction
from itertools import accumulate, product


def check_suffix_maxima(bits, slope):
    counts = list(accumulate(bits, initial=0))
    # Work in integer units of 1 / slope.denominator throughout.
    step = slope.numerator
    path = [count * slope.denominator - step * j for j, count in enumerate(counts)]
    maxima = list(reversed(list(accumulate(reversed(path), max))))
    drops = [j for j in range(len(bits)) if maxima[j] > maxima[j + 1]]
    assert step * len(drops) >= maxima[0] - maxima[-1] >= path[0] - path[-1]
    for j in drops:
        assert maxima[j] == path[j]
        assert 0 < maxima[j] - maxima[j + 1] <= step
        for v in range(len(bits) - j):
            for h in range(1, len(bits) - j - v + 1):
                count = counts[j + v + h] - counts[j + v]
                assert count * slope.denominator <= step * (h + v)


def check_sliding_windows(bits):
    counts = list(accumulate(bits, initial=0))
    for h in range(1, len(bits) + 1):
        windows = [counts[s + h] - counts[s] for s in range(len(bits) - h + 1)]
        assert set(windows) == set(range(min(windows), max(windows) + 1))
        for s, original in enumerate(windows):
            for k in range(min(h, len(windows) - s - 1) + 1):
                common = set.intersection(*[
                    {n for n in range(t, t + h) if bits[n]}
                    for t in range(s, s + k + 1)
                ])
                leaving = counts[s + k] - counts[s]
                entering = counts[s + h + k] - counts[s + h]
                assert len(common) == original - leaving
                assert max(windows[s:s + k + 1]) <= original + entering
                assert (max(windows[s:s + k + 1]) == 0) == (counts[s + h + k] == counts[s])


if __name__ == "__main__":
    for size in range(1, 10):
        for bits in product((0, 1), repeat=size):
            for slope in (Fraction(1, 4), Fraction(2, 5), Fraction(3, 4)):
                check_suffix_maxima(bits, slope)
            check_sliding_windows(bits)
    print("Verified suffix maxima, crossings, shared intersections, and exact empty runs.")
