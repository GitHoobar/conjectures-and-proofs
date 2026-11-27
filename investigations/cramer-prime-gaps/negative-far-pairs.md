# A far-pair sum that resolves one prime at a fixed start

GitHoobar · 27 November 2026 · Working research note developed with OpenAI Codex and Luna agents

The original filter compares the prime mass with the pole of zeta. Here we kill the pole and give different integers disjoint supports. This yields a different signed pair sum whose required sign can be tested to within the contribution of one prime. We use the [independently checked RH theorem](https://math.mit.edu/~drew/grh/). The calculation controls an entire range of intermediate separations pointwise. The contribution beyond this range still allows an empty interval.

## Statement

Fix $C>0$, $h=\lceil C(\log x)^2\rceil$, $L=\log x$, and an integer $x$. Put $I=(x,x+h]$, $J=[\log(x+1/2),\log(x+h+1/2)]$, $\ell=|J|$, $a=1/(16x)$. Take a fixed nonzero real smooth bump $\phi$ supported in $(-1,1)$ and set $b=\phi'+(a/2)\phi$, $D=\int b^2$. Write $\widehat b(y)=\int b(u)e^{iyu}du$. Define
$$
S(t)=\sum_{|\gamma|\le x^2}\widehat b(a\gamma)e^{it\gamma},\quad
E=a^2\mathbb E_{t\in J}|S(t)|^2
$$
with uniform log-center $t$ and all ordinates counted with multiplicity. Define $R_u^*(x)$ by expanding this last energy and retaining only the ordered pairs with $|\gamma-\gamma'|>u$, keeping their phases, averaging and factor $a^2$. The star distinguishes this detector from the [original sum](signed-far-pairs.md).

Take any fixed smooth nonnegative probability density $w$ supported in $(1,2)$. With $Q=x^\sigma$, $0<\sigma<1/2$ fixed, put $\overline R_Q=\int_1^2 w(s)R^*_{sQ}(x)\,ds$. Then at **every** sufficiently large start,
$$
\frac{\overline R_Q}{aD}
=\frac1\ell\sum_{n\in I}\frac{\Lambda(n)^2}{n}-L+o(1).
\tag{1}
$$
The error tends to zero uniformly for $\sigma$ in any fixed compact subinterval of $(0,1/2)$. The proof also permits $Q=\sqrt x/L^{3+\epsilon}$ for every fixed $\epsilon>0$. The cutoff average varies only which pairs are retained. The prime-count interval $I$ remains fixed.

Let $P_2=\ell^{-1}\sum_{p^j\in I,\ j\ge2}(\log p)^2/p^j$ and $V_Q=P_2-\overline R_Q/(aD)$. A prime $p\in I$, including $p=x+h$, contributes $(\log p)^2/(p\ell)=(1+o(1))/C$. More precisely,
$$
\frac h{L^2}(L-V_Q)=\pi(x+h)-\pi(x)+o(1).
\tag{2}
$$
Indeed $p/x=1+O(h/x)$, $\ell=(h/x)(1+O(h/x))$ and $\log p=L+O(h/x)$, and the total error from replacing these factors is $O(h^2/x)=o(1)$ even with $h$ candidates. Thus **$V_Q<L-1/(2C)$ if and only if $I$ contains a prime** for all sufficiently large $x$. Equation (2) also allows recovery of the count by rounding. Establishing that inequality uniformly for some $C$ would prove Cramér. We have not established it.

Two consequences test possible bounds.

* If $0<\sigma_1<\sigma_2<1/2$ are fixed, the difference $(\overline R_{x^{\sigma_1}}-\overline R_{x^{\sigma_2}})/(aD)$ is $o(1)$ at every start. Its pair multiplier is supported on separations between $x^{\sigma_1}$ and $2x^{\sigma_2}$ and equals one between $2x^{\sigma_1}$ and $x^{\sigma_2}$. This is signed cancellation with smooth transitions at the two ends. Its error is smaller than the effect of one prime.
* A hypothetical empty interval would force $\overline R_Q/(aD)=-L+O_C(1)$. For each exponent $j\ge2$ there is at most one $j$th power in $I$, and $\sum_{j\ge2}j^{-2}<\infty$ gives $P_2=O_C(1)$. Negative far-pair sums also occur for actual primes: the [Maier deduction](aligned-windows.md) provides parents with at most $(1-\epsilon)h/L$ primes, hence $\overline R_Q/(aD)\le-(\epsilon+o(1))L$ along such starts. At least one hard cutoff $u\in[Q,2Q]$ attains that upper bound. A blanket nonnegativity argument therefore fails. Our formula still allows the excursion all the way to vacancy.

## Why the local energy counts integers exactly

Integration by parts gives $\int b(u)e^{au/2}du=0$, which kills the pole. The compactly supported smoothed explicit formula, divided by $e^{t/2}$, then gives for $|t-\log x|\le1$
$$
A(t):=\sum_n\frac{\Lambda(n)}{\sqrt n}b((\log n-t)/a)
=-a S(t)+O(ax^{-5/2}+x^{-5}).
$$
The zero transform is $a e^{it\gamma}\widehat b(a\gamma)$ on the critical line. The trivial-zero series is $O(ax^{-5/2})$ in this range. All transforms of $b$ decay faster than every power with uniform constants for $a\le1$. The zero count $N(T)\ll T\log(2T)$ makes the tail above $x^2$ after multiplication by $a$ smaller than $x^{-5}$ by choosing a sufficiently high fixed power. It also gives $a\sup_{t\in\mathbb R}|S(t)|\ll L$. Finally $D=\int(\phi')^2+(a^2/4)\int\phi^2$ is bounded above and away from zero. [Background explicit formula](finite-zero-test.md)

Near these centers distinct log-integers are more than $2a$ apart. In $J$ the bumps of $x+1,\ldots,x+h$ fit in full, and no neighboring integer has a bump intersecting $J$. These claims follow from the mean value theorem for $\log$ and the half-integer boundary margins. Squaring $A(t)$ leaves only squares of individual terms. Integration gives
$$E=\frac{aD}{\ell}\sum_{n\in I}\frac{\Lambda(n)^2}{n}+o(a).\tag{3}$$

## Evaluating the complement of the far sum

The multiplier on the complementary pairs is $H((\gamma-\gamma')/Q)$ with $H(y)=\int_{|y|}^{\infty}w(s)ds$. This smooth even function equals one on $[-1,1]$ and vanishes outside $[-2,2]$. Let $k$ be its inverse Fourier transform in the convention $H(y)=\int k(v)e^{iyv}dv$. Then $k$ is real, even and rapidly decreasing, with $\int k=1$. It may take both signs. Expanding the finite sum gives the exact identity
$$
E-\overline R_Q=a^2\mathbb E_{t\in J}\int_{\mathbb R}Qk(Qv)|S(t+v)|^2dv.
\tag{4}
$$
We now show that (4) equals $aD(L+o(1))$ with **absolute** error $o(a)$. This precision matters since one prime changes (3) by order $a/C$.

Insert a fixed smooth cutoff $\chi(v)$ equal to one on $[-1/4,1/4]$ and zero outside $[-1/2,1/2]$. The omitted integral is $O_N(L^2Q^{-N})=o(a)$ by the global bound on $aS$. On the remaining support substitute $A$ using the explicit formula with an error in the energy of $o(a)$ (use $|aS|\ll L$ for the cross term). The integer bumps are disjoint throughout this larger region. For $K_Q(v)=\chi(v)Qk(Qv)$ their squared contribution at fixed $t$, after changing variables, is
$$
a\int b(u)^2\sum_n\frac{\Lambda(n)^2}{n}K_Q(\log n-t-au)\,du .
$$

Uniformly for $y\asymp x$ one has $\sum_{n\le y}\Lambda(n)^2=y\log y-y+O(\sqrt y\log^3(2y))$. This follows by partial summation of $\vartheta(y)=y+O(\sqrt y\log^2 y)$ and adding the proper powers: there are $O(\sqrt y)$ such powers, by counting $j=2$ separately and bounding $j\ge3$ by $O(y^{1/3}\log y)$. [Schoenfeld's RH estimate](https://doi.org/10.1090/S0025-5718-1976-0457374-X)

Apply this estimate by partial summation to $K_Q(\log y-z)/y$ with $z=t+au$. Its total variation on its support is $O((1+Q)/x)$, from $\|K_Q\|_1=O(1)$ and $\|K'_Q\|_1=O(Q)$. The inner sum therefore equals
$$
\int (z+v)K_Q(v)\,dv+O(Q L^3/\sqrt x)=L+o(1).
$$
Here $z=L+O(h/x+a)$, $\int K_Q=1+O_N(Q^{-N})$, and its absolute first moment is $O(1/Q)$. These errors have the stated uniformity in $\sigma$. This proves the evaluation of (4), and subtracting it from (3) proves (1).

## Does positivity force the missing one-prime margin?

The full energy is a squared norm. Its lower bound from positivity is zero. We tested whether that constraint, together with all the intermediate-band cancellations above, forces a larger minimum. There is a two-frequency example saturating the vacancy value under those constraints.

In normalized energy units let $t_0$ be the midpoint of $J$, $\omega=x^{3/4}$ and $D_0(t)=\sqrt{2L}\sin(\omega(t-t_0))$. Then $|D_0(t)|^2=L(1-\cos(2\omega(t-t_0)))$. All the complementary multipliers $H(2\omega/Q)$ vanish for $Q\le\sqrt x$, so every smoothed near energy is exactly $L$. But on $J$ the full energy is at most $2L(\omega\ell)^2=o(1)$. Every one of these far sums is $-L+o(1)$ and every difference between the cutoffs is exactly zero. This verifies the failure of a positivity-only argument at one-prime resolution. The example uses freely chosen frequencies and phases. Excluding the same depth for the zeta sum requires an estimate using the arithmetic of its particular ordinates or coefficients.

Earlier, Languasco, Perelli and Zaccagnini obtained a smoothed $\Lambda(n)^2/n$ main term for extended pair correlation. Here the local interval has exact integer endpoints, and the estimate for the smooth complementary multiplier isolates the effect of intermediate separations at each start. The finite checks verify the sign of the cutoff complement and replay the local explicit formula at prime, composite and proper-power inputs. With Odlyzko’s first 100,000 ordinates, the largest discrepancy across the nine pulse evaluations was $3.36\times10^{-9}$. This checks the normalization and signs in the linear formula used in (3). [LPZ, Theorem 1 and the definition of $S(X,\tau)$](https://arxiv.org/pdf/1311.0597) · [Verification script](check-far-pairs.py)

The use of RH, the explicit formula, and Fourier smoothing are established tools. The notes concern the stated choice of weights and the remaining pointwise estimate, with no claim of independent priority.
