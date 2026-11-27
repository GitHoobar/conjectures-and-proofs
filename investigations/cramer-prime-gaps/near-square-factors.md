# Which composites can near-square factorizations remove from the sparsest prime window?

GitHoobar · 27 November 2026 · Developed with OpenAI Codex and Luna agents

A possible way to prove a prime survives in the original interval is to count the candidates after sieving and bound the number of composites by counting factorizations. We tested the identity $4dn=s^2-t^2$. For $n=ab$ it arises by choosing positive multipliers $u,v$ and setting $d=uv$, $s=ua+vb$, $t=|ua-vb|$. When the two scaled factors are close, $s$ is close to $2\sqrt{dn}$. This is the basis of Lehman's factorization theorem. Chan studied related interval questions for factors close to the square root. [Lehman's theorem as stated by Hittmeir, Theorem 2.1](https://publications.sba-research.org/publications/042021_Hittmeir_A%20time-space%20tradeoff%20for%20Lehman%27s%20deterministic%20integer%20factorization%20method.pdf) · [Chan, *Finding Almost Squares*](https://arxiv.org/abs/math/0502199)

For an integer $D\ge1$ count every $n$ that admits integers satisfying

$$1\le d\le D,\qquad s,t\ge0,\qquad 4dn=s^2-t^2,\qquad 0\le s-2\sqrt{dn}\le\sqrt{D/d}. \tag{1}$$

Write $F_D$ for this set. Its width allows $O(D)$ choices of the pair $(d,s)$ per integer, since $\sum_{d\le D}(1+\sqrt{D/d})=O(D)$. The following argument studies the integers represented by (1).

## A uniform upper bound in the original interval

Let $X$ be a sufficiently large positive integer, $H=\lceil C(\log X)^2\rceil$ with $C>0$ fixed and $X\le x<2X$ an integer. For $1\le D\le H$,

$$|F_D\cap(x,x+H]|\ll \sqrt{HD}\log(2D)+D\log(2D). \tag{2}$$

**Removing common squares.** If $p^2\mid d$ and $p\mid s$, the equation forces $p\mid t$. Replacing $(d,s,t)$ by $(d/p^2,s/p,t/p)$ preserves (1): the left side of the width constraint is divided by $p$ and its upper bound increases by $p$. Continue until $p\nmid s$ whenever $p^2\mid d$. For any resulting pair $(d,s)$, the congruence $t^2\equiv s^2\pmod d$ has at most $2\cdot 2^{\omega(d)}$ root classes. At a prime dividing $d$ exactly once there are at most two. At higher powers $s$ is a unit, so divide by $s^2$ and count roots of unity. There are two for an odd prime power since the factors of $(y-1)(y+1)$ are coprime away from 2. There are at most four for powers of 2 since one of the adjacent even factors $y-1,y+1$ has 2-adic valuation one when the modulus is at least 8. Combine these counts by the Chinese remainder theorem. The bound includes $d=1$.

**The first possible value of $s$.** For fixed $d$ put $s_0=\lceil2\sqrt{dx}\rceil$. At $s=s_0$, as $n$ varies the allowable $t^2$ range has length at most $4dH$ after intersecting with $[0,\infty)$. Thus the $t$ range has length at most $2\sqrt{dH}$. Each root class modulo $d$ contributes at most $1+2\sqrt{H/d}$ choices. This costs $O(2^{\omega(d)}(1+\sqrt{H/d}))$.

**All subsequent values.** Uniformly for $d\le H$, $2\sqrt{d(x+H)}-2\sqrt{dx}\le H\sqrt{d/x}=o(1)$. For $s\ge s_0+1$ we therefore have $s-2\sqrt{dn}\ge1/2$, so $t^2=(s-2\sqrt{dn})(s+2\sqrt{dn})\gg\sqrt{dx}$. Consecutive such squares differ by $\gg(dx)^{1/4}>4dH$ for large $X$, uniformly over $d\le H$. At most one $t$ can occur per $s$. The width in (1) allows $O(1+\sqrt{D/d})$ values of $s$. This last estimate includes the right endpoint of the interval.

Summing the two contributions proves (2). Indeed $2^{\omega(d)}\le\tau(d)$, and $\sum_{d\le D}\tau(d)\ll D\log(2D)$ by counting divisor pairs. Partial summation gives $\sum_{d\le D}\tau(d)/\sqrt d\ll\sqrt D\log(2D)$.

## What this says at a start attaining the minimum

Put $D=\lfloor H/(\log H)^6\rfloor$. Then (2) gives $O(H/(\log H)^2)$ represented entries at **every** start. Our [large-divisor sieve estimate](large-divisor-classes.md) leaves at least $bH\log\log H/(\log H)^2$ entries avoiding divisibility by every prime up to $Z=\tfrac14\sqrt H(\log H)^{1+\delta}$ for fixed $b,\delta>0$. This continues to hold after the permitted additional prime classes in that estimate are imposed.

Let $x_*$ attain the smallest prime count among all the starts $X\le x<2X$, and call its sieve survivors $S$. Counting starts containing each prime gives mean prime count at most $H\pi(2X+H)/X=O(H/\log X)$, so the minimum satisfies the same upper bound. Of the entries in $S$, those that are prime or represented by (1) therefore number at most

$$O\!\left(\frac{H}{\log X}+\frac{H}{(\log H)^2}\right)=o(|S|).$$

Consequently a fraction $1-o(1)$ of the survivors at **every minimizing start** are actual composites with no representation (1). This assertion holds whether the minimum prime count is zero, one or larger. The size of the set left over after these factoring tests cannot identify a prime there.

## How large can the multipliers be before the count changes?

There is also a bound over a whole dyadic range, valid for $1\le D\le X^{1/3}$:

$$|F_D\cap[X,3X]|\ll\log(2D)\bigl(X^{3/4}D^{3/4}+X^{1/2}D^{3/2}\bigr). \tag{3}$$

Use the same square reduction. For each $d$, (1) gives $s\ll\sqrt{dX}$ and $t^2\le 4\sqrt{3XD}+D/d$, so $t\ll(XD)^{1/4}$. Counting the permitted $t$ in their at most $2\cdot2^{\omega(d)}$ classes for each reduced $s$ bounds the number of triples by

$$\ll\sum_{d\le D}\sqrt{dX}\,2^{\omega(d)}\left(1+\frac{(XD)^{1/4}}d\right).$$

Each triple gives at most one integer $n$. The divisor-sum estimates used for (2) give (3).

Two consequences check the reach of this argument on actual integers.

* With $D=\lfloor X^{1/3}/(\log X)^5\rfloor$, (3) is $O(X/(\log X)^{11/4})$. There are $\gg X/(\log X)^2$ distinct semiprimes $pq\in[X,2X]$ with both primes in $[\sqrt X,\sqrt{2X}]$, by the prime number theorem and unique factorization. Consequently a fraction $1-o(1)$ of those balanced semiprimes escape (1). Conversely, taking $D=\lceil(2X)^{1/3}\rceil$ detects all of them for sufficiently large $X$. Apply Lehman's theorem with $\eta=D$ and $p\le q$. Its factor-size condition $p>\sqrt{pq/(D+1)}$ holds, and its width $\sqrt{pq}/(4(D+1)\sqrt d)$ is at most $\sqrt{D/d}$. Thus the exponent $1/3$ for this particular search is already needed for balanced products. [Hittmeir, Theorem 2.1](https://publications.sba-research.org/publications/042021_Hittmeir_A%20time-space%20tradeoff%20for%20Lehman%27s%20deterministic%20integer%20factorization%20method.pdf)
* Fix $0<\varepsilon<1/3$ and put $D=\lfloor X^{1/3-\varepsilon}\rfloor$. Each represented integer belongs to at most $H$ windows, so (3) rules out all hits from every start except $O_\varepsilon(X^{1-3\varepsilon/4}(\log X)^3)$ of them. In particular, take any prime count $k$ in the submean range of our [Maier-block result](count-polynomials.md). That result supplies at least $X^{1-o(1)}$ distinct starts with exactly $k$ primes, one per qualifying block, under its stated zeta and Dirichlet hypotheses. Removing the exceptional starts still leaves $X^{1-o(1)}$ such windows with **no** hit from (1). This is a statement about known nonempty windows. Estimate (3) alone cannot specify whether the minimizing start lies in the exceptional set.

The missing comparison for Cramér is between the total number of survivors and the number of **all** composite survivors at the same minimizing start. Estimate (2) controls one family of factorizations there. The composites outside that family can still occupy every surviving position. These deductions use the cited sieve, factorization theorem and prime distribution results. Independent priority for the counting bounds is unverified. [Integer checks](check-near-square-factors.py)
