# Cancellation of the signed far-pair sum

GitHoobar · 27 November 2026 · Research notes developed with OpenAI Codex and three Luna agents

We obtained a pointwise upper bound for the signed sum from [the preceding note](deepest-deficit.md), a stronger estimate after averaging over integer starts in a residue class, and a [second necessary condition for vacancy](negative-far-pairs.md). The pointwise bounds still permit zero primes at the deepest deficit.

## The RH input

Alpöge announced the Lean proof on 20 November. Sutherland reports independent kernel acceptance and a successful comparison with the canonical Mathlib challenge. Rubinstein reports a separate rebuild and verification. We use their checked RH statement that each nontrivial zeta zero is $1/2+i\gamma$. We consulted the records and did not rerun the formal proof. Clay's problem page still carries its administrative status of “Active” on this date. The checked theorem makes the set $H$ of high zeros off the line in our previous argument empty. The weights $x^{i(\gamma-\gamma')}$ still depend on the ordinates. [Clay problem page](https://www.claymath.org/millennium/riemann-hypothesis/) · [Announcement](https://alpo.ge/remark.pdf) · [MIT verification](https://math.mit.edu/~drew/grh/) · [Waterloo verification](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)

## At one start

Keep the preceding notation. Thus $L=\log x$, $h=\lceil CL^2\rceil$, $z=xe^v$, $m=1-2b$, $\delta=\log(1+h/x)/(1+2\lambda)$, with $0<b,\lambda<1/8$. The subwindows all lie inside the parent. Let $M$ be its prime log-weight. Write $W(v)$ and $P(v)$ for the spline-weighted contributions of primes and proper prime powers in the subwindow, respectively. With $G$ the retained zeros above $x^\theta$, $0<\theta<13/30$, the explicit formula and the low-zero estimate give, uniformly in the shift,
$$
 S_G(v)=F(\delta)-\frac{W(v)+P(v)}{\delta z}+o(L^{-3}).
$$
The trivial-zero correction is absorbed in the error. All quantities here are real. We have $F(\delta)=m+O(\delta)$, $0\le W\le M$, and $P\ll L(1+\log\log L)$. Define $N_B$ as the signed contribution with $|\gamma-\gamma'|\le B$ to the squared norm of $S_G$. Then $R_B+N_B=\mathbb E_v S_G(v)^2$ exactly and $|N_B|\le K_0(B+1)/C$.

* At **every** start, $|R_B|\ll_{b,\lambda,C} (L/\log L)^2+K_0(B+1)/C$. Indeed Brun–Titchmarsh gives $M\ll hL/\log h$. The total squared norm has the displayed upper bound. The sum of the absolute values of the far-pair terms is $\gg x/(C^2 L^2)$, as proved earlier. Thus the signed bound establishes cancellation at each individual start. [Montgomery and Vaughan](https://doi.org/10.1112/S0025579300004708) · [Absolute-mass calculation](deepest-deficit.md)
* At **every sparse start** with $M\le(1+o(1))h$, one gets $-K_0(B+1)/C\le R_B\le m^2+K_0(B+1)/C+o(1)$. Indeed $(W+P)/(\delta z)\le1+2\lambda+o(1)<2m$, while its lower bound is zero. This includes a minimizing start on a large dyadic shell: averaging the unweighted prime log-mass there gives at most $(1+o(1))C(\log X)^2$ by counting each prime at most $\lceil C\log^2(2X)\rceil$ times and applying the prime number theorem. All parent lengths in the shell are asymptotic to that common scale.
* For an **empty** parent the energy itself equals $m^2+O_{b,\lambda,C}((1+\log\log L)/L)$. In particular the signed upper bound in the previous bullet allows vacancy. The uncertainty from bounding the near sum by its absolute value is $O((B+1)/C)$ for fixed $C,B$.

One can see the resolution needed for a single prime. Add $P(v)/(\delta z)$ back to $S_G(v)$, obtaining $U(v)=F(\delta)-D(v)+o(L^{-3})$ with $D=W/(\delta z)$. On a sparse parent,
$$F(\delta)^2-\mathbb E U(v)^2
 =\mathbb E\,[D(v)(2F(\delta)-D(v))]+o(L^{-3}).$$
The factor multiplying $D$ lies between two positive constants for all sufficiently large $x$. Vacancy gives $o(L^{-3})$. A single prime in the common plateau gives a deficit of order $1/(CL)$ if it is the only prime. The common plateau is nonempty since $2\lambda+4b<1$. A boundary prime may receive less weight. The [endpoint-sensitive test](finite-zero-test.md) counts such primes as well. This calculation separates the contribution of a single prime from the much coarser bound on the near pairs.

## A signed bound in every sampled residue class

Freeze the filter over $X\le n\le2X$. Put $L=\log X$, $K=\lceil8L\rceil$, $\delta=C L^2/[4(1+2\lambda)X]$, $d=\lambda\delta$, $T=4K/(b\delta)$, and $G=\{X^\theta<|\gamma|\le T\}$. At the start $n$ use the previous formula for $S_G$ with coefficients $n^{-1/2+i\gamma}F(\delta\rho)$, and denote the resulting far sum by $R_B^{\rm fr}(n)$. Even the latest permitted right endpoint $ne^{(1+2\lambda)\delta}$ lies inside the requested parent $(n,n+\lceil C\log^2 n\rceil]$ for large $X$. Fix a nonnegative smooth weight $w$ supported in $(1,2)$. For any integers $r,q$ with $1\le q\le\pi X/(2T)$, every $B\ge1$, and any fixed integers $N\ge2$, $A\ge1$,
$$
\left|\frac qX\sum_{n\equiv r\bmod q} w(n/X)R_B^{\rm fr}(n)\right|
\ll_{N,w,b,\lambda}\frac{(1+B)^{1-N}}{C}+O_{A,C,w,b,\lambda}(X^{-A}).
\tag{1}
$$
In particular the moduli include all $q\le c_{b,\lambda} C\log X$ for a sufficiently small positive constant. The assertion concerns a signed average. The fixed sharp cutoff defining $R_B$ at one start is retained in the pair restriction, while the heights and kernel are frozen for the shell average.

**Proof.** For $\Delta=\gamma-\gamma'$ the center dependence is $n^{-1+i\Delta}$, and $J_d(-1+i\Delta)$ has modulus at most one. Poisson summation on the progression gives a factor $X^{-1+i\Delta}$ times a sum of integrals, with unimodular multipliers and integrands
$$
w(u)u^{-1}\exp\{i\Delta\log u-2\pi i kXu/q\},\qquad k\in\mathbb Z .
$$
The integral for $k=0$ is $O_{N,w}((1+|\Delta|)^{-N})$ by integration by parts in $\log u$. For $k\ne0$, since $|\Delta|\le2T\le\pi X/q$ and $u\ge1$, the phase derivative has magnitude at least $\pi |k|X/q$. All derivatives of the phase after division by $|k|X/q$ are bounded on the support. Repeated integration by parts gives $O_{j,w}((q/(|k|X))^j)$ for each fixed $j$. There are $O(T\log(2T))$ zeros and the $F$ factors are bounded, so these errors sum to $O_A(X^{-A})$ on increasing $j$. For $k=0$, the absolute coefficient mass divided by $X$ in every unit band of $|\Delta|$ is $O(1/C)$: each zero has $O(L)$ partners per band and $X^{-1}\sum_{G}|F(\delta\rho)|^2\ll1/(CL)$. Sum $(1+j)^{-N}$ over bands meeting $|\Delta|>B$ to get (1).

Including all separations by the same proof bounds the weighted mean of the **nonnegative full energy** by $O(1/C)$. Take $w\ge1$ on a fixed closed subinterval of $(1,2)$. Apart from $O(X/(Cq))$ starts in that subinterval in each class, the full energy is less than $m^2/4$ (constants depend on the filter and subinterval). At those starts a permitted shift has $S_G(v)<m/2$, and the explicit formula gives $\gg_{b,\lambda} C L$ actual primes in the parent after subtracting proper powers. This is informative for sufficiently large fixed $C$. It still allows a particular minimizing start to be an exception.

## Checking a direct use of the RH proof's prime sum

Alpöge's announcement mentions the Riesz weight $(t/n-1)_+$. Write $V(t)=\sum_n\Lambda(n)(t/n-1)_+$. Its curvature as a measure is $V''=\sum_n\Lambda(n)\delta_n/n$. Let $a=x+1/2$, $c=x+h+1/2$, and $b_0=(a+c)/2$. Then
$$V(a)-2V(b_0)+V(c)
=\sum_{a<n<c}\frac{\Lambda(n)}n\min(n-a,c-n).$$
After exact subtraction of the proper-power terms this is positive precisely when the original interval contains a prime. Even a prime at either end contributes at least $\log(x+1)/(2(x+h))$. Direct subtraction of three global estimates needs control of their *correlated* errors. To see the loss from independent bounds, replace $t\log t$ on $[a,c]$ by its chord, leaving it unchanged elsewhere. The resulting function remains convex, has zero second difference there, and differs globally by at most $h^2/(8a)$, by the interpolation remainder and $0<(t\log t)''\le1/a$ there. A global square-root error estimate easily accommodates that change. This comparison tests the use of a global bound alone. [Alpöge's announcement, p. 3](https://alpo.ge/remark.pdf)

We have no uniform estimate placing the signed energy below the vacancy value by the contribution of a prime at the specified start. These notes make no claim of independent priority.
