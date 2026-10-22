# One bounded stronger replay

The 2026-10-22 attempt is **incomplete: timed out**. It ran the pinned
`lean4checker.exe --fresh --verbose Verification.AllRows` directly from
`verification/lean`, using the environment resolved by pinned Lake.
The 900-second timeout plus process termination took 901.47 seconds. There
was no retry or extension. No checker verdict or diagnostic was emitted;
the empty `checker.log` does not establish a successful replay.

The source came from authenticated candidate-01. Its 144 regular files
remained unchanged after execution. Project build artifacts were initially
absent; the packaged project was built successfully before this attempt.
Only the ten identified pinned dependency-package installations were reused.
The executable, source, project module and newly built olean hashes are in
[attempt.json](attempt.json).

Standard-library `subprocess.run(timeout=900)` supervised the checker directly
and killed and waited for it at timeout. Its inspected fresh path performs
the replay in process. Native sampling targeted 20 seconds and a monitored
6 GiB working-set stop ceiling. The 43 samples peaked at 4,912,455,680 bytes;
no sampled value reached the stop threshold. The initial sampling setup produced one
40.70-second interval; later intervals were about 20 seconds. These are
sampled values, not a hard allocation cap or an instantaneous peak.
See [resources.jsonl](resources.jsonl).

The sampling monitor's final identity guard stopped without acting on a
changed identity. A subsequent process query confirmed no owned checker or
child remained. The transient identity was not recoverable; no replacement
process was acted on. This monitor diagnostic is recorded separately from
the checker timeout and is not a checker rejection.

This receipt adds a bounded execution outcome. It does not replace the
separate clean source-build, axiom/statement audits, numerical validation or
independent source review. Fresh replay of every imported declaration remains
unfinished. No mathematical source, certificate, pin or historical evidence
was changed, and no external verification status is claimed. New public
metadata omits workstation paths and process identifiers; the unmodified raw
records remain available locally to the independent reviewer.
