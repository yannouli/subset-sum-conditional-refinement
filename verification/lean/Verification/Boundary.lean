import Verification.Concrete

set_option autoImplicit false

namespace Verification.Published
noncomputable section
open MeasureTheory

theorem exact_special_rows :
    SubsetSum.FilterData.certificate_3_0.comparisons = [5, 16] ∧
    SubsetSum.FilterData.certificate_3_1.comparisons = [5, 8, 16, 35] ∧
    weight SubsetSum.FilterData.certificate_3_1 1 = 0 ∧
    weight SubsetSum.FilterData.certificate_3_1 0 = 7.7547 := by
  norm_num [weight, SubsetSum.FilterData.certificate_3_0,
    SubsetSum.FilterData.certificate_3_1]

theorem concrete_budgets :
    0 < budget ∧ budget < gammaB ∧ 0 < delta ∧ 0 < transferK ∧
    (slope - slopeB) * gammaB = transferK ∧ 0 ≤ newUpperWeight := by
  norm_num [budget, delta, transferK, ratio, slope, slopeB, newUpperWeight,
    weight, SubsetSum.FilterData.certificate_3_1, eta, tau, gammaB, deltaB]

theorem low_comparisons_nonnegative (U : Fin 43 → ℝ)
    (h : ∀ j ∈ SubsetSum.FilterData.certificate_3_0.comparisons, U j ≤ U 3) :
    0 ≤ comparisonTerm SubsetSum.FilterData.certificate_3_0 2 U := by
  have h5 := h 5 (by decide)
  have h16 := h 16 (by decide)
  norm_num [comparisonTerm, SubsetSum.FilterData.certificate_3_0]
  linarith

theorem band_comparisons_nonnegative (U : Fin 43 → ℝ)
    (h : ∀ j ∈ SubsetSum.FilterData.certificate_3_1.comparisons, U j ≤ U 3) :
    0 ≤ comparisonTerm SubsetSum.FilterData.certificate_3_1 3 U := by
  have h5 := h 5 (by decide)
  have h8 := h 8 (by decide)
  have h16 := h 16 (by decide)
  have h35 := h 35 (by decide)
  norm_num [comparisonTerm, SubsetSum.FilterData.certificate_3_1]
  linarith

theorem low_pattern_domination (U : Fin 43 → ℝ) (W : ℝ)
    (hregion : W ≤ budget)
    (hselect : ∀ j ∈ SubsetSum.FilterData.certificate_3_0.comparisons, U j ≤ U 3)
    (hsample : SubsetSum.samplingFraction budget W * U 3 < delta) :
    -SubsetSum.samplingFraction budget W * U 3 ≤
      -delta + lowExponent delta budget U W := by
  have ha : SubsetSum.samplingFraction budget W = 1 := by
    simp [SubsetSum.samplingFraction, hregion]
  rw [ha] at hsample ⊢
  have hc := low_comparisons_nonnegative U hselect
  have hz0 : 1 ≤ weight SubsetSum.FilterData.certificate_3_0 0 := by
    norm_num [weight, SubsetSum.FilterData.certificate_3_0]
  have hz1 : 0 ≤ weight SubsetSum.FilterData.certificate_3_0 1 := by
    norm_num [weight, SubsetSum.FilterData.certificate_3_0]
  have hfirst := mul_nonneg (sub_nonneg.mpr hz0)
    (sub_nonneg.mpr (by simpa using hsample.le : U 3 ≤ delta))
  have hupper := mul_nonneg hz1 (sub_nonneg.mpr hregion)
  unfold lowExponent
  nlinarith

