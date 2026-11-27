# Which positions can contain the only prime after translating an interval?

GitHoobar · 27 November 2026 · Developed with OpenAI Codex and Luna agents

Write $n_i=x+i$ for $1\le i\le h$, where $x$ is a positive integer, $C>0$ is fixed and $h=\lceil C(\log x)^2\rceil$. Suppose we translate the whole interval by $D$, requiring each position outside a chosen set to keep at least one of its original prime divisors. At every sufficiently large start, at least $h-\lfloor(h-1)/2\rfloor$ positions can each be made the **only** prime in infinitely many such translates. We determine exactly which positions qualify. We also show directly in the original interval that every shift $0<|D|\le x^A$ loses all original divisors at many positions. The results leave open whether the interval already contains a prime at $D=0$.

## A spacing lemma for integers with small radicals

The radical $\operatorname{rad}(n)$ is the product of the distinct primes dividing $n$. For any fixed $a,b>0$, at most one integer in $(x,x+(\log x)^a]$ has radical at most $(\log x)^b$, for all sufficiently large $x$.

**Proof.** Set $L=\log x$ and suppose $u>v$ are two such integers. Write $u/v=\prod_{j=1}^t p_j^{b_j}$ using distinct primes and nonzero integer exponents. Then $\sum_j\log p_j\le 2b\log L$, each $|b_j|\le 2L/\log 2$, and $t!\le\prod_j p_j$ gives $t\ll_b \log L/\log\log L$. The logarithms of distinct primes are linearly independent over the rationals by unique factorization. Stewart's Lemma 3, a rational case of Matveev's bound, therefore gives, with $A_j=\max(3,p_j)$ and an absolute $c\ge1$,

$$\log|\log(u/v)|>-c^t\log(3+2L/\log 2)\prod_{j=1}^t\log A_j.$$

Write $U=\log L$. Since $\sum_j\log A_j\ll_b U$, the logarithm of $c^t\prod_j\log A_j$ is at most $t\log(c_b U/t)$ by AM–GM, with a fixed $c_b$. This is $o(U)$ uniformly because $t/U\ll_b 1/\log U$ and $s\log(c_b/s)\to0$ as $s\downarrow0$. The extra factor $\log(3+2L/\log 2)$ also has logarithm $o(U)$. Hence $\log|\log(u/v)|>-L^{o(1)}$. On the other hand $0<\log(u/v)\le(u-v)/v\le L^a/x$, giving an upper bound $-L+a\log L$. This is a contradiction. [C. L. Stewart, *On sequences of integers with small prime factors*, Lemma 3, p. 3](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/on_sequences-2.pdf)

## Retaining one original divisor at every other position

Fix a nonempty set $S$ of target positions. At each $j\notin S$ choose one prime $q_j\mid n_j$, and put $M=\prod_{q\in\{q_j:j\notin S\}}q$, with empty product 1. Every displacement divisible by $M$ preserves the chosen divisibilities. For sufficiently large positive displacements these divisors are proper, even if an original $n_j$ was prime.

There is such a choice with $M$ coprime to every target value if and only if

$$\operatorname{rad}(n_j)\nmid\prod_{i\in S}n_i\qquad(j\notin S).$$

Indeed, this says precisely that each position outside $S$ has an available prime divisor dividing no target. Choices can be made separately and the same divisor can be used more than once. If position $j$ obstructs the choice, each prime in its radical divides some difference $j-i$, so

$$\operatorname{rad}(n_j)\mid\prod_{i\in S}|j-i|\le h^{|S|}.$$

For any fixed $k$, the spacing lemma now gives at most one index $e$ with $\operatorname{rad}(n_e)\le h^k$ once $x$ is large. This uses fixed powers of $L$ bounding both $h$ and $h^k$. The same exceptional index works simultaneously for every $S$ with $1\le |S|\le k$.

**One target.** Apply this with $k=1$. If there is no $e$, every target qualifies. If $e$ exists, put $R=\operatorname{rad}(n_e)$. Target $e$ qualifies, and the blocked targets are exactly $i\ne e$ with $i\equiv e\pmod R$, since $R\mid n_e$. Their number is

$$\left\lfloor\frac{e-1}{R}\right\rfloor+\left\lfloor\frac{h-e}{R}\right\rfloor\le\left\lfloor\frac{h-1}{2}\right\rfloor.$$

At each qualifying target, Dirichlet's theorem gives infinitely many primes $n_i+tM$ with $t>0$. Every other position in the same translate is composite for all sufficiently large $t$. At a blocked target the prime chosen at $e$ always divides the translated target as well. With $x=2^v-1$ and $v$ sufficiently large, $e=1$ and $R=2$, attaining the upper bound on blocked sites. This sharpness example concerns arbitrary starts.

