"""Emit explicit Lean scalar goals, not proof-oracle numerical assumptions."""
from pathlib import Path

gaps=[
('coverage','entropy (2*mask)/2-gamma'),
('left_list','tau-left-(entropy mask-gamma)*block'),
('right_classes','tau-(1-block-left)-(1-gamma)*block'),
('pairs','tau-1+block-(entropy mask+entropy (1/2-mask)-gamma)*block+eta'),
('right_masks','2*tau-1/2-entropy (1/2-mask)*block'),
('left_map','tau-left'),('right_map','tau-(1-block-left)'),
('right_positive','1-block-left'),('sampled_map','left-block*(1-2*mask)'),
('reduction','eta-block*log2 3/2'),('block_classes','tau-block'),
('right_key_sort','2*tau-1/2-(1-block-left)-zeta'),
('small_prime','2*tau-1/2-zeta-gamma*block/2'),('prime_generation','tau-eta/2'),
('sampled_size','1/2-block*(1-2*mask)'),
('layer_size','1-2*mask-entropy (2*mask)/2-entropy mask'),
('left_masks_cheaper','entropy (1/2-mask)-entropy mask'),
('guard_collision','(eta-block*log2 3/2)/2-1/(1000000000000:Real)'),
('remove_bad_halves','(eta-block*log2 3/2)/2-(1/2-tau+zeta)'),
('density_threshold','0.013-(1/2-tau+zeta)')]
s='''import Verification.LogScalar
set_option autoImplicit false
set_option maxHeartbeats 0
namespace Verification.Published
noncomputable section
theorem log_three_coarse : log2 3 <= 2 := by
  have h := Real.log_le_log (by norm_num : (0:Real) < 3) (by norm_num : (3:Real) <= 4)
  rw [show (4:Real) = 2^2 by norm_num, Real.log_pow] at h
  norm_num at h
  unfold log2
  apply (div_le_iff\u2080 (Real.log_pos (by norm_num : (1:Real) < 2))).2
  nlinarith
'''
for name,g in gaps:
    if 'entropy' not in g and 'log2' not in g:
        s+=f'''theorem gap_{name} : aliasMargin < {g} := by
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta]
'''
        continue
    s+=f'''theorem gap_{name} : aliasMargin < {g} := by
  have ha := entropy_a
  have h2a := entropy_twoa
  have hhalf := entropy_hma
  have h3 := log_three_coarse
  norm_num [aliasMargin,mask,tau,eta,block,gamma,left,zeta] at *
  nlinarith [ha.1,ha.2,h2a.1,h2a.2,hhalf.1,hhalf.2]
'''
s+='def scalarGaps : List Real := ['+',\n'.join(g for _,g in gaps)+']\n'
s+='theorem all_alias_gaps : \u2200 g \u2208 scalarGaps, aliasMargin < g := by\n  simp only [scalarGaps,List.forall_mem_cons]\n  exact '+ '\u27e8'+', '.join('gap_'+name for name,_ in gaps)+', (by simp)\u27e9\n'
s+='''/-- Actual rational transfer margins, conditional on old moments only when
used to infer a new moment inequality. These arithmetic statements have no
old-integral hypotheses. -/
def transferredMargins : List Real :=
 [0.00025+eta-etaB-10.6428*transferK,
  0.00025+eta-etaB-lowShift,
  0.00025+eta-etaB-8.4537*(5/4)*transferK,
  4+eta-etaB-418.36*15*transferK,
  17+eta-etaB-418.36*256*(slope-slopeB)]
theorem transferred_margin_bounds : \u2200 m \u2208 transferredMargins, finiteMargin < m := by
  norm_num [transferredMargins,finiteMargin,eta,etaB,lowShift,weight,
    SubsetSum.FilterData.certificate_3_0,transferK,delta,ratio,budget,
    tau,deltaB,gammaB,slope,slopeB]
theorem error_work_and_absorption_gap :
    0 < finiteMargin-(18+6*419)*epsilon \u2227
    tau+20*epsilon = 0.48767228002 \u2227
    tau+20*epsilon < advertised \u2227
    zeta+1/(1000000000000:Real) < aliasMargin \u2227
    418.36*(1+(slope-slopeB)) < 419 \u2227
    0 < slope \u2227 slope < 1/4 := by
  norm_num [finiteMargin,epsilon,tau,advertised,zeta,aliasMargin,
    slope,slopeB,delta,budget,eta,deltaB,gammaB]
end
end Verification.Published
'''
s=s.replace('<=','\u2264')
Path('Verification/Scalar.lean').write_text(s,encoding='utf-8')
