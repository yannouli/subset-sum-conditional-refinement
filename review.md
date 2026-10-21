# Independent review — conditional subset-sum refinement

Reviewer: Reviewer-Procopius. Date: 21 October 2026.

## Verdict and exact scope

**PASS WITH EXPLICIT INHERITED ASSUMPTIONS** for the mathematical implication, scalar certificate, and nine-page integrated note at main `fbc659d`. The manuscript meets the required complete-proof standard for its stated conditional refinement to `O_c(2^(0.4876723 n))`. No unresolved new mathematical step was found. This is not an unconditional subset-sum algorithm verification or a site-issued leaderboard/Lean verdict.

Reviewed PDF SHA256: `301283c7e6fd7fcca4ef79dece019e4030befabc2c6e01710e78c98e66054091`.
Candidate SHA256: `75f66f5cc9aedb10aae7632f62bc9a9cdb330142cec488f4937045963dc602c1`.
Sources reviewed: Ed `dc7ec2f4a2c0ec4a4724932c3471303d0ee41b33`; numerical leaf `67bf292f73d8f22ecdfce1b2cfaee4f0a4aa38e7`; independent evidence in `review/`. The integrated paper differs from Ed's reviewed mathematical source only by a small-type group around references.

## What was independently checked

- Live input/computational specification, selected original A4/A5/A7 constraints and all-region certificate transfer. The extra work/coverage conditions beyond C1–C8 are recorded, rather than assumed from the optimizer.
- Filter 3's exact old multiplier rows, low two-constant shift, zero-lower-multiplier extended-band domination, full-circle integral identities and boundary coverage. This changes the analysis and internal tuple; it is not simply spending unused advertised-exponent slack.
- A separately written rational-interval checker, importing neither producer verifier nor optimizer, checked the rounded tuple and all 430 individual transfer rows. Minimum inherited-margin-based lower bound is `1.359679111211037e-7` at filter 4/rho0. Error exponent is `9.7468e-8`; internal exponent `0.48767228002` leaves `1.998e-8` to the advertised exponent. Every relevant work/auxiliary margin exceeds the common `1e-10` reserve.
- Producer interval arithmetic and checker source, its final 19-file manifest, and eight independently rerun adverse-input tests. The exact pinned baseline hash was checked. This tests a certificate, not a full subset-sum solver or original quadrature.
- The complete written conditional proof: original-premise boundary, finite-circle strict margin, approximation losses, all-run caps versus cap-failure probability, consistent phases, isolation/decision threshold, guard/fallback uniformity and ordinary-O absorption.
- Integrated README and unsent submission draft agree on conditional status, exact exponents, attribution, reproduction commands and publication restrictions. All nine PDF pages were independently rendered and viewed; equations, tables, citations and page flow are legible with no clipping or missing references observed.

## Corrections and dispositions

The early auxiliary-margin clarification was incorporated into the checker and manuscript, including preliminary/guard loss. The optional explicit positive-gamma/left-block domain guards were added and their rejection tests rerun; the original concrete candidate already satisfied them. No unresolved new mathematical correction remains in the reviewed versions.

## Qualifications and remaining delivery checks

The original OpenAI/Kapila algorithmic implementation, convergence and moment claims remain hypotheses. Their validity was not established by this review, and no new quadrature or complete solver run was performed. No local Lean build or new theorem/axiom audit exists; this is a formalization limitation distinct from a missing written proof of the new conditional implication. Site verification and global novelty/priority are not claimed.

The bounded current-source/novelty refresh and clean extracted package build are still forthcoming at this exact-version checkpoint. They require addenda before representing the entire delivery as reviewed. Coordinator owns package build/publication preparation; no external submission is authorized or executed. Any later mathematical/source change requires scoped re-review.

Reproduction of independent check: `python review/independent_check.py numerics/data/candidate.json /path/to/pinned/PROOF_0.4877.tex independent-result.json`. The script requires only the Python standard library. Detailed algebra, execution scope and hashes are in `review/FILTER3-CHECK.md`, `review/CANDIDATE-CHECK.md`, `review/MANUSCRIPT-CHECK.md`, and their companion JSON records.

