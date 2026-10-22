# Intended statements for independent meaning review

Baseline: public v1.0.0, commit 5380ae2c6411f70769df6076ca82a54d43ff09c3.
This is a statement contract, not a claim of completed Lean or numerical proof.
Released inputs remain unchanged. Ed owns this contract/written derivations;
Richardson owns their formal/numerical realization; Procopius reviews meaning.

## Concrete analytic definitions (C0)

For each exact Appendix-A filter v, r_v(x)=sum(j=1..8) r_vj cos(jx),
s_v(x)=sum s_vj cos(jx), F_v=exp(log(2) r_v), G_v=exp(log(2) s_v).
Every circle integral means (2*pi)^(-1) integral from 0 to 2*pi, not an
unnormalized integral. All score logarithms are base 2.

Zf=integral F, Zg=integral G, f=F/Zf, g=G/Zg,
P(x)=integral F(x+w)G(w), Y(x)=integral FG(r(x+w)+s(w)),
Q=P/(Zf Zg), K_x(w)=f(x+w)g(w)/Q(x).
Zfk=integral F^kappa, Zgk=integral G^kappa,
fstar=F^kappa/Zfk, gstar=G^kappa/Zgk.
D=integral K log2 K, A_score=integral K log2 fstar(x+w),
E_score=integral K log2 gstar(w), u=A_score+E_score-D,
w_score=2D-A_score-E_score.

Do not confuse the analytic function w_score with its integration variable,
the pattern value W, or the ratio A=Delta/Gamma below.

Equivalent evaluation identities to establish, not assume:
L=log2(P/(Zf Zg)), B=Y/P-log2(Zf Zg),
H=log2(Zfk Zgk)-kappa log2(Zf Zg),
D=B-L, u=L+(kappa-1)B-H, w_score=(2-kappa)B-2L+H.
As a separate normalization check:
u=log2 P+(kappa-1)Y/P-log2(Zfk Zgk),
w_score=(2-kappa)Y/P-2log2 P+log2(Zfk Zgk).

C0 target: these are actual positive continuous real functions on the
circle; the displayed normalized densities have integral 1; all scores
and moment integrands are continuous/integrable. With |r_vj|,|s_vj|<=2
and 1<=kappa<=2, prove |B|<=64, |L|<=64, |H|<=64*kappa and
|w_score|<=256. The score estimate must follow through these definitions.

## A: actual changed certificates

Use exact published Delta, Gamma, Delta_b=.02844, Gamma_b=.45925,
q=Gamma/Gamma_b, A=Delta/Gamma, Ab=Delta_b/Gamma_b,
K=Delta/q-Delta_b; require 0<Gamma<Gamma_b, Delta>0, K>0.
For pattern scores U_v,W_v, alpha=1 if W_v<=Gamma, else Gamma/W_v;
sampled means alpha*U_v<Delta. Selected v maximizes U_j, so every
listed comparison U_v-U_j is nonnegative.

A0: authenticate zero-based filter3's two actual Appendix-C records:
rho0 comparisons [5,16], multipliers [17.211,27.1977,8.3302,3.0053];
rho1 comparisons [5,8,16,35], multipliers
[7.7547,0,0,4.2699,2.2635,.461,3.4032]. In particular the lower-row
multiplier equals zero exactly. Authenticate all (v,i) in {0..42}x{0..9},
not merely 430 arbitrary records.

A1: on W3<=Gamma, replace the first two rho0 constants by Delta,Gamma;
prove -alpha U3 <= -Delta + E0_new(pattern). On
Gamma<W3<=1.25*Gamma_b, replace Ab by A in rho1 and its upper-row
coefficient 0 by 7.7547*(A-Ab); prove the same domination. Explicitly
allow W3<Gamma_b: the lower row may then be negative but has zero weight.
Require the upper row and the actual comparison rows to be nonnegative;
do not assume the conclusion as a validity predicate.

A2: for every real x, not just pattern-region points,
E0_new(x)-E0_old(x)=Lambda0
=17.211*(Delta-Delta_b)+27.1977*(Gamma-Gamma_b),
E1_new(x)-E1_old(x)=Lambda1=7.7547*1.25*K.
For actual integrable C0 functions and M2(x)=2+2cos(x), derive
integral M2*2^E_new = 2^Lambda * integral M2*2^E_old.
Integral domains are the full normalized circle, never restricted by
pattern inequalities. Concrete integrability is supplied by C0, not an
unproved assumption about arbitrary functions renamed as scores.

