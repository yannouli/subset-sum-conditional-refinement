# Verification supplement: scope and reproduction

This verification supplement supplies validated enclosures for all 430 original continuous moment inequalities and Lean-checked components of the fixed-certificate and boundary-transfer analysis. The numerical validation has an explicit outside-Lean computational trust boundary. The complete Subset Sum running-time theorem remains conditional on the stated alias-coverage, checksum-estimator, and implementation claims.

The exponent and fixed inputs are unchanged. The published v1.0.0 baseline is
`5380ae2c6411f70769df6076ca82a54d43ff09c3`; the reviewed verification source is
`f2edf57c17a555d31302e68dd2ec43722a249e56`. The original paper and historical
receipts remain intact; root README additions describe the later supplement.

Start with `verification.pdf`, `publication/SCOPE.md`,
`theory/obligations.json` and `lean/FINAL_SCOPE.md`. The theorem-to-manuscript
mapping is in `theory/formal-results.tex`; review evidence is in `review/`.
Internal agent review is not independent human peer review or website verification.

## Numerical reproduction

Use a disposable extraction and a dedicated Python 3.12 environment. From the
**repository root**, install the pinned numerical requirement:

```sh
python -m pip install -r verification/moments/requirements.txt
python -c "from pathlib import Path; Path('verification/publication/reproduce/fresh-run').mkdir(parents=True, exist_ok=False)"
python numerics/fetch_baseline.py --output verification/publication/reproduce/fresh-run/PROOF_0.4877.tex
python verification/moments/selfcheck.py --source verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --output verification/publication/reproduce/fresh-run/direct-sum.json
python verification/moments/validate.py --source verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --output verification/publication/reproduce/fresh-run/all-moments.json --all
```

The fetcher retrieves the recorded Kapila revision and verifies SHA256
`b397531cc5997e88c439d5290774861b46a34aa32d9cd71fa7dcced130359298`.
No agent-workspace path is needed. The requirement is `python-flint==0.8.0`.
Use new output filenames for every execution; do not overwrite accepted or
historical evidence, including when following older subordinate instructions.

The full validator checks all 43 filters and 430 distinct filter/region pairs,
positive denominators, inner enclosures, the common zero-free strip and outer
analytic errors. Thresholds use old margins .00025 in regions 0/1, 4 in
regions 2--8 and 17 in the tail. Certification requires strict separation
between the integral's upper enclosure and the threshold's lower enclosure.
A failed sufficient bound is unresolved, not automatically a counterexample.

Accepted `evidence/all-moments.json` has SHA256
`9646407eba82509f62c6464293d9fb472370d2e2c08a45ae07636c7bd0c84476`.
Compare mathematical enclosures, thresholds, pairs and statuses; execution
seconds and environment records can differ without changing those results.
The numerical calculation relies on Python/bindings, FLINT/Arb elementary
functions and DFT arithmetic, the authenticated parser and written analytic
error bounds. Neither floating-point grid agreement nor the baseline scalar
checker substitutes for this continuous-integral validation.

Run the original regression checks separately, still from the repository root:

```sh
python numerics/verify_certificate.py --baseline verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --output verification/publication/reproduce/fresh-run/scalar.json
python numerics/test_rejections.py --baseline verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --output verification/publication/reproduce/fresh-run/rejections.json
python review/independent_check.py numerics/data/candidate.json verification/publication/reproduce/fresh-run/PROOF_0.4877.tex verification/publication/reproduce/fresh-run/independent.json
```

The explicit-path transcription and moment-output comparison commands are in
`publication/reproduce/README.md` and `moments/README.md`. They check every
record and the exact replay enclosures without changing historical helpers.

These baseline commands check fixed scalar calculations, all eight rejection cases and the
independent 430-row certificate calculation. They do not run a Subset Sum solver
or parameter search. Two older reviewer helpers are historical and path-specific;
see `publication/HISTORICAL-REVIEW.md` for their names and portable alternatives.

## Lean source build and statement/axiom checks

Use Lean **4.24.0** and the exact dependency revisions in
`lean/lake-manifest.json`; keep that lockfile unchanged. Wharton's dependency
revision is `bed8e18f96db5955c1424abf3005b4fed4bd8d77`, mathlib is
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. Dependency source downloads and
compatible caches may be reused, but project build outputs must not substitute
for a clean build of the packaged sources. Follow `lean/README.md` for the pinned setup and compatible cache retrieval;
no caches or installed toolchain are bundled.

From **verification/lean**, after preparing those dependencies:

```sh
lake build +Verification
lake env lean Audit.lean
lake env lean AuditScalar.lean
```

These execute the final project sources and print statements and transitive
axioms. The accepted foundational scope is `propext`, `Classical.choice` and
`Quot.sound`. A clean axiom report does not establish a theorem's explicit
hypotheses. In particular, the all-row moment theorem assumes old moment
bounds and `w_v(x) <= 256`; the accepted numerical evidence and written score
proof supply those separately. Reduced-score correspondence and ordinary
sampled-pattern assembly retain written proofs. Ordinary-O absorption is
conditional on the algorithm's actual resource premise.

Source build, source replay against pinned built imports, statement review,
axiom audit and fresh replay of every imported declaration are different checks.
The historical five-minute all-import fresh attempt timed out. The one new
release-preparation attempt on `Verification.AllRows` also timed out under its
900-second cap (901.47 seconds including termination). The direct checker was
killed and waited for, and follow-up found no owned checker or child remaining.
It emitted no checker verdict or diagnostic. No sampled working-set value
reached the 6 GiB stop threshold; this was sampled monitoring, not a hard
allocation cap. The stronger replay is therefore **unfinished**, not passed;
no proof rejection was identified by this attempt. It was not repeated or
extended. The separate successful clean source build and statement/axiom audits
remain the applicable completed formal checks. The frozen receipt and resource
samples are in `publication/replay/attempt.json` and `resources.jsonl`.
The receipt also records the initial sampling-setup gap and the monitor's
termination identity-guard diagnostic separately from the checker outcome.
The corrected single-leaf command, from **verification/lean**, after the pinned
checker setup in `lean/README.md`, is:

```sh
lake env ../../.verification-tools/lean4checker/.lake/build/bin/lean4checker.exe --fresh Verification.AllRows
```

`Verification.AllRows` imports the complete project chain. The checker treats
its argument as a prefix; `Verification` selects multiple modules and is not
a valid fresh-replay entry point. This is a command-selection issue, not a
proof rejection. Use reliable finite supervision, as documented in the replay
receipt; the command alone supplies no resource cap. No removed timeout wrapper
is restored. No automated Comparator or site verification is implied.

## Supplement and evidence records

From **verification/**, build the local sources and bibliography:

```sh
tectonic verification.tex
```

A standard LaTeX/BibTeX workflow is also suitable. The Overleaf archive is made
from these same typesetting inputs; select `verification.tex` as the main file.
The manuscript records full arguments and remaining assumptions, not a complete
Lean proof of the algorithm. Alias coverage/caps, checksum-estimator correctness
and precision, and full word-RAM implementation/resource claims remain conditional.

Historical evidence and source pins retain their original versions. New release
outputs and manifests authenticate the final public tree separately; a historical
manifest does not cover an edited README or later supplement. Archive checksums
belong outside the archives they authenticate. Review receipts document internal
agent checks and their exact source identities, not independent human review.