## Bounded novelty addendum

Theory8492802 adds only a qualified source-comparison paragraph. Its novelty-check.txt and file inventory distinguish source screening from full proof review, current default branches from leaderboard pins, and application-level change from generic inherited machinery. Independently inspected the refreshed Wharton shiftCap.low, low_moment_refinement, sampling/low/band transfer declarations and Filter03 entry: the concrete old application retains 17.211K and Delta/q; the zero coefficient itself was already transcribed. The paragraph's limited distinction from inspected source applications is acceptable, without global priority. No upstream Lean was built or endorsed by this textual check. Revised compiled PDF/clean-package checks remain pending.

## Final delivery receipt — supersedes pending items above

Final scientific revision reviewed: `04febba50ba2d2e4359b069d6e69055625b1340c`. Final nine-page PDF SHA256: `a6254a11d2e82b0abc35bbdcceacf848a3b4995b340437c41c68104bd8846347`. Independently re-rendered and viewed all nine reflowed pages after the bounded-priority addition; no visual or scientific discrepancy found. Equations, parameter tuple and proofs are unchanged.

Read Coordinator's `startup/build-verification.json`: it records fresh extraction with 49 tracked files byte-verified, successful scalar/eight-rejection/independent-430-row checks, a fresh four-file Tectonic Overleaf build, and all nine rendered pages pixel-identical to this PDF. These packaging executions are Coordinator evidence inspected by the reviewer, not falsely described as another reviewer build. The final observed leaderboard still reports conditional0.487676; the refreshed source revisions are unchanged. The bounded novelty qualification is accepted as recorded above.

**Final verdict: PASS WITH EXPLICIT INHERITED ASSUMPTIONS; ready for human inspection as a conditional refinement.** The mandatory complete-proof standard for the entire new conditional implication is met. No owned mathematical, manuscript or artifact correction remains. The inherited premises and lack of Lean/site verification are material qualifications, not hidden new proof obligations. A leaderboard position, unconditional theorem or comprehensive priority is not established.

Task #4 review is complete. Coordinator may integrate this receipt and repackage without changing scientific files, then deliver locally. No new search, publication, submission or autonomous review work is authorized by this receipt. Final human acceptance and any external publication remain separate.


## Clean execution and build receipt

Inspected evidence/release-checks.json (completed 21 October 2026 at 15:44:44 UTC): fresh documented pinned retrieval with no prior dependency copy, all three requested commands exit zero, all eight rejection tests and all 430 independent rows pass. Independently hashed the fetched file to b397531cc5997e88c439d5290774861b46a34aa32d9cd71fa7dcced130359298 and compared the fresh producer JSON against its historical result (excluding only seconds), plus the entire fresh independent result against its historical result: exact equality. Internal work exponent remains 0.48767228002, advertised exponent 0.4876723, absorption gap 1.998e-8. Discovery was not rerun. Receipt records strict UTF-8 and path scans, original-preserving omissions and protected hashes consistent with my separate comparison.

The updated release-build.json records the four-file Overleaf archive SHA256 1e372b1d7363740c03a5aa5e22b5fa5f412964c068c18dc47b4e15d531cfa53b and fresh bibliography build. Independently compared rendered pixel bytes for every page of the integrated and clean-extracted PDFs: all ten identical. This resolves the byte-hash difference noted above without assuming PDF byte determinism. Fresh local release history has no configured remote; the added .gitattributes only preserves exact checkout bytes.

Verdict on the reviewed release content and executions: **PASS WITH THE SAME EXPLICIT INHERITED ASSUMPTIONS**. Changes are confined to the authorized correction scope and support the same conditional result. No new mathematical or executable change, unresolved correctness defect, claim strengthening or source-pin change was found. This is ready for final local packaging as an explicitly conditional Claimed submission, subject to the owner's later publication authorization. Final compact archive/manifest assembly must include this receipt and be checked separately; no endorsement of an unseen final archive is implied.