A3: prove exact disjoint exhaustive coverage: for v!=3 use old low/bands/
tail; for v=3 use (-infinity,Gamma], (Gamma,1.25Gamma_b], then all old
bands starting at 1.25Gamma_b and the tail (15Gamma_b,infinity).
Each finite upper endpoint belongs to the preceding region. Connect each
region's actual data to ordinary or special transfer. Include multiplier
signs, rounding perturbation bound and moment-margin connection.

## B: fixed scalar/data theorems

Preserve the exact published tuple. Prove real-log/entropy enclosures,
all twenty alias/auxiliary positive gaps, complete finite source data,
five transferred moment-margin families conditional on the *precise*
old integrals below, finite rounding allowance and multiplier budgets.
Internal work exponent=.48767228002, alpha=.4876723,
strict gap=1.998e-8; prove O(2^(beta n + O(n^.7))*poly(n+n^c))
is O_c(2^(alpha n)) for every fixed c and beta<alpha. Scalar success
does not discharge any continuous moment or algorithmic hypothesis.

## C: old integrals and validation contract

For old budgets and every old source row G_vi, the target is
I_vi=integral (2+2cos x)*2^(z_vi dot G_vi(x))
< 2^(.51613-m_i), where m0=m1=.00025, m2..m8=4, m9=17.
These are stronger region-specific inequalities than Kapila's single
Proposition-B threshold. No test may silently substitute that weaker
common threshold. Pilot: (3,0),(3,1),(4,0), plus at most one tail case.

C1 intended analytic quadrature lemma: if periodic h is holomorphic on a
neighborhood of |Im z|<=sigma and |h|<=B there, then the normalized
N-point trapezoid error is <=2B/(exp(N*sigma)-1). Prove from Fourier
coefficient contour bounds/aliasing; interval arithmetic supplies rigorous
upper bounds for each positive expression, never heuristic errors.

C2 intended zero-free/outer bound: for beta>0 let Af=integral|f(t+i beta)|^2,
Ag analogous, and independently establish q0=sqrt((Af-1)(Ag-1))<1.
For |Im z|<=2beta, prove |Q(z)-1|<=q0 by split contours, mean-one
identities and Cauchy-Schwarz. This is stronger than positivity on the
real axis. Establish the analytic log branch with
|log2 Q(z)|<=-log2(1-q0).

Let R_beta=sum |r_j|cosh(j beta), S_beta analogous. A valid bound is
|B(z)|<=sqrt(Af Ag)*(R_beta+S_beta)/(1-q0)+|log2(Zf Zg)|.
Then Ustar=|L|bound+|kappa-1|*|B|bound+|H|,
Wstar=|2-kappa|*|B|bound+2|L|bound+|H|.
Bound each old affine row's real part, multiply by its nonnegative exact
multiplier, and bound |M2| by 2+2cosh(2beta). Apply C1 at width 2beta
to the full outer integrand. Node intervals must first include all inner
quadrature and arithmetic errors, including normalization constants.

C3 intended finite-to-continuous lemma: normalized P-point definitions
replace *every* inner integral, including tilted normalizers, by its
P-point average. Prove uniform convergence of actual finite scores to C0
scores and outer moments; strict continuous slack implies eventual
finite-circle slack for each of the finitely many modified certificates.
Supply denominator lower bounds and an effective computable cutoff, not
just pointwise convergence. This is not yet a Lean theorem or numeric result.

## D: local algorithmic targets and unresolved end-to-end obligations

D1: for any nonempty family of original solution index sets and independent
uniform u_i in {1..N0}, probability of a nonunique minimum tie-weight sum
is <=n/N0<=1/12. With C=1+nN0 the transformed-target equivalence is exact;
on YES some transformed bin is unique with probability >=11/12, on NO
all are empty. Include empty subsets and repeated original weights.

D2: d_c(V)=|V|-log2|{sum(i in I)c_i:I subset V}| changes by at most one
under a single exchange and is nondecreasing under insertion. Prove
Var(d_c(V_k))<=k/4<=n/4 for uniform k-subsets by an explicit without-
replacement martingale coupling. Thus, if LD fails, a capped exact
preliminary half-sum search answers with probability 1-O(1/n), while
every run has O(2^(tau n)*poly(n+b)) cost. This does not infer LD from
an observed CONTINUE event. Bound the uniform-subset sampler's retries.

D3 remaining audit: alias completeness/deduplication and same-phase
cancellation; per-input estimator probability; finite precision and
constants; worst-history prime/table/trial/storage/address costs; full
uniform-c program/fallback. Each unresolved step must remain an explicit
obligation even if D1/D2 are discharged. No practical solver is required,
but no end-to-end cost theorem follows from scalar inequalities alone.
