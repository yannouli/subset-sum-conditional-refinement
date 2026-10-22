/-
Concrete definitions for statement review. No proof of the requested conclusions
is asserted in this file. Fixed data are imported from Wharton bed8e18, whose
finite records transcribe Kapila 44c34961; published parameters are unchanged.
-/
import SubsetSum.CertificateTransfer
import SubsetSum.FilterData

set_option autoImplicit false

namespace Verification.Published
noncomputable section
open MeasureTheory

def tau : ℝ := 0.48767228
def eta : ℝ := 0.516133678389924
def mask : ℝ := 0.008148495127574004
def block : ℝ := 0.4754356429062936
def gamma : ℝ := 0.06005543072330252
def left : ℝ := 0.483775231690629
def epsilon : ℝ := 0.000000000001
def zeta : ℝ := 0.000000000001
def finiteMargin : ℝ := 0.0000001
def aliasMargin : ℝ := 0.0000000001
def advertised : ℝ := 0.4876723
def deltaB : ℝ := 0.02844
def gammaB : ℝ := 0.45925
def etaB : ℝ := 0.51613
def delta : ℝ := eta - tau
def budget : ℝ := 2 * tau - eta
def ratio : ℝ := budget / gammaB
def slopeB : ℝ := deltaB / gammaB
def slope : ℝ := delta / budget
def transferK : ℝ := delta / ratio - deltaB
def bandTop : ℝ := (5 / 4) * gammaB

/-- Lebesgue measure on one complete period. The prefactor in circleAverage
provides normalization; no score-region restriction occurs in this measure. -/
def circleDomain : Measure ℝ := volume.restrict (Set.Icc 0 (2 * Real.pi))
def circleAverage (h : ℝ → ℝ) : ℝ :=
  (2 * Real.pi)⁻¹ * ∫ x, h x ∂circleDomain
def log2 (x : ℝ) : ℝ := Real.log x / Real.log 2
def exp2 (x : ℝ) : ℝ := SubsetSum.exp2 x
def trig (cs : List ℚ) (x : ℝ) : ℝ :=
  ((cs.zipIdx).map (fun p => (p.1 : ℝ) * Real.cos (((p.2 + 1 : ℕ) : ℝ) * x))).sum
def rawFilter (v : Fin 43) : SubsetSum.FilterData.RawFilter :=
  SubsetSum.FilterData.filters.getD v.val SubsetSum.FilterData.filter_3
def kappa (v : Fin 43) : ℝ := (rawFilter v).kappa
def r (v : Fin 43) (x : ℝ) : ℝ := trig (rawFilter v).rCoeffs x
def s (v : Fin 43) (x : ℝ) : ℝ := trig (rawFilter v).sCoeffs x
def F (v : Fin 43) (x : ℝ) : ℝ := exp2 (r v x)
def G (v : Fin 43) (x : ℝ) : ℝ := exp2 (s v x)
def Zf (v : Fin 43) : ℝ := circleAverage (F v)
def Zg (v : Fin 43) : ℝ := circleAverage (G v)
def Zfk (v : Fin 43) : ℝ := circleAverage (fun y => exp2 (kappa v * r v y))
def Zgk (v : Fin 43) : ℝ := circleAverage (fun y => exp2 (kappa v * s v y))
def P (v : Fin 43) (x : ℝ) : ℝ := circleAverage (fun y => F v (x + y) * G v y)
def Y (v : Fin 43) (x : ℝ) : ℝ :=
  circleAverage (fun y => F v (x + y) * G v y * (r v (x + y) + s v y))
def kernel (v : Fin 43) (x y : ℝ) : ℝ := F v (x + y) * G v y / P v x
def fTilt (v : Fin 43) (x : ℝ) : ℝ := exp2 (kappa v * r v x) / Zfk v
def gTilt (v : Fin 43) (x : ℝ) : ℝ := exp2 (kappa v * s v x) / Zgk v
def entropyScore (v : Fin 43) (x : ℝ) : ℝ :=
  circleAverage (fun y => kernel v x y * log2 (kernel v x y))
def fScore (v : Fin 43) (x : ℝ) : ℝ :=
  circleAverage (fun y => kernel v x y * log2 (fTilt v (x + y)))
def gScore (v : Fin 43) (x : ℝ) : ℝ :=
  circleAverage (fun y => kernel v x y * log2 (gTilt v y))
def u (v : Fin 43) (x : ℝ) : ℝ := fScore v x + gScore v x - entropyScore v x
def w (v : Fin 43) (x : ℝ) : ℝ := 2 * entropyScore v x - fScore v x - gScore v x
def uEval (v : Fin 43) (x : ℝ) : ℝ :=
  log2 (P v x) + (kappa v - 1) * Y v x / P v x - log2 (Zfk v * Zgk v)
def wEval (v : Fin 43) (x : ℝ) : ℝ :=
  (2 - kappa v) * Y v x / P v x - 2 * log2 (P v x) + log2 (Zfk v * Zgk v)
def weight (c : SubsetSum.FilterData.RawCertificate) (j : ℕ) : ℝ :=
  c.multipliers.getD j 0
def comparisonTerm (c : SubsetSum.FilterData.RawCertificate) (offset : ℕ)
    (U : Fin 43 → ℝ) : ℝ :=
  ((c.comparisons.zip (c.multipliers.drop offset)).map
    (fun p => (p.2 : ℝ) * (U c.filterIndex - U p.1))).sum
def lowExponent (D H : ℝ) (U : Fin 43 → ℝ) (W : ℝ) : ℝ :=
  weight SubsetSum.FilterData.certificate_3_0 0 * (D - U 3) +
  weight SubsetSum.FilterData.certificate_3_0 1 * (H - W) +
  comparisonTerm SubsetSum.FilterData.certificate_3_0 2 U
def bandExponent (A lower upperWeight : ℝ) (U : Fin 43 → ℝ) (W : ℝ) : ℝ :=
  weight SubsetSum.FilterData.certificate_3_1 0 * (A * W - U 3) +
  weight SubsetSum.FilterData.certificate_3_1 1 * (W - lower) +
  upperWeight * (bandTop - W) +
  comparisonTerm SubsetSum.FilterData.certificate_3_1 3 U
def lowShift : ℝ :=
  weight SubsetSum.FilterData.certificate_3_0 0 * (delta - deltaB) +
  weight SubsetSum.FilterData.certificate_3_0 1 * (budget - gammaB)
def bandShift : ℝ := weight SubsetSum.FilterData.certificate_3_1 0 * (5 / 4) * transferK
def newUpperWeight : ℝ :=
  weight SubsetSum.FilterData.certificate_3_1 2 +
  weight SubsetSum.FilterData.certificate_3_1 0 * (slope - slopeB)
def oldLow (x : ℝ) : ℝ := lowExponent deltaB gammaB (fun v => u v x) (w 3 x)
def newLow (x : ℝ) : ℝ := lowExponent delta budget (fun v => u v x) (w 3 x)
def oldBand (x : ℝ) : ℝ :=
  bandExponent slopeB gammaB (weight SubsetSum.FilterData.certificate_3_1 2)
    (fun v => u v x) (w 3 x)
def newBand (x : ℝ) : ℝ :=
  bandExponent slope budget newUpperWeight (fun v => u v x) (w 3 x)
def M2 (x : ℝ) : ℝ := 2 + 2 * Real.cos x
def integrand (E : ℝ → ℝ) (x : ℝ) : ℝ := M2 x * exp2 (E x)
def moment (E : ℝ → ℝ) : ℝ := circleAverage (integrand E)

end
end Verification.Published
