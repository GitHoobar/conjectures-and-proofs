# Exponentially many signed complete graphs with identical cycle counts

GitHoobar · Research draft developed with OpenAI Codex · 27 November 2026

Put a plus or minus sign on each edge of a complete graph. A cycle is negative if the product of its edge signs is negative. Count negative simple cycles separately at every length. How many different signings can give exactly the same answers? We identify signings related by relabeling vertices or switching signs across a cut. Either operation preserves the counts.

**Theorem.** For every integer $n\ge41$, there is a single negative cycle vector shared by at least $2^{\lfloor(n-1)/9\rfloor}$ switching-isomorphism classes on $n$ vertices. Each bit in the construction is a recoverable choice of one of two graphs.

Schaefer and Zaslavsky's Conjecture 5.1 asks for a pair at every order from eight onward. Their paper credits Gary Greaves for the eight-vertex example. Our companion note treats every order in that conjecture. The theorem here concerns the maximum number of classes that a single vector can represent. The question in the same paper about how often counts distinguish a *typical* class is addressed separately below. [Original paper, section 5.5](https://doi.org/10.26493/1855-3974.1605.43f) · [Eight-vertex graphs, inventory and proof](README.md#two-indistinguishable-signings-at-every-order)

## Replacing a block

In a signing, let $X$ be eight vertices. Suppose each outside vertex has the same sign on all its edges into $X$. The sign may depend on the outside vertex. Replacing the negative edges inside $X$ from $A$ to $B$ below preserves the entire negative cycle vector.

Write $ij$ for the edge joining vertices $i,j$ among $0,\ldots,7$. Let
$$D=\{04,05,06,15,17,26,27,45,57,67\},\qquad
A=D\cup\{36,47\},\quad B=D\cup\{16,37\}.$$
Switch all outside vertices whose edges to $X$ are negative. Every edge across the boundary of $X$ is now positive. The two resulting negative graphs are disjoint unions $A\sqcup H$ and $B\sqcup H$, with precisely the same $H$. The certificate in the companion note counts equally many linear forests of every edge count and component count in $A$ and $B$, and equally many cycles of each length. For disjoint unions the forest inventories multiply and the cycle inventories add. Expanding the cycle sign as a product over its edges then gives identical signed cycle sums, hence identical negative counts, at every length. Switching back preserves the equality. This argument works for arbitrary signs in the rest of the graph. [Inventory table and counting formula](README.md#an-inventory-that-survives-extension)

## Encoding and recovering a binary string

Set $k=\lfloor(n-1)/9\rfloor$. Construct the ordinary graph of negative edges as follows.

1. Start with a path of $k$ vertices, called anchors. Attach a single marker leaf to its first vertex.
2. Give each anchor eight private vertices inducing $A$ or $B$, according to its bit. Join that anchor to all eight. Use no other negative edges incident to these private vertices.
3. Add $n-9k-1$ isolated vertices. In the signed complete graph every edge outside this negative graph is positive.

Each private block satisfies the replacement condition. Any two binary strings differ in a sequence of single-block replacements, so they produce the same negative cycle vector.

To distinguish the strings, first observe a general fact. If two negative graphs on $n$ vertices each have maximum degree at most $d$ and $n>4d$, then switching isomorphism between them implies ordinary graph isomorphism. Indeed, any nontrivial switch is across a cut. A vertex on the smaller side acquires at least $\lceil n/2\rceil-d>d$ negative neighbors on the other side. Relabeling preserves this high degree.

In our construction each anchor has degree 9 or 10, each private vertex has degree between 2 and 6, and the marker is the only degree-one vertex. The degree bound applies with $d=10$. Inside the ordinary negative graph, the anchors are recognizable by degree and their path is oriented by its marked endpoint. At each anchor remove its path neighbors and the marker from its neighbor set. The remaining induced graph tells us the bit: $A$ and $B$ each have a unique leaf, whose neighbor has internal degree four in $A$ and five in $B$. Thus ordinary isomorphism recovers every bit in order. The $2^k$ strings represent $2^k$ distinct switching-isomorphism classes. ∎

## Why this construction leaves the typical-case question open

The following calculation tests whether the same block replacement might prove that most classes collide. It gives the opposite outcome for the *availability of this construction*.

Call an eight-vertex set usable if its cross-edge signs can be switched into the form required by the replacement lemma, without imposing any condition on its internal signs. Equivalently, its rectangular array of cross-edge signs factors as $a_i b_j$ with one sign per inside vertex and one per outside vertex. This condition is invariant under switching and relabeling when asking if *some* set is usable. In a uniform random labeled signing the probability for a fixed set is exactly $2^{-7(n-9)}$ for $n>8$. There are $8(n-8)$ independent signs and $2^{n-1}$ distinct factorizable arrays, since simultaneous negation of all factors changes nothing. The union bound over $\binom n8$ choices tends to zero.

This also holds for a uniformly chosen **switching-isomorphism type**, where orbit sizes need care. First quotient by switching only. The resulting labeled classes have equal size, since the cut group has size $2^{n-1}$ and acts freely. To transfer the bound through vertex relabelings, we show that the sum of fixed-class proportions over all nonidentity permutations is $o(1)$.

For a permutation moving $s$ vertices, a class is fixed if its representative is taken to itself followed by a switch. Any two fixed vertices have unchanged edge sign, so the switch must be constant on all fixed vertices. Modulo complement, at most $2^s$ switches are possible (also valid with zero or one fixed vertex). For a given switch, the signs along each orbit of unordered edges are determined by one sign, or are inconsistent. If there are $o$ edge orbits among $N=\binom n2$ edges, the fixed-class proportion is at most $2^{s-(N-o)}$. At most $\binom{n-s}{2}+s/2$ edges are individually fixed. Each remaining orbit has length at least two. Therefore
$$N-o\ge s(2n-s-2)/4\ge s(n-2)/4.$$
There are at most $n^s$ permutations with this support size. Summing over $2\le s\le n$ is bounded by a geometric series with ratio $n\,2^{1-(n-2)/4}$, which tends to zero. Burnside's lemma for the invariant event and for the whole set now gives the claim: the identity term of the numerator has proportion $o(1)$ and all other terms together have proportion $o(1)$ relative to the unrestricted identity term.

Consequently almost every switching-isomorphism type lacks even a candidate block for this replacement. Whether a typical type has another, entirely different signing with its cycle counts remains unresolved here. The exponential lower bound concerns a single worst-case vector at each order.

## Verification, credit and status

GitHoobar and Codex developed the block construction from the signed-graph work in the companion note. Schaefer and Zaslavsky posed the original pair conjecture and supplied the edge-subset method. The core search used McKay's unlabeled graph data. Searches on 27 November 2026 for “negative cycle vectors”, “collapsing pairs”, “same negative cycle vector”, “switching isomorphism” and exponential multiplicity returned the original paper and related work. I found no earlier proof of this amplification theorem in that search. Priority and independent expert review remain open. [Original paper](https://doi.org/10.26493/1855-3974.1605.43f) · [Graph data](https://users.cecs.anu.edu.au/~bdm/data/graphs.html)

Run `python3 check.py` for the core certificates. A second checker computes signed sums of simple paths by their exact vertex set and endpoint, then closes them into cycles. It tests all four two-block choices at every cycle length on 19 vertices. This test exercises block replacement with nonconstant exterior signs. The maximum-degree argument above proves inequivalence in the theorem's range. Compile and run the second checker with `c++ -std=c++17 -O2 verify-multiplicity.cpp -o /tmp/verify-multiplicity && /tmp/verify-multiplicity`.