theorem extended_pattern_domination (U : Fin 43 → ℝ) (W : ℝ)
    (hlower : budget < W) (hupper : W ≤ bandTop)
    (hselect : ∀ j ∈ SubsetSum.FilterData.certificate_3_1.comparisons, U j ≤ U 3)
    (hsample : SubsetSum.samplingFraction budget W * U 3 < delta) :
    -SubsetSum.samplingFraction budget W * U 3 ≤
      -delta + bandExponent slope budget newUpperWeight U W := by
  have hg := concrete_budgets.1
  have hW : 0 < W := hg.trans hlower
  have ha : SubsetSum.samplingFraction budget W = budget / W := by
    simp [SubsetSum.samplingFraction, not_le.mpr hlower]
  have hap : 0 < SubsetSum.samplingFraction budget W := by rw [ha]; positivity
  have ha1 : SubsetSum.samplingFraction budget W < 1 := by
    rw [ha]; exact (div_lt_one hW).2 hlower
  have hz : 1 ≤ weight SubsetSum.FilterData.certificate_3_1 0 := by
    norm_num [weight, SubsetSum.FilterData.certificate_3_1]
  have hb : SubsetSum.samplingFraction budget W * (slope * W) = delta := by
    rw [ha]; unfold slope; field_simp
  have hd := SubsetSum.band_domination hap (ha1.le.trans hz) hb hsample
  have hc := band_comparisons_nonnegative U hselect
  have hu := mul_nonneg concrete_budgets.2.2.2.2.2 (sub_nonneg.mpr hupper)
  have hzero := exact_special_rows.2.2.1
  unfold bandExponent
  rw [hzero]
  simp only [zero_mul, add_zero]
  linarith

theorem concrete_low_shift : ∀ x : ℝ, newLow x = oldLow x + lowShift := by
  intro x
  unfold newLow oldLow lowExponent lowShift
  ring

theorem concrete_band_shift : ∀ x : ℝ, newBand x = oldBand x + bandShift := by
  intro x
  have hzero := exact_special_rows.2.2.1
  have hk := concrete_budgets.2.2.2.2.1
  unfold newBand oldBand bandExponent newUpperWeight bandShift bandTop
  simp only [hzero, zero_mul, add_zero]
  rw [← hk]
  ring

/-- Pure integral linearity, not yet the positive/integrable concrete theorem. -/
theorem moment_add_constant (E : ℝ → ℝ) (c : ℝ) :
    moment (fun x => E x + c) = exp2 c * moment E := by
  have hf : integrand (fun x => E x + c) =
      fun x => exp2 c * integrand E x := by
    funext x
    simp only [integrand, exp2, SubsetSum.exp2_add]
    ring
  unfold moment circleAverage
  rw [hf, integral_const_mul]
  ring

/-- Exact endpoint coverage: the moved low interval, extended first band,
then the unchanged seven middle bands and tail cover every real score. -/
theorem complete_region_coverage (W : Real) :
    W ≤ budget ∨ (budget < W ∧ W ≤ bandTop) ∨
    (bandTop < W ∧ W ≤ (8/5)*gammaB) ∨
    ((8/5)*gammaB < W ∧ W ≤ 2*gammaB) ∨
    (2*gammaB < W ∧ W ≤ (13/5)*gammaB) ∨
    ((13/5)*gammaB < W ∧ W ≤ (7/2)*gammaB) ∨
    ((7/2)*gammaB < W ∧ W ≤ 5*gammaB) ∨
    (5*gammaB < W ∧ W ≤ 8*gammaB) ∨
    (8*gammaB < W ∧ W ≤ 15*gammaB) ∨ 15*gammaB < W := by
  rcases le_or_gt W budget with h | h
  · exact Or.inl h
  rcases le_or_gt W bandTop with k | k
  · exact Or.inr (Or.inl ⟨h,k⟩)
  right; right
  rcases le_or_gt W ((8/5)*gammaB) with l | l
  · exact Or.inl ⟨k,l⟩
  right
  rcases le_or_gt W (2*gammaB) with m | m
  · exact Or.inl ⟨l,m⟩
  right
  rcases le_or_gt W ((13/5)*gammaB) with n | n
  · exact Or.inl ⟨m,n⟩
  right
  rcases le_or_gt W ((7/2)*gammaB) with o | o
  · exact Or.inl ⟨n,o⟩
  right
  rcases le_or_gt W (5*gammaB) with p | p
  · exact Or.inl ⟨o,p⟩
  right
  rcases le_or_gt W (8*gammaB) with q | q
  · exact Or.inl ⟨p,q⟩
  right
  exact (le_or_gt W (15*gammaB)).imp (fun t => ⟨q,t⟩) id

end
end Verification.Published
