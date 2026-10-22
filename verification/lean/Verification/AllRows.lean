import Verification.Regions

set_option autoImplicit false
set_option maxHeartbeats 8000000
namespace Verification.Published
noncomputable section
open MeasureTheory SubsetSum.FilterData

def oldRow (c : RawCertificate) (x : Real) : Real :=
  let U := u c.filterIndex x
  let W := w c.filterIndex x
  if c.region.val = 0 then
    weight c 0*(deltaB-U)+weight c 1*(gammaB-W)+comparisonTerm c 2 (fun v => u v x)
  else if c.region.val = 9 then
    weight c 0*(slopeB*W-U)+weight c 1*(W-15*gammaB)+comparisonTerm c 2 (fun v => u v x)
  else
    weight c 0*(slopeB*W-U)+weight c 1*(W-(lowerBoundary c.region:Real)*gammaB)+
    weight c 2*((upperLevel c.region:Real)*gammaB-W)+comparisonTerm c 3 (fun v => u v x)

def newRow (c : RawCertificate) (x : Real) : Real :=
  let U := u c.filterIndex x
  let W := w c.filterIndex x
  if c.region.val = 0 then
    if c.filterIndex.val = 3 then
      weight c 0*(delta-U)+weight c 1*(budget-W)+comparisonTerm c 2 (fun v => u v x)
    else
      weight c 0*(delta/ratio-U)+weight c 1*(gammaB-W)+comparisonTerm c 2 (fun v => u v x)
  else if c.region.val = 9 then
    weight c 0*(slope*W-U)+weight c 1*(W-15*gammaB)+comparisonTerm c 2 (fun v => u v x)
  else
    weight c 0*(slope*W-U)+weight c 1*(W-
      (if c.filterIndex.val = 3 ∧ c.region.val = 1 then budget else (lowerBoundary c.region:Real)*gammaB))+
    (weight c 2+weight c 0*(slope-slopeB))*((upperLevel c.region:Real)*gammaB-W)+
    comparisonTerm c 3 (fun v => u v x)

theorem all_first_weights_nonnegative :
    ∀ c ∈ certificates, (0:Rat) ≤ c.multipliers.getD 0 0 := by decide +kernel

theorem only_special_lower_zero : ∀ c ∈ certificates,
    c.filterIndex.val = 3 → c.region.val = 1 → c.multipliers.getD 1 0 = 0 := by
  decide +kernel

@[fun_prop] theorem continuous_comparison (c : RawCertificate) (offset : Nat) :
    Continuous (fun x => comparisonTerm c offset (fun v => u v x)) := by
  unfold comparisonTerm
  apply continuous_list_sum
  intro p hp
  exact continuous_const.mul ((continuous_u c.filterIndex).sub (continuous_u p.1))

theorem continuous_oldRow (c : RawCertificate) : Continuous (oldRow c) := by
  unfold oldRow
  split_ifs <;> dsimp only <;> apply Continuous.add
  all_goals first | exact continuous_comparison c 2 | exact continuous_comparison c 3 | fun_prop

theorem continuous_newRow (c : RawCertificate) : Continuous (newRow c) := by
  unfold newRow
  split_ifs <;> dsimp only <;> apply Continuous.add
  all_goals first | exact continuous_comparison c 2 | exact continuous_comparison c 3 | fun_prop

