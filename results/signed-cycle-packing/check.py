"""Exact finite certificates for the signed-cycle packing manuscript. Python 3."""

from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations, product


def check_equal(label, actual, expected):
    if actual != expected:
        raise ValueError(f"{label}: computed {actual}, expected {expected}")


def cycle_edges(cycle):
    return frozenset(tuple(sorted((u, v))) for u, v in zip(cycle, cycle[1:] + cycle[:1]))


def simple_cycles(vertices):
    for length in range(3, len(vertices) + 1):
        for first, *others in combinations(vertices, length):
            for tail in permutations(others):
                if tail[0] < tail[-1]:  # Choose one of the two orientations.
                    yield cycle_edges((first,) + tail)


def packing_number(cycles):
    # For each realizable union of edges store its maximum packing size.
    best = {frozenset(): 0}
    for cycle in cycles:
        for used, size in list(best.items()):
            if used.isdisjoint(cycle):
                union = used | cycle
                best[union] = max(size + 1, best.get(union, 0))
    return max(best.values())


def cut_minimum(vertices, negative):
    edges = list(combinations(vertices, 2))
    return min(
        sum(((u in side) != (v in side)) != ((u, v) in negative) for u, v in edges)
        for size in range(len(vertices) + 1)
        for side in combinations(vertices, size)
    )


def verify_partition(vertices, cycles):
    counts = Counter(edge for cycle in cycles for edge in cycle)
    check_equal("edge partition", counts, Counter(combinations(vertices, 2)))


def check_five():
    vertices = list(range(1, 6))
    edges = set(combinations(vertices, 2))
    cycles = list(simple_cycles(vertices))
    check_equal("cycles by length", Counter(map(len, cycles)), {3: 10, 4: 15, 5: 12})
    negative = [c for c in cycles if len(c & edges) % 2]
    values = packing_number(negative), cut_minimum(vertices, edges), packing_number(cycles)
    check_equal("all-negative K5", values, (2, 4, 3))
    verify_partition(vertices, map(cycle_edges, [(1, 2, 3), (1, 4, 5), (2, 4, 3, 5)]))
    return values


def check_seven():
    vertices = list(range(1, 8))
    positive_edge = (1, 2)
    negative = set(combinations(vertices, 2)) - {positive_edge}
    triangles = [cycle_edges(t) for t in combinations(vertices, 3)]
    lines = [cycle_edges((a, b, c)) for a, b, c in combinations(vertices, 3) if a ^ b == c]
    verify_partition(vertices, lines)
    negative_lines = [line for line in lines if len(line & negative) % 2]
    # Seven cycles would consume all 21 edges as triangles, including the positive edge.
    check_equal("negative triangles using positive edge",
                sum(positive_edge in t and len(t & negative) % 2 for t in triangles), 0)
    values = len(negative_lines), cut_minimum(vertices, negative), len(lines)
    check_equal("mixed K7", values, (6, 8, 7))
    return values


def check_twenty_seven():
    vertices = list(product(range(3), repeat=3))
    lines = []
    for u, v in combinations(vertices, 2):
        w = tuple((-a - b) % 3 for a, b in zip(u, v))
        if v < w:  # Emit each line at its two smallest points.
            lines.append(cycle_edges((u, v, w)))
    verify_partition(vertices, lines)
    cross_counts = Counter(sum(u[:2] != v[:2] for u, v in line) for line in lines)
    check_equal("line types by number of cross edges", cross_counts, {0: 9, 3: 108})

    # A cut is determined up to graph symmetry by its sorted counts on the nine classes.
    # Internal positive edges are frustrated across the cut, cross-class negative
    # edges on the same side. This exhaustive calculation is independent of the
    # random-transversal lower bound in the proof.
    costs = []
    for side in combinations_with_replacement(range(4), 9):
        within = sum(a * (3 - a) for a in side)
        between = sum(a * b + (3 - a) * (3 - b) for a, b in combinations(side, 2))
        costs.append(within + between)
    values = cross_counts[3], min(costs), len(lines)
    check_equal("nine-class K27", values, (108, 144, 117))
    return values


if __name__ == "__main__":
    print("Graph: negative packing, frustration, unsigned packing")
    for name, verify in [("K5", check_five), ("K7", check_seven), ("K27", check_twenty_seven)]:
        print(f"{name}: {verify()}")
