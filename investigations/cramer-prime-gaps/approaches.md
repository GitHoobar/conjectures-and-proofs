# Attempts on the full prime-gap bound

GitHoobar · 27 November 2026

The target is a uniform bound $p_{n+1}-p_n=O(\log^2 p_n)$. A disproof requires an infinite sequence on which the ratio to $\log^2 p_n$ tends to infinity. One gap, however large, is consistent with the statement. The constant-one prediction from the independent random model is a stronger question. Baker, Harman and Pintz proved an unconditional bound on the scale $x^{0.525}$. Banks, Ford and Tao study extrema for a random sieve model. [Baker, Harman and Pintz](https://doi.org/10.1112/plms/83.3.532) · [Banks, Ford and Tao](https://doi.org/10.1007/s00222-023-01199-0) · [Granville on Cramér's model](https://dms.umontreal.ca/~andrew/PDF/cramer.pdf)

## Can the gap chains grow fast enough?

The chain theorem used in our [proof audit](README.md) permits arbitrary fixed multiples of $F(P)=\log P\,\log_2 P/\log_3 P$. Try multiplying all offsets by $L$ and choosing successively larger $L$. To violate Cramér, the prime $P$ witnessing the resulting chain would need $L$ to compete with $\log^2 P/F(P)$ (and to exceed that scale by an unbounded factor along the construction). The theorem chooses its subsequence after the offsets have been fixed. For each fixed $L$, the normalized gaps tend to finite constants and all sufficiently late witnesses have gaps $o(\log^2 P)$. A diagonal choice of $L$ would require an upper bound on the first suitable witness as a function of $L$. The theorem cited here supplies no bound with the required dependence. Increasing the number of consecutive gaps also leaves primes between those gaps. [Baker and Freiberg, Theorem 6.4](https://arxiv.org/pdf/1510.08054)

## Can a small product of divisors rule out a long composite run?

Suppose the integers $x+1,\ldots,x+H$ are all composite. Select a proper prime divisor for each and let $Q$ be the product of the distinct selected primes, of which there are $r$. Iwaniec's Jacobsthal bound gives $H\ll r^2\log^2(2r)$, uniformly over the choice of primes. Ordering the factors shows $Q\ge (r+1)!$, so $r\log(2r)\ll\log(2Q)$. Hence
$$H\ll\log^2(2Q).$$
If every run admitted such a cover with $Q\le x^A$ for one absolute constant $A$, this would prove Cramér. Conversely, on a sequence violating Cramér, even the **smallest** admissible $Q$ would have $\log Q/\log x\to\infty$. These are consequences of Iwaniec's bound. [Iwaniec, *On the problem of Jacobsthal*](https://doi.org/10.1515/dema-1978-0121)

A stronger bound in the September 2026 OpenAI preprint gives $H\ll r^2/(\log\log(3r))^2$. At $H=\lceil(\log X)^2\rceil$ this implies $r\gg(\log X)\log\log\log X$ (first use $r\gg\log X$). Therefore $\log Q\gg(\log X)(\log\log X)(\log\log\log X)$ at **every** covered window of that length. In particular a polynomial-size cover cannot certify a prime-free window of this length for arbitrarily large $X$. More generally, a cover $Q\le X^A$ gives $r\log(2r)\ll_A\log X$ and hence $r\ll_A L/\log L$ for $L=\log X$. Inserting this upper bound in the eventually increasing function $r^2/(\log\log(3r))^2$ gives $H\ll_A (L/(\log L\,\log\log L))^2$. Thus the proposed uniform compression would force gaps of order $o(\log^2 X)$. These are direct consequences of the cited Jacobsthal estimate. Our separate almost-all argument gives $\log Q\gg(\log X)^2$ outside a quantified exceptional set. [OpenAI, Theorem 1.1](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) · [Rough-number argument](rough-intervals.md)

We tried taking the least prime factor of every entry. The elementary estimate is only $Q\le(x+H)^{H/2}$ since each chosen divisor is at most $\sqrt{x+H}$. Combining repeated factors can improve this for individual windows. We found no uniform compression to a fixed power of $x$. Conversely, the Chinese remainder theorem constructs a window modulo $Q$ from prescribed residue classes, but gives no guarantee that a positive representative large enough to make all divisors proper also has $\log x=o(\sqrt H)$. This is the missing size estimate in a proposed disproof.

## Can a lower-bound sieve leave one prime?

Let $z=\sqrt{x+H}$ and suppose $x>z$. An entry in the interval with no prime divisor at most $z$ is prime, and all primes in the interval survive. For each squarefree divisor $d$, the exact count of its multiples in the interval is $H/d+O(1)$. A direct absolute-value bound accumulates an error of order as large as the number of divisor weights. Keeping the level $D$ on the order of $H$ gives $\log D/\log z\to0$ at $H=C\log^2 x$. The ordinary dimension-one linear sieve gives no positive lower main term for this parameter at or below 2. This calculation diagnoses the direct use of these errors. Uniform cancellation, additional arithmetic input, or a different argument would be required. [Granville, *Sieving intervals and Siegel zeros*](https://dms.umontreal.ca/~andrew/PDF/SievingSiegel.pdf)

## Can a moment estimate exclude the last empty interval?

For integer $X$, put $H=\lceil C\log^2 X\rceil$ and let $Y_x$ count primes in $(x,x+H]$ for each integer $X\le x<2X$. For even $r$, the number of empty windows satisfies the exact bound
$$\#\{x:Y_x=0\}\ \le\ \sum_{j=0}^{r}(-1)^j\sum_{x=X}^{2X-1}\binom{Y_x}{j}.$$
Indeed, for $y>0$ the truncated alternating sum is $\binom{y-1}{r}$ by Pascal's identity, and at $y=0$ it is 1. An upper bound strictly below 1, uniform for all sufficiently large dyadic $X$, would suffice. Even in an independent Bernoulli model with mean $H/\log X$, the expected truncated sum at fixed even $r\ge2$ grows like $(H/\log X)^r/r!$. The positive top-degree term swamps the empty-window probability.

There is an exact obstruction to using a small number of independent-model moments alone. Take a prime $H<q\le2H$, choose $k$ with $1\le k\le H$, and sample a uniform polynomial over the field of $q$ elements of degree less than $k$. At $H$ distinct coordinates record whether its value lies in a fixed set of size $\lfloor q/\log X\rfloor$. The indicators are $k$-wise independent by polynomial interpolation. Yet the event of a constant polynomial with value outside that set has probability $(1-\lfloor q/\log X\rfloor/q)q^{1-k}$. It gives an empty window. When $k=o(\log X/\log\log X)$ this lower bound is $X^{-o(1)}$, much larger than the $1/X$ scale needed to eliminate a possible exceptional start using its expected count. Arithmetic of actual primes could give information beyond these moments. [Exact finite example](check.py)

### A positive polynomial that detects an empty interval

The alternating sum suggests a sharper attempt. Take $X$ large, $H=\lceil16\log^2 X\rceil$, $r=\lceil\log X\rceil$, $\rho=1/\log X$ and $t=\rho/(1-\rho)$. Define $Q_r(y)$ to be the sum of the coefficients through degree $r$ of
$$(1-w)^y(1+tw)^{H-y}.$$
At zero this equals $K=\sum_{j=0}^r\binom Hj t^j$. The term at $j=r$ is at least $(H\rho/r)^r\ge8^r>X^2$ for large $X$. Here $\binom Hr\ge(H/r)^r$ follows by multiplying $(H-i)/(r-i)\ge H/r$ for $0\le i<r$.

For independent Bernoulli bits of mean $\rho$, write $Y$ for their sum. In the generating product each coordinate contributes $1+wU_i$, with $U_i=-1$ on a hit and $U_i=t$ otherwise. These centered variables satisfy $\mathbb E U_i^2=t$. Distinct squarefree monomials in the $U_i$ are orthogonal, so $\mathbb E[Q_r(Y)^2]=K$ exactly. This is the endpoint reproducing kernel for binomial orthogonal polynomials, expressed by a coefficient formula.

For actual prime counts **one arithmetic estimate would suffice**:
$$\frac1X\sum_{X\le x<2X} Q_r(Y_x)^2\ \le\ X K.$$
Indeed, every empty interval contributes $K^2$ to the sum of squares. The estimate bounds their number by $X^2/K<1$. If it held for every sufficiently large dyadic $X$, Cramér would follow by taking $x=p_n$. This criterion allows a factor $X$ over the independent-model second moment. What is missing is a uniform upper bound for this particular nonnegative polynomial average on actual primes. Its expansion reaches prime tuples of length $2\lceil\log X\rceil$. Replacing individual terms by independent probabilities fails even at two consecutive offsets, which cannot both be prime in these windows. The following script checks the polynomial identity against the exact binomial law for a finite sample of parameters. [Exact check](check.py)

## What can zero locations alone detect?

Here is a test of an attempted explicit-formula proof. Start with all ordinary primes and remove those in $(X_j,X_j+\lfloor\log^3 X_j\rfloor]$, with $X_j=2^{2^j}$ for $j\ge4$. Denote the retained set by $S$. The number of deletions up to $x$ is $O(\log^3(2x))$, by summing a geometric series in $(\log X_j)^3$. Thus $S$ is infinite by the prime number theorem. The gaps of $S$ across the deleted windows have unbounded ratio to the square of the logarithm of their left endpoint. The Chebyshev function counting powers of retained primes differs from the ordinary $\psi(x)$ by $O(\log^4(2x))$, since each deleted prime contributes at most $\log x$ in total.

For $\Re s>1$, the Euler product over $S$ equals
$$\zeta(s)\prod_{p\ \mathrm{deleted}}(1-p^{-s}).$$
For each $\delta>0$, the sum of $p^{-\delta}$ over all deleted primes is bounded by $\sum_j (\log X_j)^3 X_j^{-\delta}<\infty$. Each factor is nonzero in $\Re s>0$ and the product converges locally uniformly there to a nonvanishing holomorphic function. The modified Euler product therefore continues meromorphically to that half-plane with exactly the same zeros and poles, counting multiplicity. So an argument that uses *only* those locations and applies unchanged to these Euler products would predict a false upper bound for $S$. The actual prime Euler product has further structure, including the zeta functional equation and specific coefficients in its logarithmic derivative.

None of these arguments supplies a new uniform upper or lower bound at the Cramér scale. The two unbounded failures in the [companion note](README.md) concern the proposed intermediate inequalities for ordinary primes.
