# Conditional Subset Sum exponent 0.4876723

**Intended author: Yanni Bills. Prepared locally; not published or submitted.**

This note proves a conditional refinement to `O_c(2^(0.4876723 n))` in the
Big O Speedrun randomized word-RAM model. The internal total work exponent is
`0.48767228002`, leaving a strict `0.00000001998` absorption gap. It changes
the justified analysis and construction parameters, rather than advertising
unused slack in an existing theorem.

The contribution is a moved-boundary use of filter 3's existing certificates:
its low certificate stops at the new sampling boundary, while a zero
lower-boundary multiplier permits extending the next certificate downward.
The note proves domination, integral identities, complete region coverage,
rounding/error budgets and ordinary-O absorption. Exact rational checks
establish the new scalar feasibility conditions.

## What remains conditional

The OpenAI/Kapila isolation, implementation, alias/preliminary-search and
finite-circle arguments, and the original 430 continuous moment inequalities,
remain explicit inherited premises. They are identified in the note and
`source-audit/`. The checker does not prove those integrals or execute a
Subset Sum solver. No unresolved new mathematical step is being substituted
as an inherited assumption. Independent review assesses the full conditional
implication, separately from code execution.

No Lean toolchain was available in the inspected environment; no Lean build,
axiom audit of a new formal theorem, or site verification is claimed.
See `numerics/FORMALIZATION-SCOPE.md`. The campaign's mathematical proof and
its missing formalization are different matters.

The leaderboard checked on 21 October 2026 displays Wharton's conditional
`0.487676`; our exponent is lower by `0.0000037`. This is a local proposed
conditional refinement, not an awarded leaderboard position or an
unconditional breakthrough. See `source-audit/final-live-observation.json`
and the bounded source/priority audit. No global novelty guarantee is implied.

## Read and reproduce

- `paper.pdf`: mathematical note, with proofs and exact-certificate appendix.
- `paper.tex`, `candidate-data.tex`, `certificate-appendix.tex`,
  `references.bib`: complete Overleaf source; select `paper.tex` as main.
- `review.md` and `review/`: independent findings, corrections and evidence.
- `submission-draft.md`: unsent publication/submission text and next steps.
- `numerics/`: exact checker, fixed candidate, negative tests, discovery
  code/record, source pins and implementation attribution.
- `source-audit/`: source revisions, dependencies, access scope and priority.

From this repository root, with Python 3.12 (standard library only):

```sh
python numerics/fetch_baseline.py
python numerics/verify_certificate.py
python numerics/test_rejections.py
```

The first command fetches one pinned, SHA256-verified manuscript into ignored
local storage; the next two work offline. To use an existing copy instead,
append `--baseline /path/to/PROOF_0.4877.tex` to both check commands. Required
hash: `b397531cc5997e88c439d5290774861b46a34aa32d9cd71fa7dcced130359298`.
No unlicensed full upstream manuscript or code is redistributed.

To rebuild the PDF with Tectonic 0.17:

```sh
tectonic paper.tex
```

LaTeX with BibTeX is another build route. The Overleaf ZIP contains only the
four required source files. Discovery is optional and separate: its 24
single-process starts with seed 20261021 recorded a batch time of about
0.447 seconds (0.4465753000113182 in `numerics/evidence/discovery.json`), using Python 3.12.14,
NumPy 2.2.6 and SciPy 1.15.3. This is parameter-search time, not a Subset Sum
solver runtime. See `numerics/README.md`; verification never reruns search.

## Credit and permissions

The algorithmic framework is inherited from OpenAI and Annanay Kapila;
Joshua Wharton supplied the earlier parameter/certificate-transfer refinement.
AI assistance and the distinct team roles are acknowledged in the note.
Pinned sources and numerical constants are credited in the provenance files.
No upstream license is invented, and no blanket repository license is applied
to third-party material. Publication and any outbound submission require
Yanni's separate authorization. No remote is configured by this campaign.
