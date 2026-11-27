# Björner's identity realization question

Working note, 27 November 2026. The equal-parameter problem remains unresolved in this investigation.

## Statement and status

Given $u\le v$ in a Coxeter group, can its ordinary Kazhdan–Lusztig polynomial $P_{u,v}(q)$ always be written as $P_{e,w}(q)$ for some element of some possibly different Coxeter group? This is Björner's question, Problem 1.9 in Francesco Brenti's survey. Brenti reported no known partial results on the problem as he formulated it. Polo realized every polynomial in $1+q\mathbb{Z}_{\ge0}[q]$ with an unrestricted lower endpoint. Ordinary KL positivity and the constant-term property give the reverse inclusion. Thus it suffices, and is necessary, to realize every such polynomial at the identity. [Brenti, p. 5](https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf) · [Polo](https://doi.org/10.1090/S1088-4165-99-00074-6) · [Elias and Williamson](https://arxiv.org/abs/1212.0791)

Woo classified a family giving $1+q^h$ at the identity. Burrull, Li and Zeng's October 2026 preprint treats permutations with an irreducible singular locus and $P_{e,w}(1)=3$. These are relevant results about restricted outputs. Searches by author, problem number, endpoint, and realization terminology found no proof or counterexample to the universal statement. The stronger selection criterion that nobody has proved anything relevant is not supported. [Woo](https://arxiv.org/abs/0809.2374) · [October 2026 preprint](https://arxiv.org/abs/2610.32832)

## An ordinary construction from chord diagrams

A universal Coxeter group is a free product of order-two groups. Take a chord diagram, read the chord names around the circle after any cut, and insert two fresh simple generators between every two consecutive names. Each spacer occurs exactly once. Call the resulting reduced word $w$ of length $L$. Form the graph $G$ on chords, joining two if their endpoints alternate.

**Claim.** $P_{e,w}(q)=\sum_I q^{|I|}$, where $I$ runs over independent sets in $G$.

Use the Hecke normalization $b_s=H_s+v$ and $H_s^2=1+(v^{-1}-v)H_s$. By Dyer's multiplication formula, multiplying the canonical element of a prefix by its next simple factor gives the canonical element of the extended prefix whenever the next letter differs from the previous two. This holds throughout the padded word (the first two factors follow directly by triangularity). The product of simple canonical factors is therefore $b_w$. [Elias and Libedinsky, Proposition 3.1](https://nicolaslibedinsky.cl/wp-content/uploads/2017/11/Indecomposable.pdf)

To compute the coefficient at $H_e$, multiply from left to right. From $H_x$ one can move to $H_{xs}$ with coefficient one, or stay with coefficient $v$ on an ascent and $v^{-1}$ on a descent. Returning to the identity requires skipping every spacer. Parity in each generator forces a chord to be used at both occurrences or at neither. Two selected intersecting chords are impossible: erasing all other letters maps the group to the free product on these two, in which the alternating word of length four is nontrivial. Conversely any noncrossing selection reduces to the identity by deleting an innermost adjacent pair until none remain. Every skipped letter was never used, so every skip is an ascent. An independent set of $j$ chords contributes exactly $v^{L-2j}$. Comparing with $[H_e]b_w=v^L P_{e,w}(v^{-2})$ proves the claim, including the empty diagram.

## A construction for every target with unequal parameters

Assign any positive integer weight $a_i$ to chord $i$. Use one fresh spacer between each consecutive endpoint, of weight $M>2\sum_i a_i$. In a universal Coxeter group these are allowed Hecke weights, as there are no braid relations between distinct letters. Write $L(w)$ for the total weight. With the unequal-parameter canonical basis one gets
$$[H_e]b_w=v^{L(w)}\sum_I v^{-2\sum_{i\in I}a_i}.$$

Here is a triangularity check needed because the ordinary multiplication formula used above assumes equal parameters. For weight $a$, the simple factor is $H_s+v^a$. A stay now contributes $v^a$ or $v^{-a}$ by ascent or descent. The product of simple factors is bar-invariant. All terms are indexed by subexpressions and thus lie weakly below $w$ in Bruhat order. The unique full word gives the leading term $H_w$. If a path omits a spacer it gains at least $M$ in the exponent. No spacer stay is a descent, and losses on all chord letters together are at most $2\sum_i a_i$. Every such path therefore has strictly positive exponent. If a path uses all spacers, each permanently blocks cancellation across it. Every skipped chord occurrence is then an ascent. Thus all lower coefficients belong to $v\mathbb Z[v]$, which characterizes $b_w$ among bar-invariant elements. The same identity-path argument now proves the formula. [Lusztig, unequal-parameter basis](https://arxiv.org/abs/math/0208154)

For any target $1+\sum_{j\ge1}c_jq^j$, use $c_j$ chords of weight $j$ and draw them all pairwise crossing. Explicitly, write the list of their distinct names twice in the same order. An independent set is empty or a singleton. The formula gives the target exactly in the weighted setting. Use $w=e$ for the constant polynomial.

## Where the attempt to remove weights breaks

Setting each weight to one forgets the prescribed degrees. In the ordinary chord construction every chord is a singleton independent set, so a zero linear coefficient forces the entire polynomial to be one. Replacing a chord of weight $j$ by $j$ nested ordinary chords does not fix this: every nonempty subset can be chosen, contributing $(1+q)^j-1$ in place of $q^j$. For example the attempted replacement of $q^2$ introduces two extra linear terms.

This gives a positive ordinary construction with a precise range for this replacement scheme. For any target $P(q)=1+\sum c_jq^j$, arrange a separate nested packet of $j$ chords for each of its $c_j$ monomials. Put the packets in the same order in the two halves of the endpoint list, reversing only the order within each packet on its second appearance. Chords from distinct packets cross. The resulting identity polynomial is $1+P(1+q)-P(1)$. Recovering $P(q)$ would require an ordinary construction that reverses this shift or makes a packet selectable only as a whole. Folding theory uses equivariant traces to produce unequal parameters and does not itself equate those traces with ordinary identity KL coefficients. No such passage is proved here. [Elias, folding](https://arxiv.org/abs/1602.08449)

The arguments use no bound on rank, degree or coefficients. They are working derivations from the cited machinery, with no priority claim. The checker multiplies in the standard Hecke basis and tests triangularity and the coefficient at the identity on representative diagrams, including crossing and nested chords. Run `python3 check.py`.
