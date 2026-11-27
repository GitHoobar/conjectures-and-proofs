# What the divisor identity and the expansion at the pole detect

GitHoobar · 28 November 2026 · Developed with OpenAI Codex and Luna agents

Deleting primes in one window preserves the [distribution estimates used in the progression argument](switched-progressions.md), but changes the residue of the Euler product at 1. We tested whether exact information at that pole, together with the logarithmic divisor identity, can distinguish an empty window. The following construction matches any prescribed finite number of coefficients, with integer multiplicities and with infinitely many gaps.

## Statement

Fix an integer $r\ge0$. There exist multiplicities $b_p\in\{0,1,2\}$ on the ordinary primes with the following properties. All assertions concern the **same** system for the chosen $r$.

* For every sufficiently large $X=16^j$, some interval in $[X,2X]$ of length $\lfloor(\log X)^3\rfloor$ contains $\gg(\log X)^2$ ordinary primes and no prime of positive multiplicity.
* Its Euler product $F(s)=\prod_p(1-p^{-s})^{-b_p}$ has exactly the zeros and poles of $\zeta(s)$ in $\Re s>0$, including multiplicities. Near $1$, $F(s)/\zeta(s)=1+O_r(|s-1|^{r+1})$. In particular the residue is exactly one. The two Laurent expansions agree through degree $r-1$ inclusive.
* Write $F(s)=\sum_n a(n)n^{-s}$ for $\Re s>1$. The $a(n)$ are nonnegative integers. For every $\epsilon>0$, $\sum_{n\le t}a(n)=t+O_{r,\epsilon}(t^\epsilon)$. Their exact logarithmic divisor identity holds at every integer. The weighted prime counts in arithmetic progressions obey the same Bombieri–Vinogradov bounds as ordinary primes.

