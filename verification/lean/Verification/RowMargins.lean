import Verification.Scalar
import SubsetSum.Asymptotics

set_option autoImplicit false
set_option maxHeartbeats 8000000
set_option maxRecDepth 100000

namespace Verification.Published
noncomputable section
open SubsetSum.FilterData

def qTau : Rat := 0.48767228
def qEta : Rat := 0.516133678389924
def qGamma : Rat := 2*qTau-qEta
def qDelta : Rat := qEta-qTau
def qK : Rat := qDelta/(qGamma/0.45925)-0.02844
def qSlopeChange : Rat := qDelta/qGamma-0.02844/0.45925

theorem rational_real_parameter_bridge :
    (qTau : Real) = tau ∧ (qEta : Real) = eta ∧
    (qGamma : Real) = budget ∧ (qDelta : Real) = delta ∧
    (qK : Real) = transferK ∧ (qSlopeChange : Real) = slope-slopeB := by
  norm_num [qTau,qEta,qGamma,qDelta,qK,qSlopeChange,tau,eta,budget,delta,
    transferK,ratio,gammaB,deltaB,slope,slopeB]

def oldMargin (c : RawCertificate) : Rat :=
  if c.region.val < 2 then 0.00025 else if c.region.val = 9 then 17 else 4

def upperLevel (j : Fin 10) : Rat :=
  [1,5/4,8/5,2,13/5,7/2,5,8,15,15].getD j.val 0

/-- The conservative shift for each actual record. Tail uses the separately
proved written score bound 256; this definition does not assert that bound. -/
def rowShift (c : RawCertificate) : Rat :=
  if c.region.val = 0 then
    if c.filterIndex.val = 3 then
      c.multipliers.getD 0 0*(qDelta-0.02844)+
      c.multipliers.getD 1 0*(qGamma-0.45925)
    else c.multipliers.getD 0 0*qK
  else if c.region.val = 9 then c.multipliers.getD 0 0*256*qSlopeChange
  else c.multipliers.getD 0 0*upperLevel c.region*qK

def rowMargin (c : RawCertificate) : Rat := oldMargin c+qEta-0.51613-rowShift c

def newWeightSum (c : RawCertificate) : Rat :=
  c.multipliers.sum + if c.region.val = 0 ∨ c.region.val = 9 then 0
    else c.multipliers.getD 0 0*qSlopeChange

/-- Closed 430-record arithmetic check, not a list of floating-point outputs. -/
theorem all_430_transferred_margins :
    ∀ c ∈ certificates, (0.0000001 : Rat) < rowMargin c := by
  decide +kernel

theorem all_430_weight_sums :
    ∀ c ∈ certificates, newWeightSum c < 419 := by
  decide +kernel

theorem exact_error_and_display_gap :
    finiteMargin-(18+6*419)*epsilon = 0.000000097468 ∧
    advertised-(tau+20*epsilon) = 0.00000001998 := by
  norm_num [finiteMargin,epsilon,advertised,tau]

theorem concrete_low_threshold_transfer
    (hOld : moment oldLow ≤ exp2 (etaB-0.00025)) :
    moment newLow < exp2 (eta-finiteMargin) := by
  rw [concrete_low_moment_identity.2.2.2]
  have hmargin : lowShift+(etaB-0.00025) < eta-finiteMargin := by
    norm_num [lowShift,weight,SubsetSum.FilterData.certificate_3_0,
      delta,budget,eta,tau,etaB,deltaB,gammaB,finiteMargin]
  have hstrict : exp2 (lowShift+(etaB-0.00025)) < exp2 (eta-finiteMargin) := by
    apply Real.exp_lt_exp.mpr
    exact mul_lt_mul_of_pos_left hmargin (Real.log_pos (by norm_num))
  exact (mul_le_mul_of_nonneg_left hOld (SubsetSum.exp2_pos _).le).trans_lt
    (by simpa only [exp2,SubsetSum.exp2_add] using hstrict)

theorem concrete_band_threshold_transfer
    (hOld : moment oldBand ≤ exp2 (etaB-0.00025)) :
    moment newBand < exp2 (eta-finiteMargin) := by
  rw [concrete_band_moment_identity.2.2.2]
  have hmargin : bandShift+(etaB-0.00025) < eta-finiteMargin := by
    norm_num [bandShift,weight,SubsetSum.FilterData.certificate_3_1,
      transferK,delta,ratio,budget,eta,tau,etaB,deltaB,gammaB,finiteMargin]
  have hstrict : exp2 (bandShift+(etaB-0.00025)) < exp2 (eta-finiteMargin) := by
    apply Real.exp_lt_exp.mpr
    exact mul_lt_mul_of_pos_left hmargin (Real.log_pos (by norm_num))
  exact (mul_le_mul_of_nonneg_left hOld (SubsetSum.exp2_pos _).le).trans_lt
    (by simpa only [exp2,SubsetSum.exp2_add] using hstrict)

/-- Ordinary-O absorption for this tuple. This is not a program cost theorem. -/
theorem fixed_tuple_ordinary_O (C K : Real) :
    Asymptotics.IsBigO Filter.atTop
      (fun n : Nat => exp2 ((tau+20*epsilon)*n+
        (C*(n:Real)^(0.7:Real)+K*Real.log (n:Real))))
      (fun n : Nat => exp2 (advertised*n)) := by
  exact SubsetSum.exp2_absorption error_work_and_absorption_gap.2.2.1
    (SubsetSum.paper_overhead_sublinear C K)

end
end Verification.Published
