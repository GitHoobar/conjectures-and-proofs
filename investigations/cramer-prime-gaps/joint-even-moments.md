# How closely the joint even moments locate the next prime

GitHoobar · 28 November 2026 · Developed with OpenAI Codex and Luna agents

The [even-zeta window test](even-zeta-window.md) chose one polynomial before evaluating its moments. Here we optimize over **every** polynomial of a given degree for each actual starting point. This gives an upper bound for the next ordinary prime. We estimate both sides of that bound over a range where prime counts are independently known, and the error relative to the unknown next prime outside that range.

## The bound obtained from the moment matrix

Let $y$ be a large positive integer and $p_0$ the next prime after $y$. For every $n>1$ with least prime factor greater than $y$, put $t_n=(y/n)^2$. Define the positive measure $\mu=\sum_n t_n\delta_{t_n}$. Its moments are

$$m_j=y^{2j+2}\left(\zeta(2j+2)\prod_{p\le y}(1-p^{-2j-2})-1\right).$$

For $d\ge1$ let $H=(m_{i+j})$ and $H_1=(m_{i+j+1})$, indexed by $0\le i,j<d$. Write

$$\lambda_d=\max_{\deg Q<d,\ Q\ne0}
\frac{\int t|Q(t)|^2\,d\mu}{\int |Q(t)|^2\,d\mu},
\qquad V_d=\frac{y}{\sqrt{\lambda_d}}.$$

