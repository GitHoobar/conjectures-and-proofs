"""Exact certificates for the signed-cycle notes. Python 3.8+, standard library."""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, factorial


def edges(pairs):
    return {tuple(sorted(edge)) for edge in pairs}


BASE = edges([(0, 5), (0, 6), (1, 5), (1, 7), (2, 6), (2, 7)])
BASE_A = BASE | {(5, 7)}
BASE_B = BASE | {(3, 7)}
CORE = edges([(0, 4), (0, 5), (0, 6), (1, 5), (1, 7), (2, 6),
              (2, 7), (4, 5), (5, 7), (6, 7)])
A = CORE | {(3, 6), (4, 7)}
B = CORE | {(1, 6), (3, 7)}


def cycles(n, k):
    for vertices in combinations(range(n), k):
        for tail in permutations(vertices[1:]):
            if tail[0] < tail[-1]:
                seq = vertices[:1] + tail
                yield edges((seq[i-1], seq[i]) for i in range(k))


def direct_vector(n, negative):
    return tuple(sum(len(c & negative) % 2 for c in cycles(n, k))
                 for k in range(3, n + 1))


def triangles_and_degrees(negative):
    triangles = [v for v in combinations(range(8), 3)
                 if len(negative.intersection(combinations(v, 2))) % 2]
    return sorted((sum(i in edge for edge in negative),
                   sum(i in t for t in triangles)) for i in range(8))


def inventory(negative):
    forests, rings = Counter(), Counter()
    for size in range(1, len(negative) + 1):
        for subset in combinations(negative, size):
            neighbors = {}
            for i, j in subset:
                neighbors.setdefault(i, set()).add(j)
                neighbors.setdefault(j, set()).add(i)
            if any(len(adj) > 2 for adj in neighbors.values()):
                continue
            remaining = set(neighbors)
            components = 0
            while remaining:
                stack = [remaining.pop()]
                components += 1
                while stack:
                    new = neighbors[stack.pop()] & remaining
                    remaining -= new
                    stack.extend(new)
            if len(neighbors) == size + components:
                forests[size, components] += 1
            elif components == 1 and len(neighbors) == size:
                rings[size] += 1
    return forests, rings


def safe_comb(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def inventory_vector(n, inv):
    forests, rings = inv
    values = []
    for k in range(3, n + 1):
        n_ways = comb(n, k) * factorial(k - 1) // 2
        total = n_ways
        for (m, p), count in forests.items():
            if m + p > k:
                continue
            multiplier = 2**(p - 1) * factorial(k - m - 1) * comb(n-m-p, k-m-p)
            total += count * (-2)**m * multiplier
        total += (-2)**k * rings[k]
        assert (n_ways - total) % 2 == 0
        values.append((n_ways - total) // 2)
    return tuple(values)


def check_pair():
    assert direct_vector(8, BASE_A) == direct_vector(8, BASE_B) == (26, 110, 336, 840, 1440, 1264)
    assert sorted(b for _, b in triangles_and_degrees(BASE_A)) != sorted(b for _, b in triangles_and_degrees(BASE_B))
    inv = inventory(A)
    assert inv == inventory(B)
    forest, ring = inv
    print("Forest rows:", [[forest[m, p] for p in range(1, 5)] for m in range(1, 8)])
    print("Cycle row:", [ring[k] for k in range(3, 9)])
    for n in (8, 9):
        for core in (A, B):
            assert direct_vector(n, core) == inventory_vector(n, inv)
    data_a, data_b = map(triangles_and_degrees, (A, B))
    for power, expected in [(1, [0, 0]), (2, [0, 0, 0]), (3, [0, 96, 0, 0])]:
        coeff = [comb(power, j) * (sum(d**j * b**(power-j) for d, b in data_a)
                                   - sum(d**j * b**(power-j) for d, b in data_b))
                 for j in range(power + 1)]
        assert coeff == expected
    print("Triangle data:", data_a, data_b)
    print("Cubic difference coefficients:", coeff)


def check_membership(n, underlying):
    ordered = sorted(underlying)
    cycle_masks = []
    for k in range(3, n + 1):
        for c in cycles(n, k):
            if c <= underlying:
                cycle_masks.append((k, sum(1 << i for i, edge in enumerate(ordered) if edge in c)))
    sizes = sorted({k for k, _ in cycle_masks})
    totals = [sum(k == ell for k, _ in cycle_masks) for ell in sizes]
    def weight_vector(bits):
        return tuple(sum(bit for (k, _), bit in zip(cycle_masks, bits) if k == ell) for ell in sizes)
    def parity(x):
        return bin(x).count("1") % 2
    observed = Counter()
    for signs in range(1 << len(ordered)):
        observed[weight_vector([parity(signs & mask) for _, mask in cycle_masks])] += 1
    dependencies = Counter()
    for bits in product((0, 1), repeat=len(cycle_masks)):
        boundary = 0
        for bit, (_, mask) in zip(bits, cycle_masks):
            if bit:
                boundary ^= mask
        if boundary == 0:
            dependencies[weight_vector(bits)] += 1
    def kraw(j, d, m):
        return sum((-1)**a * safe_comb(d, a) * safe_comb(m-d, j-a) for a in range(j+1))
    tested = 0
    for x in product(*(range(m+1) for m in totals)):
        numerator = 0
        for counts, multiplicity in dependencies.items():
            term = multiplicity
            for j, d, m in zip(x, counts, totals):
                term *= kraw(j, d, m)
            numerator += term
        assert numerator * (1 << len(ordered)) == observed[x] * (1 << len(cycle_masks))
        tested += 1
    print("Membership exact on graph with", len(ordered), "edges and", tested, "candidate vectors")


if __name__ == "__main__":
    check_pair()
    for n, graph in [(4, edges(combinations(range(4), 2))),
                     (5, edges((i,j) for i in range(2) for j in range(2,5))),
                     (4, {(0,1), (2,3)})]:
        check_membership(n, graph)
