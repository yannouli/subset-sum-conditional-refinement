import Verification.Boundary

set_option autoImplicit false

namespace Verification.Published
noncomputable section
open MeasureTheory Set

theorem continuous_trig (cs : List ℚ) : Continuous (trig cs) := by
  have h : ∀ ps : List (ℚ × ℕ), Continuous
      (fun x : ℝ => (ps.map (fun p => (p.1 : ℝ) *
        Real.cos (((p.2 + 1 : ℕ) : ℝ) * x))).sum) := by
    intro ps
    induction ps with
    | nil => simpa using (continuous_const : Continuous (fun _ : ℝ => (0 : ℝ)))
    | cons p ps ih =>
      simp only [List.map_cons, List.sum_cons]
      exact (continuous_const.mul (Real.continuous_cos.comp
        (continuous_const.mul continuous_id))).add ih
  exact h cs.zipIdx

@[fun_prop] theorem continuous_r (v : Fin 43) : Continuous (r v) :=
  continuous_trig _
@[fun_prop] theorem continuous_s (v : Fin 43) : Continuous (s v) :=
  continuous_trig _
@[fun_prop] theorem continuous_exp2 : Continuous exp2 := by
  unfold exp2 SubsetSum.exp2
  fun_prop
@[fun_prop] theorem continuous_F (v : Fin 43) : Continuous (F v) :=
  continuous_exp2.comp (continuous_r v)
@[fun_prop] theorem continuous_G (v : Fin 43) : Continuous (G v) :=
  continuous_exp2.comp (continuous_s v)

theorem circle_integrable_of_continuous {f : ℝ → ℝ} (hf : Continuous f) :
    Integrable f circleDomain :=
  hf.continuousOn.integrableOn_compact isCompact_Icc

theorem circle_domain_positive : 0 < circleDomain Set.univ := by
  unfold circleDomain
  rw [Measure.restrict_apply_univ, Real.volume_Icc]
  exact ENNReal.ofReal_pos.mpr (by nlinarith [Real.pi_pos])

theorem average_positive {f : ℝ → ℝ} (hf : Continuous f) (hpos : ∀ x, 0 < f x) :
    0 < circleAverage f := by
  have hs : Function.support f = Set.univ := by
    ext x
    simp only [Function.mem_support, Set.mem_univ, iff_true]
    exact (hpos x).ne'
  have hi : 0 < ∫ x, f x ∂circleDomain :=
    (integral_pos_iff_support_of_nonneg (fun x => (hpos x).le)
      (circle_integrable_of_continuous hf)).2 (by rw [hs]; exact circle_domain_positive)
  exact mul_pos (inv_pos.mpr (by positivity : 0 < 2 * Real.pi)) hi

theorem continuous_average_parametric (f : ℝ → ℝ → ℝ)
    (hf : Continuous f.uncurry) : Continuous (fun x => circleAverage (f x)) := by
  unfold circleAverage circleDomain
  exact continuous_const.mul (continuous_parametric_integral_of_continuous hf isCompact_Icc)

theorem Zf_positive (v : Fin 43) : 0 < Zf v :=
  average_positive (continuous_F v) (fun _ => SubsetSum.exp2_pos _)
theorem Zg_positive (v : Fin 43) : 0 < Zg v :=
  average_positive (continuous_G v) (fun _ => SubsetSum.exp2_pos _)
theorem Zfk_positive (v : Fin 43) : 0 < Zfk v := by
  apply average_positive
  · exact continuous_exp2.comp (continuous_const.mul (continuous_r v))
  · intro x; exact SubsetSum.exp2_pos _
theorem Zgk_positive (v : Fin 43) : 0 < Zgk v := by
  apply average_positive
  · exact continuous_exp2.comp (continuous_const.mul (continuous_s v))
  · intro x; exact SubsetSum.exp2_pos _

@[fun_prop] theorem continuous_P (v : Fin 43) : Continuous (P v) := by
  apply continuous_average_parametric
  exact ((continuous_F v).comp (continuous_fst.add continuous_snd)).mul
    ((continuous_G v).comp continuous_snd)

theorem P_positive (v : Fin 43) (x : ℝ) : 0 < P v x := by
  apply average_positive
  · exact ((continuous_F v).comp (continuous_const.add continuous_id)).mul (continuous_G v)
  · intro y; exact mul_pos (SubsetSum.exp2_pos _) (SubsetSum.exp2_pos _)

theorem kernel_positive (v : Fin 43) (x y : ℝ) : 0 < kernel v x y :=
  div_pos (mul_pos (SubsetSum.exp2_pos _) (SubsetSum.exp2_pos _)) (P_positive v x)

