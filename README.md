# Conjectures and proofs

Mathematical research by **GitHoobar**, developed with OpenAI Codex. Each entry gives the question, the argument, its relationship to earlier work, and the available checks. These are public research manuscripts awaiting independent mathematical review.

## Start with the signed graphs

Give every edge of a complete graph a plus or minus sign. Count the cycles with negative sign, separately for every length. On **181 vertices**, at least **1,048,576** inequivalent signings have exactly the same list of counts. The construction encodes independent binary choices that can be recovered from the graph. It works at every order from 41 onward. [Read the proof](results/signed-cycle-vectors/multiplicity.md) · [Replay the checks](VERIFYING.md#signed-graphs)

## Results

| Question | Result in this collection | Verification |
|---|---|---|
| [Negative cycle vectors](results/signed-cycle-vectors/) | Proofs of Schaefer and Zaslavsky's dimension and indistinguishable-pair conjectures. An extension gives exponentially many indistinguishable signings. | Lean checks the full-span theorem on edge sets. Exact computations check the construction's finite certificates. |
| [Gaussian large doubling](results/gaussian-doubling/) | For finite-entropy inputs with finite second moments and independent nondegenerate Gaussian noise, equality holds exactly for a Gaussian input with proportional covariance. The paper treats singular noise separately. | [Mathematical proof (PDF)](results/gaussian-doubling/gaussian-doubling-equality.pdf) |
| [Irredundant covering systems](results/covering-systems/irredundant/) | Full covers of the integers, with every class indispensable, can have an arbitrarily negative coprime-triple estimate. | [Manuscript (PDF)](results/covering-systems/irredundant/irredundant-covers.pdf), Lean theorem and exact certificates |
| [Third-order coverage bound](results/covering-systems/third-order/) | A third-order upper bound on coverage by residue classes attached to divisors of an odd period. | [Manuscript (PDF)](results/covering-systems/third-order/third-order-crt.pdf). Lean checks the component identities and the final implication under the normalization described in the note. |
| [Union-family determinant](results/union-determinant/) | The exact power of each variable dividing the determinant is its frequency in the set family. Union closure gives a product formula for the quotient. | Two Lean proofs |

## Open investigations

| Problem | What the work establishes | What remains open |
|---|---|---|
| [Cramér's prime-gap conjecture](investigations/cramer-prime-gaps/) | Two inequalities in a proposed proof fail by unbounded factors. One fails throughout arbitrarily long runs of consecutive prime gaps. We also bound the [exceptional intervals lacking rough numbers](investigations/cramer-prime-gaps/rough-intervals.md) and isolate a [signed sum over zeta zeros at the midpoint of sparse intervals](investigations/cramer-prime-gaps/wide-separations.md). The [sieved model](investigations/cramer-prime-gaps/wheel-threshold.md) has a separate gap threshold. | The uniform upper bound on gaps between consecutive primes. |
| [Erdős–Selfridge odd covering problem](results/covering-systems/) | A fresh-prime repair theorem, a sharp criterion under a separation hypothesis, and a finite decision procedure for one-prime repair. | Existence of a distinct odd cover. The reduction and repair step were [merged](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/5100) [upstream](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/5353). |
| [Hofstadter's product-minus-one set](investigations/hofstadter-modular/) | An exact classification of the residue classes reached for every modulus, and positive lower density in each surviving class. | Existence of the natural density. |
| [Björner's identity-realization question](investigations/bjorner-kl-realization/) | A chord construction for ordinary Kazhdan–Lusztig polynomials and a realization of every target with unequal parameters. | Realization of every target with equal parameters. |
| [Typical signed graphs](results/signed-cycle-vectors/multiplicity.md#why-this-construction-leaves-the-typical-case-question-open) | The block construction gives large families of collisions. Almost every switching-isomorphism type lacks the block that this construction needs. | Whether negative cycle counts distinguish almost all types. |

## Reproducing and citing the work

The verification guide gives the pinned Lean environment, the exact commands, and what each check covers. The research notes credit the original problem posers and prior results. To cite a result, use its manuscript title, GitHoobar, the date on the note, and a permanent GitHub link to that file at the revision you read (press **y** on its GitHub page). [Verification guide](VERIFYING.md)
