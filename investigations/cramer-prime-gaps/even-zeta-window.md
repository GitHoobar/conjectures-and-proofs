# Testing a specified prime interval using even zeta values

GitHoobar · 28 November 2026 · Developed with OpenAI Codex and Luna agents

The [functional-equation test](euler-multiplicities.md) used a comparison system defined by removing the target primes. Here the numerical input is the ordinary zeta function and a list of primes **only through the left endpoint**. We give an exact occupancy test, a version that allows a margin at the right endpoint, and a matching degree bound for the latter's all-integer tail requirement. We also estimate how much the independently guaranteed primes beyond the window contribute. The uniform lower bound needed for Cramér remains open.

Using zeta values to recover the next prime goes back to Golomb. His sieve identity already accommodates general summable weights. A subsequent effective recurrence uses a single zeta argument equal to twice the previous prime. Our question is how far up the consecutive even arguments one has to go when combining them into a positive test with a bounded tail. Degree measures the largest index in this particular representation. It does not measure computational cost or the information content of an exactly known real number. Independent priority for the bounds below is unverified. [Golomb, *Formulas for the next prime*](https://msp.org/pjm/1976/63-2/pjm-v63-n2-p11-p.pdf) · [Effective Golomb–Keller recurrence](https://arxiv.org/abs/2508.02690)

## A threshold with no target primes as input

Take integers $2\le y<b\le2y$ and put

$$R_y(s)=\zeta(s)\prod_{p\le y}(1-p^{-s})-1,\qquad
\mathcal S(P)=\sum_{k=1}^{d} c_k b^{2k}R_y(2k),\qquad
P(t)=\sum_{k=1}^{d}c_k t^k.$$

Expanding the Euler product gives $\mathcal S(P)=\sum_{n>1,\ P^-(n)>y}P((b/n)^2)$, where $P^-(n)$ is the least prime factor. All these integers exceed $y$, and through $b$ they are primes because a composite in the sum is at least $(y+1)^2$. Euler's formula expresses each $\zeta(2k)$ as a known positive rational multiple of $\pi^{2k}$. Thus rational $P$ gives a rational polynomial evaluated at $\pi^2$, including a rational constant from the subtractions. [Euler's even zeta values](https://dlmf.nist.gov/25.6.E2)

Let $U_j$ be the Chebyshev polynomial of the second kind and put

$$F_m(t)=t\left(\frac{U_{m-1}(\sqrt t)}m\right)^4.$$

This is a rational polynomial of degree $2m-1$ with zero constant term because $U_{m-1}$ has definite parity. It is nonnegative for $t\ge0$, is one at $t=1$, and is nondecreasing for $t\ge1$. For the latter assertion use $U_{m-1}(\cosh a)=\sum_{j=0}^{m-1}\exp((m-1-2j)a)$ and pair opposite exponents. For $n>b$, the sine formula gives $|U_{m-1}(b/n)|\le(1-b^2/n^2)^{-1/2}$. Hence, without using any sieve on the exterior,

$$\sum_{n>b}F_m((b/n)^2)
\le \frac{b^2}{m^4}\sum_{n>b}\frac{n^2}{(n+b)^2(n-b)^2}
\le\frac{\zeta(2)b^2}{m^4}. \tag{1}$$

Taking $m=\lceil2\sqrt b\rceil$ makes (1) less than $1/4$. An empty window then gives $\mathcal S(F_m)<1/4$ and any prime through $b$ gives $\mathcal S(F_m)\ge1$, including a prime exactly at $b$. In particular $\mathcal S(F_m)>1/2$ is equivalent to occupancy. The largest required argument is $4m-2$. [Chebyshev trigonometric representation](https://dlmf.nist.gov/18.5.E2)

## Leaving room at the right endpoint

Let $1\le g<b-y$ and $g\le b/4$. Put $t_0=(b/(b-g))^2$ and $P=F_m/F_m(t_0)$, where

$$m=\left\lceil A\sqrt{b/g}\log(2g)\right\rceil$$

for a sufficiently large absolute constant $A$. A prime in $(y,b-g]$ contributes at least one. An empty $(y,b]$ gives $\mathcal S(P)<1/4$. A prime confined to the last $g$ positions can give an intermediate value. In all cases a value above $1/4$ certifies a prime in the original window.

To verify the tail bound, write $a=\operatorname{arcosh}(b/(b-g))\asymp\sqrt{g/b}$. Then $F_m(t_0)=t_0[\sinh(ma)/(m\sinh a)]^4$. Since $ma\gg A\log(2g)$ and $\sinh a\asymp\sqrt{g/b}$, dividing (1) by $F_m(t_0)$ gives $O(g^2\exp(-4ma))<1/4$ upon fixing $A$ large enough. For $b-y=\lceil C\log^2 y\rceil$ and $g=\lfloor(b-y)/2\rfloor$, the degree is $O_C(\sqrt y\log\log y/\log y)$. A uniform lower estimate $\mathcal S(P)>1/4$ would thus suffice for Cramér. Conversely Cramér implies this test is at least one for a sufficiently large choice of $C$, by applying the conjectured gap bound inside the shorter interval.

## Why this degree appears

Suppose a real polynomial $P$ of degree $d$ satisfies $P(t_0)\ge1$, is nonnegative at **every** exterior node $t_n=(b/n)^2$ for integers $n>b$, and has $\sum_{n>b}P(t_n)\le1/4$. Then

$$d\gg\sqrt{b/g}\log(2g). \tag{2}$$

Here the sum is an unweighted sum of polynomial values. The damping factor $t$ in the construction is part of the polynomial itself. Additional arithmetic restrictions on which exterior nodes may be occupied are outside (2).

Write $M=\max_{[0,1]}|P|$. If $d^2\ge c b$ for a fixed small $c>0$, (2) follows since $\log(2g)/\sqrt g$ is bounded. Otherwise Markov's polynomial inequality gives $\max_{[0,1]}|P'|\le2d^2M$. There is a one-sided interval of length $1/(4d^2)$ adjacent to a point attaining $M$ on which $|P|\ge M/2$. The nodes $t_n$ decrease to zero, the gap from $1$ to $t_{b+1}$ is at most $2/b$, and successive spacings are at most $2/b$ by differentiation. Consequently that interval contains $\gg b/d^2$ nodes for small enough $c$. At those nodes $P$ is nonnegative. The tail budget gives $M\ll d^2/b$. Degree zero is impossible.

For $t>1$, $|P(t)|\le M T_d(2t-1)$ by Chebyshev extrapolation. Indeed a violation allows a multiple of $P/M$ of norm less than one that meets the shifted $T_d$ at $t$; their difference already changes sign across all $d$ intervals between consecutive extrema in $[0,1]$. Since $T_d(2t_0-1)\le\exp(O(d\sqrt{g/b}))$, putting $v=d\sqrt{g/b}$ gives $g\ll v^2e^{O(v)}$, hence $v\gg\log(2g)$. This proves (2), including bounded $g$. For the exact endpoint $t_0=1$ the same argument gives $d\gg\sqrt b$ directly from $M\ge1$. [Markov's polynomial inequality](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf)

## Attempting a lower bound from ordinary primes

Use the polynomial with $g\asymp\log^2 b$ above and write $K=F_m(t_0)$. For the distant interval $(b+D,b+2D]$, the contribution of its ordinary primes to $\mathcal S(P)$ has order

$$\sum_{b+D<p\le b+2D}P((b/p)^2)\asymp\frac{b^2}{K m^4D\log b}. \tag{3}$$

This holds unconditionally for $D=b$. It also holds under the RH prime number theorem uniformly for $b^{1/2+\epsilon}\le D\le b$ for fixed $0<\epsilon<1/2$. The prime number theorem in the former case and the RH bound $\theta(t)=t+O(\sqrt t\log^2 t)$ in the latter give $\asymp D/\log b$ primes. Here $p>b>y$, so every one contributes. [Schoenfeld's estimates for the Chebyshev functions](https://doi.org/10.1090/S0025-5718-1976-0457374-X)

Write $\phi(n)=m\arccos(b/n)$. In this interval $\phi'(n)\asymp m/\sqrt{bD}$. Also $P((b/n)^2)\asymp b^2\sin^4(\phi(n))/(K m^4D^2)$, with the two sides vanishing together. The upper estimate follows immediately. For the lower estimate exclude the points where $\phi(n)$ lies within a small fixed $\eta>0$ of a multiple of $\pi$. There are $O(1+D/V)$ affected intervals of length $O(\eta V)$, where $V=\sqrt{bD}/m$. In the stated range $D/V\to\infty$ and $V\ge b^{1/5}$ for large $b$. Enlarge each affected interval to length $C_1\eta V$ with an absolute $C_1$. The Brun–Titchmarsh inequality bounds its prime count by $O(\eta V/\log b)$, with an absolute implied constant once $b$ is sufficiently large for the fixed $\eta$. Choosing $\eta$ small leaves $\gg D/\log b$ primes with $|\sin\phi(p)|\ge\sin\eta$. This proves (3). [Montgomery and Vaughan, *The large sieve*](https://doi.org/10.1112/S0025579300004708)

Even the upper side of (3) is only $O(1/(D\log b))$ times the exterior bound $\zeta(2)b^2/(K m^4)<1/4$. Thus these actual prime populations give a strictly positive lower bound at every start, but fall short of the one-prime threshold. The window test can be evaluated independently of the target primes. Proving it clears the threshold uniformly is the outstanding arithmetic step. [Verification on empty and occupied windows](check-even-zeta-window.py)

## Trying to obtain the sign from the Bernoulli formula

For the exact endpoint test write $Q(\pi^2)=\mathcal S(F_m)$, where $Q$ is the rational polynomial obtained from Euler's even zeta values and $m=\lceil2\sqrt b\rceil$. If $h=b-y\asymp\log^2 b$, then **for every start**, $Q(Z)-1/2$ has a real root within relative distance $\exp(-(4+o(1))m\log b)$ of $\pi^2$. Thus even where the detector values have a gap between $1/4$ and $1$, the corresponding polynomial in the argument has a threshold crossing extremely close to the true argument.

Indeed replacing $\pi^2$ by $z\pi^2$ multiplies the zeta term at index $k$ by $z^k$ while leaving the rational subtraction unchanged. Consequently for $z>0$,

$$Q(z\pi^2)=F_m(zb^2)-F_m(b^2)
 + \sum_{n>1,\ P^-(n)>y}F_m(zb^2/n^2).$$

Write $V=F_m(b^2)$, $E=1+hF_m((b/y)^2)$ and $\eta=4E/V$. For $0<z\le1$ the sum on the right is at most $E$. In the window, use monotonicity above $1$ and $F_m(t)\le1$ on $[0,1]$, the latter following from $|\sin(m\theta)|\le m|\sin\theta|$. Beyond $b$, the proof of (1) still bounds the tail since $t/(1-t)^2$ is increasing on $[0,1)$. For $(1-\eta)b^2>1$, monotonicity of $F_m(t)/t$ above $1$ now gives $Q((1-\eta)\pi^2)\le-4E+E$ and $Q((1+\eta)\pi^2)\ge4E$, the latter by nonnegativity of the entire sum. Apply the intermediate value theorem.

Finally $\log V=(4m-2)\log b+O(m+\log m)$ by the hyperbolic formula, whereas $\log E=O(\log(2h)+m\sqrt{h/b})=O(\log b)$. These bounds justify the condition on $\eta$ and its stated size. This tests a specific attempt to prove the missing inequality from the exact positive even zeta values: substituting them produces a polynomial for which transcendence rules out equality, but leaves the side of this nearby root undetermined.
