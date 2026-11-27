import Mathlib.LinearAlgebra.Lagrange
import Mathlib.Tactic.Ring

/-! Interpolating on a finite set of count values gives a signed change of
mass that preserves all polynomial expectations below the number of nodes.
The written argument chooses a positive step small enough for nonnegativity. -/
namespace WheelMoments

open Polynomial

variable {F ι : Type*} [Field F] [DecidableEq ι]
variable {s : Finset ι} {v : ι → F}

theorem perturbation_preserves_expectation
    (hv : Set.InjOn v s) (f : Polynomial F) (hf : f.degree < s.card)
    (originalZero step : F) (mass : ι → F) :
    (originalZero + step) * f.eval 0 +
      (∑ i ∈ s, (mass i - step * (Lagrange.basis s v i).eval 0) * f.eval (v i)) =
    originalZero * f.eval 0 + ∑ i ∈ s, mass i * f.eval (v i) := by
  have interp := congrArg (fun P : Polynomial F => P.eval 0) (Lagrange.eq_interpolate hv hf)
  have endpoint : f.eval 0 = ∑ i ∈ s, f.eval (v i) * (Lagrange.basis s v i).eval 0 := by
    simpa only [Lagrange.interpolate_apply, Polynomial.eval_finsetSum, Polynomial.eval_mul,
      Polynomial.eval_C] using interp
  have correction :
      (∑ i ∈ s, step * (Lagrange.basis s v i).eval 0 * f.eval (v i)) = step * f.eval 0 := by
    rw [endpoint, Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by ring
  simp only [sub_mul, Finset.sum_sub_distrib, correction]
  ring

#print axioms perturbation_preserves_expectation
end WheelMoments
