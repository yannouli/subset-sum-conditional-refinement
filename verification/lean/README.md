# Concrete boundary verification checkpoint

This describes the initial accepted boundary checkpoint. The final combined
target is `Verification`; see FINAL_SCOPE.md for the later scalar/region/row
targets, actual analytic premises and direct reproduction commands.

The completed target is `Verification.DataBridge`, importing `Concrete`,
`Boundary` and `Regularity`. It defines the actual normalized full-period
entropy-score moments and proves strict positivity, integrability, the two
filter-3 full-circle shifts, sampling/domination including the moved interval,
and endpoint coverage. The data bridge proves equality of all 43 filters and
430 records to a separate exact transcription of the authenticated primary
tables, exact pair coverage, list dimensions, comparison uniqueness, no
lookup fallback, no zip truncation, and the tighter non-special low cap.

Use Lean 4.24.0. From `verification/lean`, retain `lake-manifest.json` and its
fixed dependency revisions. The commands for the final combined project are:

```
lake exe cache get
lake build +Verification
lake env lean AuditScalar.lean
```

`AuditScalar.lean` prints final statements and their transitive axioms; the
historical `Audit.lean` remains available for the initial boundary checkpoint. Only
`propext`, `Classical.choice` and `Quot.sound` appear in the producer report.
No accepted chain uses sorry, native evaluation or a custom mathematical
axiom. Read the definitions/hypotheses as well as the axiom list; a build
does not by itself establish correspondence to the manuscript.

Compatible `lean4checker` source is pinned to
`da26eb05e9959402afcb9bd6dfe5dc4f700f70d6` (v4.24.0).
For a local Windows checker build, run these commands from the repository
root. The checkout is an external dependency, excluded from the public ZIP:

```
git clone --no-checkout https://github.com/leanprover/lean4checker.git .verification-tools/lean4checker
git -C .verification-tools/lean4checker checkout --detach da26eb05e9959402afcb9bd6dfe5dc4f700f70d6
lake --dir .verification-tools/lean4checker build lean4checker
```

From `verification/lean`, the actual resulting Windows executable is:

```
lake env ../../.verification-tools/lean4checker/.lake/build/bin/lean4checker.exe --fresh Verification.AllRows
```

The pinned checker requires exactly one module selection for `--fresh`.
Its argument is a prefix: `Verification` would select the root and all its
submodules and is therefore unsuitable. `Verification.AllRows` is the single
leaf importing the complete proved chain; the root contains only that import.
This stronger replay includes every imported declaration. It is distinct from
a clean project-source build against pinned dependency caches.

The historical five-minute attempt on the earlier boundary target timed out;
its receipt remains in `../evidence/boundary-checkpoint/`. The single new
publication attempt on 2026-10-22 also timed out at its 900-second limit
(901.47 seconds including termination), with no checker verdict or diagnostic.
It was not repeated or extended; its receipt and sampled resources are under
`../publication/replay/`. Fresh replay of every imported declaration remains
unfinished. Do not infer
success from a build or from this command being documented. Use reliable
bounded supervision for the stronger command; no custom timeout wrapper is
included. This pinned Lake has no Comparator command, and no external checker
or site verification status is claimed. Standard kernel/library/toolchain
trust and independent statement-meaning review remain explicit.

The later scalar/logarithm modules have a separate final checkpoint and review.
The moment enclosures are outside Lean. This checkpoint is not a formal proof of the full
Subset Sum algorithm, probabilistic coverage, or the continuous thresholds.
The unchanged published result remains explicitly conditional.

The generated constants are included and do not require regeneration to
build. The historical generator expects an authenticated source at
`verification/evidence/PROOF_0.4877.tex`; it remains unchanged. The portable
`../publication/reproduce/check_transcription.py` accepts an explicit fresh
source path and checks the included data without overwriting any proof file.
The generator is not trusted: Lean checks the emitted exact record equalities.
Imported mathematical data and reusable transfer proofs are attributed to
Joshua Wharton/QFEX and Kapila, with immutable Git pins in the Lake project;
their repository license notices remain in the fetched dependency.
