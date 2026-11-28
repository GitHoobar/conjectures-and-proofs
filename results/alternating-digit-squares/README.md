# Arbitrarily long runs in OEIS A345680

**Theorem.** For every positive integer $L$, there exist $L$ consecutive nonnegative integers each of which eventually reaches zero under the following operation. Square the decimal digits, take their alternating sum, and take the absolute value. For example, $7\mapsto49\mapsto65\mapsto11\mapsto0$. The starting point and the number of steps can depend on the run length, and different members of a run can take different numbers of steps.

Stephen Cross recorded the conjecture in 2021 and credited students at Clifton College with the initial study. The entry gives examples and an infinite family obtained by concatenating two-digit multiples of eleven. GitHoobar, working with OpenAI Codex, gives the proof below. The Lean statement was written independently by **rpabani**. [OEIS A345680](https://oeis.org/A345680) · [LeftToSolve](https://lefttosolve.com/p/oeis-a345680) · [rpabani’s statement](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/13603)

## Moving a whole set of starting values

Let $D(n)$ be the signed sum, with the units digit positive, and put $F(n)=|D(n)|$. Call a finite set $S$ **good** if some translate $k+S$ consists entirely of integers that reach zero. The singleton $\{0\}$ is good.

Appending an even number of decimal digits preserves the signs of all the preceding digits. Consequently, for $0\le r<100^p$,

$$D(100^p q+r)=D(q)+D(r).$$

Every integer is $D(q)$ for some $q$. Appending the two digits 01 increases the value by one, starting from zero. Appending one zero reverses its sign.

Suppose $c\ge0$ and $v$ is an integer such that all values $y=D(x+c)+v$, for $x\in S$, belong to a good set $T$ of nonnegative integers. Choose $k$ witnessing that $T$ is good, then choose $q$ with $D(q)=k+v$. Take $p$ large enough that each $x+c<100^p$. For every $x\in S$, the same translation gives

$$F(100^p q+c+x)=|k+v+D(x+c)|=k+y.$$

Each $k+y$ reaches zero. Thus $S$ is good. This step lets us work backwards from a small set whose behavior we understand.

## A finite certificate and the induction for all lengths

Start with every integer from 0 through 200. Apply the following pairs $(c,v)$ from left to right. Each replaces every current value $x$ by $D(x+c)+v$.

```text
(990,82) (195,77) (19,81) (981,82) (430,65) (739,23)
(833,-1) (148,44) (862,1) (973,10) (869,-77) (21,25)
(11,15) (88,0) (0,1) (5,-25) (0,0)
```

The certificate was found by searching for shifts that reduce the number of distinct values. It is verified by direct evaluation in the Lean kernel. All intermediate results are nonnegative and the final set is $\{0\}$. Reading the certificate backwards proves that $[0,200]$ is good.

For the induction, write $x=100q+r$ with $0\le r<100$. The last two digits contribute at most 81 in absolute value. Also $|D(q)|\le9q$, since each decimal digit $d$ satisfies $d^2\le9d$ and the sum of the digits is at most $q$. For $0\le x\le n$ this gives

$$|D(x)|\le B(n),\qquad B(n)=9\lfloor n/100\rfloor+81.$$

If $n\ge201$, then $2B(n)<n$ (already $0.18n+162<n$). The single pair $(0,B(n))$ sends every offset in $[0,n]$ into $[0,2B(n)]$. The latter interval is good by strong induction. Applying the translation argument proves that $[0,n]$ is good. This proves the conjecture for every run length.

## Verification and attribution

The LeftToSolve checker at revision `2af85d73` accepted `OMA.solution` against the exact statement from rpabani’s PR, with Lean 4.33.1 and the pinned Mathlib environment. The axiom report contains only `propext`, `Classical.choice`, and `Quot.sound`. The statement file contains the original open problem as a placeholder. The axiom audit establishes that the proof does not depend on that placeholder. [Lean proof](Proof.lean) · [Checker verdict](verdict.json) · [Pinned statement](https://github.com/rpabani/open-math-agents/blob/e793ecba1edeb34ade053096959185eb3fae1809/statements/oeis-a345680.lean)

To replay the proof and axiom check with the pinned Formal Conjectures checkout described in the repository verification guide, run the following from the collection root. The script fetches the statement at its exact revision and builds in a temporary directory. [Verification environment](../../VERIFYING.md#lean)

```sh
bash results/alternating-digit-squares/verify.sh /path/to/formal-conjectures
```

As of November 28, 2026, the OEIS entry still called the assertion a conjecture. Our searches of the entry, the literature on consecutive happy numbers, public Lean code, and LeftToSolve submissions turned up the proposed statement and no earlier proof of this exact assertion. Hao Pan’s consecutive-happy-number theorem concerns an unsigned sum of digit powers reaching one. Here the signs depend on position and the target is zero. The search supports attribution of this proof to GitHoobar. It cannot establish absolute publication priority. [Cross’s entry](https://oeis.org/A345680) · [Pan, *On consecutive happy numbers*](https://arxiv.org/abs/math/0607213)