theorem continuous_kernel (v : Fin 43) : Continuous (Function.uncurry (kernel v)) := by
  unfold kernel Function.uncurry
  exact (((continuous_F v).comp (continuous_fst.add continuous_snd)).mul
    ((continuous_G v).comp continuous_snd)).div
    ((continuous_P v).comp continuous_fst) (fun p => (P_positive v p.1).ne')

@[fun_prop] theorem continuous_fTilt (v : Fin 43) : Continuous (fTilt v) :=
  (continuous_exp2.comp (continuous_const.mul (continuous_r v))).div_const _
@[fun_prop] theorem continuous_gTilt (v : Fin 43) : Continuous (gTilt v) :=
  (continuous_exp2.comp (continuous_const.mul (continuous_s v))).div_const _
theorem fTilt_positive (v : Fin 43) (x : ℝ) : 0 < fTilt v x :=
  div_pos (SubsetSum.exp2_pos _) (Zfk_positive v)
theorem gTilt_positive (v : Fin 43) (x : ℝ) : 0 < gTilt v x :=
  div_pos (SubsetSum.exp2_pos _) (Zgk_positive v)

theorem continuous_log2_comp {X : Type*} [TopologicalSpace X] {f : X → ℝ}
    (hf : Continuous f) (hp : ∀ x, 0 < f x) : Continuous (fun x => log2 (f x)) :=
  (hf.log (fun x => (hp x).ne')).div_const _

@[fun_prop] theorem continuous_entropyScore (v : Fin 43) : Continuous (entropyScore v) := by
  apply continuous_average_parametric
  exact (continuous_kernel v).mul (continuous_log2_comp (continuous_kernel v)
    (fun p => kernel_positive v p.1 p.2))

@[fun_prop] theorem continuous_fScore (v : Fin 43) : Continuous (fScore v) := by
  apply continuous_average_parametric
  exact (continuous_kernel v).mul (continuous_log2_comp
    ((continuous_fTilt v).comp (continuous_fst.add continuous_snd))
    (fun p => fTilt_positive v (p.1 + p.2)))

@[fun_prop] theorem continuous_gScore (v : Fin 43) : Continuous (gScore v) := by
  apply continuous_average_parametric
  exact (continuous_kernel v).mul (continuous_log2_comp
    ((continuous_gTilt v).comp continuous_snd) (fun p => gTilt_positive v p.2))

@[fun_prop] theorem continuous_u (v : Fin 43) : Continuous (u v) :=
  ((continuous_fScore v).add (continuous_gScore v)).sub (continuous_entropyScore v)
@[fun_prop] theorem continuous_w (v : Fin 43) : Continuous (w v) :=
  ((continuous_const.mul (continuous_entropyScore v)).sub (continuous_fScore v)).sub
    (continuous_gScore v)

@[fun_prop] theorem continuous_lowExponent (D H : ℝ) :
    Continuous (fun x => lowExponent D H (fun v => u v x) (w 3 x)) := by
  unfold lowExponent comparisonTerm
  simp only [SubsetSum.FilterData.certificate_3_0, List.drop, List.zip]
  fun_prop

@[fun_prop] theorem continuous_bandExponent (A L Z : ℝ) :
    Continuous (fun x => bandExponent A L Z (fun v => u v x) (w 3 x)) := by
  unfold bandExponent comparisonTerm
  simp only [SubsetSum.FilterData.certificate_3_1, List.drop, List.zip]
  fun_prop

@[fun_prop] theorem continuous_integrand {E : ℝ → ℝ} (hE : Continuous E) :
    Continuous (integrand E) := by
  unfold integrand M2
  exact (continuous_const.add (continuous_const.mul Real.continuous_cos)).mul
    (continuous_exp2.comp hE)

theorem positive_moment {E : ℝ → ℝ} (hE : Continuous E) : 0 < moment E := by
  have hf := continuous_integrand hE
  have hn : ∀ x, 0 ≤ integrand E x := by
    intro x
    apply mul_nonneg _ (SubsetSum.exp2_pos _).le
    unfold M2
    nlinarith [Real.neg_one_le_cos x]
  have hp : integrand E (Real.pi / 2) ≠ 0 := by
    apply ne_of_gt
    unfold integrand M2
    rw [Real.cos_pi_div_two]
    exact mul_pos (by norm_num) (SubsetSum.exp2_pos _)
  have hs : IsOpen (Function.support (integrand E) ∩ Set.Ioo 0 (2 * Real.pi)) :=
    hf.isOpen_support.inter isOpen_Ioo
  have hm : 0 < volume (Function.support (integrand E) ∩ Set.Ioo 0 (2 * Real.pi)) :=
    hs.measure_pos volume ⟨Real.pi / 2, hp, by constructor <;> nlinarith [Real.pi_pos]⟩
  have hi : 0 < ∫ x, integrand E x ∂circleDomain := by
    apply (integral_pos_iff_support_of_nonneg hn (circle_integrable_of_continuous hf)).2
    unfold circleDomain
    rw [Measure.restrict_apply hf.isOpen_support.measurableSet]
    exact hm.trans_le (measure_mono (Set.inter_subset_inter_right _ Set.Ioo_subset_Icc_self))
  exact mul_pos (inv_pos.mpr (by positivity : 0 < 2 * Real.pi)) hi

theorem concrete_low_moment_identity :
    Integrable (integrand oldLow) circleDomain ∧
    Integrable (integrand newLow) circleDomain ∧
    0 < moment oldLow ∧ moment newLow = exp2 lowShift * moment oldLow := by
  refine ⟨circle_integrable_of_continuous (continuous_integrand (continuous_lowExponent _ _)),
    circle_integrable_of_continuous (continuous_integrand (continuous_lowExponent _ _)),
    positive_moment (continuous_lowExponent _ _), ?_⟩
  have h : newLow = fun x => oldLow x + lowShift := funext concrete_low_shift
  rw [h]
  exact moment_add_constant oldLow lowShift

theorem concrete_band_moment_identity :
    Integrable (integrand oldBand) circleDomain ∧
    Integrable (integrand newBand) circleDomain ∧
    0 < moment oldBand ∧ moment newBand = exp2 bandShift * moment oldBand := by
  refine ⟨circle_integrable_of_continuous (continuous_integrand (continuous_bandExponent _ _ _)),
    circle_integrable_of_continuous (continuous_integrand (continuous_bandExponent _ _ _)),
    positive_moment (continuous_bandExponent _ _ _), ?_⟩
  have h : newBand = fun x => oldBand x + bandShift := funext concrete_band_shift
  rw [h]
  exact moment_add_constant oldBand bandShift

end
end Verification.Published
