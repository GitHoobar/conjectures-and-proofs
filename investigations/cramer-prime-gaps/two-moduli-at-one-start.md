# Isolating one start with two congruences

GitHoobar · 28 November 2026 · Developed with OpenAI Codex and Luna agents

Let $J=\{X+1,\ldots,2X\}$, $h=\lceil C(\log X)^2\rceil$ for fixed $C>0$, and $V(y)=\sum_{y<p\le y+h}\log p$. The [previous argument](rational-window-weights.md) gave positive weighted averages at small denominators. At $R=\lceil2\sqrt X\rceil$, rational frequencies of denominator at most $R$ can interpolate the indicator of one start. We tested whether that fact can give $V(y)>0$. A single Fourier sum requires exponentially large coefficients to isolate an interior start. A product of two congruence indicators does it with bounded coefficients. For this second test we identify the exact obstruction in transferring the complete-residue estimate to the observed interval.

## One Fourier sum has a large coefficient cost

Write $F(m)=\sum_{\alpha\in\mathcal F_R}c_\alpha e(\alpha m)$, where $e(t)=\exp(2\pi it)$ and $\mathcal F_R$ contains each reduced fraction modulo one of denominator at most $R$ once. Suppose the restriction of $F$ to $J$ vanishes off a block of at most $h$ consecutive starts, the whole block at distance at least $X/5$ from both endpoints. Then for some absolute $c>0$ and sufficiently large $X$,

$$\sum_{\alpha}|c_\alpha|\ \ge\ \exp(c\sqrt X)\max_{m\in J}|F(m)|. \tag{1}$$

