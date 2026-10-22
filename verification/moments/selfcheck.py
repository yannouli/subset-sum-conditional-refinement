"""Small direct finite-sum fixtures, independent of DFT index identities.

These test library convention/normalization, not the analytic error theorem.
"""
import argparse, json, time
from pathlib import Path
from flint import arb,acb,ctx
from strip_probe import parse,ball,trig

def correlation_fft(a,b):
    n=len(a); ah,bh=acb.dft(a),acb.dft(b)
    return [x.real/n for x in acb.dft([ah[j]*bh[-j%n] for j in range(n)],inverse=True)]

def check(a,b):
    n=len(a);out=correlation_fft(a,b)
    for j in range(n):
        direct=sum((a[(j+t)%n]*b[t] for t in range(n)),arb(0))/n
        assert out[j].overlaps(direct)
        assert (out[j]-direct).abs_upper()<arb('1e-40')
    return n

p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
ctx.prec=160;ctx.threads=1;start=time.perf_counter()
tested=check([arb(x) for x in [1,2,4,3,8,9,1]], [arb(x) for x in [2,0,5,1,4,7,3]])
filters,_=parse(a.source);n=32;cosines=[[ball(f'{2*j*k}/{n}').cos_pi() for k in range(1,9)] for j in range(n)]
kap,cs=filters[3];r,s=[trig([ball(c) for c in coeff],cosines) for coeff in cs]
F=[(arb(2).log()*x).exp() for x in r];G=[(arb(2).log()*x).exp() for x in s]
for left,right in [(F,G),([x*y for x,y in zip(F,r)],G),(F,[x*y for x,y in zip(G,s)])]:
    tested+=check(left,right)
a.output.write_text(json.dumps({'status':'PASS','comparisons':tested,'bits':ctx.prec,'seconds':time.perf_counter()-start,
    'fixtures':'non-even asymmetric integer vectors and actual filter3 P, Fr/G and F/Gs correlations; all shifts checked by direct normalized sums',
    'limitation':'regression fixture, not an independent analytic quadrature proof'},indent=2),encoding='utf-8')
print('PASS',tested,'direct finite-sum comparisons')
