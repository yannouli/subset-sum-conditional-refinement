# Intended formal statements: review before proofs

Published baseline: v1.0.0 / 5380ae2c6411f70769df6076ca82a54d43ff09c3.
Concrete definitions are in `Verification/Concrete.lean`. They use actual
finite filter/certificate records from the pinned Wharton dependency, exact
published constants, the original entropy-score integrals and normalized
Lebesgue integration over the whole period. No theorem is proved yet.

The following are intended Lean theorem headers in namespace
`Verification.Published`; these are goals, never assumed certificate predicates.
All coefficient/transcription comparisons will be checked separately against
the pinned original source, not inferred from an upstream README.

```lean
theorem exact_special_rows :
  SubsetSum.FilterData.certificate_3_0.comparisons = [5,16] ∧
  SubsetSum.FilterData.certificate_3_1.comparisons = [5,8,16,35] ∧
  weight SubsetSum.FilterData.certificate_3_1 1 = 0 ∧
  weight SubsetSum.FilterData.certificate_3_1 0 = 7.7547

theorem low_pattern_domination (U : Fin 43 → ℝ) (W : ℝ)
  (hregion : W ≤ budget)
  (hselect : ∀ j ∈ SubsetSum.FilterData.certificate_3_0.comparisons, U j ≤ U 3)
  (hsample : SubsetSum.samplingFraction budget W * U 3 < delta) :
  -SubsetSum.samplingFraction budget W * U 3 ≤
    -delta + lowExponent delta budget U W

theorem extended_pattern_domination (U : Fin 43 → ℝ) (W : ℝ)
  (hlower : budget < W) (hupper : W ≤ bandTop)
  (hselect : ∀ j ∈ SubsetSum.FilterData.certificate_3_1.comparisons, U j ≤ U 3)
  (hsample : SubsetSum.samplingFraction budget W * U 3 < delta) :
  -SubsetSum.samplingFraction budget W * U 3 ≤
    -delta + bandExponent slope budget newUpperWeight U W

theorem concrete_low_shift : ∀ x : ℝ, newLow x = oldLow x + lowShift
theorem concrete_band_shift : ∀ x : ℝ, newBand x = oldBand x + bandShift

theorem concrete_low_moment_identity :
  Integrable (integrand oldLow) circleDomain ∧
  Integrable (integrand newLow) circleDomain ∧
  0 < moment oldLow ∧ moment newLow = exp2 lowShift * moment oldLow

theorem concrete_band_moment_identity :
  Integrable (integrand oldBand) circleDomain ∧
  Integrable (integrand newBand) circleDomain ∧
  0 < moment oldBand ∧ moment newBand = exp2 bandShift * moment oldBand
```

These unconditional concrete integral goals require proving the analytic
regularity/positivity of the actual functions in `Concrete.lean`; we will not
silently replace them by hypotheses or totalized-zero integrals. Any separately
proved conditional generic shift theorem will be labeled as such until the
concrete analytic obligations are discharged. `uEval=u` and `wEval=w`, positive
normalizers/P, continuous scores and the coarse bound `|w v x|≤256` are separate
explicit proof goals linked to Ed's C0 contract. Integrals never use a region
restriction; only pattern-domination hypotheses use score regions.

Coverage goal: for every filter v and real W there is exactly one region i.
For v=3 the regions are W≤budget, budget<W≤bandTop, then the old upper
endpoints 1.6,2,2.6,3.5,5,8,15 times gammaB, followed by W>15gammaB.
For other filters replace the first boundary by gammaB. Each finite endpoint
belongs to its preceding region. The closed fixed-data theorem must identify
the exact ordered sequence of all (v,i), v=0..42,i=0..9, and connect each
certificate's actual multipliers to its new affine exponent and margin.

Fixed-data goals: actual real-log/entropy enclosures imply all released
alias/auxiliary gaps exceed 1e-10; all 430 transferred margins exceed 1e-7
under precisely the released original-moment hypotheses; every modified
multiplier sum is below 419; residual error exponent=9.7468e-8; beta=.48767228002
and advertised-beta=1.998e-8. The last theorem will instantiate the generic
little-o/ordinary-O absorption result with these exact constants and sublinear
overhead, not assert an unimplemented program's cost theorem.

Original continuous moment hypotheses remain open pending the separate
validated integration pilot. Finite-circle convergence and end-to-end
algorithmic guarantees remain explicit obligations rather than Lean axioms.