In particular this also applies to the vector one might use inside a run of empty starts. The restriction here is **exact support**. The proof uses a gap in the sampling frequencies. Related conditioning results for Fourier and Vandermonde matrices appear in work of Barnett and Moitra. [Barnett](https://doi.org/10.1137/20M1336837) · [Moitra](https://arxiv.org/abs/1408.1681)

Take $t$ in the block where $|F|$ is largest, $K=2R$, and $k=2\lfloor X/(16K)\rfloor$. The symmetric kernel $A(v)=(2K+1)^{-1}\sum_{j=-K}^K e(jv)$ satisfies $|A(\alpha-1/(2R))|\le\rho=1/4$ for every allowed frequency. Indeed the open arc $(0,1/R)$ contains none, and the geometric sum and $|\sin \pi v|\ge2\|v\|_{\mathbb R/\mathbb Z}$ give the bound. Expand $A(v-1/(2R))^k=\sum_j a_j e(jv)$. The support has $|j|\le kK\le X/8$. Before modulation the coefficients give the law of a sum of $k$ independent uniform variables on $[-K,K]\cap\mathbb Z$. Splitting into two equal halves and using symmetry and Cauchy–Schwarz gives $a_0\ge 1/(kK+1)$.

Multiply coefficient $a_j$ by $B(j)=\prod_{u\ne t}(1-j/(u-t))$, where $u$ runs over the other starts of the block. For an allowed frequency the resulting Fourier sum has magnitude at most $\rho^k(1+kK/\rho)^h$. To verify this bound, use the differential operator $(2\pi i)^{-1}d/dv$ for multiplication by $j$. A derivative of order $b$ of one normalized kernel under this operator is bounded by $K^b$ directly from its sum. Distributing $a$ differentiations over $k$ factors costs at most $k^a K^a\rho^{k-a}$ for $a\le h<k$, since at least $k-a$ factors are untouched. Expand the product defining $B$ and use $|u-t|\ge1$. All starts $t+j$ used lie inside $J$, and $B$ kills every other position of the block. Hence

$$\frac{|F(t)|}{kK+1}\le\left|\sum_j a_j B(j)F(t+j)\right|\le\rho^k(1+kK/\rho)^h\sum_\alpha |c_\alpha|.$$

Now $k\asymp\sqrt X$ and $h\log(1+kK/\rho)=O_C((\log X)^3)=o(k)$, proving (1).

## A product with bounded coefficients selects the same start

Let $q,r$ be distinct primes between $\tfrac32\sqrt X$ and $2\sqrt X$, and $d=qr$. Such primes exist for large $X$ by the prime number theorem. For any integer $b$ let $U_b(m)={\bf1}_{q\mid m-b}$ and $W_b(m)={\bf1}_{r\mid m-b}$. Both have Fourier coefficient $\ell^1$ norm exactly one, by the elementary character expansion of a residue class; their coefficient $\ell^2$ norms are $q^{-1/2}$ and $r^{-1/2}$. The product is the indicator of $b\bmod d$. Since $d>X$, on $J$ the product for $b=y\in J$ is precisely the indicator of $y$. It can also be evaluated from the signed difference $(|U_y+W_y|^2-|U_y-W_y|^2)/4$. This identity explains why the cost bound for a single sum does not settle the prime question.

For two functions define the observed and complete forms by

$$A(F,H)=\frac1X\sum_{m\in J} V(m)F(m)\overline{H(m)},\qquad G(F,H)=\frac{M}{\varphi(M)}\mathbb E_{a\bmod M}\left[F(a)\overline{H(a)}\sum_{i=1}^h {\bf1}_{(a+i,M)=1}\right],$$

where $M=\mathrm{lcm}(1,\ldots,R)$. For our indicators, conditioning on $a\equiv b\pmod d$ and using the Chinese remainder theorem gives exactly

$$G(U_b,W_b)=\frac{C_d(b)}{\varphi(d)},\qquad C_d(b)=\#\{1\le i\le h:(b+i,d)=1\}.$$

Since $q,r>h$, $h-2\le C_d(b)\le h$. On the other hand $XA(U_y,W_y)=V(y)$ for a represented start, and $A(U_b,W_b)=0$ for a class absent from $J$.

**A uniform operator error cannot certify the target using this main term.** Some absent class $b$ has $C_d(b)=h$. Indeed the $X$ represented classes and the at most $h(d/q+d/r)$ classes that hit either prime at an offset together occupy fewer than $d$ classes. Thus the operator norm of $A-G$, using the Fourier coefficient $\ell^2$ norm in each argument, is at least $h\sqrt d/\varphi(d)$. Multiplying by the norms of $U_y,W_y$ gives $h/\varphi(d)$, already at least the entire modeled entry at the desired $y$. Improving an upper bound for that *uniform norm* cannot establish strict positivity by subtracting it here.

The mismatch also occurs using only tests anchored at the actual target. Take one prime pair from $[1.1\sqrt X,1.2\sqrt X]$ and another from $[1.8\sqrt X,1.9\sqrt X]$. Both products exceed $X$. Their observed values after multiplication by $X$ equal the very same $V(y)$. Their modeled values differ by at least $h/3$ for all large $X$, using the bounds for $C_d$ and $d/\varphi(d)=1+O(X^{-1/2})$. At least one modeled value therefore has error at least $h/6$, at **every** target $y$.

## Correcting for the actual number of starts

For these individual tests we tried replacing the modeled class frequency $1/d$ by its exact frequency on $J$. This removes the error on absent classes. For a represented class $y$, after multiplication by $X$, the resulting prediction is

$$B_d(y)=\frac d{\varphi(d)}C_d(y)=h+O(1),\qquad E_d(y)=V(y)-B_d(y)=V(y)-h+O(1),$$

uniformly over the prime pairs above. In fact $h-2\le B_d(y)\le h+O(h/\sqrt X)$. Hence the spread of the corrected errors across *all* these pairs is at most $2+O(h/\sqrt X)$, whether the target contains a prime or not. Their common value is the part that can distinguish vacancy. For any nonnegative average of the errors with weights adding to one, and all large $X$,

$$\text{a prime lies in }(y,y+h]\quad\Longleftrightarrow\quad\mathop{\mathrm{avg}}_d E_d(y)>-h+\tfrac12\log X.$$

This follows from $V(y)=0$ in an empty window and $V(y)\ge\log X$ whenever there is a prime. Moreover the [previous sparse-window result](count-polynomials.md) supplies many nonempty starts where the prime count is at most $b h/\log X$ for a fixed $b<1$. There $V(y)\le (b+o(1))h$ and every corrected error is negative of order at least $h$ in magnitude. A uniform $o(h)$ error estimate would therefore be false on actual primes. The weaker one-sided bound displayed above remains unproved at the minimizing start.

These results distinguish the coefficient cost of locating a start from the arithmetic cost of proving it contains a prime. The finite identities have an [exact checker](check-two-moduli.py). Independent priority for these deductions has not been established. Cramér's conjecture remains open.
