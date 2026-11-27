# How many joint probabilities force square-logarithmic gaps in a sieved prime model?

GitHoobar · 27 November 2026 · Research note developed with OpenAI Codex

We tried to prove Cramér's conjecture by first removing multiples of small primes, then controlling the joint probabilities at the remaining positions. This note determines the order of information that would suffice in a precise model. At a smaller order two random sets can agree on every observable of that order, both obey the prime number theorem in every fixed reduced progression, and have opposite behavior for their largest gaps. For ordinary primes we give the arithmetic estimate that is still missing. We also prove that tracking individual Hardy–Littlewood tuple predictions with small relative errors fails at a strictly lower order.

## The threshold

Write $X=2^j$ and $L=\log X$. In the integers $[X,2X)$ fix $0<\theta<1$ and put
$$z=L^\theta,\qquad W=\prod_{p\le z}p,\qquad V=\frac{\varphi(W)}W,\qquad \rho=\frac1{VL}.$$
Only integers coprime to $W$ are eligible. In the reference model each eligible position is marked independently with probability $\rho$. The finitely many initial shells with $\rho\ge1$ can be omitted. Mertens' theorem gives $\rho\asymp\log z/L$.

A law **agrees through order $k_j$** if the indicators at every set of at most $k_j$ distinct positions in this shell have exactly their joint reference distribution. Ineligible indicators are always zero. This definition imposes no independence across shells.

**Theorem.** Given any sequence of positive integers $k_j$, every such law almost surely has infinitely many marks and satisfies $b-a=O((\log a)^2)$ for all sufficiently late consecutive marked positions $a<b$, **if and only if**
$$\liminf_{j\to\infty}\frac{k_j}{\log(2^j)}>0.$$
When the liminf is zero, the construction below has unbounded normalized gaps almost surely. Both this law and the reference law can simultaneously satisfy the prime number theorem in every fixed reduced arithmetic progression almost surely.

### The sieve input

