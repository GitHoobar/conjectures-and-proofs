"""Expand products directly in the standard Hecke basis of a universal group."""
from collections import Counter


def check(endpoints, weights, spacers, spacer_weight, expected):
    word = []
    for i, s in enumerate(endpoints):
        if i:
            for j in range(spacers):
                word.append(((i, j), spacer_weight))
        word.append((s, weights[s]))
    states = Counter({((), 0): 1})
    for s, weight in word:
        following = Counter()
        for (stack, exponent), count in states.items():
            descent = bool(stack and stack[-1] == s)
            moved = stack[:-1] if descent else stack + (s,)
            following[moved, exponent] += count
            following[stack, exponent + (-weight if descent else weight)] += count
        states = following
    top = tuple(s for s, _ in word)
    length = sum(weight for _, weight in word)
    assert states[top, 0] == 1
    assert all(exponent > 0 for (state, exponent) in states if state != top)
    at_identity = {exponent: count for (state, exponent), count in states.items() if not state}
    assert at_identity == {length - 2*degree: count for degree, count in expected.items()}
    print("Endpoints", endpoints, "weights", weights, "polynomial", expected)


if __name__ == "__main__":
    check("", {}, 0, 1, {0: 1})
    check("aa", {"a": 1}, 2, 1, {0: 1, 1: 1})
    check("abab", {"a": 1, "b": 1}, 2, 1, {0: 1, 1: 2})
    check("abba", {"a": 1, "b": 1}, 2, 1, {0: 1, 1: 2, 2: 1})
    check("abcabc", {"a": 2, "b": 2, "c": 5}, 1, 19, {0: 1, 2: 2, 5: 1})
    check("abba", {"a": 2, "b": 3}, 1, 11, {0: 1, 2: 1, 3: 1, 5: 1})
