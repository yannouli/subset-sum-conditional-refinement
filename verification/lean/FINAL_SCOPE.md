# Final formal checkpoint: precise scope

All targets refer to the same immutable published tuple and source revisions.
No optimizer, new filters, solver implementation or public write was run.

| Module | New proved content |
|---|---|
| Concrete / Boundary / Regularity | Actual normalized full-circle entropy scores; concrete filter-3 domination and shifts; positive, integrable moments |
| DataBridge | Full exact primary-source transcription equality, all 43 filters and 430 ordered pairs, dimensions, no fallback/truncation, non-special low cap |
| LogScalar | Analytic real-log Taylor bounds for the new mask; actual real binary-entropy intervals |
| Scalar | All 20 alias/auxiliary gaps, conservative transferred margins, error/work/gap inequalities |
| RowMargins | Exact rational/real tuple bridge, closed checks of every actual row margin and modified weight sum; concrete filter-3 threshold transfers; ordinary-O absorption |
| Regions | Explicit region predicate, existence, disjointness and unique assignment for every filter and real score, with correct endpoints |
| AllRows | Actual old/new affine exponents using the imported records, proved continuity/integrability/positivity, exponent and moment transfers for every row |

The theorem `all_430_conditional_moment_bounds` explicitly takes the old
moment bound and `forall x, w_v(x)<=256`. The old moment is supplied by the
separate independently reviewed validated calculation, not by a Lean proof.
The coarse score bound and identities `uEval=u`, `wEval=w` are proved in the
reviewed written supplement; their complete formal proofs remain open. They
are not custom axioms and are not hidden under a certificate predicate.
This checkpoint therefore does **not** make the entire strengthened result
a closed Lean theorem. The original algorithmic obligations remain separate.
Ordinary-region pattern-domination assembly also remains a written/imported
generic argument rather than a completed concrete Lean theorem for every row.
The concrete all-row results here concern analytic exponent/moment transfer;
the new filter-3 pattern-domination theorems are separately formalized.

`fixed_tuple_ordinary_O` concerns the actual real exponential functions with
sublinear n^0.7 and logarithmic exponent overhead. It does not assert that an
unimplemented algorithm has that runtime. Its exact internal work exponent
is 0.48767228002 and the target remains 0.4876723.

The source build and `AuditScalar.lean` inspect statements and transitive
axioms. Only the permitted foundational axioms are accepted. The earlier
five-minute all-import `lean4checker --fresh` attempt timed out; it remains
unfinished. Source replay against pinned built imports and statement review
are distinct, weaker checks. No external checker, automated Comparator
result or site-awarded verification status is claimed.

No timeout wrapper is delivered. The initial wrapper could leave a child
running, and its attempted correction did not cover an exited parent whose
child retained an inherited pipe. Independent review caught that edge case
(Raft receipt 1bbe61e8). The wrapper was removed rather than expanded into
a new harness project. Historical receipts remain preserved; the initial
live-parent timeout fixture alone did not establish robust descendant control.

To rebuild/audit the final chain:

```
lake build +Verification
lake env lean AuditScalar.lean
```

The optional stronger direct command is
`lake env /path/to/lean4checker --fresh Verification`. It replays every imported
declaration, may take substantially longer than the source build, and has not
completed in the recorded attempt. No portable timeout or successful fresh
replay is claimed by this package. Save any future output to a new location.

The initial statement contract in STATEMENTS.md is preserved as the historical
early-review specification. This file maps the actual completed targets and
remaining formal obligations; it does not turn pending goals into assumptions.
