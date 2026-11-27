# Identifying individual primes from a finite sum over zeta zeros

GitHoobar · 27 November 2026 · Working note developed with OpenAI Codex and Luna agents

The [midpoint minorant](wide-separations.md) can give a small weight to a prime at the edge. Here we construct a separate test at each candidate integer, including the right endpoint. The same table of zeta zeros, up to a height $T(x)$ with $T(x)/x\to0$, suffices throughout the window. The other arithmetic inputs are the small primes in a specified modulus and their powers. This gives an exact prime count by thresholding for all sufficiently large starts. It leaves open whether the count is always at least one.

## Statement and inputs

Let $L=\log x$, $h=\lceil C L^2\rceil$, $C>0$ fixed. Let $q$ be the largest primorial (a product of consecutive primes beginning with 2) at most $\sqrt L$. Put $R=(\mathbb Z/q\mathbb Z)^\times$, using representatives $1$ through $q-1$, and $d=|R|$. For $x<j\le x+h$ coprime to $q$, write $r=j\bmod q$. With $\operatorname{sinc}(v)=\sin(v)/v$ and value one at zero, set
$$
K_r(u)=\operatorname{sinc}(\pi u/q)^{10}
 \prod_{s\in R,\ s\ne r}
 \frac{\sin^2(\pi(u+r-s)/q)}{\sin^2(\pi(r-s)/q)},\qquad
