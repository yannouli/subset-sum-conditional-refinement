# Historical reviewer helpers

The following files are preserved historical review artifacts, **not portable
reproduction entry points**:

- `verification/review/moment-audit.py`: uses the reviewer's original absolute
  source/evidence paths and local imports.
- `verification/review/check-transcription.py`: uses original absolute source
  paths and local review-copy imports.

Do not execute them as the public package's verification commands. Their
unchanged bytes and original receipts document what was inspected then;
packaging does not retroactively make those executions portable.

Use the portable commands in `verification/README.md` instead: the authenticated
fetcher, full moment validator, direct-sum selfcheck, project Lean build and
statement/axiom audits. The independent baseline scalar checker at
`review/independent_check.py` accepts all three paths explicitly. It checks the
fixed scalar certificate, not the continuous integrals.

Portable counterparts now appear under `verification/publication/reproduce/`:
`check_transcription.py` accepts explicit source/data/output paths and checks
all 43 filters and 430 records; `check_moment_outputs.py` accepts explicit
source/reference/replay/output paths and checks pair coverage, thresholds,
strict endpoint separation, positivity and exact mathematical-output agreement.
Their README gives the commands. They do not replace the actual continuous
validator or a Lean proof. They leave both historical helpers unchanged.

The generated Lean data modules are included. No regeneration is necessary to
build the project; the read-only portable transcription check authenticates
them against the pinned source. The historical generator remains available
for a disposable-copy regeneration if desired; its emitted literal equalities
are checked by Lean rather than trusted because they were generated.

The original historical manifests cover their recorded files and versions,
not the changed README or this entire new release tree. Consult the new public
package manifest and external archive checksums for the release's exact scope.
