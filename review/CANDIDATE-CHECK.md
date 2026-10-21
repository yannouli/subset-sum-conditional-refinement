# Rounded candidate: independent numerical review

Candidate SHA256 75f66f5cc9aedb10aae7632f62bc9a9cdb330142cec488f4937045963dc602c1 passes the separately implemented check in independent_check.py. It imports no producer checker or optimizer. Exact rational entropy intervals use 36 positive atanh-series terms after binary range reduction, with tail 2*z^73/(73*(1-z^2)); division by the positive enclosing interval for ln(2) preserves bounds. Floating approximations in JSON are display only.

All reconstructed alias work gaps and auxiliary gaps exceed 1e-10; zeta+guard loss=2e-12. Source SHA verified, 430 rows independently parsed and their individual transferred margins checked. Lowest margin is filter4/rho0, 1.359679111211037e-7, strictly above finite margin1e-7. Actual maximum modified multiplier sum is below419. Error exponent=9.7468e-8, internal exponent=.48767228002, display .4876723, positive absorption gap1.998e-8.

Read producer verify_certificate.py and rational_bounds.py. Their enclosing arithmetic and positive-series remainder agree with the mathematical bound. The concrete tuple has positive gamma,l,r; the producer generic basic-range guard does not expressly test gamma>0/l>0, so rejection tests could tighten these for future arbitrary inputs. This is not a defect of the accepted concrete tuple.

Executed with an existing Python 3.12 environment. Command: python review/independent_check.py <candidate.json> <pinned-PROOF_0.4877.tex> <output.json>. A plain python alias was unavailable, then the first output serialization exceeded Python's integer-string limit; neither affected inequality checks. Compact output was fixed and the complete check passed.

Scope: conditional scalar certificate and already-reviewed transfer mechanism only. Original continuous integrals/algorithmic claims remain hypotheses. No Lean build, complete solver execution, site verification, novelty beyond inspected sources, or final manuscript acceptance is asserted. Await complete new conditional implication and integrated artifacts.
