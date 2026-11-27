# Rough numbers in intervals of square-logarithmic length

GitHoobar · 27 November 2026 · Working manuscript developed with OpenAI Codex and Luna agents

Write $P^-(n)$ for the least prime divisor of $n>1$. How often can primes up to a given cutoff collectively divide **every** integer in a short interval? We give a bound on the number of integer starts for which this happens, including starts in an incomplete period of the sieve.

**Theorem.** Fix $0<b<1$. For an integer $X$ put

$$L=\log X,\qquad H=\lceil L^2\rceil,\qquad z=\exp(L^b),\qquad M=\frac{L^{1-b}}{\log L}.$$

There exist positive constants $c,C,a$ such that, for all sufficiently large $X$, all but at most $CX\exp(-cM)$ integers $x\in[X,2X)$ have the following property. The interval $(x,x+H]$ contains at least $cLM$ integers $n$ with $P^-(n)>z$. In addition, there is a block inside it of at most $\lfloor aL\rfloor$ consecutive integers containing at least $cM$ distinct numbers $n$ with $P^-(n)>z$. All logs are natural.

The exceptional proportion decreases faster than any fixed inverse power of $\log X$. The conclusion permits composites with all their factors above $z$. It gives no upper bound of order $\log^2 X$ for prime gaps.

## Choose the offsets before exposing the larger primes

