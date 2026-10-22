import Verification.RowMargins

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace Verification.Published
noncomputable section

def firstBoundary (v : Fin 43) : Real := if v = 3 then budget else gammaB

def regionPredicate (v : Fin 43) (i : Fin 10) (W : Real) : Prop :=
  match i.val with
  | 0 => W ≤ firstBoundary v
  | 1 => firstBoundary v < W ∧ W ≤ bandTop
  | 2 => bandTop < W ∧ W ≤ (8/5)*gammaB
  | 3 => (8/5)*gammaB < W ∧ W ≤ 2*gammaB
  | 4 => 2*gammaB < W ∧ W ≤ (13/5)*gammaB
  | 5 => (13/5)*gammaB < W ∧ W ≤ (7/2)*gammaB
  | 6 => (7/2)*gammaB < W ∧ W ≤ 5*gammaB
  | 7 => 5*gammaB < W ∧ W ≤ 8*gammaB
  | 8 => 8*gammaB < W ∧ W ≤ 15*gammaB
  | _ => 15*gammaB < W

theorem first_boundary_order (v : Fin 43) : firstBoundary v < bandTop := by
  unfold firstBoundary
  split_ifs <;> norm_num [bandTop,budget,gammaB,tau,eta]

theorem region_existence (v : Fin 43) (W : Real) : ∃ i, regionPredicate v i W := by
  by_cases h0 : W ≤ firstBoundary v
  · exact ⟨0,h0⟩
  by_cases h1 : W ≤ bandTop
  · exact ⟨1,lt_of_not_ge h0,h1⟩
  by_cases h2 : W ≤ (8/5)*gammaB
  · exact ⟨2,lt_of_not_ge h1,h2⟩
  by_cases h3 : W ≤ 2*gammaB
  · exact ⟨3,lt_of_not_ge h2,h3⟩
  by_cases h4 : W ≤ (13/5)*gammaB
  · exact ⟨4,lt_of_not_ge h3,h4⟩
  by_cases h5 : W ≤ (7/2)*gammaB
  · exact ⟨5,lt_of_not_ge h4,h5⟩
  by_cases h6 : W ≤ 5*gammaB
  · exact ⟨6,lt_of_not_ge h5,h6⟩
  by_cases h7 : W ≤ 8*gammaB
  · exact ⟨7,lt_of_not_ge h6,h7⟩
  by_cases h8 : W ≤ 15*gammaB
  · exact ⟨8,lt_of_not_ge h7,h8⟩
  · exact ⟨9,lt_of_not_ge h8⟩

theorem region_disjoint (v : Fin 43) (W : Real) (i j : Fin 10)
    (hi : regionPredicate v i W) (hj : regionPredicate v j W) : i = j := by
  have hF := first_boundary_order v
  norm_num [bandTop,gammaB] at hF
  fin_cases i <;> fin_cases j <;>
    norm_num [regionPredicate,bandTop,gammaB] at hi hj ⊢ <;> linarith

/-- Every actual filter and every real score has exactly one region; endpoints
belong to the preceding closed-upper interval. This is separate from record coverage. -/
theorem full_region_partition (v : Fin 43) (W : Real) :
    ∃! i, regionPredicate v i W := by
  obtain ⟨i,hi⟩ := region_existence v W
  exact ⟨i,hi,fun j hj => region_disjoint v W j i hj hi⟩

end
end Verification.Published
