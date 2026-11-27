# Prime counts at the other starts in a residue class

GitHoobar · 28 November 2026 · Developed with OpenAI Codex and Luna agents

In the [two-modulus test](two-moduli-at-one-start.md) a residue class contained a single start. Here each progression visits order $\sqrt{\log X}$ starts near the target. After averaging over the moduli, we can evaluate the total contribution from the other starts with absolute error $o(1)$, uniformly in the target. Subtracting the usual arithmetic-progression prediction then recovers the prime count in the original window to within rounding error. The proof uses Bombieri–Vinogradov and elementary estimates; it does not require GRH. Divisor switching and the influence of a distinguished term of a progression have substantial precedent, including work of Hooley and Fiorilli. [Fiorilli, *On a theorem of Bombieri, Friedlander, and Iwaniec*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0008414X00009342) · [Fiorilli, *The influence of the first term of an arithmetic progression*](https://arxiv.org/abs/1104.2542)

## The comparison

Let $X$ be a large integer, $X\le y\le 2X$ an integer, $L=\log X$, $h=\lceil C L^2\rceil$ with $C>0$ fixed, and $P(y)=\pi(y+h)-\pi(y)$. Fix a nonnegative smooth function $w$ of compact support in $(-1/4,1/4)$ with $w(0)=1$. Take

$$K=\lfloor\sqrt L\rfloor,\qquad Q=\left\lfloor\frac{\sqrt X}{K L^B}\right\rfloor,\qquad T=\left\lfloor\frac{X}{KQ}\right\rfloor,$$

where $B$ is a sufficiently large fixed constant. Average uniformly over primes $Q<q\le2Q$ and integers $T<r\le2T$. Write $d=qr$ and use $\langle\cdot\rangle$ for the average over these **pairs**, with multiplicity if a modulus recurs. The number of pairs is $N\asymp X/(KL)$ by the prime number theorem. Each $d\asymp X/K$. Define

$$I(a)=\int_{-X/4}^{X/4}\frac{w(t/X)}{\log(a+t)}\,dt,$$

$$\mathcal D(y)=\left\langle\sum_{i=1}^h\left(\sum_{p\equiv a\ (d)} w\!\left(\frac{p-a}{X}\right)-\frac{{\bf1}_{(a,d)=1}}{\varphi(d)} I(a)\right)\right\rangle,\qquad a=y+i,$$

where the inner sum is over primes and $a=y+i$ is used in each summand. Then

$$\boxed{\ \mathcal D(y)=P(y)-\frac{h}{\log y}+O_{C,w}\!\left(\frac{(\log L)^2}{\sqrt L}\right).\ } \tag{1}$$

Constants can also depend on the fixed choice of $B$. The smoothed prime sum and the progression prediction being subtracted are each of order $Kh/L$ in their background contribution. It is their **difference** whose error tends to zero. All steps below are uniform for the stated $y$.

## The actual primes away from the target

Write $p=a+kqr$. The $k=0$ terms give exactly $P(y)$. Only $0<|k|\le 2K$ need be considered for the remainder. For fixed $i,k,q$, varying $r$ now gives a progression of modulus $|k|q$. If $a$ shares a prime factor with this modulus there are no primes in range, since $a+kqr\ge 3X/4$ on the support and $|k|q<3X/4$. In reduced classes Bombieri–Vinogradov, with the maximum over endpoints and reduced residues, replaces this weighted count by

$$\frac{|k|q}{\varphi(|k|q)}{\bf1}_{(a,|k|q)=1}\int_T^{2T}\frac{w(kqt/X)}{\log(a+kqt)}\,dt.$$

The integrand is taken as zero outside the support of $w$ so that the logarithm is needed only at positive arguments. For negative $k$ reverse the prime endpoints. Partial summation costs $O_w(1)$ times the maximum progression error, since the test has bounded variation. More explicitly use the prime-count version with total error $O(X/L^{10})$ up to $4X$; it follows also from the Chebyshev version by partial summation on this support. For a fixed sign the moduli $|k|q$ are distinct, because $q>2K$ is their unique largest prime divisor. They are at most $4KQ$, within the distribution level for our choice of $B$. Summing errors first and dividing by $N$ gives $O_w(h X/(N L^{10}))=O_{C,w}(K L^{-7})$. This argument uses no assertion of equidistribution at modulus $qr$. [Bombieri–Vinogradov with the maximum over endpoints](https://dms.umontreal.ca/~andrew/Courses/Chapter13.pdf)

In this main term replace $\log(a+kqt)$ by $\log(y+kqt)$. On the support the reciprocal changes by $O(h/(XL^2))$. The multiplier $|k|q/\varphi(|k|q)\ll \log(2|k|)$, by Mertens' bound, so this change costs $O(Kh^2\log(2K)/(XL^2))$ in total after averaging. Inclusion–exclusion on $i$ gives

$$\frac{|k|q}{\varphi(|k|q)}\sum_{i\le h}{\bf1}_{(y+i,|k|q)=1}=h+O\big(2^{\omega(|k|)}\log(2|k|)\big).$$

Here $\omega(n)$ counts distinct primes. The sum of $2^{\omega(j)}$ through $2K$ is $O(K\log(2K))$, since it is bounded by the sum of the divisor function. The total cost of this replacement after averaging is $O_w(K\log^2(2K)/L)$. Finally replace the $t$-integral by the sum over integer $r$. The bounded variation of $w(kqt/X)/\log(y+kqt)$ is $O_w(1/L)$, so this costs $O_w(Kh/(TL))$. The contribution from all off-center primes is consequently

$$h\left\langle\sum_{k\ne0}\frac{w(kd/X)}{\log(y+kd)}\right\rangle+O_{C,w}\big(K\log^2(2K)/L\big). \tag{2}$$

For the sum over all integers $k$, Poisson summation gives $I(y)/d+O_{w,j}(K^{1-j}/L)$ for each fixed $j\ge2$. Indeed the smooth function of $u$, $w(u)/\log(y+Xu)$ on the support, has derivatives of each fixed order bounded by $O_{w,j}(1/L)$ and $X/d\asymp K$. Take $j=8$ and remove the $k=0$ term $1/\log y$. Thus the observed prime sum in (1) equals

$$P(y)-h/\log y + h I(y)\langle 1/d\rangle+O_{C,w}\big(K\log^2(2K)/L\big). \tag{3}$$

## The conventional progression main term

To establish (1) we must compare the subtracted progression prediction to the **whole** term $h I(y)\langle1/d\rangle$ in (3). Replacing $I(y+i)$ by $I(y)$ costs $o(1)$: $|I'(a)|\ll_w L^{-2}$ here and $1/\varphi(d)\ll L/d$. For the remaining calculation introduce

$$C_0=\prod_p\left(1+\frac1{p(p-1)}\right),\qquad S(a)=\frac{\varphi(a)}a\prod_{p\nmid a}\left(1+\frac1{p(p-1)}\right).$$

For $T\le U\le2T$ one has

$$\sum_{T<r\le U}\frac r{\varphi(r)}{\bf1}_{(a,r)=1}=(U-T)S(a)+O\big(2^{\omega(a)}\log(2T)+1\big). \tag{4}$$

Expand $r/\varphi(r)=\sum_{s\mid r}\mu^2(s)/\varphi(s)$. For $(s,a)=1$ the number of admissible multiples of $s$ is $(U-T)\varphi(a)/(sa)+O(2^{\omega(a)})$ by inclusion–exclusion. The same divisor expansion gives $\sum_{s\le t}1/\varphi(s)\ll\log(2t)$ by first summing $1/s$ over multiples and using $\prod_p(1+1/(p(p-1)))<\infty$. It also gives $\sum_{s\le t}s/\varphi(s)\ll t$. The latter bounds the omitted tail $\sum_{s>2T}1/(s\varphi(s))\ll1/T$ by dyadic summation. These estimates prove (4). Partial summation with $1/r$ gives

$$\sum_{T<r\le2T}\frac{{\bf1}_{(a,r)=1}}{\varphi(r)}= S(a)\sum_{T<r\le2T}\frac1r+O\!\left(\frac{2^{\omega(a)}\log(2T)+1}{T}\right).$$

We can use $1/(\varphi(q)\varphi(r))$ in place of $1/\varphi(qr)$ throughout the main term. They agree except for $q\mid r$, a fraction $O(1/Q+1/T)$ of pairs; each expression contributes $O_{C,w}(hKL)$ or less per pair before averaging. The change is negligible. Since $2^{\omega(a)}\le \tau(a)\ll_\epsilon X^\epsilon$, the error from the partial summation formula, multiplied by $O(hI(y)/(QT))$, is $o(1)$ (for example use $\epsilon=1/8$ and the extra $1/T$ in that formula). More explicitly it is $O_w(h X X^{1/8}\log(2T)/(LQT^2))$. Also $q/\varphi(q)=1+O(1/Q)$ and at most one $y+i$ is divisible by $q>h$. Since $S(a)\le C_0$, discarding this latter restriction costs $O_w(K/L)$ after averaging. It follows that the subtracted prediction is

$$I(y)\langle1/d\rangle\sum_{i=1}^h S(y+i)+O_{C,w}(K/L)+o(L^{-1}).$$

For completeness, $\sum_{i\le h} S(y+i)=h+O_C(\log L)$ uniformly. Write $S(a)=C_0\prod_{p\mid a}(1-v_p)$ with $v_p=p/(p^2-p+1)$. In each product the primes exceeding $W=L^4$ cost $O(L/(W\log W))$, using the number of such primes that can divide $a\le3X$. Expand the remaining finite product; the total error in replacing divisibility counts by $h/d$ is $O(\prod_{p\le W}(1+v_p))=O(\log W)$ by Mertens. The mean of the product is $C_0\prod_{p\le W}(1-v_p/p)=1+O(1/W)$ since the infinite product is exactly one. This proves the interval estimate. As $I(y)\langle1/d\rangle\ll_w K/L$, subtracting the prediction from (3) proves (1).

## What the comparison decides

For all sufficiently large $X$, $P(y)$ is the nearest integer to $\mathcal D(y)+h/\log y$ simultaneously for every target. In particular, forcing $\mathcal D(y)>-h/\log y+1/2$ everywhere would force a prime in the original interval. The uniform $o(1)$ comes from the translated primes and the conventional main term. We have no independent one-sided estimate of that strength for $\mathcal D(y)$ itself.

In fact, the [documented sparse-window argument](count-polynomials.md) gives many nonempty starts with $P(y)\le b h/L$ for a fixed $b<1$, under the hypotheses recorded there. At these starts (1) forces a negative averaged progression discrepancy of order $L$ even though the individual moduli are smaller than the sampling interval and each contains many starts. Thus an $o(L)$ absolute bound for this averaged discrepancy uniformly in the moving target would already be false. The last half-unit at a possibly empty interval is still open. Independent priority for (1) is unverified. [Exact finite checks of the switching and local factors](check-switched-progressions.py)

## Can the same distribution estimate supply the last half-unit?

The [earlier deletion construction](approaches.md#what-can-zero-locations-alone-detect) gives an exact test. Keep the moduli and prediction in (1) fixed and replace the observed primes by the set of primes remaining after deleting those in $(X_j,X_j+\lfloor\log^3 X_j\rfloor]$ for $X_j=2^{2^j}$, $j\ge4$. Up to $4X$ there are $O(L^3)$ deletions. For each modulus the maximum over endpoints and reduced residues of the change in its prime count is therefore $O(L^3)$. Summed over moduli up to $\sqrt X$ this is $O(\sqrt X L^3)=o(X/L^A)$ for every fixed $A$. The modified counts obey the same Bombieri–Vinogradov bounds used above, with the same classical main terms. The elementary mean and the modulus selection still use the ordinary integers and primes.

Now set $y=X=X_j$. At large $j$ no other deleted interval meets the support of any weight in this shell. Every deleted prime there is at distance less than $d$ from every $a=y+i$, since $d\asymp X/K$ and both lie within $O(L^3)$ of $y$. Such a prime shares the residue of $a$ precisely when it equals $a$. Thus deleting these primes decreases the observed sum by **exactly** $P(y)$ for every pair $(q,r)$, leaves all translated contributions intact, and leaves the prediction intact. The modified discrepancy equals $-h/\log y+o(1)$ along these starts. This isolates the limitation of the proposed input: even the full family of uniform distribution estimates used to prove (1) is consistent with failure of the required one-sided inequality. A proof for ordinary primes must bring in a property that distinguishes them from this subset.
