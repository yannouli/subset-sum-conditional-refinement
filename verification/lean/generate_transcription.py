"""Emit exact Lean records from the authenticated primary tables, not Lean data.

The emitted equality theorems are kernel checked; this generator is not trusted.
Run from verification/lean. No released file is changed.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, re

src = Path('../evidence/PROOF_0.4877.tex').read_bytes()
assert hashlib.sha256(src).hexdigest() == 'b397531cc5997e88c439d5290774861b46a34aa32d9cd71fa7dcced130359298'
filters, rows = {}, {}
for line in src.decode('utf-8').splitlines():
    a = [s.strip() for s in line.split('&')]
    if len(a) != 4 or not a[0].isdigit():
        continue
    v = int(a[0])
    m = re.fullmatch(r'\$\\rho_\{(\d+)\}\$', a[1])
    if m:
        rows[v, int(m[1])] = (
            [] if not a[2] else [int(x.strip()) for x in a[2].split(',')],
            [Q(x.strip()) for x in a[3].replace('\\', '').split(',')])
    elif re.fullmatch(r'\d+\.\d+', a[1]):
        filters[v] = (Q(a[1]), [[Q(x.strip()) for x in c.replace('\\', '').split(',')] for c in a[2:]])
assert set(filters) == set(range(43))
assert set(rows) == {(v, j) for v in range(43) for j in range(10)}
q = lambda x: f'({x.numerator} / {x.denominator} : Rat)'
ls = lambda xs: '[' + ', '.join(map(str, xs)) + ']'
record = lambda fields: '\u27e8' + ', '.join(fields) + '\u27e9'
s = '''/- Exact independent transcription of the pinned Kapila TeX tables.
Generated from SHA256-authenticated bytes. Equality is checked by Lean's kernel.
No continuous integral inequality is asserted by this module. -/
import Verification.Regularity
set_option autoImplicit false
set_option maxHeartbeats 8000000
set_option maxRecDepth 100000
namespace Verification.Published
open SubsetSum.FilterData
noncomputable section
'''
s += 'def expectedFilters : List RawFilter := [\n' + ',\n'.join(record([
    q(filters[v][0]), ls(map(q, filters[v][1][0])), ls(map(q, filters[v][1][1]))]) for v in range(43)) + ']\n'
s += 'def expectedCertificates : List RawCertificate := [\n' + ',\n'.join(record([
    str(v), str(j), ls(rows[v,j][0]), ls(map(q, rows[v,j][1]))]) for v in range(43) for j in range(10)) + ']\n'
s += '''theorem filter_transcription : filters = expectedFilters := by decide +kernel
theorem certificate_transcription : certificates = expectedCertificates := by decide +kernel
theorem rawFilter_index_in_bounds (v : Fin 43) : v.val < filters.length := by
  rw [filters_count]
  exact v.isLt
theorem source_filter_dimensions :
    expectedFilters.length = 43 \u2227
    (\u2200 f \u2208 expectedFilters, f.rCoeffs.length = 8 \u2227 f.sCoeffs.length = 8) := by
  rw [\u2190 filter_transcription]
  exact \u27e8filters_count, fun f hf => \u27e8(all_filters_valid f hf).1, (all_filters_valid f hf).2.1\u27e9\u27e9
theorem exact_pair_coverage :
    expectedCertificates.map (fun c => (c.filterIndex.val,c.region.val)) =
    (List.range 43).flatMap (fun v => (List.range 10).map (fun j => (v,j))) := by
  rw [\u2190 certificate_transcription]
  exact all_regions_present
/-- Every comparison and every corresponding multiplier is consumed. -/
theorem comparison_zip_no_truncation (c : RawCertificate) (hc : c \u2208 certificates) :
    let offset := if c.region.val = 0 \u2228 c.region.val = 9 then 2 else 3
    (c.multipliers.drop offset).length = c.comparisons.length \u2227
    (c.comparisons.zip (c.multipliers.drop offset)).length = c.comparisons.length := by
  dsimp
  have h := (all_certificates_valid c hc).1
  rw [List.length_drop, h]
  constructor
  \u00b7 omega
  \u00b7 simp only [List.length_zip, List.length_drop, h]
    omega
'''
for field in ['comparisons', 'multipliers']:
    vals = [len(rows[v,j][0 if field == 'comparisons' else 1]) for v in range(43) for j in range(10)]
    s += f'theorem exact_{field}_lengths : certificates.map (fun c => c.{field}.length) = {ls(vals)} := by decide +kernel\n'
s += '''theorem source_comparisons_unique : \u2200 c \u2208 certificates, c.comparisons.Nodup := by decide +kernel
theorem non_special_low_cap : \u2200 c \u2208 certificates,
    c.filterIndex \u2260 3 \u2192 c.region = 0 \u2192 c.multipliers.headD 0 \u2264 (10.6428 : Rat) := by
  decide +kernel
end
end Verification.Published
'''
Path('Verification/DataBridge.lean').write_text(s, encoding='utf-8')
print('Emitted exact 43-filter/430-row primary-table transcription')
