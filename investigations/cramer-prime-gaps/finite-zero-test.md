# A finite zero sum for the specified interval

GitHoobar · 27 November 2026 · Working manuscript developed with OpenAI Codex and Luna agents

We want to detect a prime in $(x,x+h]$ at the given integer $x$. The construction below bounds the contribution from all zeta zeros above height $O_C(x/\log x)$ and removes every proper prime power exactly. A second cutoff of order $x\log x$ gives every integer in the interval full weight, including the right endpoint. Controlling the remaining finite expression at every start is open. In particular, replacing the remaining sum by a uniform small error would contradict known intervals for the actual primes.

## The test

Fix $C>0$, $0<b<1/4$, and let $L=\log x$, $h=\lceil C L^2\rceil$, $\delta=\log(1+h/x)$, $K=\lceil8L\rceil$, $T=4K/(b\delta)$. Let $f$ be the indicator of $[b,1-b]$ convolved with $K$ copies of the uniform probability density on $[-b/K,b/K]$. Thus $0\le f\le1$, its support lies in $[0,1]$, and it equals one on $[2b,1-2b]$. Its transform is
$$F(w)=\int_0^1 f(u)e^{wu}\,du
=\left(\int_b^{1-b}e^{wu}\,du\right)
\left(\frac{\sinh(bw/K)}{bw/K}\right)^K.$$
The value at zero is $1-2b$. Write $u_n=\log(n/x)/\delta$. Define
$$
Z_T(x)=\Re\sum_{|\operatorname{Im}\rho|\le T} x^{\rho-1} F(\delta\rho),\qquad
D=\delta\int_0^1\frac{f(u)}{x^2e^{2\delta u}-1}\,du,\qquad
P=\sum_{\substack{x<p^j\le x+h\\j\ge2}}(\log p) f(u_{p^j}).
$$
The zeros $\rho$ are all the nontrivial zeros of the Riemann zeta function with multiplicity. Their real parts are retained. **No Riemann hypothesis is needed.**

Put $A(x)=\delta x\,[F(\delta)-Z_T(x)]-D-P$. Then
$$
A(x)=\sum_{x<p\le x+h}(\log p)f(u_p)+O_{b,C}(x^{-3}).
\tag{1}
$$
In particular, for all sufficiently large $x$, **$A(x)>1$ certifies an actual prime in that very interval**. A prime in the central plateau guarantees $A(x)>1$. A prime arbitrarily close to the boundary can receive a small weight.

For any fixed $b$ as above, Cramér's conjecture is equivalent to $A(x)>1$ for every sufficiently large integer $x$ for some fixed $C$. Indeed, under Cramér take $C$ large enough that the central plateau, of additive length $(1-4b+o(1))h$, must contain a prime by the gap bound. Conversely, apply the certificate at each sufficiently large prime $x=p_n$ to bound the following gap. This equivalence leaves freedom to enlarge $C$.

## Error at one location

The smoothed von Mangoldt explicit formula gives
$$\sum_n\Lambda(n) f(u_n)
=\delta x F(\delta)-\delta\sum_\rho x^\rho F(\delta\rho)-D.$$
For the normalization, Mellin inversion of the weight has transform $\delta x^s F(\delta s)$. The pole of $-\zeta'/\zeta$ at $1$ contributes its value there, nontrivial zeros give the negative sum, and the trivial zeros give $-\delta\sum_{j\ge1}x^{-2j}F(-2j\delta)=-D$. Equivalently integrate the classical explicit formula for $\psi$ against the derivative of the weight: the constant disappears and the endpoint half-weights have no effect. For each fixed $x$ this compactly supported spline has enough derivatives for absolute convergence after smoothing. [Carneiro, Milinovich and Soundararajan, §5, for the explicit-formula method in prime gaps](https://arxiv.org/pdf/1708.04122)

