# Filter 3 boundary change: independent analytic check

2026-10-21; task #4. This checks the proposed argument, not the provisional numerical exponent.

Pinned Kapila Appendix C rows inspected directly:
- filter 3, rho0: comparison filters 5,16; z=(17.211,27.1977,8.3302,3.0053).
- filter 3, rho1: comparison filters 5,8,16,35; z=(7.7547,0,0,4.2699,2.2635,0.461,3.4032).
These are exact printed decimals; no inferred approximate zero.

Let old budgets be D_b,G_b and new budgets D,G, with 0<G<G_b and A=D/G >= A_b=D_b/G_b. All integrals are the original full-circle moments, not integrals restricted to W regions.

For filter 3 and W<=G, alpha=1 and sampling gives U<D. Replace the first two low rows by D-u and G-w, respectively, retaining all multipliers. Pattern domination follows from z0>=1, D-U>0, G-W>=0 and selected-filter comparison rows. The pointwise certificate exponent shifts by exactly
L0=17.211*(D-D_b)+27.1977*(G-G_b).
Thus I_new=2^L0 I_old. A negative second contribution is legitimate; it is not a region-restricted quadrature inference.

For filter 3 and G<W<=1.25G_b, use the old rho1 certificate with first row Aw-u, retain upper boundary H*G_b (H=1.25), and increase the upper multiplier from zero to z0*(A-A_b). The old lower-row multiplier is exactly zero, so the lower row can be omitted or moved to w-G at no cost. In particular its possible negative old value for G<W<G_b contributes nothing. The upper row is nonnegative and the added multiplier nonnegative. Now alpha=G/W<1<7.7547=z0, alpha*A*W=D, and AW-U>0. Hence -alpha*U <= -D+z0*(AW-U). The pointwise exponent change is
L1=z0*(A-A_b)*H*G_b = 7.7547*H*(D*G_b/G-D_b).
Therefore I_new=2^L1 I_old.

The low/extended-band regions cover the changed boundary without a gap; equality W=G belongs to low, equality W=1.25G_b belongs to the band. Above that, old rho2 onward retain their boundaries and transfer. All other filters can use Wharton's unchanged region construction.

Required candidate checks: new transferred margins for BOTH rows, all other 428 rows, changed multiplier-sum budget and approximation losses, finite-circle slack strictly below continuous margins, and complete alias-work/guard/overhead sideconditions. The maximum low z0 after removing filter 3 has not yet been independently parsed over all rows here. No original quadrature or full-algorithm validity is established by this check. Novelty relative to other source versions remains to be assessed.
