# Final correction pass (21 October 2026)

The preserved delivered baseline is commit
`639d9d13fce9a291c6c00a565dc5ffefda9c2b78` (local tag
`delivered-v1-2026-10-21`). The conditional result and selected tuple are
unchanged: advertised exponent **0.4876723**, internal **0.48767228002**.

- Defined LD from pinned Kapila Sections 2.1 and 4, condition (LD), and
  Appendix B.1. It is the existing low-deficiency case distinction for fixed
  transformed weights and uniformly sampled half-blocks, not a new assumption
  on all inputs. No filter-3 formula or proof was changed.
- Corrected the unsupported 3.21/3.2-second prose to the preserved
  **0.4465753000113182-second** timer for the 24-start seed-20261021 discovery
  batch. Its `perf_counter` interval covers the search batch, excluding imports
  and final JSON writing. No separate recorded run supports 3.21 seconds.
  This is parameter-search time, not solver runtime. Discovery was not rerun;
  raw discovery and numerical evidence were not edited.
- Decoded the two review files strictly as Windows-1252 and encoded them as
  UTF-8. The conversion stage preserved their Unicode text exactly and
  round-tripped to the original bytes, including en/em dashes. Subsequent
  removal of the early review's workstation path is separate documentary
  sanitation. All selected text is checked by strict UTF-8 decoding.
- Removed workstation path metadata from public documentary copies and
  omitted five operational files: `PLAN.md`, `review/RESUME.md`,
  `numerics/HANDOFF.md`, `source-audit/SOURCE_LOCATIONS.txt`, and the
  private-command-path `numerics/evidence/environment.json`. Their original
  bytes remain in the preserved baseline. Runtime versions remain documented;
  all necessary mathematical and executable evidence is retained.
- Replaced the local submission checklist with ready-to-paste conditional
  text and one marked public-repository-URL placeholder. Removed a stale
  future-action sentence from the bibliography after checking the official
  pages again. No public repository or submission has been made.

The numerical producer's `numerics/manifest.json` is deliberately unchanged:
it authenticates its historical snapshot, including subsequently corrected
documentation and the omitted private environment record. The new
`release-manifest.json` identifies the selected corrected publication files;
it is the release integrity manifest. Historical review hash records also
refer to their named earlier snapshots, not the corrected manuscript.

All executable files, the selected candidate, floating discovery log,
certificate outputs, rejection evidence and supporting transfer argument are
protected against the baseline. The appendix's timing sentence and
bibliography's observation note are the only authorized textual exceptions
among the additionally monitored TeX files; their mathematical content is
unchanged. Baseline and final hashes and authorized omissions are recorded
with release verification.

The result remains conditional on the inherited algorithmic claims and
original continuous moments. The checkers do not establish those integrals.
No new Lean development or complete implemented solver was delivered, and
local agent review does not confer a site verification category. Intended
submission category is conditional **Claimed**, not an awarded status.

The exact clean-release executions, build and final independent disposition
are recorded in `evidence/release-checks.json`, `evidence/release-build.json`
and the correction addendum to `review.md`.
