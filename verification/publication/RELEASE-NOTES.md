# Proposed v1.1.0: verification supplement

This verification supplement supplies validated enclosures for all 430 original continuous moment inequalities and Lean-checked components of the fixed-certificate and boundary-transfer analysis. The numerical validation has an explicit outside-Lean computational trust boundary. The complete Subset Sum running-time theorem remains conditional on the stated alias-coverage, checksum-estimator, and implementation claims.

The exponent remains **0.4876723**. This adds the verification supplement,
source project, validated moment evidence and pinned reproduction instructions
to the original conditional result; it does not replace the v1.0.0 proof or
change its fixed parameter tuple.

- Validated FLINT/Arb enclosures cover all 430 original continuous moment
  inequalities, including the stronger middle-region and tail thresholds.
- Lean component proofs cover the concrete boundary/data analysis, real
  logarithm/entropy bounds, fixed certificate margins, unique regions and
  all-row conditional analytic transfers. Their explicit mathematical
  premises are documented separately from transitive axioms.
- Written arguments establish the concrete analytic links and several inherited
  local algorithmic steps; the remaining full algorithmic claims stay explicit.

The historical stronger all-import replay timed out after five minutes.
The single new release-preparation attempt on `Verification.AllRows` also timed
out at its 900-second cap (901.47 seconds including termination). It emitted
no verdict or checker diagnostic. No sampled working-set value reached the
6 GiB stop threshold; monitoring was sampled, not a hard allocation cap.
The checker was terminated with no owned checker or child remaining. It was not
repeated or extended. The stronger replay remains unfinished; this is neither
a successful replay nor an identified proof rejection. Successful clean
project-source builds and axiom audits against pinned imports are recorded
separately. Exact source/executable identities, resource samples and termination
checks accompany `verification/publication/replay/attempt.json` and its
resource record; monitoring limitations and the final monitor diagnostic are
disclosed there separately from the checker timeout.

No Human Verified, Lean Verified, external peer-review or site-awarded status
is claimed. Internal review is by research agents. The numerical thresholds
retain the outside-Lean Python/FLINT/Arb and written-analysis trust boundary.

Attribution to OpenAI, Annanay Kapila and Joshua Wharton/QFEX remains in the
original source records and supplement. Existing agent-assistance disclosures
and third-party notices are preserved. No public tag, push or submission is
performed by this release-preparation task.
