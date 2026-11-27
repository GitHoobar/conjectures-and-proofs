# How much prime-count information does the gap bound require?

GitHoobar · 27 November 2026 · Working note developed with OpenAI Codex

Our previous sufficient condition uses a squared polynomial in the number of primes in a window. We show that, in the parameter range used there, this condition would force a growing minimum count even in windows of twice the test length. A different average gives an exact reformulation of the ordinary gap bound. [Previous polynomial](wheel-threshold.md)

## An equivalent test on actual primes

Let $X$ range over powers of two. Fix $C>0$, write $h=\lceil C(\log X)^2\rceil$, and count primes in $(x,x+h]$ by $Y_x$. For integer starts $X\le x<3X$, let $E$ be the number with $Y_x=0$. With $q=h/(2X)<1$ for large $X$,

$$ E\le\sum_{X\le x<3X} q^{Y_x}\le E+h.$$

Indeed, each empty interval contributes one. The combined contribution of the other intervals is at most $2Xq=h$.

**Proposition.** Cramér's conjecture is equivalent to the existence of fixed $C,K>0$ such that this sum is at most $Kh$ for all sufficiently large dyadic $X$.

Under the conjecture, the gap following the last prime at or before $x$ has length $O(\log^2(3X))$ uniformly in the indicated range. Choose $C$ large enough that every interval contains a prime. Then the upper bound holds with $K=1$. Conversely take a prime $p\in[X,2X)$. If its next gap exceeds $(K+2)h$, the starts $p,p+1,\ldots,p+\lfloor(K+1)h\rfloor$ all have empty windows and all lie in $[X,3X)$ for large $X$. Their contributions alone exceed $Kh$. This proves the equivalence. The outstanding step is to bound this sum for actual primes. Our follow-up gives a bound in every class of a suitable modulus and measures exactly how a long gap can escape such classwise estimates. [Testing exceptional starts](primes-in-residue-classes.md)

## What the squared polynomial forces

Use $r\asymp\log X$ and take $C$ large enough that $r\le m\rho/4$ at every start. Here $m$ is the number of eligible positions in its window, $0<\rho\le1/2$ is the reference marking probability and $t=\rho/(1-\rho)$. The earlier note gives the uniform lower bound for $m\rho$ used in this choice of $C$. Write $Q(y)$ for the sum of the coefficients through degree $r$ of $(1-w)^y(1+tw)^{m-y}$ and write $K_0=Q(0)$.

For $y\ge1$, summing coefficients is equivalent to taking $[w^r](1-w)^{y-1}(1+tw)^{m-y}$. In particular, $Q(1)=\binom{m-1}r t^r\ge K_0/2$. To see the inequality, successive terms of $K_0$ in descending order have ratio at most $r/((m-r+1)t)\le 2/7$, while $\binom{m-1}r/\binom mr=1-r/m\ge7/8$.

Put $d=y-1$ and $u=r/((m-1)\rho)\le1/3$ for large $r$. Replacing each $1-w$ by $(1+tw)-(1+t)w$ gives the exact identity, with falling factorials $(n)_j$,

$$\frac{Q(y)}{Q(1)}=\sum_{j=0}^d(-1)^j\binom dj\,\rho^{-j}\frac{(r)_j}{(m-1)_j}.$$

For $j\le d\le\tfrac12\log r$, the factor multiplying $(-1)^j\binom dj$ differs from $u^j$ by at most $u^j j(j-1)/(2r)$. Indeed the ratio to $u^j$ is the product of $(1-i/r)/(1-i/(m-1))$ for $0\le i<j$. This product is at most one and at least $1-\sum_{i<j}i/r$. The absolute error in replacing the displayed sum by $(1-u)^d$ is at most $d^2(1+u)^d/(2r)$. Its relative error is at most $d^2 2^d/(2r)=o(1)$ uniformly. Thus $Q(y)/K_0\ge (2/3)^y/4$ whenever $0\le y\le\tfrac12\log r$, including $y=0$ directly.

Suppose a window $(s,s+2h]$ contains at most $\tfrac12\log r$ primes and that the $h$ starts from $s$ through $s+h-1$ are in the summation range of the earlier test. Every one of their length-$h$ windows then has at most that many primes. Their contribution to $\sum_x(Q_x(Y_x)/K_{0,x})^2$ is at least $h(2/3)^{\log r}/16$, which tends to infinity since $h\asymp r^2$. Hence an upper bound below one for that sum would force more than $\tfrac12\log r$ primes in every such double window.

A square-logarithmic gap bound alone has no comparable implication for general integer sets. For example take $a_1=3$ and $a_{n+1}=a_n+\lceil(\log a_n)^2\rceil$. The defining gaps obey the bound, and windows of length $2C\log^2 X$ inside $[X,2X]$ contain only $O_C(1)$ terms because successive terms there are at least $\log^2 X$ apart. For ordinary primes the weighted count in the proposition removes this extra minimum-count requirement. It still requires control over exceptional locations across the entire dyadic range. [Exact coefficient checks](check-rough.py)
