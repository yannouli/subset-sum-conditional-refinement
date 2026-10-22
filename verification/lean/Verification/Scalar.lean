import Verification.LogScalar
set_option autoImplicit false
set_option maxHeartbeats 0
namespace Verification.Published
noncomputable section
theorem log_three_coarse : log2 3 ≤ 2 := by
  have h := Real.log_le_log (by norm_num : (0:Real) < 3) (by norm_num : (3:Real) ≤ 4)
  rw [show (4:Real) = 2^2 by norm_num, Real.log_pow] at h
  norm_num at h
  unfold log2
  apply (div_le_iff₀ (Real.log_pos (by norm_num : (1:Real) < 2))).2
  nlinarith
theorem gap_coverage : aliasMargin < entropy (2*mask)/2-gamma := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_left_list : aliasMargin < tau-left-(entropy mask-gamma)*block := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_right_classes : aliasMargin < tau-(1-block-left)-(1-gamma)*block := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_pairs : aliasMargin < tau-1+block-(entropy mask+entropy (1/2-mask)-gamma)*block+eta := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_right_masks : aliasMargin < 2*tau-1/2-entropy (1/2-mask)*block := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_left_map : aliasMargin < tau-left := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_right_map : aliasMargin < tau-(1-block-left) := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_right_positive : aliasMargin < 1-block-left := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_sampled_map : aliasMargin < left-block*(1-2*mask) := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_reduction : aliasMargin < eta-block*log2 3/2 := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_block_classes : aliasMargin < tau-block := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_right_key_sort : aliasMargin < 2*tau-1/2-(1-block-left)-zeta := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_small_prime : aliasMargin < 2*tau-1/2-zeta-gamma*block/2 := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_prime_generation : aliasMargin < tau-eta/2 := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_sampled_size : aliasMargin < 1/2-block*(1-2*mask) := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
theorem gap_layer_size : aliasMargin < 1-2*mask-entropy (2*mask)/2-entropy mask := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_left_masks_cheaper : aliasMargin < entropy (1/2-mask)-entropy mask := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_guard_collision : aliasMargin < (eta-block*log2 3/2)/2-1/(1000000000000:Real) := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_remove_bad_halves : aliasMargin < (eta-block*log2 3/2)/2-(1/2-tau+zeta) := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
theorem gap_density_threshold : aliasMargin < 0.013-(1/2-tau+zeta) := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
def scalarGaps : List Real := [entropy (2*mask)/2-gamma,
tau-left-(entropy mask-gamma)*block,
tau-(1-block-left)-(1-gamma)*block,
tau-1+block-(entropy mask+entropy (1/2-mask)-gamma)*block+eta,
2*tau-1/2-entropy (1/2-mask)*block,
tau-left,
tau-(1-block-left),
1-block-left,
left-block*(1-2*mask),
eta-block*log2 3/2,
tau-block,
2*tau-1/2-(1-block-left)-zeta,
2*tau-1/2-zeta-gamma*block/2,
tau-eta/2,
1/2-block*(1-2*mask),
1-2*mask-entropy (2*mask)/2-entropy mask,
entropy (1/2-mask)-entropy mask,
(eta-block*log2 3/2)/2-1/(1000000000000:Real),
(eta-block*log2 3/2)/2-(1/2-tau+zeta),
0.013-(1/2-tau+zeta)]
theorem all_alias_gaps : ∀ g ∈ scalarGaps, aliasMargin < g := by
  simp only [scalarGaps,List.forall_mem_cons]
  exact ⟨gap_coverage, gap_left_list, gap_right_classes, gap_pairs, gap_right_masks, gap_left_map, gap_right_map, gap_right_positive, gap_sampled_map, gap_reduction, gap_block_classes, gap_right_key_sort, gap_small_prime, gap_prime_generation, gap_sampled_size, gap_layer_size, gap_left_masks_cheaper, gap_guard_collision, gap_remove_bad_halves, gap_density_threshold, (by simp)⟩
/-- Actual rational transfer margins, conditional on old moments only when
used to infer a new moment inequality. These arithmetic statements have no
old-integral hypotheses. -/
def transferredMargins : List Real :=
 [0.00025+eta-etaB-10.6428*transferK,
  0.00025+eta-etaB-lowShift,
  0.00025+eta-etaB-8.4537*(5/4)*transferK,
  4+eta-etaB-418.36*15*transferK,
  17+eta-etaB-418.36*256*(slope-slopeB)]
theorem transferred_margin_bounds : ∀ m ∈ transferredMargins, finiteMargin < m := by
  norm_num [transferredMargins,finiteMargin,eta,etaB,lowShift,weight,
    SubsetSum.FilterData.certificate_3_0,transferK,delta,ratio,budget,
    tau,deltaB,gammaB,slope,slopeB]
theorem error_work_and_absorption_gap :
    0 < finiteMargin-(18+6*419)*epsilon ∧
    tau+20*epsilon = 0.48767228002 ∧
    tau+20*epsilon < advertised ∧
    zeta+1/(1000000000000:Real) < aliasMargin ∧
    418.36*(1+(slope-slopeB)) < 419 ∧
    0 < slope ∧ slope < 1/4 := by
  norm_num [finiteMargin,epsilon,tau,advertised,zeta,aliasMargin,
    slope,slopeB,delta,budget,eta,deltaB,gammaB]
end
end Verification.Published
