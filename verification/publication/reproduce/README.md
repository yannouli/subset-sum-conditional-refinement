# Portable executable reproduction support

Run from the repository root with the isolated Python 3.12 environment and
`verification/moments/requirements.txt`. Follow `verification/README.md` for
the release-level scope and environment setup. All outputs below go into the
new `fresh-run` directory created by `verification/moments/README.md`.

After the authenticated fetch and full continuous-moment run documented there:

```
python numerics/verify_certificate.py --baseline verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --output verification/publication/reproduce/fresh-run/scalar.json
python numerics/test_rejections.py --baseline verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --output verification/publication/reproduce/fresh-run/rejections.json
python review/independent_check.py numerics/data/candidate.json verification/publication/reproduce/fresh-run/PROOF_0.4877.tex verification/publication/reproduce/fresh-run/independent.json
python verification/publication/reproduce/check_transcription.py --source verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --lean-data verification/lean/Verification/DataBridge.lean --output verification/publication/reproduce/fresh-run/transcription.json
python verification/moments/selfcheck.py --source verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --output verification/publication/reproduce/fresh-run/direct-sum.json
```

The original scalar checker and its eight rejection tests are regression
checks. They do not replace the full continuous-moment calculation. The
independent scalar checker checks every one of the 430 records under its
documented inherited premises. `check_transcription.py` compares all 43
filters and all 430 ordered records against the authenticated primary tables.
`check_moment_outputs.py` checks exact pair coverage, every required threshold,
strict endpoint separation, denominator positivity and mathematical-output
correspondence with the delivered evidence. It ignores measured timing changes.
The actual validator and its written analytic error theorem are still required;
the output checker alone cannot establish an integral inequality.

Both portable checkers accept explicit input/output paths and reject an
existing output file. They adapt the corresponding historical checks, leaving
the original reviewer scripts and their receipts intact. The originals
`verification/review/moment-audit.py` and `verification/review/check-transcription.py`
contain workstation paths and are historical review artifacts, not portable
reproduction entry points. Do not execute them for this release.

The generated Lean modules are already included. The transcription check is
read-only; no generator or proof edit is needed to rebuild them. See
`verification/lean/README.md` for the pinned source-build, statement/axiom audit
and the correct single-leaf stronger-replay command.

`fresh-run/`, isolated Python environments, `.verification-tools/` and `.lake/`
are local execution/dependency directories. They are excluded from the source
and manual-upload archives. Save new evidence separately; the accepted
`verification/evidence/` records remain historical and unchanged.
