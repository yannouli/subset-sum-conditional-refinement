# Exact scalar certificate for a conditional Subset Sum refinement

The fixed candidate advertises **0.4876723**, with internal work exponent
**0.48767228002**. A new filter-3 proof boundary is the analytic change;
`transfer-note.tex` derives it. This directory contains no Subset Sum solver.
Original continuous moments and algorithmic correctness/resource lemmas remain
explicit inherited premises. Independent review determines acceptance.

## Reproduce the exact checks

Python 3.12 was used; the certificate checker and rejection tests need only the
standard library. From the repository root:

```sh
# Optional network step: retrieves the pinned, hash-checked manuscript into ignored storage.
python numerics/fetch_baseline.py
# Both subsequent commands are offline.
python numerics/verify_certificate.py --output numerics/evidence/certificate-check.json
python numerics/test_rejections.py --output numerics/evidence/rejections.json
```

Alternatively, give both checking commands `--baseline /path/to/PROOF_0.4877.tex`.
The exact required SHA-256 is
`b397531cc5997e88c439d5290774861b46a34aa32d9cd71fa7dcced130359298`.
The local `.gitattributes` preserves bytes across Git checkouts so the producer
manifest is portable across line-ending settings.
The program parses all 43 filters and all 430 certificates from that input,
checks finite-data prerequisites, encloses entropy/logarithms by rational
intervals, and checks every listed inequality using `Fraction` decisions.
Displayed decimal endpoints are rounded outward. Elapsed seconds vary between
replays; all mathematical fields must agree.

The eight rejection tests challenge parameter signs, the advertised exponent,
finite-circle margin, guard, alias margin, checksum feasibility and source authenticity.
They test certificate failure modes rather than a solver's correctness.

## Inputs and provenance

`data/candidate.json` contains terminating decimals interpreted as exact
rationals, not floating estimates. `SOURCE-REVISIONS.json` records source pins
and implementation provenance. Full downloaded upstream sources remain outside
the publishable repository; `baseline/` is ignored. No upstream implementation
is vendored. Finite mathematical constants and source locations are credited.

`evidence/certificate-check.json` is the producer run, not an independent
review. In particular it does **not** evaluate the original 430 continuous
integrals. The new smallest lower bound is above 1.35967911e-7, conditional
on their old conservative margins. The finite-circle margin is 1e-7 and the
remaining mean-square error exponent is 9.7468e-8. All alias/auxiliary checks
exceed a common 1e-10 margin; the guard and preliminary slack consume 2e-12.

## Discovery versus certification

`batch-plan.json` records the predeclared bounded batch. `discover.py` ran
24 single-process SLSQP starts using seed 20261021, NumPy 2.2.6 and SciPy
1.15.3 on Python 3.12.14. The preserved `evidence/discovery.json` records
0.4465753000113182 seconds (about 0.447 seconds) for the batch timer inside
`discover.py`, after imports and before JSON serialization. This is parameter-search
time, not a Subset Sum solver runtime. Its floating results
are retained in `evidence/discovery.json`; several optimizer success flags or
tiny negative residuals are not proof of feasibility. Some loose algorithmic
side conditions were not included in discovery and were checked only by the
final exact certificate. The selected tuple was rounded before exact checking.
The batch compared the inherited uniform transfer and the moved-boundary
family; it neither proves an optimum nor justifies practical performance.

Re-running discovery is optional and does not affect certificate checking:

```sh
python -m pip install numpy==2.2.6 scipy==1.15.3
python numerics/discover.py
```

No new continuous quadrature, filter search, solver timing or large experiment
was performed. Lean was unavailable and not installed; see
`FORMALIZATION-SCOPE.md`. Public submission/publication is outside this work.
