# How many large divisor classes can cover a prime-free interval?

GitHoobar · 27 November 2026 · Research note developed with OpenAI Codex and Luna agents

In an interval of $H$ consecutive integers, forbid one residue at every prime through $Z=\tfrac14\sqrt H(\log H)^{1+\delta}$ and at any $k$ additional primes. For some absolute $\delta,c,b>0$ and every sufficiently large $H$, at least

$$bH\frac{\log\log H}{(\log H)^2}\quad\text{positions remain whenever}\quad k\le c\sqrt H(\log H)^\delta\log\log H.$$

The classes, including those at the additional primes, can depend on the interval. We derive this from the survivor theorem in OpenAI's September 2026 Jacobsthal preprint. The proof keeps track of how the deletion from a single extra prime varies with its size. It yields a logarithmic-power saving for the uniform Jacobsthal function and a necessary condition on the prime divisors in a hypothetical Cramér-scale gap. The last section tests whether this suffices to detect a prime at that same start. [OpenAI, Theorems 1.1 and 1.2](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf)

## The cost of each additional prime

Translate the interval to the coordinates $1,\dots,H$, translating the forbidden residues with it. Put $z=\tfrac14\sqrt H\log H$ and $Y=\lfloor z^2/(\log z)^2\rfloor\sim H/4$. By Theorem 1.2 of the preprint, forbidding the classes through $z$ leaves at least $b_0 H\log\log H/(\log H)^2$ positions in $[1,Y]$, and therefore in $[1,H]$, for some absolute $b_0>0$. Indeed its lower bound is a constant times $YV_0/B^2$, with $w=\log z/(\log\log z)^2$, $B=\log z/\log w$ and $V_0\asymp1/\log w$. Let $S_0$ be the survivors in $[1,H]$.

**One progression.** For $z\le T\le z\log H$, a prime $p>T$ and any residue $a\bmod p$,

$$\#\{i\in S_0:i\equiv a\pmod p\}\le K\frac{H}{T\log H} \tag{1}$$

with an absolute $K$. The same estimate holds for $p=T$ if $p>z$. Write $i=a+pt$ and enclose the possible $t$ in an interval of $N=\lceil H/T\rceil+2$ consecutive integers. This works even when $p>H$. Put $Q=\lfloor\sqrt N\rfloor$. For large $H$, $Q<z<p$, and $\log N\asymp\log H$ throughout the stated range for $T$. For each prime $q\le Q$, the survivor condition forbids one residue of $t\bmod q$ because $p$ is invertible modulo $q$.

For clarity, let $A$ be any subset of $N$ consecutive integers missing a residue $a_q$ at each prime $q\le Q$. For squarefree $d\le Q$, combine those residues for $q\mid d$ into $a_d$ by the Chinese remainder theorem. Each $t\in A$ has $\gcd(t-a_d,d)=1$, so its Ramanujan sum $\sum_{(u,d)=1}e^{2\pi i u(t-a_d)/d}$ over reduced residues equals $\mu(d)$. Summing over $t$ and applying Cauchy–Schwarz gives

$$\sum_{u\bmod d}^{*}\left|\sum_{t\in A}e^{2\pi iut/d}\right|^2\ge |A|^2/\varphi(d).$$

