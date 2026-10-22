# Validated continuous moment calculations

This is a new verification artifact, separate from the immutable published
conditional certificate. It uses the actual full-circle averages and scores
in the independently reviewed `theory/analytic-contract.tex`. The original
coefficients and multipliers are exact rationals from the pinned source.

Install ordinary Python 3.12 and `python-flint==0.8.0` in a dedicated environment.
From the repository root, create a new output directory and fetch the
authenticated input. These commands leave the accepted evidence unchanged.
If `fresh-run` already exists, choose a new directory name consistently:

```
python -c "from pathlib import Path; Path('verification/publication/reproduce/fresh-run').mkdir(parents=True, exist_ok=False)"
python numerics/fetch_baseline.py --output verification/publication/reproduce/fresh-run/PROOF_0.4877.tex
python verification/moments/validate.py --source verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --output verification/publication/reproduce/fresh-run/all-moments.json --all
python verification/publication/reproduce/check_moment_outputs.py --source verification/publication/reproduce/fresh-run/PROOF_0.4877.tex --reference verification/evidence/all-moments.json --replay verification/publication/reproduce/fresh-run/all-moments.json --output verification/publication/reproduce/fresh-run/moment-correspondence.json
```

The full command covers the pilot rows as well as all remaining cases. Optional
pilot and strip-probe commands use the same authenticated input and separate
new output filenames. See `../publication/reproduce/README.md` for the baseline
regressions and exact-transcription check. The Python interpreter here must be
the isolated Python 3.12 environment with the pinned requirements installed.

The four pilot rows are (3,0), (3,1), (4,0), (4,9). Thresholds are
`2^(0.51613-m)` with `m=.00025` in regions 0/1, `m=4` in regions 2--8,
and `m=17` in the tail. Every attempted pair receives its own status.
The enclosures use 160-bit Arb arithmetic, including exact rational node
angles, cosine/exponential/logarithm enclosures, DFTs, positive denominators
and both tilted normalizers. The finite correlation is evaluated as
`inverseDFT(DFT(F)[k]*DFT(G)[-k])/N`; Y uses the two corresponding products.
These are enclosures of the actual node sums, rather than double-precision
FFT estimates.

Each inner sum is enlarged by the reviewed analytic trapezoid error before
division or logarithms. A separately enclosed sufficient zero-free bound
q0<1 justifies the complex log on the common strip. Each outer moment is
then enlarged by its own analytic strip error. Increasing precision or
mesh agreement is not the justification for those error bounds. Printed
balls retain radii; comparisons are performed on Arb balls, not their text.

The Python parser, FLINT/Arb elementary functions and DFT implementation,
Python bindings, and written analytic theorem are outside the Lean trust
boundary. The delivered evidence has internal agent review and a separate
replay; fresh local reproduction is a distinct check. These
calculations do not prove the full algorithm or assign a site status.
Fixed limits are one thread, 131072 nodes, and a 600-second campaign cap;
the original pilot completed with at most 4096 nodes. A failed sufficient
bound is unresolved, not evidence of a counterexample.
