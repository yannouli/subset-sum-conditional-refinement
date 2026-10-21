# Early independent review — 2026-10-21

Task #4, parent #1. Scope: specification, consequential constraints and ultimately certificates/manuscript. No final result accepted yet.

## Live specification
Independently opened https://bigospeedrun.com/subset-sum on 2026-10-21. Confirmed positive integer inputs, nonnegative target, repeated values and empty subset, one randomized program independent of polynomial-bit-bound exponent c, per-input success at least 2/3, halting and cost bound on every random outcome. Word size ceil(4(n+b+log2(n+2))); overflow is multi-operation, input preparation counts, retained randomness uses memory, no advice/external tables. The displayed leading exponent is 0.487676, Claimed and explicitly conditional on inherited work. Local formal proofs cannot imply the site's exact-statement rebuild status.

## Inspected sources and reconstructed conditions
Read Ed's immutable raw wharton-pinned-paper.tex in full and Kapila-pinned-PROOF.tex sections 5.5–5.7 (source directory below). These are source inspection, not validation of original moment integrals.

Wharton transfer algebra checks independently:
- With q=Gamma/Gamma_b in (0,1), Delta>0, K=Delta/q-Delta_b>0, the low old region gives alpha>=q. Sampled U<Delta/alpha entails -alpha U <= -Delta+z0(Delta/q-U) for z0>=1. This needs the sampling condition, not an assumption U>=0.
- In bounded old regions the changed first row and increased upper-bound multiplier cancel the w dependence exactly, yielding z0*K*H. New alpha<q/L<=z0 supplies domination. Retain OLD region endpoints.
- Tail loss is at most B*z0*K/Gamma_b. Score bound B=256 follows from the stated finite coefficient bounds and kappa in [1,2]; those finite facts still require transcription verification.
- New multiplier sum and score approximation losses must be included; continuous margin must strictly exceed the selected finite-circle margin, not merely equal it.

Kapila A4/A5/A7 source reading independently confirms Ed's additional obligations:
- delta=(eta-(mu/2)*log2(3))/2 must exceed the guard bit exponent and 1/2-tau+zeta, for collision fraction decay and coverage after removing bad half-blocks.
- A7 contains mu<tau, r+1/2-tau+zeta<tau, and 1/2-tau+zeta+gamma*mu/2<tau in addition to C1–C8.
- For the inherited common alias-work slack epsilon0, do not merely test these against tau: account for epsilon0, zeta and guard costs consistently in each A7 item. It suffices to choose a positive common work margin beneath every relevant cost gap, then fit guard+preliminary slack within it. Loose conditions cannot be silently omitted in an expanded search.
- Derivation of balanced l: equating C2 and C3 with r=1-mu-l cancels gamma and gives 2l=1-mu*h(a). This balances those two costs only; remaining constraints and admissible l,r must still pass.

## Review dependencies
Await candidate certificate and final dependency map from tasks #2/#3. Independently reproduce consequential inequalities and verify exact rounded constants. No unrestricted source theorem, original quadrature certification, new exponent or formalization accepted at this stage.

Source identification: pinned Wharton and Kapila files recorded in source-audit/source-versions.json and download-ledger.json; full upstream copies are not redistributed.

## Source-contract reception (2026-10-21)
Read theory commit 01bab470 source-audit/source-contract.txt and dependency-map.json. Its specification, C1–C8 versus auxiliary A4/A5/A7 distinction, fixed-boundary transfer, finite-circle strict-gap and ordinary-O obligations agree with the independently inspected portions recorded above. This is not independent certification of every O/K algorithmic lemma in that map. Stronger printed regional minima remain explicitly unverified lower bounds and should not enter an accepted new certificate without their own justification. Await frozen rounded candidate and full note.
