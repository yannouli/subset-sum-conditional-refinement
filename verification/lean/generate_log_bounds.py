"""Emit rational endpoints for new tuple. Lean proves the analytic bounds.

Decimal.ln chooses candidates only; it is outside the proof trust boundary.
The proof uses the pinned, analytically proved real-log Taylor remainder.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR
from fractions import Fraction as Q
from pathlib import Path

def f(q):
    q=Q(q)
    return f'({q.numerator} / {q.denominator} : Real)'

def enclosure(q,width):
    with localcontext() as c:
        c.prec=70
        x=(Decimal(q.numerator)/Decimal(q.denominator)).ln()
        lo=(x/width).to_integral_value(rounding=ROUND_FLOOR)*width
        return str(lo-width),str(lo+2*width)

up=Path('.lake/packages/subset_sum_bound/SubsetSum/Numerics.lean').read_text(encoding='utf-8')
lemma=up[up.index('lemma log_ratio_interval'):up.index('theorem log_two_bounds')]
s='''/- Generic log-ratio proof reused verbatim from Joshua Wharton bed8e18,
Numerics.lean, under its repository license; the rational endpoints below
are newly checked for the exact published tuple. No numerical log premise. -/
import SubsetSum.LogBounds
import Verification.DataBridge
set_option autoImplicit false
set_option maxHeartbeats 0
set_option maxRecDepth 100000
namespace Verification.Published
noncomputable section
open SubsetSum
'''+lemma
a=Q('0.008148495127574004')
ys={'two':Q(2),'reduced_a':128*a,'reduced_na':2*(1-a),'reduced_n2a':2*(1-2*a),'reduced_ha':2*(Q(1,2)+a)}
for name,y in ys.items():
    z=(y-1)/(y+1);lo,hi=enclosure(y,Decimal('1e-14'))
    s+=f'''theorem ln_{name} : {lo} <= Real.log {f(y)} ∧ Real.log {f(y)} <= {hi} := by
  have h := log_ratio_interval 32 {f(z)} {lo} {hi}
    (by norm_num)
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
    (by norm_num [realLogTaylor, Finset.sum_range_succ])
  norm_num at h ⊢
  exact h
'''
s+='''private theorem log_scale (x : Real) (m : Nat) (hx : 0 < x) :
    Real.log (x * (2 : Real)^m) = Real.log x + m * Real.log 2 := by
  rw [Real.log_mul hx.ne' (by positivity), Real.log_pow]
'''
xs={'a':(a,7,'reduced_a'),'na':(1-a,1,'reduced_na'),'twoa':(2*a,6,'reduced_a'),
    'n2a':(1-2*a,1,'reduced_n2a'),'hma':(Q(1,2)-a,2,'reduced_n2a'),'hpa':(Q(1,2)+a,1,'reduced_ha')}
for name,(x,m,reduced) in xs.items():
    lo,hi=enclosure(x,Decimal('1e-12'))
    s+=f'''theorem ln_{name} : {lo} <= Real.log {f(x)} ∧ Real.log {f(x)} <= {hi} := by
  have h := ln_{reduced}
  have h2 := ln_two
  have he := log_scale {f(x)} {m} (by norm_num)
  norm_num at he
  constructor <;> linarith [h.1,h.2,h2.1,h2.2]
'''
s+='''def entropy (x : Real) : Real :=
  (-x * Real.log x - (1-x)*Real.log (1-x))/Real.log 2
'''
for name,x,n1,n2 in [('a',a,'a','na'),('twoa',2*a,'twoa','n2a'),('hma',Q(1,2)-a,'hma','hpa')]:
    with localcontext() as c:
        c.prec=70;t=Decimal(x.numerator)/Decimal(x.denominator)
        ent=(-t*t.ln()-(1-t)*(1-t).ln())/Decimal(2).ln()
        lo=(ent*10**10).to_integral_value(rounding=ROUND_FLOOR)/10**10-Decimal('1e-10')
        hi=lo+Decimal('3e-10')
    s+=f'''theorem entropy_{name} : {lo} <= entropy {f(x)} ∧ entropy {f(x)} <= {hi} := by
  have h1 := ln_{n1}
  have h2 := ln_{n2}
  have hL := ln_two
  have hp : 0 < Real.log 2 := by linarith [hL.1]
  unfold entropy
  constructor
  \u00b7 apply (le_div_iff\u2080 hp).2
    nlinarith [h1.1,h1.2,h2.1,h2.2,hL.1,hL.2]
  \u00b7 apply (div_le_iff\u2080 hp).2
    nlinarith [h1.1,h1.2,h2.1,h2.2,hL.1,hL.2]
'''
s+='end\nend Verification.Published\n'
s=s.replace('<=','\u2264')
Path('Verification/LogScalar.lean').write_text(s,encoding='utf-8')
print('Generated analytic Real.log/entropy targets for unchanged tuple')
