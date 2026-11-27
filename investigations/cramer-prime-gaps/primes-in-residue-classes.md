# Actual primes after fixing congruences on the starting point

GitHoobar · 27 November 2026 · Research note developed with OpenAI Codex and three Luna agents

Can the square-logarithmic vacancy test detect a prime even at an exceptional start? We tried conditioning on all the small-prime congruences of the start and allowing an arbitrary choice of candidate positions. This gives actual primes with a sharp order of magnitude for the fraction of successful starts in each class. A sparse-deletion argument then measures how much information about the worst start these estimates lose. Cramér's conjecture remains open. [Vacancy test](vacancy-test.md) · [Earlier rough-number result](rough-intervals.md)

## A classwise estimate

Let $L=\log X$, $h=\lceil L^2\rceil$, and $d=\log L/L$. There are absolute constants $0<a<\eta$ sufficiently small for the following assertions. Put $y=aL$. Take any squarefree $M\le X^\eta$ divisible by every prime up to $y$. Such moduli exist since the logarithm of their required prime product is asymptotic to $aL$.

There is a choice of $W=M$ or $W=M/\ell$ for one prime $\ell\mid M$, made **once for the whole modulus**. For every residue $r\bmod W$, choose any subset $I\subseteq\{1,\ldots,h\}$ of offsets with $\gcd(r+i,W)=1$. Write $m=|I|$. Sample an integer $x$ uniformly from the starts in $[X,2X)$ congruent to $r\bmod W$, and let $Y_I$ count actual primes among $\{x+i:i\in I\}$. Then, for large $X$,

$$\Pr_r(Y_I>0)\asymp \min(1,md). \tag{1}$$

If $md\ge1$, a positive absolute fraction of the starts have $Y_I\ge c\,md$ for an absolute $c>0$. All constants in these assertions are uniform in $r,M,I$. In particular the order of magnitude in (1) holds for every preselected set of columns, including the least favorable choice. The offsets may depend on the class, but must be fixed before sampling its start.

**With all the original congruences retained**, every class modulo $M$ satisfies the unconditional weaker lower bound

$$\Pr_r(Y_I>0)\gg_\epsilon M^{-\epsilon}\min(1,md)\qquad(\epsilon>0). \tag{2}$$

Here eligibility and probability both use $M$, and the constant in (2) can be ineffective. When $I$ consists of all eligible offsets, $m\gg L^2/(\log L)^2$ in every class, for either modulus. Thus (1) gives at least $cL/\log L$ actual primes in a positive fraction of the windows in each class modulo $W$. Equation (2) reaches every original class, including any class lost by omitting a factor. Neither assertion specifies which start in that class succeeds.

**Consequence for an individual exceptional start.** Fix $0<b<1$ and take any specific $x_0\in[X,2X)$. Keep its residues at **every** prime up to $aL$. Also keep its residues at any $k\le (\eta/4)L^{1-b}$ additional primes up to $\exp(L^b)$. There exists a start in the **same shell**, agreeing with $x_0$ on **every one** of these congruences, whose length-$h$ interval contains an actual prime. In fact at least $\gg_\epsilon (X/M)M^{-\epsilon}$ such starts work, where $M$ is the product of the distinct prescribed primes. To prove it, $\log M\le (a+o(1))L+kL^b<\eta L$. Apply (2) with all eligible offsets and use $md\gg L/\log L$. For sufficiently small fixed $\epsilon$ the lower bound on the number of starts tends to infinity. All starts in the final residue class give the same transcript even if the extra primes were chosen adaptively from earlier answers. Any rule that certified vacancy from this transcript alone would issue the same verdict at a prime-bearing start. The conclusion supplies other starts and leaves the status of $x_0$ itself open.

### A prime at a single specified offset

For $B=W$ or $M$ and a reduced residue $r+i\bmod B$, the exact column count is the number of primes in $[X+i,2X+i)$ congruent to $r+i\bmod B$. The number $T$ of starts in the class satisfies $T=X/B+O(1)$. We use Thorner and Zaman's Theorem 1.1 on the interval of length $X$ with right endpoint $2X+i-1$ (take $X$ integer). Their weighted prime count is comparable to $\lambda X/\varphi(B)$. To check the range, their sufficient condition (1.8) holds with, for instance, $\delta_1=1/100$, $\delta_2=\eta$, and $\varepsilon=1/100$ after decreasing $\eta$, even for their exceptional exponent $32/37$. The right endpoint divided by the interval length is bounded. The relative error in Theorem 1.1 is then $O(\exp(-c/\eta))+o(1)$, less than $1/2$ after a further absolute decrease in $\eta$. Divide by the prime logarithm, which is comparable to $L$. [Thorner and Zaman, Theorem 1.1 and (1.7)–(1.8)](https://arxiv.org/pdf/2108.10878)

