import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.LinearAlgebra.StdBasis
import Mathlib.Tactic

/-! The character argument for the full-dimension theorem.
An undirected simple cycle is represented by its edge set. For a signing σ,
(1 - character C σ) / 2 is exactly the indicator that cycle C is negative. -/

namespace NegativeCycle
open scoped BigOperators
open Finset
variable {E : Type*} [Fintype E] [DecidableEq E]

private def factor (C : Finset E) (e : E) (b : Bool) : ℝ :=
  if e ∈ C then (if b then -1 else 1) else 1

def character (C : Finset E) (σ : E → Bool) : ℝ := ∏ e, factor C e (σ e)

theorem orthogonality (C D : Finset E) :
    ∑ σ : E → Bool, character C σ * character D σ =
      if C = D then (2 : ℝ) ^ Fintype.card E else 0 := by
  classical
  unfold character
  simp_rw [← Finset.prod_mul_distrib]
  rw [← Fintype.prod_sum (fun e b => factor C e b * factor D e b)]
  by_cases h : C = D
  · subst D
    simp only [if_true]
    have step (e : E) : ∑ b : Bool, factor C e b * factor C e b = 2 := by
      by_cases he : e ∈ C <;> norm_num [factor, he]
    simp only [step, Finset.prod_const, Finset.card_univ]
  · rw [if_neg h]
    obtain ⟨e, he⟩ : ∃ e, ¬ (e ∈ C ↔ e ∈ D) := by
      by_contra! ha
      exact h (Finset.ext ha)
    apply Finset.prod_eq_zero (Finset.mem_univ e)
    by_cases hc : e ∈ C <;> by_cases hd : e ∈ D <;>
      simp_all [factor]

/-- Every linear relation on the negative counts vanishes on each occurring
length. Set a(C) to the coefficient indexed by the length of C. -/
theorem no_relation (cycles : Finset (Finset E)) (a : Finset E → ℝ)
    (h : ∀ σ : E → Bool, ∑ C ∈ cycles, a C * ((1 - character C σ) / 2) = 0)
    {T : Finset E} (hT : T ∈ cycles) (hne : T.Nonempty) : a T = 0 := by
  classical
  have mean : ∑ σ : E → Bool, character T σ = 0 := by
    simpa [character, factor, hne.ne_empty] using (orthogonality T ∅)
  have eqn : ∑ σ : E → Bool, ∑ C ∈ cycles,
      a C * ((character T σ - character T σ * character C σ) / 2) = 0 := by
    apply Finset.sum_eq_zero
    intro σ _
    calc
      _ = character T σ * (∑ C ∈ cycles, a C * ((1 - character C σ) / 2)) := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro C _
        ring
      _ = 0 := by rw [h, mul_zero]
  rw [Finset.sum_comm] at eqn
  simp_rw [← Finset.mul_sum, ← Finset.sum_div, Finset.sum_sub_distrib,
    mean, orthogonality] at eqn
  rw [Finset.sum_eq_single T] at eqn
  · simpa using eqn
  · intro C _ hCT
    simp [Ne.symm hCT]
  · exact fun hnot => (hnot hT).elim

variable {K : Type*} [Fintype K] [DecidableEq K]

/-- Group the negative indicators by label. In the graph application the
labels are exactly the occurring lengths. -/
noncomputable def counts (cycles : Finset (Finset E)) (label : Finset E → K)
    (σ : E → Bool) : K → ℝ :=
  ∑ C ∈ cycles, ((1 - character C σ) / 2) • Pi.single (label C) (1 : ℝ)

/-- The span is the full coordinate space whenever each label occurs on a
nonempty edge set. Distinct simple cycles have distinct nonempty edge sets. -/
theorem full_span (cycles : Finset (Finset E)) (label : Finset E → K)
    (occurs : ∀ k, ∃ C ∈ cycles, C.Nonempty ∧ label C = k) :
    Submodule.span ℝ (Set.range (counts cycles label)) = ⊤ := by
  classical
  apply Submodule.dualAnnihilator_eq_bot_iff.mp
  apply bot_unique
  intro f hf
  change f = 0
  apply (Pi.basisFun ℝ K).ext
  intro k
  obtain ⟨C, hC, hn, rfl⟩ := occurs k
  simp only [Pi.basisFun_apply, LinearMap.zero_apply]
  apply no_relation cycles (fun D => f (Pi.single (label D) 1)) _ hC hn
  intro σ
  have h := (Submodule.mem_dualAnnihilator f).mp hf (counts cycles label σ)
    (Submodule.subset_span (Set.mem_range_self σ))
  simpa [counts, mul_comm] using h

#print axioms full_span
end NegativeCycle
