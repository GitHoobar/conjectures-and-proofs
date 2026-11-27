# Which weighted prime counts can detect an empty window?

GitHoobar · 27 November 2026 · Developed with OpenAI Codex and Luna agents

Fix $C>0$. Let $X$ be a large integer, $L=\log X$, $h=\lceil CL^2\rceil$ and $P(m)=\pi(m+h)-\pi(m)$ for $X<m\le 2X$. Write $e(t)=\exp(2\pi i t)$ and consider every weight $|F(m)|^2$ with

$$F(m)=\sum_{\alpha\in\mathcal F_R}c_\alpha e(\alpha m),\qquad \mathcal F_R=\{a/q\bmod 1:(a,q)=1,\ 1\le q\le R\},\qquad R=\lfloor X^{1/8}\rfloor.$$

The coefficients can be complex and can be chosen after seeing the primes. This includes linear combinations of divisibility tests whose periods are at most $R$. For example, simultaneous conditions $d_i\mid m+i$ either define a residue class modulo the least common multiple of the $d_i$ or are incompatible. The product cutoffs in smooth divisor sums give precisely this kind of upper bound on the period. The adjacent-interval weights in the OpenAI gap-frequency preprint motivated the test. Its frequency theorem holds for each fixed multiple of the mean gap. Here the window length grows as a multiple of $(\log X)^2$. [OpenAI, *Positive lower density of large prime gaps*, §§2–4](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf)

**Weighted prime bound.** Using Dirichlet GRH, for some $b>0$ and all sufficiently large $X$,

$$\frac1X\sum_{X<m\le2X}P(m)|F(m)|^2\ \ge\ R^{-1}\exp\!\left(b\frac{L\log\log L}{\log L}\right)\sum_\alpha|c_\alpha|^2. \tag{1}$$