The additive large sieve over the distinct reduced fractions of denominator at most $Q$ bounds the sum of the left sides by $(N+Q^2)|A|$. The sum of $1/\varphi(d)$ over squarefree $d\le Q$ is $\gg\log Q$, since it dominates the harmonic sum over squarefree integers, which have positive density. Hence $|A|\ll N/\log N$. Applied to the enclosed progression this proves (1). It requires no distribution assumption on $S_0$ modulo $p$. The preprint uses the corresponding per-progression sieve estimate in its final deduction. [Montgomery and Vaughan, *The large sieve*](https://doi.org/10.1112/S0025579300004708) · [OpenAI, final deduction from the survivor theorem](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/sections/assembly.tex)

**All primes between the two cutoffs.** Take $0<\delta\le1$, to be fixed below, and put $Z=z(\log H)^\delta$. Use (1) with $T=p$ for each $z<p\le Z$. Each dyadic segment $(u,2u]$ contains $O(u/\log u)$ primes by Chebyshev's bound, so it contributes $O(1/\log H)$ to the reciprocal sum. There are at most $1+\delta\log\log H/\log 2$ such segments. With an absolute $K_1$, the total loss is therefore at most

$$K_1\,H\frac{1+\delta\log\log H}{(\log H)^2}.$$

Fix $\delta$ small enough that $K_1\delta<b_0/8$. Take $H$ sufficiently large that the term without $\delta\log\log H$ also costs less than an eighth of the initial lower bound.

**The specified primes above the second cutoff.** Apply (1) with the common $T=Z$. The total loss for $k$ further primes is at most $KkH/(Z\log H)$. For $k\le c\sqrt H(\log H)^\delta\log\log H$ this is at most $4KcH\log\log H/(\log H)^2$. Fix $c$ so that $4Kc<b_0/4$. At least half the initial lower bound remains. The argument also covers a list that includes primes below $Z$ when their prescribed classes agree with those already used there.

## Consequences for covers and for the actual interval

Let $J(k)$ be the least integer $m$ such that, for every modulus with at most $k$ distinct prime divisors, each interval of $m$ consecutive integers contains an integer coprime to that modulus. In the theorem prescribe the divisor classes at the small primes of the modulus and arbitrary classes at the other primes through $Z$. There are at most $k$ remaining divisor primes. For large $k$, choose $H$ to be the ceiling of $D k^2/((\log k)^{2\delta}(\log\log k)^2)$, with a sufficiently large absolute $D$. Then $\log H\sim2\log k$ and $c\sqrt H(\log H)^\delta\log\log H\ge k$. This gives

$$J(k)\ll \frac{k^2}{(\log k)^{2\delta}(\log\log k)^2}.$$

Compared with the preprint's stated Theorem 1.1, the additional factor $(\log k)^{2\delta}$ in the denominator arises from summing (1) at its individual prime scale in the band $z<p\le Z$. This is a deduction from its stronger Theorem 1.2. We have not established independent priority or an explicit value of $\delta$.

Now take $H=\lceil C(\log x)^2\rceil$ for a fixed $C>0$ and forbid divisibility in the actual interval $(x,x+H]$. If it is prime-free, its entries with no prime factor through $Z$ must collectively have more than $c\sqrt H(\log H)^\delta\log\log H$ distinct **least** prime factors, each in $(Z,\sqrt{x+H}]$. Otherwise those least primes would cover every remaining entry, contradicting the theorem. In fact any selection of one witness prime divisor per entry in the full interval must use more than that many distinct primes above $Z$ (apply the same covering argument to the selected witnesses). Their product $M$ therefore satisfies

$$\log M\gg \sqrt H(\log H)^{1+\delta}\log\log H.$$

This restricts a potential counterexample. The size of $x$ still allows that many distinct least prime factors below $\sqrt{x+H}$.

## Testing the survivors for a prime

Take the set $S$ of entries left by this sieve at the original start, using only divisibility classes and any permitted list of extra primes at most $\sqrt{x+H}$. For sufficiently large $x$, every prime of the interval lies in $S$. Write $P$ for their number. For real $u>0$ define

$$W(u)=\sum_{n\in S}u^{\Omega(n)-1},$$

where $\Omega$ counts prime factors with multiplicity. We tested the lower estimate $2W(r)>W(2r)$ with $r=(\log H)^{1/3}/\sqrt H$. The signed difference gives weight $1$ on primes, $0$ on semiprimes, and $-(2^{j-1}-2)r^{j-1}$ at $\Omega(n)=j\ge3$. Each negative contribution has magnitude at most $4r^2$ when $2r\le1$. By the large-sieve argument above, now on the full interval with $Q=\lfloor\sqrt H\rfloor<Z$, $|S|\ll H/\log H$. Uniformly in the start and allowable extra primes,

$$ P-O((\log H)^{-1/3})\le 2W(r)-W(2r)\le P.$$

Thus strict positivity of the difference is necessary and sufficient for a prime once $x$ is large. The direct lower bound obtained from the survivor theorem is $W(r)\ge |S|r^{\lfloor\log(x+H)/\log Z\rfloor-1}$, since each remaining prime factor exceeds $Z$. It gives no strict comparison with $W(2r)$. Even a set consisting entirely of semiprimes would have $W(2r)=2W(r)$ regardless of its size. No uniform strict lower bound for the signed difference, or resolution of Cramér's conjecture, is established here.

The finite checks cover the change of progression coordinates, the Ramanujan-sum energy inequality, and the signs and errors of the prime weights. The asymptotic bounds above have written proofs. [Exact checker](check-large-divisor-classes.py)