Set $y=aL$ and $W=\prod_{p\le y}p$. We use the theorem on p. 226 of Iwaniec's *On the problem of Jacobsthal*. For $k>1$ distinct primes of product $W$, an interval of length at least an absolute constant times $k^2\log k\prod_{p\mid W}(1-1/p)^{-1}$ contains at least $k^2$ integers coprime to $W$. For the primes up to $y$, the prime number theorem and Mertens' product formula bound this length by an absolute constant times $y^2$. Fix $a>0$ small enough that $H$ exceeds this length and $W\le X^{1/8}$ for all sufficiently large $X$. The second condition uses $\log W\sim y$. [Iwaniec, printed p. 226](https://doi.org/10.1515/dema-1978-0121)

For each residue of $x$ modulo $W$, at least $\pi(y)^2$ offsets $i\in\{1,\ldots,H\}$ have $(x+i,W)=1$. Partition the offsets into consecutive blocks of size $\lfloor y\rfloor$, with a possibly shorter final block. Some block contains at least

$$\frac{\pi(y)^2}{\lceil H/\lfloor y\rfloor\rceil}\gg_a \frac{L}{(\log L)^2}$$

eligible offsets. We can use offsets from the whole interval. Put $m=\lfloor\kappa L/(\log L)^2\rfloor$ and split the eligible offsets of each block, in increasing order, into groups of $m$, discarding its last incomplete group. If $G$ is the total number of complete groups, then
$$G\ge \frac{\pi(y)^2}{m}-\left\lceil\frac H{\lfloor y\rfloor}\right\rceil\gg_a L.$$
Indeed the first term is asymptotic to $(a^2/\kappa)L$ and the second to $L/a$. Choose $\kappa$ sufficiently small in terms of $a$. Group membership depends only on $x\bmod W$. Fix a residue and any one complete group for now. The possible $x$ form a progression $x_0+Wt$ on $T\ge\lfloor X/W\rfloor$ consecutive integer values of $t$. The offsets in that group are distinct modulo every prime $y<p\le z$, since their differences have absolute value less than $y$.

## Count survivors over a complete period

First take $t$ uniformly modulo the product of the primes $y<p\le z$. By the Chinese remainder theorem, each such prime independently hits each particular selected offset with probability $1/p$ and hits at most one of them. A hit means $p\mid x_0+Wt+i$. Let $U$ count offsets hit by none of these primes. Set

$$v=\prod_{y<p\le z}(1-1/p),\qquad \mu=mv,\qquad \lambda=\sum_{y<p\le z}1/p.$$

Mertens' formulas give $v\sim\log y/\log z$, $\mu\sim\kappa M$, and $\lambda\le2\log L$ eventually. For any $s$ specified offsets the probability that all survive is $\prod_{y<p\le z}(1-s/p)\le v^s$. Consequently $\mathbb E_{\rm full}\binom Us\le\binom ms v^s$.

We also need $\mathbb E_{\rm full}2^{-U}\le(1-v/2)^m$. For a set of offsets, the probability that all are hit is at most the product of their hit probabilities. To see this, condition on one offset $i$ being unhit. Independently for each prime that landed on $i$, redraw its outcome conditional on avoiding $i$, retaining every other outcome. This produces the conditional law and preserves all existing hits on other offsets. The probability that a specified list of other offsets are all hit therefore increases weakly under the conditioning. Subtracting the joint event with $i$ unhit shows that adjoining the requirement that $i$ be hit costs a factor at most $1-v$. Induct on the list size. Now expand the product $\prod_i(1+\mathbf1_{\{i\text{ hit}\}})/2^m=2^{-U}$ and apply the bound to each nonnegative term. In particular $\mathbb E_{\rm full}2^{-U}\le e^{-\mu/2}$.

## Transfer to the actual starts

Let $R$ be the smallest even integer at least $8\mu$. Eventually $R+1\le m$. We first compare the survival probability of any fixed $s$ offsets, $1\le s\le R$, on our progression of $T$ starts and on the full period. Let $D_t$ count the primes hitting one of these $s$ offsets. The two successive Bonferroni sums of orders $J$ and $J+1$ for $\mathbf1_{\{D_t=0\}}$ bracket it pointwise, where $J=\lceil100R\log L\rceil$.

For $j$ specified distinct primes there are exactly $s^j$ hitting residue classes modulo their product. Each class has frequency within $1/T$ of its full-period value over any $T$ consecutive values of $t$. If $N$ is the number of sieving primes between $y$ and $z$, then either truncated sum has expectation differing between the two laws by at most

$$\frac1T\sum_{j=0}^{J+1}\binom Nj s^j\le\frac{(2Rz)^{J+2}}{T}.$$

In the full-period law, the distance between the two bracketing expectations is $\mathbb E_{\rm full}\binom{D_t}{J+1}$. Independence across primes bounds this by $(s\lambda)^{J+1}/(J+1)!$, at most $(2e/100)^{J+1}\le e^{-5R\log L}$. This proves a two-sided comparison even though individual terms in the sums have alternating signs.

To bound the prefix error, observe that $(J+2)\log(2Rz)=(800\kappa+o(1))L$ for fixed $b$. Decrease $\kappa$ so that $800\kappa<1/4$, also retaining the pigeonhole bound above. Then $T\ge\lfloor X^{7/8}\rfloor$, and every joint survival probability through order $R$ has error at most

$$\delta=e^{-5R\log L}+X^{-1/2}.$$

Apply inclusion–exclusion a second time. With $B_R(u)=\sum_{s=0}^R(-1/2)^s\binom us$, one has

$$0\le B_R(u)-2^{-u}\le 2^{-(R+1)}\binom u{R+1}.$$

These are the even and odd Bonferroni bounds for choosing no objects when each of $u$ objects is chosen independently with probability $1/2$. The sum of all absolute coefficients of the individual offset events in $B_R(U)$ is at most $\sum_{s=0}^R\binom ms\le(1+m)^R$. By the first comparison,

$$\mathbb E_T 2^{-U}\le \mathbb E_{\rm full}2^{-U}+
  \left(\frac{e\mu}{2(R+1)}\right)^{R+1}+(1+m)^R\delta.$$

The middle term uses the full-period factorial moment proved above. It is $O(e^{-2\mu})$. Eventually $\log(1+m)\le\log L$ and $R\log L=O(L^{1-b})=o(L)$, so the last term is also $O(e^{-2\mu})$. Markov's inequality now gives

$$\Pr_T(U\le\mu/4)\le 2^{\mu/4}\mathbb E_T2^{-U}
  \ll \exp\bigl(-[1/2-(\log2)/4]\mu\bigr).$$

The estimate is uniform over the $G$ groups in each residue class. By linearity of expectation the expected number of groups with $U\le\mu/4$ is $O(G e^{-c_1\mu})$ for an absolute $c_1>0$. Markov's inequality makes the proportion of starts where at least half the groups fail $O(e^{-c_1\mu})$, with no independence assumption between groups. At each remaining start, the disjoint groups contribute at least $G\mu/8\gg LM$ distinct survivors, and any successful group lies in a single block of length at most $\lfloor y\rfloor$. Every survivor was already coprime to $W$. Summing over the disjoint progressions, whose lengths total $X$, proves the theorem.

## What this contributes to the prime-gap investigation

**Cover-product corollary.** At each nonexceptional start, suppose a positive squarefree integer $Q$ has $\gcd(Q,n)>1$ for every $n$ in the window. For each of the $\gg LM$ rough survivors choose a prime divisor common to $n$ and $Q$. These primes exceed $z>H$, so two distinct survivors cannot share one. Hence
$$\log Q\gg LM\log z=\frac{(\log X)^2}{\log\log X}.$$
**Using several cutoffs gives $\log Q\gg(\log X)^2$.** This holds simultaneously for all covers at all but $O(X\exp(-c L^{1/3}/\log L))$ starts. To see the uniformity needed here, set $t=\log z$ and restrict $L^{1/3}\le t\le L^{2/3}$. The same $a,\kappa,m$ and the same groups work throughout. Mertens gives $v=(1+o(1))\log y/t$ uniformly, and $\lambda\le2\log L$. The rounding errors in $R$ are negligible uniformly because $\mu\gg L^{1/3}/\log L$. The estimate $(J+2)\log(2Rz)=(800\kappa+o(1))L$ is also uniform, since $\log(2R)=O(\log L)=o(t)$. Finally $R\log L=O(L^{2/3})$. Thus the argument gives at least $c L^2/(t\log L)$ rough survivors except for a fraction $O(\exp(-c L^{1/3}/\log L))$, with uniform constants.

Take the $t_j=2^j L^{1/3}$ for integers $j\ge0$ up to $t_j\le L^{2/3}$. There are $\asymp\log L$ choices. Their combined exception bound has the asserted form after decreasing $c$. For each remaining start and each cover $Q$, define $F(t)$ to be the number of distinct prime factors of $Q$ exceeding $e^t$. The distinct-divisor argument gives $F(t_j)\gg L^2/(t_j\log L)$. Integrating on the disjoint intervals $(t_j/2,t_j]$ counts at least $\gg L^2/\log L$ per interval. Since $\log Q=\int_0^\infty F(t)\,dt$, summing yields $\log Q\gg L^2$.

Both estimates allow factors equal to the covered integer. The September 2026 Jacobsthal bound also forces a superpolynomial product at every start, with a weaker quantitative estimate. Its consequence for our earlier small-product approach is spelled out separately. [The proposed cover criterion](approaches.md#can-a-small-product-of-divisors-rule-out-a-long-composite-run)

A congruence construction that covers an entire window using only primes up to $z$ must likewise land in the exceptional set. Its upper bound still grows without bound. Also, for each fixed $b<1$, the cutoff $z=X^{o(1)}$ lies below $\sqrt X$. To make this sieve certify primes directly one would need to exclude all possible prime divisors through $\sqrt{2X+H}$. At that cutoff $\mu$ for the selected offsets is of order $1/\log L$ and the growing-order argument disappears. Even a strong count of these rough numbers leaves open whether a particular window contains a prime. [An equivalent criterion using actual primes](vacancy-test.md)

Gafni and Tao study least prime factors between consecutive primes and prove concentration bounds for counts of rough numbers in short intervals. Their Lemma 3.1 uses a fixed moment order. Here we group offsets using the small primes and track growing truncation orders on the actual progression. Matomäki's Theorem 1.1 gives almost all intervals of length $h\log X$ many integers with at most two prime factors and least factor above $X^{1/8}$, with exceptional measure $O(X/h)$ in its stated range. At square-logarithmic length that is $O(X/\log X)$. By the same distinct-divisor argument Matomäki's theorem already implies $\log Q\gg L^2$ with exceptional measure $O(X/\log X)$ at this length. To express her estimate using integer left endpoints, take the ambient parameter to be $2X$ or $4X$ and choose $h$ so that the interval length is the integer $H$. The count is constant on each unit interval of right endpoints. The strength here for this corollary is the smaller exceptional bound. We have not established priority for the precise estimate in this note. The asymptotic argument is a written proof awaiting independent review. [Gafni and Tao](https://arxiv.org/pdf/2508.06463) · [Matomäki](https://arxiv.org/pdf/2012.11565) · [Exact finite checks](check-rough.py)
