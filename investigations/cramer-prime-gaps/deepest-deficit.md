# Which zeros can sustain an empty window?

GitHoobar · 27 November 2026 · Working research note developed with OpenAI Codex and three Luna agents

Fix an integer start $x$, let $L=\log x$ and $h=\lceil C L^2\rceil$ for fixed $C>0$. Our [endpoint-sensitive test](finite-zero-test.md) equals the prime weight $M=\sum_{x<p\le x+h}\log p$ to within $O_C(x^{-3})$. We seek a lower bound even if $x$ minimizes that weight. We derive a bound for the specified window, identify two terms which could still make it vacuous, and test whether estimates for their absolute values suffice. The uniform inequality needed for Cramér remains open.

## A lower bound at the original start

Fix $0<b,\lambda<1/8$, $0<\theta<13/30$, and $\theta<\eta<13/15$. Use the spline $f$ and its transform $F$ from the [previous note](finite-zero-test.md), now with
$$
\delta=\frac{\log(1+h/x)}{1+2\lambda},\quad d=\lambda\delta,\quad
K=\lceil8L\rceil,\quad T=4K/(b\delta),\quad m=F(0)=1-2b.
$$
Sample $v$ as the sum of two independent uniforms on $[0,d]$ and write $\|g\|_2=(\mathbb E_v|g(v)|^2)^{1/2}$. Every subwindow $(xe^v,xe^{v+\delta}]$ lies inside $(x,x+h]$. This is the only averaging over starts in the argument.

For each nontrivial zeta zero $\rho=\beta+i\gamma$, counted with multiplicity, write $a_\rho=x^{\rho-1}F(\delta\rho)$. For a set of zeros $J$ put $S_J(v)=\sum_{\rho\in J}a_\rho e^{(\rho-1)v}$. Among $x^\theta<|\gamma|\le T$, set aside the zeros in
$$
H=\{\rho:x^\eta<|\gamma|\le T,\ \beta>1/2+1/L\}.
$$
Let $G$ consist of the other zeros in the indicated band. For fixed $B\ge1$ define the real signed sum over ordered pairs
$$
R_B=\Re\sum_{\substack{\rho,\rho'\in G\\|\gamma-\gamma'|>B}}
a_\rho\overline{a_{\rho'}}\,J_d(\rho+\overline{\rho'}-2),\qquad
J_d(s)=\left(\frac{e^{ds}-1}{ds}\right)^2,\quad J_d(0)=1.
$$

**Bound.** There is a constant $K_0$ depending at most on $b,\lambda,\theta,\eta$ such that, at every sufficiently large start for fixed $C,B$,
$$
M\ \ge\ \delta x
\left[m-\|S_H\|_2-\sqrt{R_B+K_0(B+1)/C}\right]_+
-O_{b,\lambda,\theta,\eta,C,B}\bigl(L(1+\log\log L)\bigr).
\tag{1}
$$
Here $[t]_+=\max(t,0)$. The original endpoint-sensitive test differs from $M$ by $O_C(x^{-3})$, so (1) bounds that test directly without shifting its endpoint filter. If the bracket before taking the positive part exceeds a fixed positive margin, the original interval contains $\gg_{C} L$ actual primes (with the implied constant also depending on that margin and the fixed filter). Under the Riemann hypothesis (RH), $H$ is empty. In that case a uniform upper bound on the *signed* $R_B$ strictly below $m^2-K_0(B+1)/C$ by a fixed margin would suffice. The margin condition is a sufficient condition that also forces growing prime counts.

### Removing low zeros and bounding nearby pairs

For $j=1,2$ and fixed $0<\alpha<13j/30$ one has, for every fixed $A>0$,
$$
\sum_{|\gamma|\le x^\alpha}x^{j(\beta-1)}=o(L^{-A}).
\tag{2}
$$
This is a direct use of Guth and Maynard's density estimate (13.3) and the Vinogradov–Korobov zero-free region. For $U=x^\alpha$ and $1/2\le\sigma<1$ their bound is $N(\sigma,U)\ll U^{(30/13+o(1))(1-\sigma)}(\log U)^{O(1)}$. Split $\beta\ge1/2$ into strips of width $1/L$ with lower edge $\sigma$. Each term is at most $e^j x^{-j(1-\sigma)}$, and nonempty strips have $1-\sigma\gg L^{-2/3}(\log L)^{-1/3}$. Since $j-(30/13)\alpha>0$, the exponential saving absorbs every power of $L$, including the number of strips. Zeros with $\beta<1/2$ contribute $O(x^{\alpha-j/2}L)$. This is why the squared weights admit a larger cutoff than the linear weights. [Guth and Maynard, §13.2, especially (13.3)](https://arxiv.org/html/2405.20552v2#S13.SS2) · [Ford, zero-free regions](https://arxiv.org/abs/1910.08205)

The integral formula gives $|F(\delta\rho)|\ll\min(1,1/(\delta|\gamma|))$. For the second bound integrate the box factor explicitly and bound the transforms of the uniform densities by $e^{b\delta}$ in product. Equation (2) with $j=1$ therefore makes the low linear sum $o(L^{-A})$ uniformly in $v$. With $j=2$ it bounds the squared coefficients through height $x^\eta$. For the remaining zeros of $G$, $x^{2(\beta-1)}\le e^2/x$. The ordinary zero count $N(t)\ll t\log(2t)$ and a dyadic sum above $1/\delta$ give
$$
\sum_{\rho\in G}|a_\rho|^2\ll o(L^{-2})+
\frac{\log(2/\delta)}{x\delta}\ll \frac1{CL}.
$$
The final implied constant can be chosen independently of fixed $C$ for sufficiently large $x$ depending on $C$.