In every interval of $h$ consecutive integers, with $h$ between a fixed positive multiple of $L^2$ and $2L^2\log L$, the number $m$ of eligible positions satisfies
$$c_\theta hV\le m\le C_\theta hV$$
for all sufficiently large $X$, uniformly in the start. To see this, apply the dimension-one linear sieve at level $D=h^{1-\eta}$, for a fixed $0<\eta<1-\theta$. The divisibility count for each squarefree $d$ is $h/d+O(1)$. The absolute sum of the remainders through $D$ is $O(D)=o(hV)$. The ratio $\log D/\log z$ tends uniformly to $2(1-\eta)/\theta>2$, so the lower sieve function is strictly positive and the upper sieve function is bounded. The resulting constants need only depend on $\theta$ after choosing $\eta$. [Friedlander and Iwaniec, *Opera de Cribro*, chapter 12](https://doi.org/10.1090/coll/057) · [Granville, §1.2, equations (1) and (2)](https://dms.umontreal.ca/~andrew/PDF/SievingSiegel.pdf)

### Upper bound for all matching laws

If the liminf is positive, choose $d>0$ such that $2r\le k_j$ eventually for $r=\lfloor d L\rfloor$. Use a window of length $h=\lceil C L^2\rceil$ inside the shell. Write $Y$ for its number of marks, $t=\rho/(1-\rho)$, and $Q(y)$ for the sum of coefficients of degrees $0$ through $r$ in $(1-w)^y(1+tw)^{m-y}$. Then
$$Q(0)=K=\sum_{s=0}^r {m\choose s}t^s,\qquad \mathbb E Q(Y)^2=K.$$
For the expectation, assign to each eligible bit the value $-1$ on a hit and $t$ on a miss. Its mean is zero and its second moment is $t$. In the square of the subset expansion, distinct subsets are orthogonal and a subset of size $s$ contributes $t^s$. Every expectation uses at most $2r$ distinct bits, so this proof applies to every matching law.

Now $K\ge(m\rho/r)^r$ and $m\rho\ge c_\theta C L$. Choose the fixed $C$ sufficiently large in terms of $d,\theta$ to make $K\ge X^3$ eventually. Each window is empty with probability at most $1/K$. The union bound over at most $X$ starts gives probability at most $X^{-2}$, summable over the dyadic shells. Borel–Cantelli gives the assertion inside every sufficiently late shell. Its first and last windows also contain marks, bounding gaps across shell boundaries. This argument applies in particular to the fully independent reference law.

### Construction with opposite gaps

We first give a finite interpolation argument. Given $m$ eligible bits, $0<\rho\le1/2$, mean $\mu=m\rho\ge4$, and integer $1\le k\le\mu/4$, one can match every $k$-bit law and give the all-zero event probability at least
$$\delta=\frac1{2(m+1)}\left(\frac{k}{16e\mu}\right)^k.$$

Start with the binomial masses $b_y$. Use the $k+1$ nodes $s_i=\lfloor\mu\rfloor+i$ for $0\le i\le k$. They are positive and at most $m$. Write $\lambda_i$ for the Lagrange coefficient giving evaluation at zero at node $s_i$. For every polynomial $f$ of degree at most $k$, we have $f(0)=\sum_i\lambda_i f(s_i)$. Also
$$|\lambda_i|\le\frac{(\mu+k)^k}{i!(k-i)!}\le(4e\mu/k)^k.$$
The binomial mode is at $s_0$ or $s_0+1$, and $b_{s_0+1}/b_{s_0}\le2$, so $b_{s_0}\ge1/[2(m+1)]$. For $s_0\le y<s_k$ the successive mass ratio is
$$(\mu-\rho y)/((1-\rho)(y+1))\ge1/4,$$
using $y\le5\mu/4$, $y+1\le5\mu/4$ and $\rho\le1/2$. Thus $b_{s_i}\ge 4^{-k}/[2(m+1)]$. Add $\delta$ to $b_0$ and subtract $\delta\lambda_i$ from $b_{s_i}$. All masses stay nonnegative. Interpolation preserves total mass and every moment through degree $k$. Given a sampled count $y$, choose a uniform $y$-element subset of the $m$ positions. The inclusion probability for any $s\le k$ positions equals $\mathbb E\binom Ys/\binom ms=\rho^s$, which gives every mixed pattern by inclusion–exclusion. This proves the finite claim. Lean verifies the polynomial-expectation identity for arbitrary distinct interpolation nodes over any field. The nonnegativity estimate and the infinite construction are proved here in writing. [Lean proof](WheelMoments.lean)

If the liminf is zero, select a subsequence of shells where $g=L/k_j\to\infty$. Set $B=\min(g,\log L)$ and divide each such shell into disjoint full blocks of length $H=\lceil B L^2\rceil$ and one remainder. Use the finite construction independently in each full block with its actual $m$, and use reference marks in the remainder and on other shells. A tuple spanning several blocks has the required joint law by independence across blocks.

Here $\mu\asymp_\theta B L$, so $k_j\le\mu/4$ eventually. Uniformly in the full blocks, $\log(2(m+1))=O(\log L)$ and
$$\log(1/\delta)\le O(\log L)+(L/g)\log(O_\theta(Bg))=o(L).$$
There are $\lfloor X/H\rfloor$ independent blocks. The probability that none is empty is at most $\exp(-\lfloor X/H\rfloor X^{-o(1)})\le\exp(-\sqrt X)$ eventually. Almost surely there is an empty block in every sufficiently late selected shell. Since $B\to\infty$, its length divided by $\log^2(2X)$ tends to infinity. The counting argument below ensures infinitely many marks, so these blocks indeed lie between consecutive marks.

### Prime number theorem in progressions for both examples

Fix $q$ and a reduced class $a\bmod q$. Eventually every prime divisor of $q$ divides $W$. By counting whole periods of $\operatorname{lcm}(W,q)$, in any interval of length $u$ in the shell the expected number of marks in that class is
$$\frac{u}{\varphi(q)L}+O(qW\rho).$$
Indeed the eligible proportion in the class, measured among all integers, is $V/\varphi(q)$ by the Chinese remainder theorem. We have $W=X^{o(1)}$ since $\log W\le z\log z=o(L)$.

In either constructed law, independent blocks have length at most $H_* = \lceil 2L^2\log L\rceil$ (use singleton blocks for independent marks). The sum of their count variances is at most $X H_*$, since a block of length $h$ has variance at most $h^2$. Kolmogorov's maximal inequality bounds the probability that a centered count at any block boundary exceeds $X/L^2$ in absolute value by $H_* L^4/X$. This is summable over dyadic $X$. Within a block the extra error is at most $2H_*$. Borel–Cantelli and the expectation formula therefore give a uniform shell-prefix error $O_q(X/L^2)$ almost surely. Summing the shells and replacing $1/L$ by $1/\log t$ on each one gives
$$\#\{a'\le x : a'\text{ marked},\ a'\equiv a\pmod q\}\sim\frac{\operatorname{Li}(x)}{\varphi(q)}.$$
There are countably many fixed pairs $(a,q)$, so this holds simultaneously.

## Testing the argument on actual primes

Take $x$ uniform among the integer starts in $[X,2X)$ and let $Y_x$ count actual primes in $(x,x+h]$ with $h=\lceil C L^2\rceil$. The prime number theorem gives $\mathbb E Y_x\sim h/L$ by summing over offsets. A genuine two-point estimate also survives: Siebert's prime-pair sieve gives $\mathbb E[Y_x(Y_x-1)]\ll h^2/L^2$. Indeed, for even difference $d$ the number of contributing prime pairs per pair of offsets is $\ll (X/L^2)\prod_{p\mid d,\ p>2}(1+1/(p-2))$. Odd differences contribute nothing for these large primes. The product has bounded average over $d\le h$: expand over odd squarefree divisors and use the convergent product $\prod_{p>2}(1+1/(p(p-2)))$. Summing over the at most $h$ pairs of offsets of each difference gives the estimate. Cauchy–Schwarz now gives $\Pr(Y_x\ge \mathbb E Y_x/2)\gg1$. Thus a positive fraction of actual windows contain at least a constant times $\log X$ primes, by existing results. [Siebert, *Montgomery's weighted sieve for dimension two*](https://doi.org/10.1007/BF01351768)

### Why termwise relative error fails earlier

Fix any $\varepsilon>0$ and put $k=\lceil(1+\varepsilon)L/\log L\rceil$. For each $k$-element set of offsets $T\subseteq\{1,\ldots,h\}$, let $N_T$ count the starts $X\le x<2X$ such that $x+t$ is prime for every $t\in T$. Write $M_T$ for the usual dyadic Hardy–Littlewood main term
$$M_T=\mathfrak S(T)\int_X^{2X}\frac{dt}{(\log t)^k},\qquad
\mathfrak S(T)=\prod_p\frac{1-\nu_p(T)/p}{(1-1/p)^k},$$
where $\nu_p(T)$ counts the residues represented modulo $p$. This is the main term whose range of uniformity is being tested. The usual fixed-tuple conjecture has different quantifiers. [Banks, Ford and Tao, §1](https://arxiv.org/pdf/1908.08613)

**Proposition for ordinary primes.** Uniformly over all these tuples, $0\le M_T\le X^{-\varepsilon+o(1)}$, yet for every sufficiently large $X$ at least one admissible tuple has $N_T\ge1$. In fact the normalized total absolute error tends to its maximum:
$$\frac{\sum_T |N_T-M_T|}{\sum_T(N_T+M_T)}\longrightarrow1.$$

**Proof.** For $p>h$, all $k$ offsets are distinct modulo $p$, and $1-k/p\le(1-1/p)^k$. For $p\le h$, simply bound the numerator by 1. Mertens' product theorem yields $\mathfrak S(T)\le (C_1\log h)^k$ with an absolute $C_1$. Therefore
$$M_T\le X(C_1\log h/L)^k=X^{-\varepsilon+o(1)}$$
as an upper bound, since $h=\lceil C L^2\rceil$. On the other hand $\mathbb E Y_x\sim C L>k$ eventually, so at least one actual window contains $k$ primes. Its offsets form an admissible tuple: for $p\le k$ they miss the residue $-x\bmod p$ because those primes exceed $k$, and for $p>k$ their number is too small to cover every residue.

Set $\eta=\max_T M_T=o(1)$. For each integer count $N_T$, $\min(N_T,M_T)\le\eta N_T$. Consequently the difference between the denominator and numerator in the displayed ratio is at most $2\eta\sum_T N_T$, proving the limit. ∎

Thus termwise matching in relative error, or summing absolute errors relative to the combined mass, breaks down already at order $(1+\varepsilon)\log X/\log\log X$. The model's universal upper bound requires order comparable to $\log X$. The same integrality argument applies to termwise expected counts in the small-prime model for starts and windows within a shell, since each expectation is at most $X\rho^k$. Signed averages and bounds for whole sums remain possible even when these individual predictions are too small to approximate an integer count.

### What an actual-prime upper bound still needs

For the upper-bound argument to eliminate the last empty window, one sufficient estimate on actual primes is
$$\sum_{X\le x<2X}\left(\frac{Q_x(Y_x)}{K_x}\right)^2<1,$$
where the polynomial and its normalization use the eligible count for that start, with the wheel fixed at the shell's $X$. Every prime in the window is eligible for large $X$, including when a window crosses $2X$. Every empty window contributes 1 to the sum. The prime-pair bound controls only degree two in the indicators. We have no bound below 1 for this sum, whose summands have degree up to $2r$. The threshold theorem concerns exact matching to the specified probability law. Other arithmetic information about the primes could bypass it.

## Relation to earlier work

Granville introduced prime models that thin a set sieved by small primes. Banks, Ford and Tao study a different random sieve and derive results about extreme gaps and Hardy–Littlewood correlations. The extremal probability of all-zero bits under limited independence is an established discrete moment problem. Peled, Yadin and Yehudayoff give stronger finite bounds in broad parameter ranges. Our note gives a direct interpolation proof sufficient for this application, the dyadic threshold in the stated sieved model, and the simultaneous progression asymptotics. We have not established independent priority for the threshold. [Granville](https://dms.umontreal.ca/~andrew/PDF/cramer.pdf) · [Banks, Ford and Tao](https://doi.org/10.1007/s00222-023-01199-0) · [Peled, Yadin and Yehudayoff](https://arxiv.org/abs/0801.0059) · [Exact finite checks](check-wheel.py)