**Several targets.** Fix $m\ge2$ and then $k\ge k_m$ as in the Maynard–Tao theorem. If the exceptional $e$ for $h^k$ exists, choose one prime $p_*\mid n_e$. Take as the target pool all sites coprime to every prime $p\le k$ and also to $p_*$ when present. Its size is $\gg_k h$ uniformly in $x$ and $p_*$, by inclusion–exclusion with rounding error at most $2^{\pi(k)+1}$ and density at least $\tfrac12\prod_{p\le k}(1-1/p)$. For every $k$-subset $S$ in this pool, $p_*$ is available at $e$ if needed, and every other site outside $S$ has an available divisor by the criterion. Choose $M$ accordingly. To check admissibility of the shifts $\{n_i:i\in S\}$, observe that for each $p\le k$ the residue zero is missing, and for $p>k$ there are too few shifts to cover all residues. Also $M$ is coprime to their product. Theorem 1 of Banks, Freiberg and Turnage-Butterbaugh, with $g=M$, now gives a fixed $m$-subset whose translated entries are consecutive primes for infinitely many $t$. Every prime in each sufficiently large such window lies in $S$. The theorem makes no assertion that all $k$ targets are prime. [*Consecutive primes in tuples*, Theorem 1](https://arxiv.org/pdf/1311.7003)

## What survives inside the original interval

Fix $A>0$. Set $L=\log x$, $z=\tfrac12\sqrt C\,L\log L$ and $Y=\lfloor z^2/(\log z)^2\rfloor\sim h/4$. For every sufficiently large $x$ and every integer $0<|D|\le x^A$, the number of sites in the original interval such that $n_i$ has no prime divisor at most $z$, is coprime to $D$, and is not a proper power is

$$\gg_C \frac{h\log\log L}{(\log L)^2}.$$

The threshold in $x$ can depend on $A,C$. To see this, take the forbidden residue $-x\bmod p$ for every prime $p\le z$ in Theorem 1.2 of the OpenAI Jacobsthal preprint. In the first $Y$ sites it leaves $\gg Y\log\log z/(\log z)^2$ survivors. This is the theorem's $YV_0/B^2$ bound, with $w=\log z/(\log\log z)^2$, $V_0\asymp1/\log w$ and $B=\log z/\log w$. At most $AL/\log z$ primes above $z$ divide $D$. Each removes at most $Y/z+1$ sites, a total of $O_{A,C}(h/(\log L)^2)$. The first lower bound dominates by a factor tending to infinity. Finally, for each integer exponent $d\ge2$ consecutive $d$th powers near $x$ have spacing at least of order $\sqrt{x}$, since $(a+1)^d-a^d\ge d a^{d-1}$ for $a^d\ge x$. At most one lies in the interval for each $d\le\log(x+h)/\log 2$, so removing all proper powers costs $O(L)$ sites. [OpenAI, *A quadratic bound for Jacobsthal's function*, Theorem 1.2](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf)

Since $\gcd(n_i,n_i+D)=\gcd(n_i,D)$, each of these sites loses **every** original prime divisor under that displacement. Thus no nonzero shift bounded by a fixed power of $x$ can preserve one divisor at every site outside a fixed number of targets. The exact-window survivors could all be composites with at least two distinct prime factors above $z$. Ruling this out at every start is the missing step.

## Can a uniform bound on surviving composites close the gap?

Already with $D=1$, arbitrarily far out there are original windows containing $\gg_C h/\log L$ qualifying **composites**. This exceeds the order of the guaranteed survivor count by a factor of order $\log L/\log\log L$. Thus one cannot finish by subtracting a uniform upper bound for the composites from that lower bound.

Here is an elementary average giving the obstruction. On $[X,2X]$ use the common cutoff $Z=\tfrac12\sqrt C\log(2X)\log\log(2X)$, which dominates all local cutoffs. Put $\lambda=\sum_{p\le Z}1/p$ and let $J$ be the first odd integer at least $10e(1+\lambda)$. Odd Bonferroni truncation gives a lower bound for the number of integers avoiding all primes through $Z$. Each intersection has count $X/\prod p+O(1)$. The total rounding error is $O((2Z)^{J+1})=X^{o(1)}$ since $J=O(\log\log Z)$. The corresponding truncated sum of densities differs from $\prod_{p\le Z}(1-1/p)$ by at most $\sum_{j>J}\lambda^j/j!=o(1/\log Z)$ by the choice of $J$ and Mertens' theorem. Thus $\gg X/\log Z$ integers survive. Removing all primes costs $O(X/\log X)$, and removing all proper powers costs $O(\sqrt X\log X)$. Both are negligible.

Partition into intervals of length $\lfloor C(\log X)^2\rfloor$, discarding the last incomplete interval. One full interval contains $\gg_C (\log X)^2/\log Z$ surviving composites. Extending its right endpoint to the locally prescribed length $h$ can only increase the count. A proof by subtraction would therefore have to compare the two counts at the *same* start with finer accuracy.

For a finite example, $114,\ldots,125$ are all composite. The position occupied by $121$ becomes the sole prime, $331$, after shifting by $210$. Every other entry retains a divisor among $2,3,5,7$. The prime at the translated position makes no assertion about primality of $121$. [Reproducible checks](check-divisor-translates.py)

The spacing estimate is an application of a linear-forms bound, the primes in the translates come from Dirichlet and Banks–Freiberg–Turnage-Butterbaugh, and the fixed-window count uses the cited sieve theorem. The classification records what follows when the divisors must come from the starting interval. Independent priority for these deductions is unverified. Cramér's conjecture remains open.
