import json,re,hashlib,sys
from fractions import Fraction as F
from pathlib import Path
p=Path(sys.argv[1]); src=Path(sys.argv[2]); out=Path(sys.argv[3])
c=json.loads(p.read_text()); d={k:F(v) for k,v in c['parameters'].items()}
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def scale(a,b):return (a[0]*b,a[1]*b) if b>=0 else (a[1]*b,a[0]*b)
def sub(a,b):return add(a,scale(b,-1))
def exact(x):return(F(x),F(x))
def ln(y):
 z=(y-1)/(y+1); total=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0)); tail=2*z**73/(73*(1-z*z)); return total,total+tail
l2=ln(F(2))
def log(x):
 k=0
 while x<1:x*=2;k-=1
 while x>2:x/=2;k+=1
 a,b=ln(x);return F(k)+a/l2[1],F(k)+b/l2[0]
def h(x):return add(scale(log(x),-x),scale(log(1-x),x-1))
t,e,a,m,g,l=(d[k] for k in ['tau','eta','a','mu','gamma','l']);r=1-m-l
ha,h2,hb=h(a),h(2*a),h(F(1,2)-a); ep=d['epsilon'];z=d['zeta']; theta=1/d['input_guard_coefficient']; margin=d['alias_margin']
assert 0<g and 0<l and 0<r and 0<a<F(1,4) and 0<m<1 and 0<t<F(1,2) and t<e<2*t and e<1
costs={'left':add(exact(l-g*m),scale(ha,m)), 'right':exact(r+(1-g)*m), 'pairs':add(exact(1-m-g*m-e),scale(add(ha,hb),m)), 'masks':add(exact(F(1,2)-t),scale(hb,m)), 'leftmap':exact(l), 'rightmap':exact(r), 'samplemap':exact(m*(1-2*a)), 'classes':exact(m), 'sorting':exact(r+F(1,2)-t+z), 'smallprime':exact(F(1,2)-t+z+g*m/2)}
gaps={k:sub(exact(t),v) for k,v in costs.items()}
extra={'coverage':sub(scale(h2,F(1,2)),exact(g)), 'layer':sub(exact(1-2*a),add(scale(h2,F(1,2)),ha)), 'maskorder':sub(hb,ha), 'sampleleft':exact(l-m*(1-2*a)), 'samplehalf':exact(F(1,2)-m*(1-2*a)), 'prime':exact(t-e/2)}
delta=scale(sub(exact(e),scale(log(F(3)),m/2)),F(1,2));extra['collision']=sub(delta,exact(theta));extra['badhalves']=sub(delta,exact(F(1,2)-t+z))
assert all(v[0]>margin for v in [*gaps.values(),*extra.values()]);assert theta+z<margin
text=src.read_text();assert hashlib.sha256(src.read_bytes()).hexdigest()==c['baseline_sha256']
rows={}
for match in re.finditer(r'^([0-9]+) & \$\\rho_\{([0-9]+)\}\$ & ([^&]*) & (.*)\\\\',text,re.M):
 v,j=int(match[1]),int(match[2]); rows[v,j]=[F(x.strip()) for x in match[4].split(',')]
assert len(rows)==430 and set(rows)=={(v,j) for v in range(43) for j in range(10)}
D=e-t;G=2*t-e;Db=F('.02844');Gb=F('.45925');eb=F('.51613');K=D*Gb/G-Db;slope=D/G-Db/Gb
assert 0<G<Gb and K>0 and 0<D/G<F(1,4)
assert rows[3,1][:3]==[F('7.7547'),0,0]
H=[None,F('1.25'),F('1.6'),F(2),F('2.6'),F('3.5'),F(5),F(8),F(15)]
results={};sums=[]
for (v,j),zs in rows.items():
 assert all(x>=0 for x in zs) and sum(zs)<=F('418.36')
 old=F('.00025') if j<2 else F(4) if j<9 else F(17)
 if j==0:loss=zs[0]*(D-Db)+zs[1]*(G-Gb) if v==3 else zs[0]*K
 elif j<9:loss=zs[0]*K*H[j]
 else:loss=zs[0]*256*slope
 mm=old+e-eb-loss;assert mm>d['finite_moment_margin'];results[f'{v}:{j}']=mm
 sums.append(sum(zs)+(zs[0]*slope if 0<j<9 else 0))
assert max(sums)<419
err=d['finite_moment_margin']-(18+6*419)*ep; beta=t+20*ep;absorb=d['target_exponent']-beta
assert err>0 and absorb>0 and beta<F('.4876759502')
def report(x):return {'exact':str(x) if x.denominator.bit_length()<4096 else 'Exact interval endpoint computed; see script','approx':float(x)}
result={'status':'PASS conditional scalar checks; no original moment quadrature verified','candidate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'work_gaps':{k:report(v[0]) for k,v in gaps.items()},'auxiliary_lower_bounds':{k:report(v[0]) for k,v in extra.items()},'minimum_per_row_moment':report(min(results.values())),'limiting_row':min(results,key=results.get),'max_actual_multiplier_sum':report(max(sums)),'error_exponent':report(err),'internal_exponent':report(beta),'absorption_gap':report(absorb),'rows_checked':len(rows)}
out.write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k not in ['work_gaps','auxiliary_lower_bounds']},indent=2))