/-- Actual exponent transfer for every concrete record. The coarse score bound
is an explicit analytic premise, separately proved in the written supplement;
it has not been silently assumed as a Lean axiom. -/
theorem all_row_exponent_transfer (c : RawCertificate) (hc : c ∈ certificates)
    (x : Real) (hW : w c.filterIndex x ≤ 256) :
    newRow c x ≤ oldRow c x + (rowShift c:Real) := by
  have hz : (0:Real) ≤ weight c 0 := by
    unfold weight
    exact_mod_cast all_first_weights_nonnegative c hc
  have hp := mul_nonneg hz (sub_nonneg.mpr hW)
  by_cases h0 : c.region.val = 0
  · by_cases hv : c.filterIndex.val = 3
    · simp only [oldRow,newRow,rowShift,if_pos h0,if_pos hv]
      push_cast
      norm_num [qDelta,qGamma,qEta,qTau,delta,budget,deltaB,gammaB,eta,tau,weight]
      ring_nf
      exact le_rfl
    · simp only [oldRow,newRow,rowShift,if_pos h0,if_neg hv]
      push_cast
      norm_num [qK,qDelta,qGamma,qEta,qTau,delta,ratio,budget,deltaB,gammaB,eta,tau,weight]
      ring_nf
      exact le_rfl
  · by_cases h9 : c.region.val = 9
    · simp only [oldRow,newRow,rowShift,if_neg h0,if_pos h9]
      push_cast
      norm_num [qSlopeChange,qDelta,qGamma,qEta,qTau,slope,slopeB,delta,budget,deltaB,gammaB,eta,tau,weight] at hp ⊢
      nlinarith [hp]
    · by_cases hs : c.filterIndex.val = 3 ∧ c.region.val = 1
      · have hz1 : weight c 1 = 0 := by
          unfold weight
          exact_mod_cast only_special_lower_zero c hc hs.1 hs.2
        simp only [oldRow,newRow,rowShift,if_neg h0,if_neg h9,if_pos hs,hz1,zero_mul,add_zero]
        push_cast
        norm_num [qK,qDelta,qGamma,qEta,qTau,slope,slopeB,delta,budget,deltaB,gammaB,eta,tau,weight]
        ring_nf
        exact le_rfl
      · simp only [oldRow,newRow,rowShift,if_neg h0,if_neg h9,if_neg hs]
        push_cast
        norm_num [qK,qDelta,qGamma,qEta,qTau,slope,slopeB,delta,budget,deltaB,gammaB,eta,tau,weight]
        ring_nf
        exact le_rfl

theorem all_row_regular (c : RawCertificate) :
    Integrable (integrand (oldRow c)) circleDomain ∧
    Integrable (integrand (newRow c)) circleDomain ∧
    0 < moment (oldRow c) ∧ 0 < moment (newRow c) :=
  ⟨circle_integrable_of_continuous (continuous_integrand (continuous_oldRow c)),
    circle_integrable_of_continuous (continuous_integrand (continuous_newRow c)),
    positive_moment (continuous_oldRow c),positive_moment (continuous_newRow c)⟩

theorem all_row_moment_transfer (c : RawCertificate) (hc : c ∈ certificates)
    (hW : ∀ x, w c.filterIndex x ≤ 256) :
    moment (newRow c) ≤ exp2 (rowShift c:Real)*moment (oldRow c) := by
  have hM : ∀ x, 0 ≤ M2 x := by
    intro x
    unfold M2
    nlinarith [Real.neg_one_le_cos x]
  have h := SubsetSum.moment_transfer_bound circleDomain M2 (oldRow c) (newRow c)
    (rowShift c:Real) hM (fun x => all_row_exponent_transfer c hc x (hW x))
    (all_row_regular c).1 (all_row_regular c).2.1
  have hp : 0 ≤ (2*Real.pi)⁻¹ := by positivity
  have h2 := mul_le_mul_of_nonneg_left h hp
  simpa only [moment,circleAverage,SubsetSum.moment,integrand,exp2,
    mul_assoc,mul_left_comm (2*Real.pi)⁻¹] using h2

/-- Closed-record result with its genuine analytic premises displayed:
the old moment and coarse score bound are not Lean axioms or conclusions
assumed under a certificate predicate. Numerical evidence discharges the old
moments outside Lean; the written supplement proves the score bound. -/
theorem all_430_conditional_moment_bounds (c : RawCertificate) (hc : c ∈ certificates)
    (hW : ∀ x, w c.filterIndex x ≤ 256)
    (hOld : moment (oldRow c) ≤ exp2 (etaB-(oldMargin c:Real))) :
    moment (newRow c) < exp2 (eta-finiteMargin) := by
  have hm : (0.0000001:Real) < (rowMargin c:Real) := by
    have hq := (Rat.cast_lt (K := Real)).2 (all_430_transferred_margins c hc)
    norm_num at hq ⊢
    exact hq
  have hmargin : (rowShift c:Real)+(etaB-(oldMargin c:Real)) < eta-finiteMargin := by
    norm_num [rowMargin,qEta,eta,etaB,finiteMargin] at hm ⊢
    linarith
  have he : exp2 ((rowShift c:Real)+(etaB-(oldMargin c:Real))) <
      exp2 (eta-finiteMargin) := by
    apply Real.exp_lt_exp.mpr
    exact mul_lt_mul_of_pos_left hmargin (Real.log_pos (by norm_num))
  exact (all_row_moment_transfer c hc hW).trans_lt
    ((mul_le_mul_of_nonneg_left hOld (SubsetSum.exp2_pos _).le).trans_lt
      (by simpa only [exp2,SubsetSum.exp2_add] using he))

end
end Verification.Published