For $0<\Re\rho<1$ and $\gamma=\Im\rho\ne0$, the transform gives
$$|F(\delta\rho)|\le3\left(\frac{K}{b\delta|\gamma|}\right)^K$$
for large $x$. Indeed $|\sinh z|\le e^{|\Re z|}$, and the $K$ numerator factors together cost at most $e^{b\delta}$. On dyadic shells above $T$, the classical zero count $N(t)\ll t\log(2t)$ therefore bounds the discarded contribution in absolute prime-weight units by
$$\ll\delta x\, T\log(2T)\,4^{-K}.$$
The geometric sum over successive shells has a bounded factor since $K\ge3$. As $\delta x\sim h$, $T\asymp_{b,C}x/L$ and $K\ge8L$, the displayed error is $O(x^{-3})$.

For each integer $2\le j\le\log(x+h)/\log2$, the interval contains at most one integer $j$th power for large $x$. Neighboring $j$th powers near or above $x$ are separated by at least a constant times $\sqrt x$, uniformly in $j$, since $(n+1)^j-n^j\ge jn^{j-1}$ for $n^j\ge x$. Thus the sum $P$ can be obtained by taking one integer root per exponent and testing its base for primality. It obeys $0\le P\ll L\sum_{j\ll L}1/j\ll L\log L$. Subtracting the exact $P$, including powers whose exponents are themselves composite, gives (1).

## An endpoint-sensitive test at exactly the requested start and length

There is also a necessary **and** sufficient test at the individual integer pair $(x,h)$, at the cost of a higher zero cutoff. Place the support endpoints at $a=x+1/2$ and $a+h=x+h+1/2$. Use the same formulas with anchor $a$, $\delta'=\log(1+h/a)$, $b'=1/(16h)$ and $K'=\lceil8\log a\rceil$. Denote the resulting statistic by $A_{\rm cell}(x,h)$. The plateau starts at $ae^{2b'\delta'}$ and ends at $ae^{(1-2b')\delta'}$. Each end of the support is within $2b'(a+h)\delta'\le4b'h=1/4$ of its corresponding plateau endpoint for sufficiently large $x$, since $h=o(x)$. Thus the weight is exactly one at each integer $x+1,\ldots,x+h$ and vanishes at every other integer. In particular the proper-power subtraction is now simply the sum of $\log p$ over proper prime powers in the given interval.

Here $T'=4K'/(b'\delta')=O_C(x\log x)$. The bound on the transform above height $T'$ has the same absolute prefactor $3$, uniformly in $b'$. The omitted tail is $O(\delta'a\,T'\log(2T')4^{-K'})=O_C(x^{-3})$. Hence
$$A_{\rm cell}(x,h)=\sum_{x<p\le x+h}\log p+O_C(x^{-3}).$$
For all sufficiently large integer $x$ and $h=\lceil C(\log x)^2\rceil$, the interval contains a prime **if and only if** $A_{\rm cell}(x,h)>1$. An empty window gives $O_C(x^{-3})$ while any prime contributes at least $\log(x+1)$. This removes the tapered test's ambiguity about a prime on the boundary without moving the set of integers tested.

Consecutive empty starts $s,\ldots,s+k-1$ for windows of a common integer length $h$ amount to one empty interval $(s,s+h+k-1]$. For $s$ large, $h\asymp(\log s)^2$ and $1\le k\le h$, the same tail estimate applies to that length. Thus a whole run would force $A_{\rm cell}(s,h+k-1)=O(s^{-3})$. A value above one for this union excludes the run, but a prime in the union need not lie in its first window. To certify the first window itself, the statistic must exceed one at $(s,h)$.

## How much can a different smoothing kernel lower the cutoff?

There is a matching lower bound for the particular strategy of suppressing **all real frequencies** above the cutoff by a fixed power of $x$. For any nonzero integrable $w\ge0$ supported in $[0,1]$, normalize
$$H(z)=\frac{\int_0^1 w(u)e^{izu}\,du}{\int_0^1 w(u)\,du}.$$
For every $B>0$,
$$\sup_{|t|\ge B}|H(t)|\ \ge\ e^{-2B}.$$