Here $\lambda=1$ unless the modulus has an exceptional real zero $\beta$. In that case $\lambda=1-\chi(r+i)\xi^{\beta-1}$ with $X\le\xi\le3X$, and $\lambda\le2$. We now justify a uniform lower bound for $W$. In the standard zero-free region at height zero for the product of the Dirichlet $L$-functions modulo $M$, there is at most one zero above $1-c_0/\log(3M)$, with $c_0>0$ an absolute constant. If it exists, drop one prime divisor of its primitive conductor to form $W$. Otherwise use $W=M$. Any real zero that close to one attached to a character modulo $W$ would also occur modulo $M$, by inducing the character. The added Euler factors have no zeros on the positive real axis. The exceptional primitive character removed from $M$ cannot be induced from $W$ because $M$ is squarefree. Thus any residual exceptional zero for $W$ satisfies $(1-\beta)L\ge c_0 L/\log(3M)$. This gives $\lambda\gg1$ for $W$. For $M$ itself, the Siegel bound (1.2) in the same paper gives $\lambda\gg_\epsilon M^{-\epsilon}$ without removing anything. This last bound follows also when $\chi(r+i)=-1$, in which case $\lambda\ge1$ directly.

Both moduli contain all primes up to $y$ with at most one omission. Extra prime factors above $y$ satisfy $\sum_{p\mid M,\,p>y}1/p\le\log M/(y\log y)$. Mertens' formula gives $B/\varphi(B)\asymp\log L$. It follows that each eligible column has probability $\asymp d$ for $W$, and between $\gg_\epsilon M^{-\epsilon}d$ and $O(d)$ for $M$.

### Uniform control of two columns

Write $x=r+Bt$ over $T$ consecutive integers $t$. For distinct $i,j\in I$ and any prime $p>y$ not dividing $B$, the simultaneous primality of $x+i,x+j$ excludes two residues of $t\bmod p$, except that it excludes one if $p\mid i-j$. We only sieve to $u=Z^{1/16}$ with $Z=\lfloor\sqrt T\rfloor$, so both candidate integers exceed every sieving prime. Primes dividing $B$ are omitted. Write $\nu_p$ for the number of excluded classes, using zero for primes outside the sieve.

In the arithmetic large sieve the upper bound on the pair count is $(T+Z^2)/G(Z)$, where
$$G(Z)=\sum_{\substack{s\le Z\\s\ \mathrm{squarefree}}}\prod_{p\mid s}\frac{\nu_p}{p-\nu_p}.$$
For completeness, compare $G(Z)$ with $P=\prod_{y<p\le u,\,p\nmid B}(1-\nu_p/p)^{-1}$, in which the product of the selected primes has no size restriction. Normalize its positive expansion to a probability law on squarefree $s$. Each prime divides $s$ with probability $\nu_p/p$, so $\mathbb E\log s\le2\sum_{p\le u}(\log p)/p\le3\log u$ for large $X$. Markov gives $G(Z)\ge P/2$. Omitting the primes dividing $B$ above $y$ costs a bounded factor by the reciprocal sum above. Replacing two exclusions by one for prime factors of $|i-j|$ also costs a bounded factor, since their reciprocal sum above $y$ is at most $\log h/(y\log y)$. Mertens' product now gives $P\gg(\log u/\log y)^2\gg d^{-2}$. This proves $\Pr_r(x+i,\ x+j\text{ both prime})\ll d^2$, uniformly for either modulus. [Montgomery's arithmetic large sieve, stated and proved in Ford's Theorem 6.5](https://ford126.web.illinois.edu/sieve_notes_large_sieve.pdf)

### Combining the columns

For $W$, linearity gives $\mathbb E_r Y_I\asymp md$ and the pair estimate gives $\mathbb E_r Y_I^2\ll md+(md)^2$. Cauchy–Schwarz proves the lower bound in (1), and the union bound proves its upper bound. Paley–Zygmund at half the mean gives the stated lower count for $md\ge1$. For the full $M$, the second-moment upper bound is identical and the first-moment lower bound loses at most a factor $M^{-\epsilon/2}$. Cauchy–Schwarz proves (2).