Independence of the two uniform shifts gives $\mathbb E_v e^{sv}=J_d(s)$. Expand $\|S_G\|_2^2$ in ordered pairs. For $|\gamma-\gamma'|\le B$ the factor $|J_d|\le1$. Each zero has $O((B+1)L)$ neighbors with multiplicity by the unit-interval zero count. Summing $2|a_\rho a_{\rho'}|\le |a_\rho|^2+|a_{\rho'}|^2$ gives the absolute bound $K_0(B+1)/C$ for these pairs, including the diagonal. Hence $0\le\|S_G\|_2^2\le R_B+K_0(B+1)/C$. The cited density paper also uses this unit-interval count in §13.2.

The same neighbor argument applies to **any** chosen unit band of differences $j\le|\gamma-\gamma'|<j+1$, however far from zero. For each first zero the second lies in at most two intervals of unit length. The sum of absolute terms in any such band is at most $K_1/C$ with a common constant. Thus even an adaptive selection of $k$ unit bands accounts for at most $K_1 k/C$. Inserting Montgomery's classical weight $4/(4+(\gamma-\gamma')^2)$ would bound the absolute contribution beyond $B$ by $O(1/(CB))$, on summing $j^{-2}$ over those bands. Our required signed sum has no such extra weight. The [companion calculation](extended-pair-correlation.md) tests the published extension with a variable weight at exactly the localization width needed here.

### Recovering primes, including at the worst start

The explicit formula in the previous note applies with real anchor $xe^v$ and the fixed parameters above. Its discarded tail is $O_C(x^{-3})$ uniformly in $v$ with filter parameters fixed. The full finite zero sum is real by conjugation. Its $L^2$ norm is at most $\|S_H\|_2+\|S_G\|_2+o(L^{-3})$, so at some permitted $v$ its value is at most this bound. The pole contributes $\delta xe^v F(\delta)$, with $F(\delta)\ge m$, and the trivial-zero correction is $O(\delta/x^2)$.

There is a sharper bound for the proper powers to be subtracted. If distinct $p^j,q^k\in(x,x+h]$ have $j,k\ge2$ with a common divisor $r>1$, they are distinct $r$th powers. Consecutive such powers at or above $x$ have spacing at least $r x^{1-1/r}\ge2\sqrt{x}>h$. Thus the occurring exponents are pairwise coprime. Assign each one a prime divisor of its exponent. They are all distinct, so Mertens' reciprocal-prime estimate gives
$$
\sum_{x<p^j\le x+h,\ j\ge2}\log p
\le \log(x+h)\sum_{\substack{\ell\le\log_2(x+h)\\\ell\ {\rm prime}}}\frac1\ell
\le L(\log\log L+O(1)),
$$
where $\log_2(x+h)$ in the summation limit means the base-two logarithm. Subtract this upper bound in the subwindow, use $0\le f\le1$, and use $M\ge0$ if the bracket is negative. This proves (1). The finite test still admits exact subtraction when the proper powers are known.

## Two attempts to finish the estimate

**Taking absolute values fails even for the far pairs.** Put $U=1/(2\delta)$. By Conrey's theorem and the zero count, $\gg U\log U$ zeros on the critical line have positive ordinate in $(x^\theta,U]$. They all belong to $G$. On this group $\Re F(\delta\rho)\ge m\cos(1/2)$, so $|a_\rho|\gg x^{-1/2}$. For any two in the group, $|J_d(\rho+\overline{\rho'}-2)|\gg1$, since $|v(\gamma-\gamma')|\le 2d U=\lambda$ and $e^{-v}$ is bounded below. Omitting $O((B+1)L)$ neighbors per zero leaves $\gg (U\log U)^2$ ordered pairs. Thus the sum of absolute values on the far pairs alone is $\gg x/(C^2 L^2)$. This obstruction holds unconditionally and diverges for every fixed $C$. [Conrey, *More than two fifths of the zeros of the Riemann zeta function are on the critical line*](https://doi.org/10.1515/crll.1989.399.1)

**Even a signed bound tending to zero would overshoot under RH.** The [aligned-deficit note](aligned-windows.md) gives arbitrarily large starts where the parent contains at most $(1-\epsilon)h/L$ primes for a fixed $\epsilon>0$ and any fixed $C$ (decrease $\epsilon$ to absorb rounding or the change of logarithm). Take $b,\lambda<\epsilon/16$. By containment alone, each subwindow then has weighted prime mass at most $(1-\epsilon+o(1))h$, whereas $\delta xe^v\sim h/(1+2\lambda)$. The explicit formula and the proper-power bound give the full normalized zero sum at least $m-(1-\epsilon)(1+2\lambda)-o(1)>\epsilon/2$ **for every shift** in the averaging range. Under RH it follows that $R_B\ge\epsilon^2/4-K_0(B+1)/C-o(1)$ along these starts. For fixed $B$ and sufficiently large fixed $C$ this is bounded away from zero. An actually empty parent would instead require $R_B\ge m^2-K_0(B+1)/C-o(1)$ under RH. Our estimates allow the first excursion and do not exclude the second. [Maier's short-interval theorem](https://doi.org/10.1307/mmj/1029003189)

Pair correlation and prime gaps have a long history. The quantity above retains the phase at the specified integer $x$. An average taken over an entire dyadic range does not bound it there. The explicit formula, density estimates, critical-line proportion and Maier intervals are published inputs. We claim no priority for this localization. The [finite verification](check-deficit.py) checks the pair identity including off-line parameters and multiplicities, the interval containment, and the exponent argument. [Heath-Brown, *Gaps between primes, and the pair correlation of zeros of the zeta-function*](https://matwbn.icm.edu.pl/ksiazki/aa/aa41/aa4118.pdf)
