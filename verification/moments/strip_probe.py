"""Finite, rigorous probe of the reviewed sufficient zero-free strip bound.

No moment threshold is claimed by this probe. Exact source rationals and Arb
balls are used; the analytic trapezoid remainder is included in every integral.
"""
import argparse, hashlib, json, re, time
from pathlib import Path
from fractions import Fraction
from flint import arb, ctx

def parse(source):
    data=source.read_bytes()
    assert hashlib.sha256(data).hexdigest()=='b397531cc5997e88c439d5290774861b46a34aa32d9cd71fa7dcced130359298'
    filters, rows = {}, {}
    for line in data.decode('utf-8').splitlines():
        a=[s.strip() for s in line.split('&')]
        if len(a)!=4 or not a[0].isdigit(): continue
        v=int(a[0]); m=re.fullmatch(r'\$\\rho_\{(\d+)\}\$',a[1])
        if m:
            rows[v,int(m[1])]=([] if not a[2] else list(map(int,a[2].split(','))),
                [Fraction(x.strip()) for x in a[3].replace('\\','').split(',')])
        elif re.fullmatch(r'\d+\.\d+',a[1]):
            filters[v]=(Fraction(a[1]), [[Fraction(x.strip()) for x in c.replace('\\','').split(',')] for c in a[2:]])
    assert len(filters)==43 and len(rows)==430
    return filters,rows

def ball(x):
    x=Fraction(x)
    return arb(x.numerator)/x.denominator

def widen(x,error):
    return x+arb(0,error.abs_upper())

def rem(bound,width,n):
    assert width>0
    return 2*bound/((n*width).exp()-1)

def trig(cs,cosines):
    return [sum((c*t for c,t in zip(cs,node)),arb(0)) for node in cosines]

def strip(filters,needed,beta,n=512):
    ln2=arb(2).log(); sigma=arb('0.1')
    cosines=[[ (ball(Fraction(2*j*k,n))).cos_pi() for k in range(1,9)] for j in range(n)]
    report={}
    for v in needed:
        kap,cs=filters[v]; kap=ball(kap); r,s=[[ball(x) for x in coeff] for coeff in cs]
        R=lambda c,t:sum((abs(x)*(k*t).cosh() for k,x in enumerate(c,1)),arb(0))
        norm=[]; tilts=[]; norms2=[]
        for coeff in (r,s):
            vals=trig(coeff,cosines)
            z=widen(sum(((ln2*x).exp() for x in vals),arb(0))/n,rem((ln2*R(coeff,sigma)).exp(),sigma,n))
            zk=widen(sum(((ln2*kap*x).exp() for x in vals),arb(0))/n,rem((ln2*kap*R(coeff,sigma)).exp(),sigma,n))
            shifted=[x*(k*beta).cosh() for k,x in enumerate(coeff,1)]
            vals2=trig(shifted,cosines)
            z2=widen(sum(((2*ln2*x).exp() for x in vals2),arb(0))/n,rem((2*ln2*R(shifted,sigma)).exp(),sigma,n))
            assert z>0 and zk>0 and z2>0
            norm.append(z);tilts.append(zk);norms2.append(z2/z**2)
        af,ag=norms2
        # The theorem proves Af,Ag>=1; strict interval positivity here permits
        # direct square-root evaluation without needing interval intersections.
        assert af>1 and ag>1
        q=((af-1)*(ag-1)).sqrt()
        result={'Af':str(af),'Ag':str(ag),'q0':str(q),'zero_free_proved':bool(q<1)}
        if q<1:
            L=-(1-q).log()/ln2
            B=(af*ag).sqrt()*(R(r,beta)+R(s,beta))/(1-q)+abs((norm[0]*norm[1]).log()/ln2)
            H=abs((tilts[0]*tilts[1]).log()/ln2-kap*(norm[0]*norm[1]).log()/ln2)
            U=L+abs(kap-1)*B+H; W=abs(2-kap)*B+2*L+H
            result.update(U=U,W=W,L=L,B=B,H=H)
        report[v]=result
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    ctx.prec=128;ctx.threads=1;start=time.perf_counter()
    filters,rows=parse(a.source)
    pairs=[(3,0),(3,1),(4,0),(4,9)]
    needed=sorted({v for v,j in pairs}|{c for pair in pairs for c in rows[pair][0]})
    output={'purpose':'rigorous sufficient-strip feasibility probe only; no moment threshold evaluation',
            'bits':ctx.prec,'nodes':512,'needed_filters':needed,'probes':[]}
    for b in ['0.005','0.01','0.02','0.04','0.08']:
        t=time.perf_counter();r=strip(filters,needed,arb(b))
        output['probes'].append({'beta':b,'seconds':time.perf_counter()-t,'filters':{v:{k:str(x) if isinstance(x,arb) else x for k,x in d.items()} for v,d in r.items()}})
        print(b,[(v,r[v]['q0'],r[v]['zero_free_proved']) for v in needed],flush=True)
        output['seconds']=time.perf_counter()-start
        a.output.write_text(json.dumps(output,indent=2),encoding='utf-8')