To get the unconditional count of eligible offsets, let $k$ be the number of prime factors of $B$. The inequality $k!\le B$ gives $k\ll\eta L/\log L$ for fixed $\eta$ and large $X$ with an absolute implied constant. Iwaniec's theorem gives at least $k^2$ coprime integers in every interval of length at least an absolute constant times $k^2\log k\cdot B/\varphi(B)$. This length is $\ll\eta^2 L^2$, so choose $\eta$ small and then fix $a=\eta/4$. Also $k\ge\pi(aL)-1\gg_a L/\log L$. These estimates prove the asserted lower bound for $m$. [Iwaniec, p. 226](https://doi.org/10.1515/dema-1978-0121)

## Applying the vacancy test to the exceptional starts

Use $q=h/(2X)$ from the test. With all eligible offsets and $W$ fixed as above, each class has
$$\sum_{x\equiv r\bmod W,\ X\le x<2X} q^{Y_x}\le (1-c)T+cTq$$
for an absolute $c>0$. This is an actual-prime bound within every class. It leaves room for a run of adjacent empty windows, whose starts lie in **different** classes. The exceptional set from the rough-number note depends on the whole start. It is not specified by $r$, so intersecting that exceptional set with the successful starts in (1) has no positive lower bound from (1) alone.

We can quantify this loss. Keep the same fixed $a$ as above. From the ordinary primes delete all those in $(N_j,N_j+D_j]$, where $N_j=2^{2^j}$ and $D_j=\lfloor N_j^{a/4}\rfloor$. Call the remaining sequence $S$. It is infinite by the prime number theorem applied between the deleted intervals. It violates the square-logarithmic gap bound since the gaps spanning the deletions have length at least $D_j$ and left endpoint at most $N_j$.

Nevertheless **all** the estimates (1) and (2) hold for $S$ at the same moduli and with the same eligible offsets, up to changes of absolute or $\epsilon$-dependent constants. For all sufficiently large $X$, the enlarged shell $[X,2X+h]$ meets at most one deletion interval and then $N_j\asymp X$. The potentially affected starts belong to one interval of length at most $D_j+h+1$. Every modulus being used is at least $\prod_{p\le aL}p/(aL)$ if the omitted prime is small, and at least the entire primorial otherwise. Hence $B\ge X^{a+o(1)}$ and $D_j+h+1<B$. **At most one start per residue class changes**, even if the set of tested offsets varies by class. The perturbation in any hit probability, or in the probability of exceeding any given count, is at most $1/T\ll X^{-1+\eta}$. This is $o(d)$ and also of smaller order than the right side of (2) for $m\ge1$ and small fixed $\epsilon$. The smaller exponents imply the assertion for larger ones. The changed sequence still obeys the estimates for every sufficiently large shell. This construction tests what the estimates can imply. It does not exhibit a gap of this length between actual primes.

The choice $h=\lceil L^2\rceil$ fixes a representative square-logarithmic length. The proof and the deletion test work for any fixed $h=\lceil C L^2\rceil$, $C>0$, after choosing the constants $a,\eta$ sufficiently small in terms of $C$ in the eligibility step. Cramér asks for the existence of one such $C$.

At $X=N_j$ there are at least $D_j-h$ empty length-$h$ windows for $S$ in the original test range $[X,3X)$. They already contribute more than any fixed multiple of $h$. Trying to multiply probabilities from neighboring classes assumes independence that fails at precisely this step. In fact, $k$ consecutive starts all have empty length-$h$ windows if and only if their union, an interval of length $h+k-1$, is empty.

## Other routes checked and attribution

* **Gap lengths.** For consecutive actual primes $p<p'$, the empty starts in their gap are exactly the integers in $[p,p'-h)$. Intersect this interval with the actual summation range before counting. This gives the exact vacancy count with correct endpoints even if a large gap crosses a boundary. A mean-square estimate can allow a single gap whose length greatly exceeds $h$.
* **Sieving to primality.** With only divisibility counts $h/s+O(1)$ and a level of order $h$, the ratio of the logarithm of the level to the logarithm of the required cutoff $\sqrt{2X+h}$ tends to zero. The classical linear lower sieve has no positive main term in this range. A count of semiprimes can therefore coexist with zero primes in a particular window. [Granville on sieving intervals](https://dms.umontreal.ca/~andrew/PDF/SievingSiegel.pdf)
* **Earlier matrix arguments.** Averaging primes down columns and comparing rows goes back to Maier. The prime-count input, the large sieve and Iwaniec's bound belong to their cited authors. Our deductions here quantify arbitrary column selection, the possible modulus loss, and the one-row sensitivity of the vacancy test. Independent review and priority for this combination are unestablished. [Maier, *Primes in short intervals*](https://doi.org/10.1307/mmj/1029003189)

The asymptotic arguments are written proofs. The finite check exercises the row and column counts, clipping of gap endpoints, and the effect of deleting primes on each residue class. [Exact checks](check-prime-rows.py)