This is the largest generalized eigenvalue of $(H_1,H)$. The denominator is positive since the support is infinite. Its largest support point is $(y/p_0)^2$, so $p_0\le V_d$. All inputs to $V_d$ use only primes through $y$ and ordinary even zeta values through $\zeta(4d)$. The usual $d$-node Gaussian quadrature rule for $\mu$ has positive weights, largest node $\lambda_d$, and matches all moments through $m_{2d-1}$. Thus any argument based solely on these moments and positivity on a real interval must allow a measure supported entirely at or below $\lambda_d$. [Golub and Welsch, *Calculation of Gauss Quadrature Rules*](https://math.berkeley.edu/~mgu/MA228A/Quadrature.pdf)

We obtain the following estimates, with absolute constants.

1. For $1\le d\le c y^{19/80}$, uniformly at **every** start,
   $$V_d-y\asymp y/d^2. \tag{1}$$
2. For every $d\ge1$, if $A=y/d^2$, then
   $$0\le V_d-p_0\ll (1+A)\log^2(2+A). \tag{2}$$
   For $d\ge C\sqrt y$ we have $0\le V_d-p_0<1$, hence $\lfloor V_d\rfloor=p_0$.
3. At $d=\lceil\sqrt y\log\log y/\log y\rceil$, (2) gives $V_d-p_0=O(\log^2 y)$. Therefore $V_d-y=O(\log^2 y)$ at this degree is equivalent to Cramér's conjecture. In (2) the error is relative to the first actual prime, whose distance from $y$ is unknown.

The exponent in (1) comes from the short-interval prime theorem used below. No optimality for that exponent, or independent priority for these deductions, is asserted.

## Sampling a polynomial on ordinary prime bases

Write $\theta=0.525$. Baker, Harman and Pintz give $\gg x^\theta/\log x$ primes in an interval of length $x^\theta$ at large $x$ (final estimate on p. 562). By packing disjoint such intervals, a segment in $[N,2N]$ of length $L\ge C_0N^\theta$ contains $\gg L/\log N$ primes. Brun–Titchmarsh gives $\ll L/\log L$ as an upper bound. We use a small enough absolute $c$ in (1), so $y/d^2\ge c^{-2}y^\theta$. [Baker, Harman and Pintz](https://www.cs.umd.edu/~gasarch/BLOGPAPERS/BakerHarmanPintz.pdf) · [Montgomery and Vaughan](https://doi.org/10.1112/S0025579300004708)

Fix a small constant $a>0$. In any subinterval of $[0,1]$ of length $a/d^2$ we may retain a subinterval of length comparable to $a/d^2$ on which $t\asymp u$ for some $a/(4d^2)\le u\le1$. For example use the upper quarter of the interval. Its preimage under $t=(y/n)^2$ lies at $N\asymp y/\sqrt u$ and has length $L\asymp_a y/(d^2u^{3/2})$. The endpoints are within a fixed factor of each other. The ratio $L/N^\theta\gg_a (y^{1-\theta}/d^2)u^{-(3-\theta)/2}$ is sufficiently large. All the primes there exceed $y$, up to the harmless left endpoint, and $N\ll_a yd$. They therefore contribute at least

$$\gg_a \frac{uL}{\log N}\gg_a\frac{y}{d^2\log y} \tag{3}$$

to $\mu$ in that subinterval. The primes themselves number at least this many since $t\le1$. Constants here may depend on the fixed $a$; choose $c$ after the fixed interval lengths needed below.

## Proof of (1)

For $\deg Q<d$ and $M=\max_{[0,1]}|Q|$, Markov's inequality gives $|Q|\ge M/2$ on a one-sided interval of length $1/(4d^2)$ adjoining a maximizer. It suffices to consider real polynomials by the real symmetric matrix formulation. By (3), $\int Q^2\,d\mu\gg M^2y/(d^2\log y)$. In the top strip $1-\eta/d^2<t\le1$ the corresponding integers lie in an interval of length $O(\eta y/d^2)$ and all contributing integers are prime (they are less than $(y+1)^2$). Brun–Titchmarsh bounds their number by $O(\eta y/(d^2\log y))$, with an absolute implied constant for fixed $\eta>0$ and sufficiently large $y$. Choosing $\eta$ small shows at least half of $\int Q^2\,d\mu$ lies outside that strip. Thus $1-\lambda_d\gg 1/d^2$. [Markov's polynomial inequality](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf)

In the other direction choose $m=\lfloor(d+1)/2\rfloor$ and $Q(t)=[U_{m-1}(\sqrt t)/m]^4$, a polynomial of degree $2m-2<d$. Here $U_j(\cos v)=\sin((j+1)v)/\sin v$. On $1-a/m^2\le t\le1$ we have $Q\gg1$ for a small fixed $a$ by that formula. Equation (3) gives a denominator $\gg y/(m^2\log y)$. On $[0,1]$,
$$ Q(t)^2\le\min\{1,[m^2(1-t)]^{-4}\}.$$
In $0\le1-t\le1/m^2$ the numerator $\int(1-t)Q^2\,d\mu$ contributes $O(y/(m^4\log y))$ for $m\ge2$, by Brun–Titchmarsh. In each band $v\le1-t\le2v$ cut off at $t=1/2$, with $v=2^j/m^2$ and $j\ge0$, its mass is $O(vy/\log y)$ by the same upper sieve (enlarge a clipped interval before applying it). Multiplication by $2v(m^2v)^{-4}$ and summation gives $O(y/(m^4\log y))$. Finally $\mu([0,1])\ll y/\log y$: up to $y^2$ sum $y^2/p^2$ over primes $p>y$ by partial summation, and beyond $y^2$ sum over all integers at cost $O(1)$. This controls $t<1/2$ with the displayed decay. It follows that $1-\lambda_d\ll 1/d^2$. For small $d$, $\lambda_d\ge\lambda_1\gg1$ by the primes in $(y,2y]$ and the same total-mass bound. Since $\lambda_d$ is uniformly bounded below, $V_d-y\asymp y(1-\lambda_d)$. [Chebyshev formula](https://dlmf.nist.gov/18.5.E2)

## Reaching the unknown prime for general degrees

Rescale to $v=(p_0/n)^2$, so the first atom has coordinate and weight one in $\sum_n v\delta_v$. Write $\lambda'$ for the same variational maximum in this scale. A change of variable gives $V_d=p_0/\sqrt{\lambda'}$. In particular $p_0\asymp y$ by Bertrand's postulate.

Keep $m=\lfloor(d+1)/2\rfloor$, and put $A'=p_0/m^2$ and $h=B(1+A')\log^2(2+A')$ for a sufficiently large fixed $B$. If $h$ is a fixed positive fraction of $p_0$ or larger, $V_d\ll y$ already suffices. Otherwise put $s=p_0+h/2$ and try the polynomial
$$Q(v)=\left[\frac{U_{m-1}(s\sqrt v/p_0)}{U_{m-1}(s/p_0)}\right]^4.$$
Its contribution at $p_0$ makes the denominator at least one. Up to $n=p_0+h$, $1-v\le 2h/p_0$, so this portion of the deficit numerator costs at most $2h/p_0$ times the full denominator. Beyond $p_0+h$, $1-(s/n)^2\gg1-v$. The sine formula bounds the remaining numerator by
$$\ll U_{m-1}(s/p_0)^{-8}\sum_{n>p_0+h}\frac{v}{(1-v)^3}
\ll U_{m-1}(s/p_0)^{-8}\frac{p_0^3}{h^2}.$$
The last sum can include all integers: up to $2p_0$ sum $O((p_0/(n-p_0))^3)$ and beyond it sum $O((p_0/n)^2)$. Let $a=\operatorname{arcosh}(s/p_0)\asymp\sqrt{h/p_0}$. Then $U_{m-1}(s/p_0)=\sinh(ma)/\sinh a$, and the last bound is $O((h^2/p_0)e^{-8ma})$. The choice of $B$ ensures $ma\gg\sqrt B\log(2+A')$ and $e^{8ma}\ge h$ (increase $B$ to absorb its own logarithm). This proves $1-\lambda'\ll h/p_0$. The earlier crude bound $V_d\ll y$ handles the range where this upper bound is not small, proving (2).

For the rounding assertion take the unshifted $Q(v)=[U_{m-1}(\sqrt v)/m]^4$. The atom at one still contributes one to the denominator and zero to the deficit numerator. Including all exterior integers bounds $1-\lambda'$ by $m^{-8}\sum_{n>p_0}v/(1-v)^3\ll p_0^3/m^8$ by the same split starting at $n=p_0+1$. Therefore $V_d-p_0\ll p_0^4/m^8$ for $d\ge C\sqrt y$. Choosing $C$ large makes the difference less than one. The trial polynomials in this proof may use the unknown $p_0$: they prove an error bound for a maximum whose matrix inputs are independent of $p_0$.

## Which estimate would finish the argument?

At the Cramér-scale degree in part 3, a sufficient one-sided estimate is that $H_1-(y/(y+C\log^2 y))^2 H$ has a positive eigenvalue at every sufficiently large $y$ for some fixed $C$. It would put the next actual prime inside the interval. In the proof of (1) the smallest intervals sampled near $t=1$ have physical length comparable to $y/d^2$. At the degree in part 3 this is $\asymp\log^2 y/(\log\log y)^2$. The short-interval prime input used for (3) does not reach that scale. The approximation to $p_0$ in (2) gives no uniform upper bound on $p_0-y$. [Rational checks of the moment criterion](check-even-zeta-window.py)

## Requiring the exterior support to consist of actual prime bases

Quadrature allows arbitrary real support points. We also tested whether the same low moments force a local prime when only ordinary prime bases may carry Euler factors. For $d\le c y^{19/80}$, let $J=(y,y+\kappa y/d^2]$ with a sufficiently small fixed $\kappa>0$. There exists a weighted Euler product $F$ that uses all the ordinary primes through $y$ with weight one, deletes every prime in $J$, and satisfies
$$F(2k)=\zeta(2k)\quad(1\le k\le d).$$
Its other changes are real weights between $1/2$ and $3/2$ on finitely many ordinary primes between the end of $J$ and $Cyd$. The interval $J$ itself contains $\gg |J|/\log y$ ordinary primes by Baker–Harman–Pintz, taking $c$ small after fixing $\kappa$. This is a separate comparison system for each $y,d$.

Here are the linear constraints including repeated prime powers. For real $P$ of degree at most $d$ with $P(0)=0$ use the linear functional
$$K_p(P)=\sum_{j\ge1}\frac{P((y/p^j)^2)}{j}.$$
If $M=\max_{[0,1]}|P|$, Markov gives $|P(t)|\le 2d^2Mt$. Uniformly for $p>y$ this shows $|K_p(P)-P(t_p)|\ll M d^2 y^2/p^4=o(M)$ from the terms $j\ge2$. The peak interval used in (3) contains $\gg y/(d^2\log y)$ actual prime bases $p\le Cyd$ where $|P(t_p)|\ge M/2$. Brun–Titchmarsh bounds the total number of deleted primes by $O(\kappa y/(d^2\log y))$ with an absolute implied constant for large $y$. Choosing $\kappa$ small leaves enough exterior primes that
$$\left|\sum_{p\in J}K_p(P)\right|\le\frac12\sum_{y+|J|<p\le Cyd}|K_p(P)|$$
simultaneously for all such $P$. Here $|J|=\kappa y/d^2$ denotes interval length.

View the functionals as vectors in the dual of this finite-dimensional polynomial space. The right side is the maximum of $\sum_p e_p K_p(P)$ over the box $|e_p|\le1/2$. If the target functional $\sum_{p\in J}K_p$ were outside the image of that box, separation of a point from a compact convex set would give a polynomial violating the inequality. Hence a **single** choice of corrections works for every polynomial. Set the multiplicities to zero in $J$, to $1+e_p$ on the correction primes, and to one elsewhere. For $P(t)=t^k$ the functional is $-y^{2k}\log(1-p^{-2k})$. The corrections therefore preserve the logarithm of the full Euler product at all the displayed arguments simultaneously. They also preserve all the zeros and poles in $\Re s>0$, since each changed Euler factor has a holomorphic logarithm there.

The real-weight qualification is essential for this finite construction. If the changes were rational, equality at $s=2$ would, after clearing denominators, give $\prod_p(p^2/(p^2-1))^{a_p}=1$ for a nonzero finitely supported integer family. At the largest changed prime $P>3$, none of $q^2-1=(q-1)(q+1)$ for smaller primes $q$ is divisible by $P$: this could only occur for $q=P-1$, an even integer greater than two. The $P$-adic valuation of the product is $2a_P\ne0$. Ordinary Euler multiplicities are fixed integers. The construction isolates what low even moments, genuine prime locations and positivity can enforce without that restriction.
