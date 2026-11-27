# Wide zero separations at the center of a sparse prime interval

GitHoobar · 27 November 2026 · Research note developed with OpenAI Codex and Luna agents

For an interval of length $h=\lceil C(\log x)^2\rceil$, we isolate a signed sum of zero pairs at its exact logarithmic midpoint. If the interval has a fixed fractional shortage of primes, this sum is at most $-c\log x$ for some $c>0$ depending on the shortage. Its multiplier vanishes unless the separation lies between $\sqrt{x}/\log^4 x$ and a constant times $x/h$. Maier's theorem supplies infinitely many actual intervals exhibiting the effect. We also give a formula that converts a band of pairs into individual zeros in the same band, with an explicit correction at prime powers. The remaining bound for an actual prime at the minimum is open.

## A finite band at the specified interval

Let $x$ be an integer, $C>0$ fixed, $L=\log x$, $I=(x,x+h]$. Write $m$ and $\delta$ for the midpoint and **half** the length of $[\log(x+1/2),\log(x+h+1/2)]$. In particular $2\delta\sim h/x$. We use RH as recorded in the [independent Lean verification](https://math.mit.edu/~drew/grh/).

Use the pulse of the [preceding note](negative-far-pairs.md). For clarity, $a=1/(16x)$, $b=\phi'+a\phi/2$ for a fixed real nonzero smooth $\phi$ compactly supported in $(-1,1)$, $D=\int b^2$, $c_\gamma=\widehat b(a\gamma)$, and $\widehat g(y)=\int g(v)e^{iyv}dv$. For an even real multiplier $M$ let
$$
P_m[M]=\frac{a}{D}\sum_{|\gamma|,|\gamma'|\le x^2}
c_\gamma\overline{c_{\gamma'}}e^{im(\gamma-\gamma')}M(\gamma-\gamma').
$$
This sum is real and counts ordered pairs with multiplicity. Fix a smooth even low-frequency cutoff $H$ supported on $[-2,2]$, equal to one on $[-1,1]$, as in the preceding note. Put $Q_0=\sqrt{x}/L^4$.

Given $0<\eta<1$, choose a fixed even real Schwartz function $f$ with
$$
f(u)\le {\bf1}_{[-1,1]}(u),\qquad A_f=\int f>2-\eta,\qquad
\operatorname{supp}\widehat f\subset[-B,B].
$$
Here $B$ depends on $\eta$. Define $M(d)=\widehat f(\delta d)(1-H(d/Q_0))$. At every sufficiently large start we obtain
$$
P_m[M]\ \le\ \delta^{-1}\sum_{n\in I}\frac{\Lambda(n)^2}{n}-A_fL+o(1). \tag{1}
$$
The multiplier is exactly zero for $|d|\le Q_0$ and for $|d|>B/\delta$. Large *individual* ordinates can still participate in a pair whose difference is in this band.

If $I$ contains no prime, the surviving proper powers on the right contribute $O_C(1)$. More precisely their contribution is the computable sum $U=\delta^{-1}\sum_{p^j\in I,\,j\ge2}(\log p)^2/p^j$. For each exponent there is at most one such integer, by the spacing of consecutive $j$th powers near $x$, and $\sum_{j\ge2}j^{-2}<\infty$. A prime contributes $(2+o(1))/C$. Thus, for example, a proof of $P_m[M]+A_fL-U>1/C$ at every sufficiently large start would force a prime in every target interval. Inequality (1) gives only a sufficient test in this direction. A prime near the edge can receive little weight from the minorant.

If $I$ contains at most $(1-\eta)h/L$ primes, (1) gives
$$
P_m[M]\le -\eta L+O_C(1)+o(1).
$$
Indeed each prime has weight $(L^2/(x\delta))(1+O(h/x))$, and $h/(x\delta)=2+O(h/x)$. For every fixed $C$ there is some fixed $\eta>0$ for which such intervals exist at arbitrarily large $x$, by applying Maier's theorem as in the [aligned-window deduction](aligned-windows.md). This gives a sign and order of magnitude on real sparse intervals. A uniform $o(L)$ bound for the absolute value of this signed band is consequently false. [Maier, *Primes in short intervals*](https://doi.org/10.1307/mmj/1029003189)

The large negative value also occurs at windows that contain many primes. To see this, start at a Maier-deficient $x_0$ with fractional deficit $\eta_0>0$, and keep $h(y)=\lceil C\log^2 y\rceil$ as the start moves through $[x_0,2x_0]$. Averaging the counts for the shorter fixed length $h(x_0)$ and using the prime number theorem supplies a start with at least $(1-o(1))C\log x_0$ primes. Consecutive moving-window counts differ by at most two, since the right endpoint advances by at most two integers. They must cross $(1-\eta_0/2)C\log x_0$ to within two. At a crossing the interval contains $(1-\eta_0/2)h(y)/\log y+O_C(1)$ primes. Choose $\eta=\eta_0/4$ in (1). The negative excursion persists there even with a prime count growing proportionally to $\log y$.

### Proof of the minorant and (1)

Choose a real even smooth cutoff $0\le r\le1$, compactly supported in $(-1,1)$, equal to one on a central interval long enough that $\int r^2>2-\eta$. Set $q(u)=r(u)/\sqrt{1-u^2}$ on its support and zero elsewhere. Multiply $\widehat q$ by smooth compactly supported even cutoffs equal to one on growing centered intervals. Their inverse transforms $g$ converge to $q$ in Schwartz space. Then $(1-u^2)g^2$ converges to $r^2$ there and is nonpositive outside $[-1,1]$. Divide it by the larger of one and its maximum on $[-1,1]$. The divisor tends to one. For a sufficiently large fixed cutoff the resulting $f$ has the asserted integral and sign, and its Fourier transform has compact support by convolution and differentiation.

We record a kernel identity also used below. If $M(d)=F(d/Q)$, let $k$ be the inverse transform of $F$, and $K(v)=\chi(v)Qk(Qv)$ for a fixed even smooth $0\le\chi\le1$ supported in $(-1/2,1/2)$ and equal to one on $[-1/4,1/4]$. Use $x^\epsilon\le Q\le xL^A$ for fixed $0<\epsilon<1$ and $A\ge0$. Here $F$ is smooth, with uniformly bounded derivatives of every fixed order and support in a fixed compact set. Write $\mathbb E_u$ for the probability density $b(u)^2/D$ and $z=m+au$. Fourier inversion and the disjoint integer pulses give
$$
P_m[M]=\mathbb E_u\sum_n\frac{\Lambda(n)^2}{n}K(\log n-z)+o(1). \tag{2}
$$
Indeed expand $|\sum c_\gamma e^{i(m+v)\gamma}|^2$ against $Qk(Qv)$ and use the local explicit formula from the preceding note. The discarded physical tail is $O_N(a^{-1}L^2Q^{-N})$ since $a|\sum c_\gamma e^{it\gamma}|\ll L$. On the retained support the replacement of the pulse by the arithmetic sum has error $O(ax^{-5/2}+x^{-5})$ before squaring, and $\|K\|_1=O(1)$. Different integers have disjoint pulses throughout that region. Changing variables in each squared pulse gives (2). The estimates are uniform for the multiplier families just specified.

For $M(d)=\widehat f(\delta d)$, use $Q=1/\delta$ in (2). Each weight $\chi(v)f(v/\delta)$ is at most one and nonpositive for $|v|>\delta$. For $|u|\le1$, the interval $[z-\delta,z+\delta]$ contains the logarithms of precisely the integers of $I$. Its endpoints are shifts by at most $a$ of the log half-integers, strictly smaller than their distances to adjacent log integers for large $x$. Hence the full multiplier contributes at most the first term of (1).

For the low part, apply (2) with $Q=Q_0$ and $F(y)=H(y)\widehat f(\delta Q_0 y)$. The derivatives are uniformly bounded since $\delta Q_0=o(1)$. The RH estimate $\sum_{n\le v}\Lambda(n)^2=v\log v-v+O(\sqrt v\log^3(2v))$ and partial summation give $zF(0)+O(Q_0L^3/\sqrt x)+o(1)=LA_f+o(1)$. Here the total variation of $K(\log v-z)/v$ is $O(Q_0/x)$, and $K$ has mass $F(0)+O_N(Q_0^{-N})$ and absolute first moment $O(1/Q_0)$. Subtraction proves (1). [Derivation of the RH estimate and pulse formula](negative-far-pairs.md)

## From pairs to individual zeros in the same band

For $M(d)=F(d/Q)$ as in (2), define the signed, explicit proper-power correction
$$
D_M=\mathbb E_u\sum_{j\ge2,\,p\ {\rm prime}}\frac{(j-1)(\log p)^2}{p^j}K(\log p^j-z).
$$
Uniformly at the given start,
$$
P_m[M]=LM(0)-D_M-
\mathbb E_u\left[z e^{-z/2}\sum_{\gamma}e^{i\gamma z}M(\gamma)\right]+o(1). \tag{3}
$$
By subtraction this also holds for the band in (1), with its two respective kernels and $M(0)=0$. It holds after averaging $m$ over the original log interval as well, since the proof of (2) and (3) is uniform in that region. In particular two smoothed cutoffs $H(d/Q_2)-H(d/Q_1)$ in the earlier pair sum transfer to the same two cutoffs on individual ordinates. This retains the absolute $o(1)$ precision even for $Q_2$ above $\sqrt x$. It computes the unknown term in a different form.

**Proof.** At primes $\Lambda(n)\log n=\Lambda(n)^2$. At $p^j$ the excess is $(j-1)(\log p)^2$, giving the sign of $D_M$. Apply the smooth explicit formula to $G(y)=(\log y)K(\log y-z)/y$. Its Mellin transform is
$$
\int_0^\infty G(y)y^{s-1}dy
=e^{(s-1)z}\int(z+v)e^{(s-1)v}K(v)dv .
$$
At the pole this is $zF(0)+o(1)$. The trivial zeros have total contribution $O(Lx^{-3})$ using $|v|<1/2$ and the resulting geometric series. At $s=1/2+i\gamma$, after factoring out $e^{-z/2+i\gamma z}$, the integral is
$$
zF(\gamma/Q)+O_N\left(\frac LQ(1+|\gamma|/Q)^{-N}\right).
$$
To see the decay, set $r=Qv$ and subtract $zk(r)$ from $(z+r/Q)e^{-r/(2Q)}\chi(r/Q)k(r)$. The difference and each fixed derivative have $L^1$ norm $O_N(L/Q)$ by the first-order Taylor bound on the cutoff support and rapid decay outside it. Integration by parts gives the estimate. The zero count $N(T)\ll T\log(2T)$ bounds the sum of these errors by $O(L\log(2Q)/\sqrt x)=o(1)$. The zero terms enter with a minus sign. This proves (3).

For the particular band (1), $|D_M|=O_C(\log L)$. For a fixed $j$ the log integers $\log(k^j)$ in the compact physical support are spaced by $\gg 1/\sqrt x$ (apply the mean value theorem to $y^{1/j}$ there). Thus the sum of the absolute kernel weights for these points is $O(Q+\sqrt x)$ by Schwartz decay. Each arithmetic coefficient is $O(L^2/(jx))$, and $j=O(L)$. Sum over $j$ at $Q=1/\delta$ and $Q_0$ to get the bound. For one-prime precision use the exact $D_M$ in (3).

### A signed sum at the midpoint itself

The phase average in (3) comes from the original pulse. We can also locate the single-zero excursion at $m$ itself. Write $S_m=\sum_\gamma M(\gamma)e^{im\gamma}$ for the band in (1). Then
$$
m e^{-m/2} S_m \ \ge\ A_f L-
\delta^{-1}\sum_{n\in I}\frac{\Lambda(n)\log n}{n}+o(1). \tag{4}
$$
Indeed apply the Mellin calculation above directly at $z=m$ to the arithmetic weight $\Lambda(n)\log n/n$. The full kernel minorizes the scaled interval indicator and the arithmetic weights are nonnegative. For the low kernel the pole is $A_f L+o(1)$ and the zero term is $O(LQ_0\log(2Q_0)/\sqrt x)=o(1)$ by absolute values. Subtract the two identities. This time no expectation over $u$ occurs.

The proper powers in (4) contribute $O_C(\log L)$ by summing $O_C(1/j)$ over the exponents. Keep their exact sum $U_{\log}$ to work at one-prime precision. A fixed fractional deficit forces $S_m\gg_\eta\sqrt{x}$, and an empty interval would force $m e^{-m/2}S_m\ge A_fL-U_{\log}+o(1)$. In particular any uniform upper bound below $A_f L-U_{\log}-1/C$ in this normalization would suffice. This is a one-sided certificate for the interval with its original endpoints.

## The upper tail of the original pair detector

There is also a tail we can discard at **every** start. In the original window-averaged detector let $Q=x\,r(x)$ with $r(x)\to\infty$ and $r(x)\le L^A$. Its far sum satisfies $\overline R_Q/(aD)=o(1)$. This concerns the old multiplier $1-H(d/Q)$ itself. The finite band in (1) uses a different multiplier that gives a one-sided inequality at the much lower upper separation $B/\delta$.

To prove the tail estimate, average (2) over $m=t\in J$, the original log interval, using $F=H$ and kernel $K$. Uniformly in $|u|\le1$, the integral $\int_J K(\log n-t-au)\,dt$ approximates $\mathbf1_I(n)$. For $n\asymp x$ write $d_n=\min(|n-x|,|n-x-h|)$. The distance to the nearer shifted log endpoint is $\gg(1+d_n)/x$, by the half-integer margins. The integrated Schwartz tail bounds the error by $O_N((1+r(x)(1+d_n))^{-N})$, plus $O_N(Q^{-N})$ for an inside integer from the kernel's total mass. Only $n\asymp x$ can meet its compact support. There are $O(1)$ integers at each distance, and $\Lambda(n)^2/(n|J|)=O_C(1)$. The summed error is $O_{N,C}(r(x)^{-N}+hQ^{-N})=o(1)$ for $N>1$. The full energy has exactly this interval mass up to $o(1)$ by the original pulse identity. Their difference is the claimed far tail.

## Where the attempt to force a prime stops

RH locates every ordinate on the critical line and permits (3). Bounding the individual terms by absolute value at height $B/\delta$ gives $O((x/h)L)$ for the unscaled sum, far above $\sqrt{x}$. A Cauchy–Schwarz estimate over centers would have to control the exceptional midpoint itself. Cully-Hugill and Dudek obtain an explicit positive proportion of good centers at this length scale. Their theorem allows exceptional centers. The one-sided Riesz estimate in the RH argument also supplies no lower bound for the second difference at three specified points. We checked these routes independently with Luna agents. The necessary estimate still missing is a pointwise **lower** bound on (1)'s signed pair sum strong enough to beat $U-A_fL$, or the corresponding **upper** bound in (3). [Cully-Hugill and Dudek](https://arxiv.org/abs/2206.00433) · [Riesz curvature calculation](signed-far-pairs.md) · [Alpöge's announcement](https://alpo.ge/remark.pdf)

Fourier minorants in prime-gap problems and explicit formulas relating zero pairs to prime powers have substantial precedent. This note derives the finite band, phase at the specified midpoint, and proper-power correction for our detector. We have not established independent priority or obtained a proof or disproof of Cramér's conjecture. [Carneiro, Milinovich and Soundararajan](https://doi.org/10.4171/CMH/467) · [Languasco, Perelli and Zaccagnini](https://arxiv.org/abs/1311.0597) · [Ford and Zaharescu](https://arxiv.org/abs/1305.2520)

The accompanying finite replay compares a difference of two smoothings on individual zeros with its arithmetic value at four intervals. One ends immediately before a prime, another includes that endpoint, and a third comparison tests a negative proper-power correction. The maximum absolute residual was below $4\times10^{-8}$. This checks the transform normalization, signed correction and pole cancellation for the numerical example. The general estimates above have written proofs. [Replay and its scope](../../VERIFYING.md#covering-systems-and-open-investigations) · [Script](check-wide-band.py)
