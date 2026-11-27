# A test against the published extended pair-correlation conjecture

GitHoobar · 27 November 2026 · Working research note developed with OpenAI Codex

Could an existing conjecture about the zeta zeros supply the bound in [the single-window argument](deepest-deficit.md)? Languasco, Perelli and Zaccagnini (LPZ) study the precise quantity
$$
\mathcal F(Y,t,\tau)=
\sum_{|\gamma|,|\gamma'|\le t}Y^{i(\gamma-\gamma')}
\frac{4}{4+\tau^2(\gamma-\gamma')^2}.
$$
Their conjecture gives an asymptotic for $\tau\ge\min(Y,t)^{-1+\nu}$ for fixed $\nu>0$ and comparable logarithms of $Y,t$. They explicitly identify Maier's oscillations as a reason to restrict this range. Heath-Brown had earlier obtained bounds for individual prime gaps under RH and a hypothesis on the classical pair function. This establishes direct prior art for the research strategy. [LPZ, conjecture and Remark 4](https://arxiv.org/pdf/1311.0597) · [Heath-Brown, Corollary 2](https://matwbn.icm.edu.pl/ksiazki/aa/aa41/aa4118.pdf)

**Deduction under RH.** Fix $C>0$ and $0<\xi<1/6$. At arbitrarily large integer starts $x$, set $h=\lceil C(\log x)^2\rceil$, $Y=\sqrt{x(x+h)}$. There is a $\tau\asymp h/Y$ and a real height
$$Y^{5/6-\xi}\le t\le Y^{1+\xi}$$
for which
$$
\frac{\mathcal F(Y,t,\tau)}{t\log(2t)}\gg C\log Y.
\tag{1}
$$
The local averaging width $\tau$ is below the published conjecture's range for every such $t$ and every fixed $0<\nu<1$, since $\tau\ll_C(\log Y)^2/Y=o(Y^{-1+\nu})$. Thus merely extending its usual order of magnitude down to the width needed here already fails on known deficient windows. The result quantifies the Maier obstruction discussed by LPZ. We have not established priority for (1).

**The arithmetic side.** Use the [Maier deduction](aligned-windows.md) to choose starts with at most $(1-\epsilon)h/\log x$ primes, with fixed $\epsilon>0$. Fix $0<\lambda<\epsilon/16$ and take
$$\delta=\frac{\log(1+h/x)}{2(1+\lambda)},\qquad \tau=\lambda\delta.$$
Choose an even smooth function $f$ with compact support in $(-1,1)$, $0\le f\le1$, and $m=\int f>2-\epsilon/4$. Write $g(u)=\int f(w)e^{iuw}\,dw$. The function $g$ is real and even, and $g$ and its derivatives decay faster than every inverse power.

For $|v|\le\tau$ put $z=Ye^v$. Weight each integer $n$ by $f(w)e^{-\delta w/2}$, where $w=\log(n/z)/\delta$. The support fits within the deficient parent. Its von Mangoldt mass is at most $(1-\epsilon+o(1))h$, since the prime weights are at most $(1+o(1))\log(x+h)$ and the [proper-power contribution](deepest-deficit.md) is $o(h)$. The smooth explicit formula under RH gives
$$
\sum_n\Lambda(n) f(w)e^{-\delta w/2}
=\delta z\int f(u)e^{\delta u/2}du
-\delta\sqrt z\, S(v)+O(\delta/x^2),\qquad
S(v)=\sum_\gamma (Ye^v)^{i\gamma}g(\delta\gamma).
$$
Indeed the factor $e^{-\delta w/2}$ cancels the real part of each zero in the transform. The trivial zeros give the stated error by summing $(ze^{-\delta})^{-2j}$. The support endpoints have zero weight. Since $\delta z\sim h/(2(1+\lambda))$ and $m-2(1+\lambda)(1-\epsilon)>0$, this proves $S(v)\gg\sqrt Y$ throughout $|v|\le\tau$.

**The zero side.** Give $v$ the probability density $e^{-2|v|/\tau}/\tau$ on the real line. The preceding interval has probability $1-e^{-2}$, so $\|S\|_2\gg\sqrt Y$. The characteristic function of this density is $4/(4+\tau^2 u^2)$. Consequently the truncated sum $B_t(v)=\sum_{|\gamma|\le t}(Ye^v)^{i\gamma}$ satisfies $\|B_t\|_2^2=\mathcal F(Y,t,\tau)$ exactly.

Partial summation using the evenness and rapid decay of $g$ gives $S(v)=-\int_0^\infty g'(u)B_{u/\delta}(v)\,du$. The trivial bound $|B_t|\ll t\log(2+t)$ suffices at the ends. For $t_- =Y^{5/6-\xi}$, the contribution from $u\le\delta t_-$ is $O(\delta^2 t_-^3\log Y)=o(\sqrt Y)$ since $g'(u)=O(u)$ near zero. For $t_+=Y^{1+\xi}$, the contribution from $u\ge\delta t_+$ is $O_N(\delta^{-1}(\delta t_+)^{2-N}\log Y)=o(\sqrt Y)$ upon choosing $N>2+1/\xi$. These estimates hold uniformly in $v$.

On the remaining range put $Q=\sup_{t_-\le t\le t_+}\mathcal F(Y,t,\tau)/(t\log(2t))$. The triangle inequality for the integral in $L^2$ bounds its norm by
$$
\sqrt{Q\log(2t_+)/\delta}\ \int_0^\infty |g'(u)|\sqrt u\,du.
$$
Comparison with $\|S\|_2\gg\sqrt Y$ gives $Q\gg Y\delta/\log Y\asymp C\log Y$. Taking a height attaining at least half this supremum proves (1).

## A narrower height range for the deepest deficits

Under RH, suppose a particular parent interval is empty, or along a sequence its prime weight is $o(h)$. For every fixed $0<\xi<1/6$, (1) must then occur at a height in the narrower band
$$Y^{1-\xi}\le t\le Y^{1+\xi}.$$
This time the lower bound concerns the center of **that parent**, with constants allowed to depend on $\xi$. A signed filter can isolate this band because all prime contributions in the parent vanish or are small even in absolute value.

To construct it, take a real even smooth bump $\phi$ supported in $(-1,1)$ with integral one. Its transform $g_0$ is even with $g_0(0)=1$. Let $P$ be the degree-$2k$ Taylor polynomial of $1/g_0$ at zero. Then $g=P g_0$ is the transform of a real even smooth $f$ with the same support bound, since multiplication by $u^{2j}$ transforms $(-1)^j\phi^{(2j)}$. We have $g(0)=1$ and $g'(u)=O_k(|u|^{2k+1})$ near zero. With $k$ fixed in terms of $\xi$, the von Mangoldt mass in absolute value is bounded by $(1+o(1))\|f\|_\infty$ times the total prime and proper-power weight in the parent. This is $o(h)$ under the stated deficit assumption. The pole now gives $S(v)=(1+o(1))\sqrt Y$ on $|v|\le\tau$.

For $t_-=Y^{1-\xi}$ the discarded low integral is
$$
O_k(\delta^{2k+2}t_-^{2k+3}\log Y)
=O_{k,C}\bigl((\log Y)^{4k+5}Y^{1-(2k+3)\xi}\bigr).
$$
Choosing $(2k+3)\xi>1/2$ makes it $o(\sqrt Y)$. The upper tail and the remaining norm estimate are as before. This signed filter uses the stronger deficit assumption. A fixed small fractional shortfall of Maier's size does not bound a signed weight with a possibly large supremum norm in the same way.

**Keeping the height below the earlier zero cutoff.** For an empty or $o(h)$ parent we can further take $t\ll_C Y/\log Y$, so the resulting range is $[Y^{1-\xi},O_C(Y/\log Y)]$. Choose the base bump $\phi\ge0$ supported in $(-1/2,1/2)$ and first convolve it with $K=\lceil8\log Y\rceil$ uniform probability densities on $[-b/K,b/K]$, with $b=1/4$. Its new transform is $g_{0,K}(u)=g_0(u)r(u)^K$, $r(u)=\sin(bu/K)/(bu/K)$. Form $P_K$ from the reciprocal Taylor polynomial as before. The convolved bump has mass one and support in $[-3/4,3/4]$. Its moments through every fixed order are uniformly bounded, so the reciprocal Taylor coefficients through order $2k$ are bounded independently of $K$. Applying the resulting differential operator to $\phi$ before convolution also bounds the physical filter's supremum norm uniformly in $K$.

For $g=P_Kg_{0,K}$, the low Taylor bound stays uniform by the bounded support and supremum norm. The rapid decay of $g_0$ and $g_0'$ gives $|g'(u)|\ll_{N,k}(1+|u|)^{-N}$ uniformly, because $|r|\le1$ and $|r'|\le b/K$ from the uniform density's transform. Moreover, for $u\ge4K/b$ each derivative term retains at least $K-1$ factors of $r$, where $|r|\le1/4$. The same bound on $g'$ gains a factor $4^{1-K}$ there. Consequently the tail starting at $t_+=4K/(b\delta)$ has norm $\ll_k 4^{1-K}\delta^{-1}\log Y=o(\sqrt Y)$. This proves the sharper upper cutoff with the same lower height and the same logarithmic excess in (1).

Could the same argument use a width $\tau'$ *inside* the published conjecture's range? For $\tau'\ge\tau$, the Laplace probability of the shifts controlled by this parent is $1-e^{-2\tau/\tau'}\asymp\tau/\tau'$. Using only those shifts reduces our forced lower bound for $Q$ by this factor. At $\tau'\ge Y^{-1+\nu}$ the quantity $C\log Y\cdot(\tau/\tau')$ that this argument forces is at most $O_C((\log Y)^3/Y^\nu)$ and tends to zero. This transfer loses the information about the individual window before reaching the conjectured range.

The proof uses actual deficient intervals, which can contain primes. To prove a prime at the deepest deficit, an upper bound would have to allow excursions of the size in (1) while still excluding vacancy. Neither the published conjecture in its stated range nor this deduction supplies that upper bound.
