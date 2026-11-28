# Counterexamples to Zaslavsky's negative-cycle packing conjecture

GitHoobar, with OpenAI Codex · 28 November 2026

Thomas Zaslavsky's Conjecture 5.4⁻ asserts that the maximum number of edge-disjoint negative cycles in a signed graph always attains the smaller of two upper bounds. The all-negative complete graph on five vertices refutes the assertion. A complete graph on seven vertices already gives a counterexample with both positive and negative triangles. An infinite family below has an exact deficit quadratic in the number of vertices. [Zaslavsky, §5.1, Conjecture 5.4⁻](https://doi.org/10.1016/j.akcej.2018.01.011)

**Earlier work and our contribution.** Guenin gave the negative packing number and frustration index for the five-vertex example in 2014. We exhibit the unsigned packing that completes its contradiction to Zaslavsky's later conjecture, give a mixed-sign counterexample on seven vertices, and prove exact formulas for all three quantities in the nine-class family. The finite-geometry constructions use the usual lines over fields of two and three elements. [Guenin's report](https://publications.mfo.de/bitstream/handle/mfo/3441/OWR_2014_51.pdf?isAllowed=y&sequence=1)

For a signed graph $\Sigma$ on an underlying graph $G$, write $\nu_-(\Sigma)$ for the maximum number of pairwise edge-disjoint negative simple cycles, $\nu(G)$ for the maximum number of pairwise edge-disjoint simple cycles of either sign, and $\ell(\Sigma)$ for the fewest edges whose deletion destroys all negative cycles. A cycle is negative when it has an odd number of negative edges. The conjectured identity is

$$\nu_-(\Sigma)=\min\{\ell(\Sigma),\nu(G)\}.$$

## Five vertices

Give every edge of $K_5$ a negative sign. Its negative cycles are exactly its odd cycles.

* **The unsigned packing number is three.** The cycles $(1,2,3)$, $(1,4,5)$, and $(2,4,3,5)$ partition the ten edges. Four cycles would require at least twelve edges.
* **The negative packing number is two.** The first two triangles give a packing. Three edge-disjoint odd cycles would all have to be triangles, since $3+3+5>10$. Their union would have even degree at every vertex. The complement of this union in the even-degree graph $K_5$ would also have even degrees, yet it would consist of just one edge.
* **The frustration index is four.** Destroying all odd cycles leaves a bipartite graph. A cut of $K_5$ contains at most $2\cdot3=6$ edges, and this bound is attained. Thus precisely $10-6=4$ deletions suffice.

The proposed equality reads $2=\min\{4,3\}=3$. Zaslavsky reports immediately after the conjecture that he had checked $K_5$. The two signed parameters of this example already appear in Bertrand Guenin's 2014 report on packing odd $T$-joins, where the all-negative $K_5$ is a standard obstruction. The additional unsigned parameter follows from the displayed cycle partition. [Guenin, *Packing odd T-joins with at most two terminals*, Oberwolfach Report 51/2014](https://publications.mfo.de/bitstream/handle/mfo/3441/OWR_2014_51.pdf?isAllowed=y&sequence=1)

## Seven vertices with mixed signs

Give one edge of $K_7$ a positive sign and all other edges a negative sign. Index vertices by the seven nonzero vectors of $\mathbf F_2^3$. Each edge $uv$ belongs to exactly one triangle $\{u,v,u+v\}$. These seven triangles partition all 21 edges, so the unsigned packing number is seven. Dropping the triangle containing the positive edge gives six negative triangles. A packing of seven negative cycles would have to partition the graph into triangles, but every triangle containing the positive edge is positive. Thus $\nu_-=6$.

The all-negative $K_7$ has frustration $21-3\cdot4=9$. Changing one edge sign changes the minimum by at most one: for any fixed division of the vertices into two parts, the number of edges inconsistent with positive edges within parts and negative edges across parts changes by exactly one. Minimizing this number gives frustration, since a graph is balanced precisely when it admits such a division. Taking a $3+4$ division with the positive edge inside one part attains eight. Hence $6<\min\{8,7\}$.

## A quadratic deficit on complete graphs

For any integer $d\ge1$, put $s=3^d$. Take the $9s$ points of $\mathbf F_3^{d+2}$ as vertices. Divide them into nine classes by their first two coordinates. An edge within a class is positive and an edge between classes is negative. Then

$$\nu_-=12s^2,\qquad \ell=16s^2,\qquad \nu=\frac{9s(9s-1)}{6}.$$

**Packings.** Every affine line consists of three points, and every pair of distinct points determines one line. The line triangles partition the edges and give the largest possible unsigned packing. Projection to the first two coordinates is either constant on a line or takes three distinct values. The latter lines partition the $\binom92 s^2=36s^2$ edges between classes into $12s^2$ negative triangles. Every negative cycle crosses between classes an odd number of times. A closed cycle cannot change classes just once, so it uses at least three of these edges. This proves optimality of the negative packing among cycles of **every length**.

**Frustration.** Take any edge set whose deletion makes the signed graph balanced. Choose one vertex uniformly and independently from each class. The induced transversal is an all-negative $K_9$, so it must lose at least $36-4\cdot5=16$ edges. Every deleted cross edge is selected with probability $1/s^2$. Taking expectations shows that at least $16s^2$ cross edges must be deleted. Conversely, divide the nine classes into groups of four and five. Delete the cross-class edges joining two classes in the same group. This deletes $(\binom42+\binom52)s^2=16s^2$ edges, and the remaining signing is balanced by the indicated two groups.

The conjectured right-hand side equals $\nu$. Its excess over the actual negative packing number is exactly

$$\nu-\nu_-=\frac{3s(s-1)}{2}.$$

For example, the 27-vertex graph packs 108 negative cycles, has frustration 144, and packs 117 cycles when signs are ignored. The formula proves that the discrepancy grows quadratically along the family.

## Verification and attribution

From the root of the repository run `python3 -B results/signed-cycle-packing/check.py`. The [standalone checker](check.py) enumerates all simple cycles and computes the two packing optima on $K_5$. It enumerates cuts on $K_5$ and the mixed $K_7$, verifies the edge partitions on all three graphs, and checks every cut of the 27-vertex example up to permutations of classes and of vertices within a class. The crossing-edge bound in the proof establishes the packing upper bound at 27 vertices and throughout the infinite family.

We found the conjecture in the published problem collection and the prior five-vertex packing obstruction in Guenin's report. A search of the author's publication entry, papers indexed as citing the problem collection, and indexed searches using the conjecture number and packing terminology did not turn up an explicit correction to Conjecture 5.4⁻ or this nine-class calculation. These searches do not establish priority. This is a public mathematical note awaiting independent review. [Author's publication entry](https://people.math.binghamton.edu/zaslav/Tpapers/index.html#NPC)
