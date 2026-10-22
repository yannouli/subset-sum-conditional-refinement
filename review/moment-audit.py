import json,hashlib,pathlib
from flint import arb,acb,ctx
from strip_probe import parse
ctx.prec=160
base=pathlib.Path(__file__).parent
src=pathlib.Path('C:/Users/yanni/Desktop/SubsetSum-Speedrun-2026-10-21/upstream/ed-startup-2026-10-21/kapila-pinned-PROOF.tex')
filters,rows=parse(src)
assert set(filters)==set(range(43))
assert set(rows)=={(v,j) for v in range(43) for j in range(10)}
for (v,j),(c,z) in rows.items():
 assert len(z)==len(c)+(2 if j in (0,9) else 3)
 assert all(x>=0 for x in z)
 assert all(0<=k<43 for k in c)
for n in (3,8,17):
 a=[arb((j*j+2*j+1)%19) for j in range(n)]
 b=[arb((3*j*j+5)%23) for j in range(n)]
 ah,bh=acb.dft(a),acb.dft(b)
 out=acb.dft([ah[j]*bh[-j%n] for j in range(n)],inverse=True)
 for j,x in enumerate(out):
  exact=sum((a[(j+t)%n]*b[t] for t in range(n)),arb(0))/n
  assert (x.real/n).contains(exact) and x.imag.contains(0)
original=src.read_bytes();lines=original.splitlines(keepends=True)
idx=next(i for i,s in enumerate(lines) if s.strip().startswith(b'3 & $\\rho_{0}$'))
mutations={'missing':b''.join(lines[:idx]+lines[idx+1:]),'duplicate':b''.join(lines[:idx]+[lines[idx]]+lines[idx:]),'coefficient':original.replace(b'17.211',b'17.212',1)}
rejected=[]
for name,data in mutations.items():
 p=base/(name+'.tex');p.write_bytes(data)
 try:parse(p)
 except AssertionError:rejected.append(name)
 else:raise AssertionError(name+' accepted')
def audit_report(p):
 d=json.loads(p.read_text());pairs=[(x['filter'],x['region']) for x in d['results']]
 assert len(pairs)==430 and len(set(pairs))==430 and set(pairs)==set(rows)
 assert d['complete'] and d['source_sha256']==hashlib.sha256(original).hexdigest()
 for r in d['results']:
  m=arb('0.00025') if r['region']<2 else arb(17 if r['region']==9 else 4)
  expected=((arb('0.51613')-m)*arb(2).log()).exp()
  threshold=arb(r['threshold']);interval=arb(r['integral_enclosure'])
  assert threshold.overlaps(expected)
  assert interval<expected and r['status']=='certified' and arb(r['strict_gap'])>0
 return d
producer=audit_report(pathlib.Path('C:/Users/yanni/Desktop/SubsetSum-Speedrun-2026-10-21/verification-worktrees/implementation/verification/evidence/all-moments.json'))
replay=audit_report(base/'independent-all.json')
for x,y in zip(producer['results'],replay['results']):
 for key in ('filter','region','nodes','status','integral_enclosure','threshold','strict_gap','outer_error'):
  assert x[key]==y[key],(key,x['filter'],x['region'])
result={'source_sha256':hashlib.sha256(original).hexdigest(),'pairs':430,'statuses':'all certified under reviewed analytic contract','replay_seconds':replay['seconds'],'producer_seconds':producer['seconds'],'replay_enclosures_identical':True,'direct_sum_DFT_lengths':[3,8,17],'malformed_source_rejections':rejected,'trust':'Python/FLINT/Arb and reviewed written analytic theorem; not Lean'}
(base/'audit.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
