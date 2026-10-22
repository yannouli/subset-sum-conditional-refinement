# Verification scope

This verification supplement supplies validated enclosures for all 430 original continuous moment inequalities and Lean-checked components of the fixed-certificate and boundary-transfer analysis. The numerical validation has an explicit outside-Lean computational trust boundary. The complete Subset Sum running-time theorem remains conditional on the stated alias-coverage, checksum-estimator, and implementation claims.

The advertised exponent remains **0.4876723**, with internal work exponent
0.48767228002. The public v1.0.0 baseline is
`5380ae2c6411f70769df6076ca82a54d43ff09c3`; the reviewed verification source is
`f2edf57c17a555d31302e68dd2ec43722a249e56`. Release-preparation commits change
packaging, documentation and separately recorded reproduction support, not
proofs, fixed inputs or historical receipts.

## Evidence and remaining premises

- **Written proofs:** concrete score bounds and reduced-score identities,
  validated-integration error analysis, effective finite-circle approximation,
  isolation, the preliminary-search/low-deficiency case split, structural alias
  soundness and a conditional alias-output precision bound.
- **Validated numerical evidence:** every pair in `{0,...,42} x {0,...,9}`,
  using the actual full-circle integrands and region-specific thresholds.
  The old margin is .00025 in regions 0/1, 4 in regions 2--8 and 17 in region 9.
  All 430 upper enclosures are strictly below the corresponding lower threshold
  endpoints. Trust includes Python, its bindings, FLINT/Arb elementary functions
  and DFT arithmetic, the authenticated source parser, and written error proofs.
  These numerical thresholds are not Lean theorems.
- **Lean results:** concrete filter-3 pattern domination and full-circle shifts,
  positive integrable moments, exact 43-filter/430-record bridges and dimensions,
  actual real-log/entropy bounds, fixed gaps and margins, unique region assignment,
  all-row analytic moment transfers and conditional ordinary-O absorption.
  The all-row moment theorem explicitly assumes the old moment bounds and
  `w_v(x) <= 256`; these are discharged outside Lean and by written proof,
  respectively. Reduced-score correspondence and ordinary-region sampled-pattern
  assembly also remain written. The runtime absorption theorem does not prove
  that the complete algorithm meets its resource premise.
- **Review/reproduction:** internal agent review and actual source builds with
  pinned built imports are recorded separately from mathematical hypotheses.
  The permitted transitive foundational axioms are `propext`, `Classical.choice`
  and `Quot.sound`. No complete Lean proof of the algorithm is claimed.

The unresolved algorithmic obligations are alias probabilistic coverage and
caps, checksum-estimator correctness/probability and precision, and complete
word-RAM implementation/resource accounting. They remain conditions, not tasks
that must be completed to publish this accurately scoped supplement.

## Stronger replay and external status

The historical five-minute all-import `lean4checker --fresh` attempt timed out.
That is distinct from the successful project-source builds and axiom audits.
The single release-preparation attempt on `Verification.AllRows` also timed
out under the 900-second cap: 901.47 seconds including termination and one thread.
No sampled working-set value reached the 6 GiB stop threshold; sampled
monitoring is not a hard allocation cap. No checker verdict or diagnostic
was emitted; the checker was killed and waited for and follow-up found no owned
checker or child remaining. This is unfinished stronger replay, not success
or an identified proof rejection. It was not repeated or extended. The receipt,
resource samples and termination checks are preserved in `replay/attempt.json`
and `replay/resources.jsonl`, including the sampling-setup gap and monitor's
final identity-guard diagnostic. Neither is a checker rejection.
This disclosed limit does not erase the successful clean source builds and
statement/axiom audits, and does not make the conditional theorem unconditional.
No automated Comparator result or external/site verification is asserted.
A Claimed listing, internal review, numerical validation and Lean component
proofs do not imply Human Verified, Lean Verified or external peer review.
