# How far do low prime counts line up?

GitHoobar · 27 November 2026 · Research note developed with OpenAI Codex and three Luna agents

Write $Y_x(h)=\pi(x+h)-\pi(x)$. For integer starts, $k$ consecutive empty length-$h$ windows are exactly one empty interval of length $h+k-1$. We looked for a pointwise bound that could exclude this event for $h$ a constant times $(\log x)^2$. We found that **fixed fractional deficits in actual prime counts do line up**, even across several window lengths at once. We can guarantee primes in some runs of deficient windows. The sparse interval producing the longest deficit need not be one of those runs. A [separate pointwise test](finite-zero-test.md) identifies what still has to be bounded at its actual location.

## Simultaneous deficits in actual primes

There are absolute constants $\epsilon,c>0$ and arbitrarily large integers $X$ with the following property. Put $L=\log X$ and $R=\lfloor L^3\rfloor$. There are at least $cR$ integer starts $s$ in $[X,X+R)$ such that, **simultaneously** for every positive integer $h\le cR$ and every integer $0\le v\le\epsilon h$,
$$Y_{s+v}(h)\le(1-\epsilon)h/L.$$
At $h=\lceil C L^2\rceil$ this gives a run of order $h$ consecutive starts, all deficient by the same fixed fraction of the usual count. The same choice of $X$ and $s$ works for every length in range.

**Proof.** Maier's short-interval theorem with exponent three supplies arbitrarily large $X$ for which $Y_X(R)\le(1-4\epsilon)R/L$ for some fixed $0<\epsilon<1/10$. Passing from real endpoints to these integer endpoints costs $O(1)$, absorbed by choosing $\epsilon$ smaller. This low total is Maier's result. [Maier, *Primes in short intervals*](https://doi.org/10.1307/mmj/1029003189)

For $0\le j\le R$, set $F(j)=Y_X(j)-dj$, $d=(1-2\epsilon)/L$, and $M(j)=\max_{j\le i\le R}F(i)$. Since $M(0)\ge0$ and $M(R)\le-2\epsilon R/L$, these suffix maxima fall by at least $2\epsilon R/L$ in total. Each strict drop at $j$ requires $F(j)=M(j)$, and its size is at most $d$, because $F(j+1)\ge F(j)-d$. There are therefore at least $2\epsilon R/(1-2\epsilon)$ distinct drop positions. Discarding the last $\lceil\epsilon R\rceil$ indices still leaves at least $cR$, with $c=\epsilon/4$ for all large $X$.

At each retained $s=X+j$, every prefix of the remaining interval satisfies $Y_s(u)\le du$. Nonnegativity gives $Y_{s+v}(h)\le Y_s(h+v)\le d(h+v)$ whenever $h+v\le R-j$. Our ranges ensure this and $(1-2\epsilon)(1+\epsilon)\le1-\epsilon$. This proves the assertion. The count $cR$ concerns distinct starts, whose associated runs may overlap.

## A run where the deficient windows share actual primes

For each fixed $C>0$ and arbitrarily large $X$, put $h=\lceil C L^2\rceil$ and $\mu=h/L$. There is a start $s\in[X,2X]$ and an integer $k\gg_C L\log L$ such that all windows $(s+v,s+v+h]$, $0\le v\le k$, contain at most $(1-\epsilon/2)\mu$ primes. Their **common intersection** contains at least $\mu/2$ primes. The run here can be elsewhere in the shell than the run in the first theorem.

**Proof.** At a retained start $u$ in the preceding proof use $v=0$, which gives the stronger bound $Y_u(h)\le(1-2\epsilon)\mu$. There also exists $t\in[X,2X]$ with $Y_t(h)\ge(1-\epsilon/4)\mu$. Indeed, averaging over that shell counts each prime between $X+h$ and $2X$ exactly $h$ times and the prime number theorem gives a mean at least $(1-o(1))\mu$. Since $|Y_{x+1}(h)-Y_x(h)|\le1$, walking between $u$ and $t$ attains $\lfloor(1-\epsilon)\mu\rfloor$ at some $s$.

Choose $k=\lfloor\kappa\mu\log\mu\rfloor$ with $\kappa>0$ sufficiently small in terms of $\epsilon$. The uniform Brun–Titchmarsh bound for an interval of length $k$ is $O(k/\log k)$. Thus the intervals $(s,s+k]$ and $(s+h,s+h+k]$ each contain at most $\epsilon\mu/4$ primes for large $X$. Removing the former leaves at least $\mu/2$ in $(s+k,s+h]$, common to every window. Adding the latter keeps every count below $(1-\epsilon/2)\mu$. This proves the claim. At $k$ proportional to $h$, the same upper sieve gives only $O(h/\log h)$, too large compared with $h/L$. [Montgomery and Vaughan, *The large sieve*](https://doi.org/10.1112/S0025579300004708)

## Why the minimum is still open

The first theorem gives a persistent upper bound, which permits zero. The second uses a crossing between a low count and a higher count. It locates primes inside windows at the crossing and leaves the minimum count undetermined. In particular this argument cannot place a prime at a prescribed start just because it belongs to the first run.

We also tried using the largest prime divisor of $\binom{x+h}{h}$. For integers $x>h$, that divisor exceeds $x$ exactly when $(x,x+h]$ contains a prime. Any prime factor above $x$ must equal one of the numerator terms since $x+h<2x$, and the denominator has none. The classical Sylvester–Schur bound gives a divisor above $h$, which leaves the entire range from $h$ to $x$ unresolved. [Ecklund, *On prime divisors of the binomial coefficient*](https://msp.org/pjm/1969/29-2/pjm-v29-n2-p04-p.pdf)

The suffix-max argument and the crossing argument are elementary deductions from the cited theorems. We have not established priority for the formulations here. The finite checks verify the combinatorial steps and interval endpoints. [Exact checks](check-alignment.py) · [Finite-height test for a prime at a specified start](finite-zero-test.md)
