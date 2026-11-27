# What negative cycle counts determine about a signed graph

Research note, 27 November 2026. Prepared with Codex for GitHoobar. Public research draft.

Give each edge of a finite simple graph a sign. The sign of a simple undirected cycle is the product of its edge signs. The negative cycle vector lists the number of negative cycles of each length. Switching at a vertex reverses the signs of its incident edges and preserves every cycle sign. Switching isomorphism allows any sequence of switches and a relabeling of vertices.

Alex Schaefer and Thomas Zaslavsky ask several distinct questions about these vectors. Below are proofs of their dimension conjecture and their conjecture on indistinguishable pairs, an exact membership test for their characterization question, and bounds addressing their open asymptotic question. The conjecture numbers and the asymptotic question refer to the 2019 journal version. [Original paper, sections 4.1 and 5](https://dlib.si/stream/URN%3ANBN%3ASI%3ADOC-FLBNZGZF/1722aafb-6ba1-4807-8df6-8c905b4c01c4/PDF) · [Publisher DOI](https://doi.org/10.26493/1855-3974.1605.43f)

The companion paper gives an exponential strengthening of the pair construction. At 181 vertices it gives 1,048,576 inequivalent signings with the same negative cycle counts at every length. [General theorem and proof](multiplicity.md)

## The dimension conjecture

**Theorem 1 (Schaefer's Conjecture 1.1).** For every finite simple graph, the dimension of the real span of its negative cycle vectors equals the number of distinct lengths of its cycles.

**Proof.** Write $m_k$ for the number of cycles of length $k$, and keep precisely the coordinates with $m_k>0$. Suppose a linear functional with coefficients $a_k$ vanishes on every negative cycle vector. Choose edge signs independently, each with mean $t$, for any real $-1<t<1$. A $k$-cycle then has mean sign $t^k$, so its probability of being negative is $(1-t^k)/2$. Taking the expectation of the functional gives
$$\sum_k a_k m_k(1-t^k)=0.$$
This is a polynomial identity on an interval. For each cycle length $k$, its coefficient of $t^k$ is $-a_km_k$, so $a_k=0$. The span has trivial annihilator, proving the claim. For a forest both dimensions are zero. The all-positive signing gives the zero vector, so the affine dimension agrees as well. ∎

One can extract an explicit linear certificate. Fix any one cycle $C$ of length $k$. Average the negative cycle vector multiplied by the sign of $C$ over independent uniform edge signs. Distinct cycles have distinct edge sets, so the product of their signs has mean zero. The resulting vector is exactly $-e_k/2$. This gives a second proof using each coordinate separately.

## Two indistinguishable signings at every order

**Theorem 2 (Schaefer–Zaslavsky Conjecture 5.1).** For every $n\ge8$ there are two switching-nonisomorphic signings of $K_n$ with identical negative cycle vectors. For $n>8$, any prescribed signing on the remaining $n-8$ vertices can occur as the same induced signing in both examples.

### An inventory that survives extension

Let $F$ be the graph of negative edges in a signing of $K_n$. Define $f_{m,p}(F)$ to be the number of edge subsets forming a disjoint union of $p$ nonempty paths with $m$ edges in total. Ignore isolated vertices. Let $c_k(F)$ count undirected simple $k$-cycles in $F$.

These two inventories determine every negative cycle count. For a $k$-cycle $C$, expand its sign as the product of $1-2\mathbf1_{e\in F}$ over its edges. A nonempty proper subset of the edges of $C$ is a linear forest. A specified linear forest with $m$ edges and $p$ paths uses $m+p$ vertices. If $m+p\le k$, it occurs in
$$2^{p-1}(k-m-1)!\binom{n-m-p}{k-m-p}$$
undirected $k$-cycles. Choose the remaining vertices and contract each oriented path to a block. The $k-m$ blocks have $(k-m-1)!$ directed cyclic orders, the paths have $2^p$ orientations, and reversing the resulting cycle identifies exactly two directed traversals because $k\ge3$. This derivation also covers a single path on all $k$ vertices.

Write $T_k=\binom nk(k-1)!/2$. Summing the expansion over cycles gives the sum $S_k$ of their signs:
$$S_k=T_k+
\sum_{m,p\ge1,\ m+p\le k}(-2)^m f_{m,p}(F)\,2^{p-1}(k-m-1)!\binom{n-m-p}{k-m-p}
+(-2)^k c_k(F).$$
The negative count is $(T_k-S_k)/2$. The last summand records the choice of the whole cycle. This is the edge-subset counting principle of section 3 of the source paper, specialized to an inventory suitable for extensions.

### A certificate on eight vertices

Use vertices $0,\ldots,7$. Write $ij$ for one undirected edge. Set
$$D=\{04,05,06,15,17,26,27,45,57,67\},\quad
A=D\cup\{36,47\},\quad B=D\cup\{16,37\}.$$
The two negative graphs have the same forest inventory. All nonzero possibilities are in the following table.

| Edges $m$ | One path | Two paths | Three paths | Four paths |
|---:|---:|---:|---:|---:|
| 1 | 12 | 0 | 0 | 0 |
| 2 | 30 | 36 | 0 | 0 |
| 3 | 56 | 116 | 24 | 0 |
| 4 | 83 | 182 | 50 | 1 |
| 5 | 82 | 143 | 24 | 0 |
| 6 | 41 | 33 | 0 | 0 |
| 7 | 4 | 0 | 0 | 0 |

Their cycle counts for lengths $3,4,5,6,7,8$ are respectively $(4,4,6,4,1,0)$. The table can be audited with 4,096 subsets per graph. Discard a subset if any degree exceeds two. If $v$ vertices are incident with the subset and it has $p$ components, count it as a forest if $v=m+p$, or as a cycle if $p=1$ and $v=m$. These operations are implemented in the accompanying checker.

Take a negative graph $H$ on $t=n-8$ new vertices. Use $A\sqcup H$ and $B\sqcup H$, so all edges between the two vertex sets are positive. Forest inventories, with the empty forest included, multiply as polynomials in markers for edges and components. Cycle inventories add. Thus the extensions have identical negative cycle vectors for every $H$.

To distinguish them, let $b_i$ be the number of negative triangles through vertex $i$ in the eight-vertex core and $d_i$ its negative degree. The following multisets of $(d_i,b_i)$ are obtained directly by testing each of the 56 triples.

| Core | Pairs with multiplicity |
|---|---|
| $A$ | $(1,11),(2,10),(2,10),(3,9),(3,11),(4,10),(4,14),(5,9)$ |
| $B$ | $(1,9),(2,10),(2,14),(3,9),(3,11),(4,10),(4,10),(5,11)$ |

Write $h=|E(H)|$. In an extension each core vertex belongs to $b_i+t d_i+h$ negative triangles. Each new vertex $j$ belongs to $12+8d_H(j)+b_H(j)$ negative triangles in either signing. From the table the differences (core $A$ minus core $B$) between the sums of first, second and third powers of $b_i+t d_i$ are respectively $0,0,96t$. Expanding the cube after adding $h$ therefore leaves the difference $96t$. The sum over all vertices of the cubes of their negative triangle counts is a switching-isomorphism invariant. It separates the two extensions for every $t>0$.

For $n=8$ the original paper already gives Greaves's example. Here is an independently checkable base certificate. Start with $J=\{05,06,15,17,26,27\}$ and use $J\cup\{57\}$ and $J\cup\{37\}$. Both cycle vectors are $(26,110,336,840,1440,1264)$. The sorted negative triangle counts by vertex are $(7,7,9,9,11,11,12,12)$ and $(7,8,9,9,11,11,11,12)$. Direct enumeration suffices for this base. The identity $96t$ and the common inventory prove all larger orders. ∎

## Which vectors are attainable?

Section 5.4 asks which integral vectors are realized. The following exact test takes as input only the unsigned graph and the proposed vector. It counts signings even when several cycles of the same length share edges.

Let $M=\sum_k m_k$. A *cycle dependency* is any subset $D$ of the graph's simple cycles in which each edge occurs an even number of times. Let $d_k(D)$ count selected $k$-cycles. Define
$$K_j(d;m)=[z^j](1-z)^d(1+z)^{m-d}.$$
For $0\le x_k\le m_k$, the number of signings with negative cycle vector $x$ is exactly
$$2^{|E|-M}\sum_{D\text{ a cycle dependency}}\prod_k K_{x_k}(d_k(D);m_k).$$
In particular, $x$ is attainable exactly when this sum is positive. Coordinates outside their indicated ranges are impossible.

**Proof.** Use independent uniform edge signs. If $s_C$ is the sign of cycle $C$, the generating factor for its negative indicator is $((1+z_k)+(1-z_k)s_C)/2$. Multiply these factors over all cycles. On taking expectation a selected product of signs contributes one exactly when each edge occurs evenly, and zero otherwise. Extract the coefficient of $\prod_k z_k^{x_k}$ and multiply the probability by $2^{|E|}$. ∎

This is a specialization of the partition weight enumerator form of the MacWilliams transform. The criterion can be expensive to evaluate: there may be exponentially many dependencies even in the number of cycles. It provides an algebraic membership condition and an exact multiplicity. A simpler structural description of the attainable integer points would be a stronger result. [MacWilliams identities for partition enumerators](https://trumpf.id.au/UH60Festschrift.pdf)

To compute the sum from a supplied cycle list, row-reduce its cycle-by-edge incidence matrix over the binary field and enumerate a basis expansion of its left kernel. If that kernel has dimension $r$, there are $2^r$ terms. When $r=0$ every vector in the coordinate box is attainable. There is also a simple exact criterion when the only nonempty dependency is $D$. For each length $k$, form the interval of integers
$$\max(0,x_k-m_k+d_k(D))\ \le j_k\le\ \min(x_k,d_k(D)).$$
The vector is attainable exactly when the sum of these intervals contains an even integer. Indeed, $j_k$ is the possible number of selected negative $k$-cycles in $D$. Over the binary field the column space is the orthogonal complement of the left kernel, so even total parity on $D$ is the sole restriction on selecting the negative cycles in this case. This gives an interval test without enumerating signings.

## The harder asymptotic question

Let $I_n$ be the number of switching-isomorphism types of signed complete graphs, and $V_n$ the number of different negative cycle vectors. Section 5.5 asks whether $V_n/I_n\to1$, and if that fails, whether the ratio tends to zero. I found no published bound addressing this limit directly in the sources searched. The following attempts cover unrestricted graph orders.

**How far do the constructed collisions reach?** Let $M_n$ count the types whose vector occurs for at least two types. For $n\ge9$, Theorem 2 gives
$$I_n-V_n\ \ge\ M_n/2\ \ge\ I_{n-8}/\bigl(2\binom n8\bigr).$$
Indeed every signed tail type occurs as an induced restriction of a colliding type. One type on $n$ vertices can supply at most $\binom n8$ distinct tail types. A fiber of size $a\ge2$ contributes $a-1\ge a/2$ to the deficit. The resulting lower bound on the deficit does not decide its size relative to $I_n$.

**How much information can short cycles supply?** For $3\le k\le m$ the $k$th count has at most $1+n^k$ values. The number of possible truncated vectors therefore has base-two logarithm at most $m+\frac12 m(m+1)\log_2 n$. On the other hand there are $2^{\binom{n-1}{2}}$ labeled switching classes (switch all edges incident with one chosen vertex positive), and at most $n!$ labelings per type. Thus $\log_2 I_n\ge\binom{n-1}{2}-\log_2(n!)$. For any fixed $0<\epsilon<1$, if $m\le(1-\epsilon)n/\sqrt{\log_2 n}$, the number of truncated vectors divided by $I_n$ tends to zero exponentially in $n^2$. The unrestricted question uses all cycle lengths. Neither argument determines that limit.

## Provenance and verification

The dimension conjecture had published graph-family cases. The collisions conjecture had Greaves's eight-vertex witness. The authors describe earlier constraints for complete graphs in section 5.4 and say they knew no partial results for other graphs *on that characterization question*. Their section 5.5 poses the limiting-ratio question separately. The full dimension argument and arbitrary-tail construction here address the two numbered conjectures without a bound on the graph order.

On 27 November 2026 I checked the journal paper, the authors' preprint and publication pages, Zaslavsky's problem collection, the indexed citing work in OpenAlex, and searches combining the titles and authors with “proof”, “dimension”, “orthogonality”, “negative circle vectors”, “same negative cycle vector”, “switching isomorphism”, and “collapsing pairs”. I found no earlier general solution to either numbered conjecture. Bibliographic coverage is incomplete. Both proofs await independent expert review. The scope of the Lean check is specified below. [Author preprint](https://arxiv.org/abs/1706.09041) · [Zaslavsky's problem collection](https://doi.org/10.1016/j.akcej.2018.01.011) · [Indexed citing works](https://api.openalex.org/works?filter=cites:W2731748107)

The extension cores were found by grouping small unlabeled graphs by path and cycle inventories using Brendan McKay's graph data. The search proposed candidates. The named edge sets, the two finite tables, the invariant and the extension argument are the proof. The ordinary eight-vertex case was checked separately. [Graph data](https://users.cecs.anu.edu.au/~bdm/data/graphs.html)

Run `python3 check.py` with Python 3.8 or newer. The script checks the inventory against a second direct cycle-count implementation at orders eight and nine, checks the polynomial coefficients symbolically, verifies the separate eight-vertex witness and compares the membership formula to all signings on three graphs.

The accompanying Lean file proves `NegativeCycle.full_span` for any family of distinct finite edge sets, grouped into labels, provided each label occurs on a nonempty member. For simple cycles take each member to be its edge set and use its length as label. If there are no occurring lengths, the coordinate space is zero. The file defines the signed products and the count vector, proves character orthogonality, and concludes that the real span is the entire coordinate space. The identification of undirected graph cycles with their edge sets is made in the prose. The [verification guide](../../VERIFYING.md#lean) gives the command and pinned Mathlib environment for Lean 4.33.1. The kernel accepted the theorem with exactly `propext`, `Classical.choice` and `Quot.sound`. The pair construction has a mathematical proof and Python certificate, and has not been formalized in Lean.
