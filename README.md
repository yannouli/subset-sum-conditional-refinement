# Conditional Subset Sum exponent 0.4876723

**Author: Yanni Bills.** Public repository: https://github.com/yannouli/subset-sum-conditional-refinement. Listed on the [Big O Speedrun Subset Sum leaderboard](https://bigospeedrun.com/subset-sum) as **Claimed** (rank 1 on 21 October 2026).

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

The original v1.0.0 note records its inherited algorithmic and continuous-moment
premises. The separately documented [verification supplement](verification/README.md)
reduces those premises without changing the exponent or rewriting that note.

This verification supplement supplies validated enclosures for all 430 original continuous moment inequalities and Lean-checked components of the fixed-certificate and boundary-transfer analysis. The numerical validation has an explicit outside-Lean computational trust boundary. The complete Subset Sum running-time theorem remains conditional on the stated alias-coverage, checksum-estimator, and implementation claims.

The supplement distinguishes reviewed written arguments, validated FLINT/Arb
calculations and Lean theorems with explicit hypotheses. Internal agent review
and source replay are not independent human peer review or a site-awarded status.
The historical `numerics/FORMALIZATION-SCOPE.md` describes v1.0.0; the current
formalization scope is [verification/lean/FINAL_SCOPE.md](verification/lean/FINAL_SCOPE.md).

On 21 October 2026, Big O Speedrun listed this conditional result at rank 1
with evidence level **Claimed**, ahead of Wharton's earlier conditional
`0.487676` by `0.0000037`. The [listing](https://bigospeedrun.com/subset-sum)
confirms publication and problem matching; it is **not** independent proof
review, Lean verification, or an unconditional algorithmic breakthrough.
`source-audit/final-live-observation.json` preserves the pre-submission
snapshot; the bounded source/priority audit does not guarantee global novelty.

## Read and reproduce

- `verification/verification.pdf` and `verification/README.md`: verification supplement and reproduction instructions.
- `paper.pdf`: original mathematical note, with proofs and exact-certificate appendix.
- `paper.tex`, `candidate-data.tex`, `certificate-appendix.tex`,
  `references.bib`: complete Overleaf source; select `paper.tex` as main.
- `review.md` and `review/`: independent findings, corrections and evidence.
- `submission-draft.md`: archived draft submission wording and listing status
  (not a verbatim transcript of the Discord post).
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
to third-party material. The author published the public repository and
subsequently submitted it to Big O Speedrun; the entry is listed as **Claimed**
as of 21 October 2026. The completed agent campaign itself did not authorize
external publication, which was performed separately by the author.
