# What low-degree count polynomials see in actual prime intervals

GitHoobar · 27 November 2026 · Research note developed with OpenAI Codex and Luna agents

A possible proof of Cramér's conjecture is to assign a nonnegative weight of one to an empty window and bound the sum of the weights over the shell. An upper bound of order the window length suffices, since a much longer gap produces many consecutive empty windows. We tested whether the square of a polynomial in the prime count could give this upper bound. We obtain a lower bound of $X^{1-o(1)}$ for the contribution of **nonempty windows alone** whenever the degree is $o(\log X)$. The argument concerns actual primes and allows the polynomial to be chosen separately on each block described below. [Vacancy criterion](vacancy-test.md) · [Earlier threshold for a random marking law](wheel-threshold.md)

## Many blocks attain every count in an interval

Fix $C>0$ and $0<\beta<1$. For large $X$ write $L=\log X$, $h=\lceil C L^2\rceil$, $\mu=h/L$, and $Y(t)=\pi(t+h)-\pi(t)$ at integer starts. There are constants $0<a<b<1$ and an integer $Q$ with $L^A=o(Q)$ for every fixed $A$ and $\log Q=O(L^\beta)$, such that the following holds. At least $cX/Q$ disjoint blocks $(mQ,(m+1)Q]\subset[X,2X]$ each contain, for **every** integer $k\in[a\mu,b\mu]$, a full length-$h$ window with exactly $k$ primes. Here $a,b,c$ can depend on the fixed parameters. We use Dirichlet GRH and RH as recorded in the [independent verification](https://math.mit.edu/~drew/grh/).

**Sparse first windows.** Choose a fixed $u>2/\beta$ for which $\rho=e^\gamma\omega(u)<1$, where $\omega$ is Buchstab's function and $\gamma$ is Euler's constant. Such $u$ exist arbitrarily far out by the sign changes of $\omega(u)-e^{-\gamma}$. Put $z=h^{1/u}$ and $Q=\prod_{p\le z}p$. The prime number theorem gives $\log Q\sim z$, with the asserted growth. Write $\alpha=1-\rho$ and $s=\alpha/32$. Work with the consecutive full blocks in $[X,(1+s/4)X]$, of which there are $T\sim sX/(4Q)$. [Maier, *Primes in short intervals*](https://doi.org/10.1307/mmj/1029003189) · [Buchstab estimates and the Maier matrix](https://ford126.web.illinois.edu/Sieve_methods_notes_part8.pdf)

Only columns $i\in[1,h]$ coprime to $Q$ can contain primes at $mQ+i$. Their number satisfies $\Phi(h,z)\sim h\omega(u)/\log z$. For each eligible column the GRH prime number theorem in progressions gives $(1+o(1))TQ/(\varphi(Q)L)$ primes over these rows, uniformly in $i$. Indeed the column spans a fixed positive fraction of $X$, the per-class error in the weighted prime count is $O(\sqrt X\log^2(XQ))$, and $Q=X^{o(1)}$. Partial summation, or simply $\log p=L+O(1)$ throughout, converts to a count. Mertens' product gives $Q/\varphi(Q)\sim e^\gamma\log z$. Multiplying the column count by the number of columns and dividing by $T$ shows that the mean of $Y(mQ)$ is $(1-\alpha+o(1))\mu$. Markov's inequality puts $Y(mQ)\le(1-3\alpha/4)\mu$ in a positive fraction of these blocks. This is the classical Maier mechanism. [Ernvall-Hytönen and Palojärvi, GRH estimates in progressions](https://arxiv.org/abs/2003.01925)

**A larger count in the same block.** All but $o(T)$ of the full blocks contain at least $(1-\alpha/8)Q/L$ primes. Here is the exceptional-set estimate that makes the same-block assertion possible. Set $\delta=(1-s)Q/X$. If a block fails this count, its total $\theta$-mass (sum of $\log p$) is at most $(1-4s+o(1))Q$. For a real start $v$ in its first $sQ/4$ positions, the interval $(v,v+\delta v]$ stays inside the block: its length lies between $(1-s)Q$ and $(1-s)(1+s/4)Q$. Thus the absolute error $|\theta(v+\delta v)-\theta(v)-\delta v|$ is at least $2sQ$ there for large $X$. Selberg's RH estimate bounds the integral of the squared error up to $2X$ by $O(\delta X^2 L^2)$. The disjoint contributions give $O_s(X L^2/Q^2)=o(T)$ failing blocks. [Cully-Hugill and Dudek, Theorem 1](https://arxiv.org/html/2206.00433)

In each remaining block with a sparse first window, partition the block into full length-$h$ windows and a remainder of fewer than $h$ integers. Even counting every remainder integer as prime costs $h=o(Q/L)$. Some full window therefore contains at least $(1-\alpha/4)\mu$ primes. Move the start one integer at a time from the first window to this one. The count changes by at most one at a step, so it attains every integer between the endpoints. Taking $a=1-\alpha/2$ and $b=1-\alpha/3$ proves the assertion.

## Consequence for a vacancy certificate

For each block choose any real or complex polynomial $P_m$ of degree at most $d=o(L)$ and satisfying $P_m(0)=1$. Even if chosen after seeing that block, they satisfy
$$
\sum_{\substack{(t,t+h]\text{ inside a full block }m\\ a\mu\le Y(t)\le b\mu}} |P_m(Y(t))|^2
\ \ge\ c\frac{X}{Q}K^{-2d},
$$
where $K>1$ is fixed. The right-hand side is $X^{1-o(1)}$ since $\log Q=o(L)$ and $d=o(L)$. The lower bound also holds for a single polynomial used on the entire shell.

To prove it, put $A=\lceil a\mu\rceil$, $B=\lfloor b\mu\rfloor$. For $d\ge1$ use $d+1$ nodes $k_i=A+i v$, where $v=\lfloor(B-A)/d\rfloor$. For large $X$, $v\ge c_1\mu/d$ and $B\le b\mu$. In Lagrange interpolation at zero the absolute coefficient of $P_m(k_i)$ is at most
$$
\frac{B^d}{v^d i!(d-i)!}.
$$
The sum of these upper bounds is $(2B/v)^d/d!\le K^d$ by $d!\ge(d/e)^d$. Since $P_m(0)=1$, at least one node has $|P_m(k_i)|\ge K^{-d}$. Degree zero gives the same bound directly. Each of the good blocks attains its selected node. Its witness is distinct from those in all other blocks. This proves the estimate.

This rules out a total squared weight of order $h$ with these degrees. The block adaptation concerns one scalar polynomial shared by the starts of a block. Tests that depend on the identities of the occupied offsets, or that change their polynomial at each start, are outside this argument. Degree comparable to $\log X$ also remains open.

### After conditioning on the small-prime residues

Suppose the polynomial may additionally depend on the start modulo $W$, where $W\mid Q$ and $W\le\sqrt L$. This includes the primorial used in the [individual-prime sampling formula](wheel-sampling.md), since its largest prime is eventually below $z$. Write $J=\varphi(W)$. For $dJ=o(L)$, the same sum of squared weights over nonempty windows is at least $c(X/Q)W K_1^{-2d}$ for a fixed $K_1>1$. Thus recording the full eligibility pattern for this wheel still leaves a degree obstruction, with a weaker degree range.

In each good block and for each residue, shift the low window forward and the high window backward by fewer than $W$ places to reach the required residue. The count changes by at most $J$ in either shift, since any $W$ consecutive integers have exactly $J$ eligible sites and primes in this shell exceed $W$. The low and high starts remain in the correct order: the difference between their original counts is a fixed multiple of $\mu$, whereas starts within $2W$ can differ in count by at most $2J=o(\mu)$. Now walk in steps of $W$. Each count changes by at most $J$. Inside $[a\mu,b\mu]$, choose integer targets as above, leaving a margin $J$ below the upper end. Their spacing $v\asymp\mu/d$ exceeds $2J$ for large $X$ when $d\ge1$. At the first crossing of each target $k_i$, the attained count lies in $[k_i,k_i+J]$. The attained nodes have mutual separation at least $|i-j|v/2$ and stay inside the stated count range. The same interpolation argument, with $v/2$ in the denominator, supplies a witness for that residue's polynomial. Different residues supply distinct starts. Degree zero is immediate. This extension also allows choosing the polynomials separately in every block.

**A check on using higher centered moments.** For each fixed $0<\nu<1$ and $r=\lceil L^\nu\rceil$, the normalized $L^r$ norm of $(\mu-Y(t))_+$ over the shell is comparable to $\mu$. Indeed take $\beta<\nu$ above. At least $cX/Q$ starts have deficit at least $(1-b)\mu$, giving a lower bound $(1-b)\mu(c/Q)^{1/r}$, while $\mu$ bounds every deficit. In particular a uniform estimate of order $\sqrt{r\mu}$ for this one-sided norm fails on ordinary primes. These estimates concern counts bounded away from zero and give no positive lower bound at the deepest window.

The number-theoretic inputs and the interpolation formula are established results. The deductions here concern the multiplicity of exact intermediate counts and their effect on blockwise polynomial tests. No independent priority or formal verification is claimed. [Finite combinatorial checks](check-count-polynomials.py)

## Consequence for cancellation among the zeta zeros

At each start $t$ use the midpoint $m_t$, half-width $\delta_t$ and signed sum $S_{m_t}$ of [equation (4) in the finite-band note](wide-separations.md#a-signed-sum-at-the-midpoint-itself), with the common length $h$ here. Its derivation is uniform for $h\asymp_C\log^2 t$. Choose the minorant there with integral greater than $2-(1-b)/2$. At a witness with $Y(t)\le b\mu$, the normalized prime contribution in that formula is at most $(2b+o(1))L$, since $\log t=L+O(1)$ and $t\delta_t\sim h/2$. The proper powers cost $O_C(\log L)$. Consequently $S_{m_t}\gg\sqrt X$ at at least $cX/Q$ starts at which the window itself contains at least $a\mu$ primes.

For each fixed $0<\nu<1$, taking $\beta<\nu$ again and $r=\lceil L^\nu\rceil$, the positive part of the signed sum therefore has normalized $L^r$ norm at least $c_\nu\sqrt X$. In particular a bound $O(\sqrt{rX/L})$ cannot hold throughout these growing orders for all the fixed filters in question. Here $x/h$ is the order of the upper frequency cutoff; counting zeros at that height gives the independent-phase variance scale $X/L$. The contradiction is with extrapolating this scale to high moments. It leaves open a bound distinguishing complete vacancy from the nonempty windows above.