These are generalized primes in the sense that two copies of a prime are distinct generators, so their products are counted with multiplicity. The comparison is unconditional. Beurling prime systems have long been used to separate hypotheses concerning prime and integer counts. Diamond, Montgomery and Vorhauer construct systems with large oscillations. Our question concerns simultaneous matching at the pole and a prescribed order of gaps using integer multiplicities on ordinary prime bases. Independent priority for this combination is unverified. [Diamond, Montgomery and Vorhauer](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/46253/208_2005_Article_638.pdf) · [Classical Euler product and Laurent expansion](https://dlmf.nist.gov/25.2)

## Matching the coefficients with integer changes

Put $\delta_p=b_p-1$. Start with every $\delta_p=0$. At scale $X$ and for $0\le k\le r$ assign a column to each prime $p$ with entries

$$v_X(p)_k=X\sum_{m\ge1}\frac{(\log(p^m/X))^k}{m p^m}.$$

A zeroth power is one. For $X\le p\le8X$ these columns are bounded in maximum norm by a constant $M_r$, uniformly for large $X$. Writing $z=\log(p/X)$, their main column is $e^{-z}(1,z,\ldots,z^r)^t$. The tail from $m\ge2$ is $O_r((1+\log X)^r/X)$ by summing the geometric tail with a fixed polynomial factor.

Maintain a bound on the signed sum $E_X=\sum_{p\ \mathrm{changed\ so\ far}}\delta_p v_X(p)$ after each scale, including **all** earlier changes. Specifically we keep $\|E_X\|_\infty\le(r+1)M_r$. To pass from $X$ to $16X$, each previous coordinate transforms by the binomial theorem:

$$ (E_{16X}^{\mathrm{old}})_k
=16\sum_{i=0}^k {k\choose i}(-\log16)^{k-i}(E_X)_i.$$

Thus each new scale starts with inherited error $O_r(1)$. The initial error is zero.

Partition $[X,2X]$ into full intervals of $H=\lfloor(\log X)^3\rfloor$ consecutive integers and a remainder. By the prime number theorem there are $\asymp X/\log X$ primes there, and the remainder contains at most $H$. Some full interval contains $\gg H/\log X$ primes. Set $\delta_p=-1$ at all its primes. After these deletions the current vector $u$ has norm $O_r(1+H)$.

Choose $r+1$ pairwise separated closed subintervals of positive length inside $(1,2)$ for $z$. A matrix with one main column from each interval is invertible by the Vandermonde determinant. Compactness and the separation give a uniform inverse bound depending only on $r$ and the chosen intervals. The same holds for the exact columns for large $X$ by the tail bound. Each interval supplies $\gg_r X/\log X$ primes by the prime number theorem. These primes lie above $eX$ and below $e^2X$, outside the target and below the next scale.

Take $N=\lceil C_r(1+H)\rceil$ disjoint groups of $r+1$ such primes, one per interval per group. In each group solve the real linear system whose columns are the $v_X(p)$ and whose right side is $-u/N$. For $C_r$ sufficiently large all coordinates have magnitude at most one. Together these groups therefore give a feasible point of the cube $[-1,1]^{N(r+1)}$ at which the corrections cancel $u$ exactly.

Intersect this cube with those $r+1$ linear constraints and choose a vertex. At most $r+1$ coordinates are strictly between the endpoints: otherwise their columns have a nontrivial dependence, giving a line segment through the vertex in the feasible set. Set all those interior coordinates to zero and keep the endpoint coordinates. The resulting corrections lie in $\{-1,0,1\}$. Their rounding changes the vector by at most $(r+1)M_r$ in each coordinate. This proves the induction bound, using $O_r(1+H)$ prime changes at this scale. Distinct scales use disjoint primes.

## Passing to one infinite system

Through $t$ there are $O_r((\log(2t))^4)$ changed primes by summing the cubic bound over geometric scales. Consequently

$$B(s)=\sum_p\delta_p\sum_{m\ge1}\frac{1}{m p^{ms}}$$

converges locally absolutely in $\Re s>0$, including after any fixed number of differentiations. There $G=\exp B$ is holomorphic and nonvanishing and $F=\zeta G$ continues the Euler product. To verify exact matching, take the partial sum of $B$ through the last completed scale $X$. Its $k$th derivative at 1 for $k\le r$ is

$$\frac{(-1)^k}{X}\sum_{i=0}^k{k\choose i}(\log X)^{k-i}(E_X)_i.$$

This tends to zero for every $k\le r$. Hence all these derivatives of $B$ vanish at 1, giving the stated matching for $G$. Each fixed $r$ yields its own system. Agreement to infinite order for a single analytic quotient would instead force $G\equiv1$.

For the integer counts, the Dirichlet coefficients $g(d)$ of $G$ satisfy $\sum_d |g(d)|d^{-\sigma}<\infty$ for each $\sigma>0$. Indeed each changed prime contributes either $1-p^{-s}$ or $(1-p^{-s})^{-1}$ and $\sum_{p\ \mathrm{changed}}p^{-\sigma}<\infty$. Since $a=1*g$ under Dirichlet convolution, summing floors gives

$$\sum_{n\le t}a(n)=\sum_{d\le t}g(d)\lfloor t/d\rfloor=tG(1)+O_{r,\epsilon}(t^\epsilon).$$

For $0<\epsilon<1$ both the floor error and the tail after extension to $d>t$ are bounded by $t^\epsilon\sum_d|g(d)|d^{-\epsilon}$. The Euler factors of $F$ give nonnegative integer coefficients. Define $\Lambda_b(p^m)=b_p\log p$ for $m\ge1$ and set it to zero otherwise. Multiplying $-F'/F$ by $F$ gives, coefficient by coefficient,

$$a(n)\log n=\sum_{d\mid n}\Lambda_b(d)a(n/d).$$

In any prime-count progression up to $t$ the change from ordinary primes is $O_r((\log(2t))^4)$, even with a maximum over endpoints and residues. For Chebyshev counts including powers it is $O_r((\log(2t))^5)$, since each changed base contributes at most $\log t$ in weight. Summing this error over moduli up to $\sqrt t$ costs $o(t/(\log t)^A)$ for every fixed $A$, preserving the usual Bombieri–Vinogradov estimate. [Bombieri–Vinogradov with endpoint maxima](https://dms.umontreal.ca/~andrew/Courses/Chapter13.pdf)

## Where ordinary integers give extra information

There is an arithmetic reason the repairs continue through infinitely many scales. A finite change of integer Euler multiplicities that preserves the residue would give $\prod_p(p/(p-1))^{\delta_p}=1$. For the largest changed prime $P$, the $P$-adic valuation of this rational number is $\delta_P\ne0$. Our construction can match the residue exactly only in the limit.

For ordinary integers every coefficient $a(n)$ equals one. At a deleted prime $p$ in the constructed system, $a(n)=0$ on **every multiple** of $p$. In particular the multiples of the primes deleted from one target occupy natural density $1-\prod_{p\ \mathrm{in\ target}}(1-1/p)\gg (\log X)^2/X$. The formula follows by inclusion–exclusion, using $p\le2X$ and $H/X=o(1)$. Thus dilation really does expose the missing primes in the coefficients, even though their cumulative count differs from $t$ by $O_\epsilon(t^\epsilon)$ and the listed data at the pole agree exactly. A lower bound for the prime count at a prescribed ordinary start still requires an argument using information these comparisons lose. [Finite algebra checks](check-euler-multiplicities.py)

## A test that detects the changes on the critical line

The ordinary zeta functional equation supplies a symmetry that the modified products violate. On the critical line form

$$D(t)=B(1/2+it)-B(1/2-it).$$

If $F$ satisfied the same completed functional equation as $\zeta$, its quotient $G$ would obey $G(s)=G(1-s)$ in the strip by continuation across the common zeros. Then $D(t)$ would be a continuous multiple of $2\pi i$ with $D(0)=0$, hence identically zero. In fact absolute convergence and orthogonality of distinct real frequencies give

$$\lim_{T\to\infty}\frac1T\int_0^T|D(t)|^2\,dt
=2\sum_p\delta_p^2\sum_{m\ge1}\frac{1}{m^2p^m}.$$

The positive frequencies $\log(p^m)$ are distinct by unique factorization. Integrating a finite partial sum gives the formula by elementary exponentials, and uniform absolute convergence bounds the tails. [Classical functional equation](https://dlmf.nist.gov/25.4)

More locally, a time average through height $T=\sqrt X$ detects the changes at the particular target built at scale $X$. Let $u$ be its midpoint. Choose a fixed nonnegative even smooth $w$ supported in $(-1,1)$ with integral one. Set $\widehat w(v)=\int w(t)e^{-itv}dt$ and define

$$J_X=\frac1T\int_{-T}^T w(t/T)e^{it\log u}D(t)\,dt.$$

Then $J_X$ is real and
$$J_X=-\sum_{p\ \mathrm{in\ target}}\frac1{\sqrt p}
       +O_r\!\left(\frac{1+\log\log X}{\sqrt X}\right).$$

To see this, expand $B$. The term at $n=p^m$ in the first half receives the factor $\widehat w(T\log(n/u))$; the reflected half receives $\widehat w(T\log(nu))$. The latter half and the terms with $n\notin[X/2,4X]$ in the first half contribute $O_r(T^{-2})$, since $|\widehat w(v)|\ll(1+|v|)^{-2}$ and the full series is absolutely summable on the line. Among first powers in $[X/2,4X]$, the nonzero changes outside the target are a fixed positive logarithmic distance from $u$: the correction primes exceed $eX$, the previous scale ends below $X/2$, and the next starts at $16X$. These terms also cost $O_r(T^{-2})$. For target primes, $|T\log(p/u)|\ll H/\sqrt X$. Evenness gives $\widehat w(v)=1+O(v^2)$, so the total replacement error there is $O(H^3/X^{3/2})$.

For each $m\ge2$, successive integer $m$th powers in $[X/2,4X]$ differ by $\gg\sqrt X$ by the mean value theorem. Their scaled logarithms $T\log(n/u)$ therefore have separation $\gg1$. The sum of $(1+|T\log(n/u)|)^{-2}$ over each such sequence is $O(1)$, uniformly in $m$. Each term carries weight at most $O(1/(m\sqrt X))$ and $m\le\log(4X)/\log2$, giving the stated error. The target sum is $\gg (\log X)^2/\sqrt X$ because of how the target was selected. Thus this functional-equation test distinguishes the constructed systems even on a finite height range. Selection of a window already rich in ordinary primes is used only to establish this size of the signal and the analogous positive-density assertion above. No such lower bound has been obtained at an arbitrary ordinary start.

There is a version at the margin of one prime. Prescribe any interval $I$ of length at most $H$ inside $[X,2X]$ at each scale and use it in place of the selected target. The induction is unchanged since it needs only the upper bound $H$ on deletions. With midpoint $u$, explicitly subtract the proper powers near the target frequency by setting

$$J_X^{\rm pow}=\sum_{\substack{m\ge2,\ X/2\le p^m\le4X}}\frac{\delta_p}{m p^{m/2}}\widehat w\!\left(T\log(p^m/u)\right).$$

Every base in this term is at most $2\sqrt X$, so its multiplicity has already been fixed before this scale. The preceding estimates now give, uniformly in these choices,

$$-\sqrt u\,(J_X-J_X^{\rm pow})=\#\{p\in I\}
  +O_r\!\left(X^{-1/2}+H^3/X\right).$$

Indeed the far and reflected terms cost $O_r(\sqrt X/T^2)$ after scaling, the smoothing error costs $O(H^3/X)$, and replacing $\sqrt{u/p}$ by one costs $O(H^2/X)$ over the target. The absolute-series bound used here is uniform in target choice because the same number-of-changes bound holds in every shell. Rounding recovers the ordinary count at a prescribed start, even one with zero or one prime. The remaining dependence matters: $J_X$ uses the Euler quotient of a system in which exactly the target primes were removed. This identity supplies no independent strict lower bound for the corrected functional-equation defect there.