This gives a positive lower bound simultaneously for every nonzero coefficient vector. Yet even erasing every prime in one interval of length $X^{7/8}$ leaves (1) true with a smaller $b$. The pointwise conclusion needs a larger family of weights or finer information about the actual counts. The last section makes this distinction exact. We use the character version of the GRH prime number theorem and the independently checked Dirichlet GRH record. The argument below has a written proof and finite checks. [GRH verification record](https://math.mit.edu/~drew/grh/) · [GRH prime sums for Dirichlet characters](https://arxiv.org/abs/2003.01925)

## Replacing one integer average by a residue-class average

Let $M=\mathrm{lcm}(1,\ldots,R)$ and take $r$ uniformly modulo $M$. All the displayed frequencies are distinct characters of this group, so $\mathbb E|F(r)|^2=\sum_\alpha|c_\alpha|^2=:E$. The complete residue-class expression for the prime-weighted sum is

$$G=\frac{M}{\varphi(M)}\,\mathbb E\left[|F(r)|^2\sum_{i=1}^h {\bf 1}_{(r+i,M)=1}\right].$$

Write $\theta_0(n)=\log n$ if $n$ is prime and zero otherwise. Uniformly in the coefficients,

$$\left|\frac1X\sum_{X<m\le2X}|F(m)|^2\sum_{i=1}^h\theta_0(m+i)-G\right|\ll h X^{-1/2}R^3 L^2 E. \tag{2}$$

To verify this, expand $|F|^2$ and write one frequency difference as $a/q$ in lowest terms, with $q\mid M$ and $q\le R^2$. The contribution of shift $i$ to the model entry is $e(-ia/q)\mu(q)/\varphi(q)$, by summing over units modulo $q$; this includes the diagonal $q=1$. On the actual interval substitute $n=m+i$. Expand $e(an/q)$ on the units modulo $q$ in Dirichlet characters. Its coefficient at the principal character is $\mu(q)/\varphi(q)$. Parseval gives sum of squared coefficient magnitudes one, and hence sum of magnitudes at most $\sqrt{\varphi(q)}$. Under Dirichlet GRH the sum of $\theta_0(n)\chi(n)$ on $(X+i,2X+i]$ is $X{\bf1}_{\chi\text{ principal}}+O(\sqrt X\log^2(qX))$. Both endpoints are at most $3X$. Passing from the von Mangoldt sum to primes costs $O(\sqrt X\log^2 X)$, and the excluded prime divisors of $q$ cost at most $\log q$. The same bound covers imprimitive characters by removing the primes at which the induced character differs. Thus each entry has error $O(\sqrt{q/X}\,L^2)$ for each shift. Finally $(\sum|c_\alpha|)^2\le |\mathcal F_R|E\ll R^2 E$ and $\sqrt q\le R$. This proves (2).

## A lower bound over all residues, including the rare starts

Put $z=\tfrac14\sqrt h\log h$ and freeze the prime-power coordinates of $r$ belonging to primes $p\le z$ in the Chinese remainder representation of $\mathbb Z/M\mathbb Z$. Call offset $i$ eligible when $r+i$ avoids those primes. For **every** freezing there are $\gg h\log\log h/(\log h)^2$ eligible offsets. This is Theorem 1.2 of the Jacobsthal preprint applied to the forbidden classes $-r\bmod p$ on $[1,\lfloor z^2/(\log z)^2\rfloor]\subset[1,h]$, as in the [previous deduction](large-divisor-classes.md). Partition $[1,h]$ into at most $\lceil h/\lfloor z\rfloor\rceil$ consecutive blocks. Some block has $\gg z\log\log h/(\log h)^2$ eligible offsets. This exceeds

$$j=1+\left\lfloor\frac{\log R}{\log z}\right\rfloor$$

for large $X$, since $z\asymp_C L\log L$ and the ratio of the lower bound to $j$ tends to infinity. Choose $j$ such offsets $T$ deterministically from the frozen coordinates. Their residues are distinct modulo every $p>z$. [OpenAI, Jacobsthal survivor theorem](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf)

For each $p^a\Vert M$ with $p>z$, independently draw an alternative coordinate uniformly from the residues modulo $p^a$ avoiding all $-i\bmod p$ for $i\in T$. Each original coordinate hits at most one such $i$. For $S\subseteq T$ construct $r_S$ by changing precisely the coordinates whose original hit belongs to $S$, using the alternative already drawn. In particular $r_\varnothing=r$. Every $i\in S$ now satisfies $(r_S+i,M)=1$.

Fix both sets of coordinates. As a function of the $j$ binary choices defining $S$, any single character $e(\alpha r_S)$ has multilinear degree less than $j$. Indeed it factors over the prime powers in its denominator; each large prime coordinate depends on at most one binary choice, and a denominator at most $R$ has fewer than $j$ distinct prime factors greater than $z$. The other coordinates are fixed. Consequently the alternating sum of $F(r_S)$ over the cube vanishes, and Cauchy–Schwarz gives

$$|F(r)|^2\le(2^j-1)\sum_{\varnothing\ne S\subseteq T}|F(r_S)|^2. \tag{3}$$

For each fixed $S$ conditional on the freezing, the output law still factors over the large primes. At a coordinate modulo $p^a$, the residues hitting $S$ lose their mass and redistribute it evenly over the fraction $(p-j)/p$ avoiding $T$. The density relative to uniform is at most $1+|S|/(p-j)$. Write

$$A=\prod_{z<p\le R}\left(1+\frac{j}{p-j}\right),\qquad B=\{r:\exists i\in[1,h],\ (r+i,M)=1\}.$$

For nonempty $S$ the output is supported on $B$. Thus its conditional expectation of $|F|^2$ is at most $A$ times the conditional expectation of $|F(r)|^2{\bf1}_B(r)$. This is valid for each of the deterministically indexed subsets after freezing, even though $T$ varies between freezings. Average (3) over all coordinates and alternatives. Parseval now yields

$$E\le4^j A\,\mathbb E[|F(r)|^2{\bf1}_B(r)]\le4^j A G. \tag{4}$$

The size of $A$ matters at $R=X^{1/8}+O(1)$. Write $l=\log L$. Then $\log z=l+\log l+O_C(1)$, $j/z=O_C(l^{-2})$, and Mertens' reciprocal prime sum gives

$$\log(4^j A)\le j\left(\log 4+(1+O_C(l^{-2}))\sum_{z<p\le R}p^{-1}\right)\le j\,(l-\log l+O_C(1)).$$

Using $j\le1+\log R/(l+\log l+O_C(1))$, this is at most $\log R-b_0 L\log l/l$ for some $b_0>0$ and large $X$. Therefore (4) gives $G\ge R^{-1}\exp(b_0 L\log l/l)E$. In (2), $X^{-1/2}R^3\le R^{-1}$, and the exponential gain absorbs $hL^2$. Dividing the resulting lower bound by $\log(3X)$, an upper bound for every prime weight in the interval, proves (1) with a smaller $b$.

## How much of a gap could these tests miss?

First remove all primes in any one interval of length at most $X^{7/8}$. The affected starts lie in a consecutive interval of length at most $X^{7/8}+h+2$. Their prime counts each decrease by at most $h$. The reduced fractions in $\mathcal F_R$ are separated modulo one by at least $R^{-2}$. The additive large sieve bounds the sum of $|F(m)|^2$ on any $N$ consecutive integers by $(N+R^2)E$. The decrease on the left of (1) is therefore at most

$$\frac hX (X^{7/8}+h+2+R^2)E\ll_C L^2 X^{-1/8}E.$$

This is smaller than its lower bound by a factor tending to zero, uniformly in $F$. Thus the modified sequence still satisfies (1) with a smaller positive $b$, even though it can have an empty interval far longer than $h$. This deletion tests what follows from the weighted inequalities alone. [Montgomery and Vaughan, *The large sieve*](https://doi.org/10.1112/S0025579300004708)

There is also a direct obstruction to putting most of the mass on a specified start at this level. Cauchy–Schwarz gives $|F(m_0)|^2\le |\mathcal F_R|E\ll R^2 E$. The diagonal in $\sum_{X<m\le2X}|F(m)|^2$ contributes $XE$. By the geometric sum formula and the frequency spacing, each off-diagonal entry has absolute value $O(R^2)$, giving total error $O(R^4E)=o(XE)$. A single start therefore receives at most $O(R^2/X)$ of the total mass.

At a different level the weighted test recovers the exact minimum. Take $R'=\lceil 2\sqrt X\rceil$. There are $(3/\pi^2+o(1))(R')^2>X$ distinct reduced frequencies by the summatory totient estimate. Select any $X$ of them. Evaluating their characters on the $X$ consecutive starts gives an invertible Vandermonde matrix after multiplying columns by nonzero phases. Its span includes the indicator of each individual start. Consequently

$$\inf_{F:\sum_m|F(m)|^2>0}\frac{\sum_mP(m)|F(m)|^2}{\sum_m|F(m)|^2}=\min_{X<m\le2X}P(m)$$

at this level, with both sums over the stated starts. Positivity at that level for every sufficiently large dyadic shell, for a single fixed $C$, would force an actual prime in every required window up to the immaterial change of the constant between adjacent shells. Estimate (2) is too weak there, and an arbitrary full-period lower bound cannot be compared to the interval by our error estimate. Cramér's conjecture remains open. Independent priority for the weighted inequality and its proof has not been established. [Exact finite checks](check-rational-window-weights.py)
