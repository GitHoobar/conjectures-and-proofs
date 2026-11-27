import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum

/-! Finite counterexamples to two inequalities in arXiv:2605.14871v9.
The list enumerates primes from 2 through 29, with zero-based list indices.
The argument n below uses Wang's one-based indexing. -/
namespace PrimeGapAudit

private def primes := (List.range 30).filter Nat.Prime
private def p (n : ℕ) : ℚ := (primes[n-1]?.getD 0 : ℕ)
private def g (n : ℕ) : ℚ := p (n+1) - p n
private def A (n : ℕ) : ℚ := (p (n+1) - 2) / n

theorem prime_inventory : primes = [2,3,5,7,11,13,17,19,23,29] := by decide

theorem lemma_2_4_counterexample :
    A 8 < g 8 ∧ g 8 < g 9 ∧ g 9 < g 8 * g 8 / A 8 := by
  norm_num [A, g, p, prime_inventory]

theorem eq_2_11_counterexample :
    g 5 < A 5 ∧ A 4 < A 6 ∧ A 6 < g 6 ∧
      (4/6 : ℚ) * (g 6 - A 5) / (A 5 - g 5) = 6 ∧ (7/2 : ℚ) < 6 := by
  norm_num [A, g, p, prime_inventory]

#print axioms lemma_2_4_counterexample
#print axioms eq_2_11_counterexample
end PrimeGapAudit
