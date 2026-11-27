# Two inequalities in a proposed proof of Cramér's conjecture fail by unbounded factors

GitHoobar · 27 November 2026 · Research note developed with OpenAI Codex and Luna agents

Cramér's prime-gap conjecture asks whether some constant $C$ satisfies $p_{n+1}-p_n\le C(\log p_n)^2$ for all sufficiently large $n$. We attempted both directions. The conjecture remains open. Our definite finding concerns version 9 of Cheng-Ting Wang's *On Maximal Prime Gaps*, dated 23 November 2026. Its proof of Theorem 2.6 uses two estimates for adjacent gaps. Each estimate fails by an unbounded factor on actual primes. We derive this from earlier theorems of Baker–Freiberg and Pintz. [Wang, version 9, §2](https://arxiv.org/html/2605.14871v9) · [Formal Conjectures target](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/CramerConjecture.lean#L89) · [Our attempts on the conjecture](approaches.md)

We also determined how many joint probabilities guarantee square-logarithmic gaps in a model that removes multiples of small primes. An unconditional counting argument for ordinary primes shows that term-by-term relative estimates fail before that order. [Sieved model and actual-prime obstruction](wheel-threshold.md)

For actual integer intervals of square-logarithmic length, we derive a bound on the exceptional starts where primes below a growing cutoff can divide every entry. The proof also gives a lower bound on the product of prime divisors needed to cover a typical interval. A companion note identifies the exact estimate still needed for ordinary primes. [Rough numbers and covering products](rough-intervals.md) · [Prime-count criterion](vacancy-test.md)

We then tested actual prime counts after fixing congruences on the start. For any given start, many other starts match all the prescribed residue answers and have a prime in their window. The proof gives the allowable number of prime moduli. A separate construction shows how a long gap can escape all of these estimates. [Actual primes after fixing congruences](primes-in-residue-classes.md)

We next examined consecutive starts. Fixed fractional deficits in prime counts can persist on a whole run at the Cramér scale. In some deficient runs every window shares actual primes. A finite sum over zeta zeros tests for a prime at a specified start, and a higher cutoff resolves primes exactly on the right endpoint. We bound its truncation error and prove a matching cutoff order for uniform suppression by positive smoothing kernels. [Aligned windows](aligned-windows.md) · [Pointwise zero-sum test](finite-zero-test.md)

We attacked the lower bound at the deepest deficit. The resulting inequality isolates a signed sum over widely separated zero ordinates and a possible contribution from high zeros to the right of the critical line. A comparison under RH with the extended pair-correlation function of Languasco, Perelli and Zaccagnini shows quantitatively why extrapolating its conjectured size down to a square-logarithmic window would fail. The universal prime certificate remains open. [Lower bound for a specified interval](deepest-deficit.md) · [Extended pair correlation and prior work](extended-pair-correlation.md)

The independent Lean verification of Alpöge's RH proof removes the off-line term above. We use RH to bound the signed far-pair sum at individual starts and on average in each sampled congruence class. A second filter resolves individual integers. For that filter a smoothed band of intermediate zero separations cancels pointwise to less than the effect of one prime. The larger separations still permit an empty window. [Signed bounds and RH record](signed-far-pairs.md) · [One-prime resolution and remaining obstruction](negative-far-pairs.md) · [MIT verification](https://math.mit.edu/~drew/grh/)

At the exact midpoint of a square-logarithmic interval, we isolate a band of zero separations with upper cutoff proportional to $x/h$. Infinitely many intervals containing order $\log x$ primes already produce a large negative signed pair sum in this band. We transfer the pair sum to individual zeros with an explicit proper-power correction and bound the upper tail of the earlier detector. The remaining one-prime margin at the deepest interval is open. [Wide separations at a sparse interval](wide-separations.md)

We can also identify every prime in the exact interval by using a separate zero sum at each integer coprime to a small primorial. The required maximum zero height is a vanishing fraction of the start. This includes a lone endpoint prime and distinguishes it from a proper power. The open step is to prove that at least one of the candidates passes the test at every start. [Sampling on the coprime residue classes](wheel-sampling.md)

We tested how much the many overlapping windows inside one gap improve a moment bound. In many disjoint blocks of actual primes, sliding the window attains every count in a fixed range below the mean. Those nonempty windows force a contribution of $X^{1-o(1)}$ to any normalized squared count-polynomial sum of degree $o(\log X)$, even with separate polynomials per block. [Exact counts and the degree obstruction](count-polynomials.md)

We characterized which positions can become the sole prime in a translate that retains an original prime divisor at every other position. At least half qualify at every sufficiently large start. Inside the original interval, a quantitative sieve bound shows how many positions lose every original divisor under any nonzero polynomially bounded shift. [Divisor-preserving translates and the fixed-interval estimate](divisor-preserving-translates.md)

Using the September 2026 Jacobsthal survivor theorem, we derived a logarithmic-power saving over its stated uniform bound for arbitrary prime sets. In a prime-free window this gives a lower bound on the number of distinct large least prime factors. A signed weight cancels semiprimes and detects a single actual prime if it is positive. Proving that sign at every start remains open. [Large divisor classes and the signed test](large-divisor-classes.md)

## Two checks by hand

Use Wang's one-based indexing $p_1=2$. Write $g_n=p_{n+1}-p_n$ and $A_j=(p_{j+1}-2)/j$, the average of the first $j$ gaps.

* **Lemma 2.4.** The premise is $A_{n-1}<g_{n-1}<g_n$. The asserted conclusion is $g_{n-1}^2/A_{n-1}\le g_n$. At $n=9$, the consecutive primes are 19, 23 and 29. The premise reads $21/8<4<6$. The conclusion requires $128/21\le6$, or $128\le126$.
* **Equation (2.11).** In the branch $g_{n-1}<A_{n-1}$ the proof bounds the quantity $D_n$ displayed below by $7/2$. At $n=6$, the primes 11, 13 and 17 give $g_5=2$, $g_6=4$, $A_4=9/4$, $A_5=11/5$ and $A_6=5/2$. These satisfy $g_5<A_5$, $A_4<A_6<g_6$. Direct substitution gives $D_6=(4/6)(4-11/5)/(11/5-2)=6$.

$$D_n=\frac{n-2}{n}\,\frac{g_n-A_{n-1}}{A_{n-1}-g_{n-1}}.$$

The sign of $A_{n-1}-A_{n-2}$ in this branch is negative, as Wang observes at the start of the branch. The sentence introducing (2.11) prints the opposite sign. The counterexample uses the branch in which the denominator of $D_n$ is positive. [Version 9, Theorem 2.6](https://arxiv.org/html/2605.14871v9#S2.Thmtheorem6)

## Arbitrarily long runs of failure for Lemma 2.4

**Proposition.** For every integer $m\ge1$ and every $B>0$, there are infinitely many blocks of $m$ consecutive indices at which the premise of Lemma 2.4 holds and $g_{n-1}^2>B A_{n-1}g_n$.

**Proof.** Write $\log_j$ for the $j$-fold iterated natural logarithm. Put
$$F(t)=\log t\,\frac{\log_2 t}{\log_3 t}.$$
Baker and Freiberg's unconditional Theorem 6.4 treats vectors of $a$ consecutive gaps, each divided by $F$ at its own left endpoint. This scale is admissible by the choice of functions in their deduction of Theorem 1.1. For any ordered list of $K=8a^2+16a$ nonnegative reals, at least one vector of $a$ successive differences from an increasing subsequence of $a+1$ list entries occurs as a limit point. [Baker and Freiberg, Theorem 6.4 and the deduction of Theorem 1.1](https://arxiv.org/pdf/1510.08054) · [Journal version](https://doi.org/10.1093/qmath/haw003)

Take $a=m+1$ and use the list $1,2,4,\ldots,2^{K-1}$. In **every** increasing subsequence, a jump ending at $2^j$ is smaller than $2^j$, and the next jump is at least $2^j$. Consequently the limit vector has fixed coordinates $0<u_1<\cdots<u_a<\infty$. Along the subsequence attaining it, write $P$ for the left endpoint of the first gap. For each fixed offset the prime number theorem gives $p_{k+j}/p_k\to1$. Hence the $a$ normalizing factors are all asymptotic to $F(P)$, and all corresponding running averages are asymptotic to $\log P$.

For each adjacent pair $g_{n-1},g_n$ in the block, with limit coordinates $u_j,u_{j+1}$, eventually $A_{n-1}<g_{n-1}<g_n$, and
$$\frac{g_{n-1}^2}{A_{n-1}g_n}
\sim \frac{u_j^2}{u_{j+1}}\frac{\log_2 P}{\log_3 P}\ \longrightarrow\ \infty.$$
There are finitely many pairs in the chosen block, so the conclusions hold simultaneously. ∎

## The other branch also has no constant bound

**Proposition.** For every fixed $k\ge1$, there is an infinite sequence of indices $n$ on which the preceding $k$ gaps are bounded by a constant depending only on $k$, and $D_n\to\infty$. The branch assumptions $g_{n-1}<A_{n-1}$ and $A_n<g_n$ both hold eventually.

**Proof.** Pintz constructs blocks of consecutive primes in a bounded interval followed immediately by a gap of length at least a constant times $\log N\,\log_2 N\,\log_4 N/(\log_3 N)^2$, with indices of order $N$. Take a cluster containing at least $k+1$ primes and let $p_n$ be its last prime. This uses the bounded-cluster assertion in the proof of Theorem 2, not only the theorem's displayed ratio. It supplies $g_{n-1}=O_k(1)$ and $g_n/\log p_n\to\infty$ along a subsequence. The prime number theorem gives $A_{n-1}\sim\log p_n$. The identity $A_n=((n-1)A_{n-1}+g_n)/n$ puts $A_n$ strictly between $A_{n-1}$ and $g_n$. Also $A_n-A_{n-2}=(g_{n-1}+g_n-2A_{n-2})/n>0$ eventually. Thus the positive denominator of $D_n$ is asymptotic to $\log p_n$, while its numerator apart from the prefactor is asymptotic to $g_n$. This proves the claim. ∎ [Pintz, §4, especially (4.1) and (4.50)](https://arxiv.org/pdf/1406.2658) · [Published chapter](https://doi.org/10.1007/978-3-319-22240-0_17)

## Consequences and attribution

Theorem 2.6 claims $g_n<4A_{n-1}^2$. Its first branch invokes Lemma 2.4 and its second uses (2.11). Discarding finitely many primes or changing either intermediate estimate by a fixed factor cannot repair these steps. The truth of Theorem 2.6's conclusion and the asymptotic Cramér bound remains undetermined here. Indeed, the gaps in our first construction have size comparable to $F(P)=o((\log P)^2)$.

The chain-of-gaps and bounded-cluster theorems belong to the cited authors. Our contribution here is the choice of offsets, the two deductions for Wang's specific claims, and reproducible witnesses. Independent priority and peer review of this note have not been established. The finite certificates use Python and Lean. The infinite-sequence arguments above are written proofs using the published theorems. [Exact Python checks](check.py) · [Lean certificates](Counterexamples.lean) · [Reproduction guide](../../VERIFYING.md)