B=\frac{(2d+8)\pi}{q}.
$$
Use $\widehat K_r(t)=\int K_r(u)e^{itu}\,du$. The explicit correction for powers of primes dividing $q$ is
$$
V_j=\sum_{p\mid q}\ \sum_{k\ge1:\, j/2\le p^k\le2j}(\log p)K_r(p^k-j),
$$
where $p$ is prime. Define the real statistic
$$
D_j=\widehat K_r(0)-V_j-
\frac{1}{\sqrt j}\sum_{|\gamma|\le Bj} j^{i\gamma}\widehat K_r(\gamma/j).
\tag{1}
$$
The sum counts zeros with multiplicity, and conjugates pair up. We use the [independently verified RH statement](https://math.mit.edu/~drew/grh/).

**Claim.** Uniformly in the eligible $j$,
$$
D_j=\Lambda(j)+O(x^{-1+o(1)}).
\tag{2}
$$
In particular $j$ is prime exactly when $D_j>3\log(j)/4$ for all sufficiently large $x$. Indeed a prime gives $\Lambda(j)=\log j$, a proper power gives at most $(\log j)/2$, and other integers give zero. Every prime in this window is coprime to $q$. Consequently we may count all the primes, even a lone endpoint prime, by counting the candidates passing the test. No primality test on the candidates or correction using unknown neighboring primes enters (1). The spectral input consists of ordinates up to $T(x)=B(x+h)$ at sufficient precision. This assertion concerns the mathematical formula. Its conditioning and running time depend on $q$.

## Why the bandwidth decreases

At any integer displacement $v$ with $r+v$ coprime to $q$, $K_r(v)=\mathbf1_{v=0}$. For $v\ne0$ in the original class the sinc factor vanishes. In any other eligible class the corresponding sine factor vanishes. Ineligible integers can have a nonzero von Mangoldt weight only at powers of primes dividing $q$.

The transform of the tenth power of the sinc is supported on $[-10\pi/q,10\pi/q]$ by convolution of ten interval functions. Each sine square adds at most $2\pi/q$ to the largest frequency. This proves $\operatorname{supp}\widehat K_r\subset[-B,B]$. If $y$ is the largest prime in $q$, then $q/d=\prod_{p\le y}(1-1/p)^{-1}\ge\sum_{n\le y}1/n$ by expansion of the finite Euler product. As $x\to\infty$, $y\to\infty$, so $B\to0$.

The coefficient sizes also matter. For $k=0,1,2$,
$$
|K_r^{(k)}(u)|\le q^{O(q)}(1+|u|)^{-10}.
\tag{3}
$$
Distinct residues give $|\sin(\pi(r-s)/q)|\ge2/q$. Differentiating the sine product at most twice costs a polynomial factor in $q$, absorbed in the bound. The sinc power and its first two derivatives have the stated decay with polynomial factors in $q$, by its elementary formula away from zero and smoothness near zero. Since $q\le\sqrt L$, $q^{O(q)}=x^{o(1)}$. The increasing modulus is chosen slowly enough for this loss to be harmless.

## Transferring the integer samples to the explicit formula

Fix a smooth real cutoff $0\le\chi\le1$ supported in $(-1/2,1/2)$, equal to one on $[-1/4,1/4]$. Use the test
$$
G_j(y)=\sqrt{j/y}\ \chi(\log(y/j)) K_r(j\log(y/j)).
$$
Only $j/2\le y\le2j$ can contribute. In this range write $v=n-j$, $u=j\log(n/j)$. The numbers $|u|$ and $|v|$ are comparable, they have the same sign, and $|u-v|\ll v^2/j$. Also $|\sqrt{j/n}\chi(\log(n/j))-1|\ll |v|/j$. By (3) and the mean value theorem,
$$
\left|G_j(n)-K_r(v)\right|\ll
\frac{q^{O(q)}}j\,(|v|+v^2)(1+|v|)^{-10}.
$$
Summing with $\Lambda(n)\le\log(2j)$ costs $O(x^{-1+o(1)})$. The additive cardinal identity and the excluded-power correction now give
$$
\sum_n\Lambda(n)G_j(n)=\Lambda(j)+V_j+O(x^{-1+o(1)}).
\tag{4}
$$

For the Mellin side set $y=je^{u/j}$. The transform at $s$ is
$$
j^{s-1}\int_{\mathbb R} e^{(s-1/2)u/j}\chi(u/j)K_r(u)\,du.
$$
At $s=1$ its value is $\widehat K_r(0)+O(x^{-1+o(1)})$ by (3) and the finite first absolute moment. On RH the exponential in the integral at a nontrivial zero is exactly $e^{i\gamma u/j}$. Removing $\chi$ gives $\widehat K_r(\gamma/j)$. The error in this last integral is
$$
O\left(q^{O(q)}j^{-9}(1+|\gamma|/j)^{-2}\right).
$$
Indeed $(1-\chi(u/j))K_r(u)$ and its first two derivatives have $L^1$ norms $O(q^{O(q)}j^{-9})$, since they live on $|u|\ge j/4$. Integrate by parts twice. The zero count $N(t)\ll t\log(2t)$ gives a total error of $O(x^{-17/2+o(1)})$ after multiplication by $j^{-1/2}$. At the trivial zeros $s=-2k$, their total transforms are $O(q^{O(q)}j^{-3})$, since $|u/j|<1/2$ and the geometric series has ratio at most $e/j^2$. The smooth explicit formula takes the pole transform minus the transforms at all the zeros. Substitution into (4) proves (2). [Background on the explicit formula in this investigation](finite-zero-test.md)

## Can the tests all give a composite answer?

A vacant window would impose many simultaneous conditions on the same ordinates. It contains $h d/q+O(q)$ eligible integers by periodicity. At most $O(L)$ are proper powers because consecutive integer $k$th powers near $x$ are separated by $\gg\sqrt x$ for every $k\ge2$, and there are $O(L)$ possible exponents. Since $d/q\ge1/q\ge L^{-1/2}$, at least $(1-o(1))h d/q$ candidates would have $D_j=O(x^{-1+o(1)})$ under vacancy. The exceptional proper powers must give their smaller positive weights. Ruling out that simultaneous outcome for actual zeta ordinates would put a prime in the original interval.

We tested whether the large number of conditions, nonnegativity and bandwidth alone furnish a contradiction. They permit even exact vacancy on this sampling set. For any finite assignment $a_j\ge0$ to eligible integer sites, the nonnegative function $F(t)=\sum_j a_j K_{j\bmod q}(t-j)$ has transform supported in $[-B,B]$ and takes exactly the assigned values at every eligible site (zero at unassigned sites). We may fill both neighboring windows while prescribing zero throughout the central one. This proves a limitation of an argument using sampling and positivity alone. The missing step must use additional information, such as the particular phases and coefficients in (1).

## Attribution and finite checks

Reconstruction of arithmetic weights from zeta zeros has a long history, including Landau's formula. Analytic prime-counting algorithms and cardinal interpolation on periodic sets also predate this note. Our derivation combines periodic coprime sampling with a controlled change from the integer to the logarithmic grid. We have not established priority for the combination. [Landau–Gonek formula and context](https://pure.manchester.ac.uk/ws/portalfiles/portal/1790789781/2601.18025v1.pdf) · [Analytic prime counting with the explicit formula](https://doi.org/10.1090/mcom/3038) · [Cardinal interpolation and periodic sampling](https://doi.org/10.1007/s43670-022-00041-7)

The replay checks weights on three residue systems, then evaluates (1) on six integers with fixed illustrative moduli 6 and 30. It distinguishes the primes 127 and 1021, the powers 121, 125 and 961, and the composite 1001. The largest discrepancy in the reconstructed von Mangoldt weight was below 0.009. The cutoff tending to a vanishing fraction of $x$ is an asymptotic conclusion of the proof. [Replay](check-wheel-sampling.py)
