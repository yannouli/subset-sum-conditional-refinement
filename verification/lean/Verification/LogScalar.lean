/- Generic log-ratio proof reused verbatim from Joshua Wharton bed8e18,
Numerics.lean, under its repository license; the rational endpoints below
are newly checked for the exact published tuple. No numerical log premise. -/
import SubsetSum.LogBounds
import Verification.DataBridge
set_option autoImplicit false
set_option maxHeartbeats 0
set_option maxRecDepth 100000
namespace Verification.Published
noncomputable section
open SubsetSum
lemma log_ratio_interval (n : ℕ) (z lo hi : ℝ) (hz : |z| < 1)
    (hl : lo ≤ realLogTaylor (n + 1) z - realLogTaylor (n + 1) (-z) -
      2 * (|z| ^ (n + 1) * (1 - |z|)⁻¹ / (n + 1)))
    (hu : realLogTaylor (n + 1) z - realLogTaylor (n + 1) (-z) +
      2 * (|z| ^ (n + 1) * (1 - |z|)⁻¹ / (n + 1)) ≤ hi) :
    lo ≤ Real.log ((1 + z) / (1 - z)) ∧
    Real.log ((1 + z) / (1 - z)) ≤ hi := by
  have hp := abs_le.mp (real_log_taylor_bound n hz)
  have hm := abs_le.mp (real_log_taylor_bound n (x := -z) (by simpa using hz))
  simp only [abs_neg, ← sub_eq_add_neg] at hm
  have hzp : 0 < 1 + z := by have := (abs_lt.mp hz).1; linarith
  have hzm : 0 < 1 - z := by have := (abs_lt.mp hz).2; linarith
  rw [Real.log_div hzp.ne' hzm.ne']
  constructor <;> linarith [hp.1, hp.2, hm.1, hm.2]

theorem ln_two : 0.69314718055993 ≤ Real.log (2 / 1 : Real) ∧ Real.log (2 / 1 : Real) ≤ 0.69314718055996 := by
  have h := log_ratio_interval 32 (1 / 3 : Real) 0.69314718055993 0.69314718055996
    (by norm_num)
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
  norm_num at h ⊢
  exact h
theorem ln_reduced_a : 0.04210824821746 ≤ Real.log (2037123781893501 / 1953125000000000 : Real) ∧ Real.log (2037123781893501 / 1953125000000000 : Real) ≤ 0.04210824821749 := by
  have h := log_ratio_interval 32 (83998781893501 / 3990248781893501 : Real) 0.04210824821746 0.04210824821749
    (by norm_num)
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
  norm_num at h ⊢
  exact h
theorem ln_reduced_na : 0.68496530498867 ≤ Real.log (247962876218106499 / 125000000000000000 : Real) ∧ Real.log (247962876218106499 / 125000000000000000 : Real) ≤ 0.68496530498870 := by
  have h := log_ratio_interval 32 (122962876218106499 / 372962876218106499 : Real) 0.68496530498867 0.68496530498870
    (by norm_num)
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
  norm_num at h ⊢
  exact h
theorem ln_reduced_n2a : 0.67671593370843 ≤ Real.log (122962876218106499 / 62500000000000000 : Real) ∧ Real.log (122962876218106499 / 62500000000000000 : Real) ≤ 0.67671593370846 := by
  have h := log_ratio_interval 32 (60462876218106499 / 185462876218106499 : Real) 0.67671593370843 0.67671593370846
    (by norm_num)
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
  norm_num at h ⊢
  exact h
theorem ln_reduced_ha : 0.01616561968434 ≤ Real.log (127037123781893501 / 125000000000000000 : Real) ∧ Real.log (127037123781893501 / 125000000000000000 : Real) ≤ 0.01616561968437 := by
  have h := log_ratio_interval 32 (2037123781893501 / 252037123781893501 : Real) 0.01616561968434 0.01616561968437
    (by norm_num)
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
  norm_num at h ⊢
  exact h