Indeed $|H|\le1$ on the closed upper half-plane and $H(iB)\ge e^{-B}$. Put $q=\sup_{|t|\ge B}|H(t)|$. The Poisson kernel at $iB$ gives the exterior of $[-B,B]$ harmonic measure $1/2$, since $\int_{-B}^B B/(\pi(t^2+B^2))\,dt=1/2$. The two-constants theorem for a bounded analytic function gives $|H(iB)|\le q^{1/2}$. Equivalently apply the subharmonic Poisson inequality to $\log|H|$, bounded on the exterior by $\log q$ and elsewhere by zero. This proves the inequality, also for a weight chosen separately at each $x$.

If the desired suppression is $x^{-A}$ for fixed $A>0$, the scaled cutoff must satisfy $\delta T\ge(A/2)\log x$. Hence $T\gg_{A,C}x/\log x$. This reasoning applies along any fixed real part of the Mellin transform by incorporating the positive exponential factor into $w$. Our spline attains that order. The displayed transform bound at $4K/(b\delta)$ gives a fixed power saving, and increasing the multiplier of $\log x$ in $K$ gives any prescribed power saving. The lower bound concerns continuous-frequency suppression by a nonnegative weight. The zeros sample discrete frequencies, and cancellation between their contributions remains available.

## Which estimate fails, and which remains open?

Fix the $\epsilon>0$ from [the alignment theorem](aligned-windows.md), choose $b<\epsilon/8$, and fix any $C>0$. There are arbitrarily large $X$ with runs of $\gg_C(\log X)^2$ consecutive starts $x$ for which
$$ Z_T(x)\ge\epsilon/2.$$
To see this, use the simultaneous bound there with the actual $h=\lceil C(\log x)^2\rceil$. The allowed shifts include every $v\le(\epsilon/2)C(\log X)^2$ after any retained anchor, for large $X$. All prime weights together are then at most $(1-\epsilon+o(1))h$, because $f\le1$ and $\log p\sim\log X$. Also $P=o(h)$, $D=o(1)$, $\delta x\sim h$ and $F(\delta)=1-2b+O(\delta)$. Equation (1) gives the assertion. Thus a uniform upper bound $Z_T=o(1)$ is already false, even for strings of consecutive starts. Under RH the unnormalized exponential sum $\Re\sum x^{i\gamma}F(\delta\rho)$ on those starts is at least $(\epsilon/2)\sqrt x$.

If a window is actually empty, (1) instead gives
$$ Z_T(x)=F(\delta)-(D+P)/(\delta x)+O(x^{-3}/h).$$
The unresolved estimate is whether the zero sum stays below $F(\delta)-(D+P+1)/(\delta x)$ at **every** sufficiently large integer $x$ for a suitable $C$. Known deficient windows force a positive excursion. They do not force the nearly full excursion at vacancy.

We tried bounding the finite sum term by term. For $|\gamma|\le 1/(2\delta)$, the real part of $F(\delta\rho)$ is at least $(1-2b)\cos(1/2)$ by its integral representation. By symmetry about the critical line at least half the zeros in the range have $\Re\rho\ge1/2$. The Riemann–von Mangoldt counting asymptotic gives $\gg\delta^{-1}\log(1/\delta)$ such zeros, counting multiplicities and allowing a fixed absolute factor. Consequently the sum of absolute values of the normalized terms already exceeds a constant times $\sqrt{x}/\log x$. This calculation identifies the missing cancellation inside the retained sum. Controlling the tail to less than one prime does not give that cancellation.

The explicit formula, smoothing by convolution, and zero counting are classical. We claim no independent priority for this choice of filter or cutoff. The [companion note](aligned-windows.md) supplies the aligned deficits. The optional [numerical replay](check-zero-sum.py) compares both formulas with a direct prime count. In $(113,126]$ the tapered test sees only proper powers, and in $(113,127]$ the prime 127 has zero endpoint weight. In $(113,130]$ its weight contributes about 4.8434 after multiplication by $\log 127$. The endpoint-sensitive test recovers zero on $(7,10]$ and $\log 11$ on $(7,11]$, subtracting $\log 2+\log 3$ for 8 and 9 in both cases. All five floating-point discrepancies are below $3\cdot10^{-9}$. These are checks of normalization and endpoints. Equation (1) and its endpoint-sensitive variant have analytic error bounds for large $x$.