private theorem log_scale (x : Real) (m : Nat) (hx : 0 < x) :
    Real.log (x * (2 : Real)^m) = Real.log x + m * Real.log 2 := by
  rw [Real.log_mul hx.ne' (by positivity), Real.log_pow]
theorem ln_a : -4.809922015704 ≤ Real.log (2037123781893501 / 250000000000000000 : Real) ∧ Real.log (2037123781893501 / 250000000000000000 : Real) ≤ -4.809922015701 := by
  have h := ln_reduced_a
  have h2 := ln_two
  have he := log_scale (2037123781893501 / 250000000000000000 : Real) 7 (by norm_num)
  norm_num at he
  constructor <;> linarith [h.1,h.2,h2.1,h2.2]
theorem ln_na : -0.008181875573 ≤ Real.log (247962876218106499 / 250000000000000000 : Real) ∧ Real.log (247962876218106499 / 250000000000000000 : Real) ≤ -0.008181875570 := by
  have h := ln_reduced_na
  have h2 := ln_two
  have he := log_scale (247962876218106499 / 250000000000000000 : Real) 1 (by norm_num)
  norm_num at he
  constructor <;> linarith [h.1,h.2,h2.1,h2.2]
theorem ln_twoa : -4.116774835144 ≤ Real.log (2037123781893501 / 125000000000000000 : Real) ∧ Real.log (2037123781893501 / 125000000000000000 : Real) ≤ -4.116774835141 := by
  have h := ln_reduced_a
  have h2 := ln_two
  have he := log_scale (2037123781893501 / 125000000000000000 : Real) 6 (by norm_num)
  norm_num at he
  constructor <;> linarith [h.1,h.2,h2.1,h2.2]
theorem ln_n2a : -0.016431246853 ≤ Real.log (122962876218106499 / 125000000000000000 : Real) ∧ Real.log (122962876218106499 / 125000000000000000 : Real) ≤ -0.016431246850 := by
  have h := ln_reduced_n2a
  have h2 := ln_two
  have he := log_scale (122962876218106499 / 125000000000000000 : Real) 1 (by norm_num)
  norm_num at he
  constructor <;> linarith [h.1,h.2,h2.1,h2.2]
theorem ln_hma : -0.709578427413 ≤ Real.log (122962876218106499 / 250000000000000000 : Real) ∧ Real.log (122962876218106499 / 250000000000000000 : Real) ≤ -0.709578427410 := by
  have h := ln_reduced_n2a
  have h2 := ln_two
  have he := log_scale (122962876218106499 / 250000000000000000 : Real) 2 (by norm_num)
  norm_num at he
  constructor <;> linarith [h.1,h.2,h2.1,h2.2]
theorem ln_hpa : -0.676981560877 ≤ Real.log (127037123781893501 / 250000000000000000 : Real) ∧ Real.log (127037123781893501 / 250000000000000000 : Real) ≤ -0.676981560874 := by
  have h := ln_reduced_ha
  have h2 := ln_two
  have he := log_scale (127037123781893501 / 250000000000000000 : Real) 1 (by norm_num)
  norm_num at he
  constructor <;> linarith [h.1,h.2,h2.1,h2.2]
def entropy (x : Real) : Real :=
  (-x * Real.log x - (1-x)*Real.log (1-x))/Real.log 2
theorem entropy_a : 0.0682522167 ≤ entropy (2037123781893501 / 250000000000000000 : Real) ∧ entropy (2037123781893501 / 250000000000000000 : Real) ≤ 0.0682522170 := by
  have h1 := ln_a
  have h2 := ln_na
  have hL := ln_two
  have hp : 0 < Real.log 2 := by linarith [hL.1]
  unfold entropy
  constructor
  · apply (le_div_iff₀ hp).2
    nlinarith [h1.1,h1.2,h2.1,h2.2,hL.1,hL.2]
  · apply (div_le_iff₀ hp).2
    nlinarith [h1.1,h1.2,h2.1,h2.2,hL.1,hL.2]
theorem entropy_twoa : 0.1201108633 ≤ entropy (2037123781893501 / 125000000000000000 : Real) ∧ entropy (2037123781893501 / 125000000000000000 : Real) ≤ 0.1201108636 := by
  have h1 := ln_twoa
  have h2 := ln_n2a
  have hL := ln_two
  have hp : 0 < Real.log 2 := by linarith [hL.1]
  unfold entropy
  constructor
  · apply (le_div_iff₀ hp).2
    nlinarith [h1.1,h1.2,h2.1,h2.2,hL.1,hL.2]
  · apply (div_le_iff₀ hp).2
    nlinarith [h1.1,h1.2,h2.1,h2.2,hL.1,hL.2]
theorem entropy_hma : 0.9998084073 ≤ entropy (122962876218106499 / 250000000000000000 : Real) ∧ entropy (122962876218106499 / 250000000000000000 : Real) ≤ 0.9998084076 := by
  have h1 := ln_hma
  have h2 := ln_hpa
  have hL := ln_two
  have hp : 0 < Real.log 2 := by linarith [hL.1]
  unfold entropy
  constructor
  · apply (le_div_iff₀ hp).2
    nlinarith [h1.1,h1.2,h2.1,h2.2,hL.1,hL.2]
  · apply (div_le_iff₀ hp).2
    nlinarith [h1.1,h1.2,h2.1,h2.2,hL.1,hL.2]
end
end Verification.Published
