"""Validated original continuous moments for fixed exact source records.

Arb arithmetic and its DFT implement outward enclosures of finite sums.
Analytic errors are from the reviewed analytic-contract.tex, NOT mesh agreement.
All trust in FLINT/Python and that written theorem is explicitly outside Lean.
No candidate parameters, source data or historical evidence are modified.
"""
import argparse, hashlib, json, math, platform, time
from pathlib import Path
import flint
from flint import arb, acb, ctx
from strip_probe import parse, ball, widen, rem, strip, trig

def encode(x):
    if isinstance(x,arb):
        # Full enclosing ball text; never trim radii or round an endpoint inward.
        return x.str(40)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(v) for v in x]
    return x

def row_bound(v,j,rows,bounds,beta):
    c,z=rows[v,j]; U,W=bounds[v]['U'],bounds[v]['W']
    gamma=arb('0.45925'); delta=arb('0.02844'); slope=delta/gamma
    levels=list(map(arb,['0','1','1.25','1.6','2','2.6','3.5','5','8','15']))
    if j==0:
        ss=[delta+U,gamma+W]
    elif j==9:
        ss=[slope*W+U,W-15*gamma]
    else:
        ss=[slope*W+U,W-gamma*levels[j],gamma*levels[j+1]+W]
    ss += [U+bounds[k]['U'] for k in c]
    assert len(ss)==len(z)
    exponent=sum((ball(a)*b for a,b in zip(z,ss)),arb(0))
    logB=(2+2*(2*beta).cosh()).log()+arb(2).log()*exponent
    margin=arb('0.00025') if j<2 else arb(17 if j==9 else 4)
    threshold=((arb('0.51613')-margin)*arb(2).log()).exp()
    return logB,threshold

def scores(v,n,filters,cosines):
    k,cs=filters[v]; k=ball(k); r,s=[trig([ball(c) for c in coeff],cosines) for coeff in cs]
    ln2=arb(2).log(); sigma=arb('0.1')
    F=[(ln2*x).exp() for x in r];G=[(ln2*x).exp() for x in s]
    R,S=[sum((abs(ball(c))*(j*sigma).cosh() for j,c in enumerate(coeff,1)),arb(0)) for coeff in cs]
    zfk=widen(sum(((ln2*k*x).exp() for x in r),arb(0))/n,rem((ln2*k*R).exp(),sigma,n))
    zgk=widen(sum(((ln2*k*x).exp() for x in s),arb(0))/n,rem((ln2*k*S).exp(),sigma,n))
    assert zfk>0 and zgk>0
    logZ=(zfk*zgk).log()/ln2
    # Inverse DFT is normalized. Reverse G's Fourier indices for correlation
    # sum_t F[j+t]G[t]; then divide by n for the circle probability average.
    fh=acb.dft(F);gh=acb.dft(G)
    frh=acb.dft([x*y for x,y in zip(F,r)])
    gsh=acb.dft([x*y for x,y in zip(G,s)])
    ph=acb.dft([fh[j]*gh[-j%n] for j in range(n)],inverse=True)
    yh=acb.dft([frh[j]*gh[-j%n]+fh[j]*gsh[-j%n] for j in range(n)],inverse=True)
    eP=rem((ln2*(R+S)).exp(),sigma,n)
    eY=rem((R+S)*(ln2*(R+S)).exp(),sigma,n)
    us,ws=[],[];minP=None
    for p,y in zip(ph,yh):
        assert p.imag.contains(0) and y.imag.contains(0)
        P=widen(p.real/n,eP);Y=widen(y.real/n,eY)
        assert P>0
        minP=P.lower() if minP is None else minP.min(P.lower())
        a=P.log()/ln2;b=Y/P
        us.append(a+(k-1)*b-logZ)
        ws.append((2-k)*b-2*a+logZ)
    return us,ws,{'minimum_P_lower':minP,'Zfk':zfk,'Zgk':zgk,'P_inner_error':eP,'Y_inner_error':eY}

def evaluate(pairs,source,output,bits=160,max_nodes=131072,max_seconds=600):
    ctx.prec=bits;ctx.threads=1;start=time.perf_counter()
    filters,rows=parse(source);beta=arb('0.08')
    needed=sorted({v for v,j in pairs}|{c for pair in pairs for c in rows[pair][0]})
    bounds=strip(filters,needed,beta)
    assert all(bounds[v]['zero_free_proved'] for v in needed)
    plans={};largest=0
    for v,j in pairs:
        logB,threshold=row_bound(v,j,rows,bounds,beta)
        n=512
        while not rem(logB.exp(),2*beta,n)<threshold/10**9 and n<max_nodes: n*=2
        assert n<=max_nodes and rem(logB.exp(),2*beta,n)<threshold/10**9
        plans[v,j]=(n,logB,threshold);largest=max(largest,n)
    report={'purpose':'original continuous inequalities, fixed source data; not Lean proof or complete algorithm verification',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'python':platform.python_version(),
        'python_flint':flint.__version__,'bits':bits,'threads':1,'beta':beta,'inner_sigma':'0.1',
        'max_nodes':max_nodes,'max_seconds':max_seconds,'planned_pairs':pairs,
        'largest_node_count':largest,'strip_bounds':bounds,'results':[]}
    output.write_text(json.dumps(encode(report),indent=2),encoding='utf-8')
    for n in sorted({p[0] for p in plans.values()}):
        active=[pair for pair in pairs if plans[pair][0]==n]
        ids=sorted({v for v,j in active}|{c for pair in active for c in rows[pair][0]})
        cosines=[[(ball(f'{2*j*k}/{n}')).cos_pi() for k in range(1,9)] for j in range(n)]
        saved={};normalizers={}
        for v in ids:
            assert time.perf_counter()-start<max_seconds, 'finite campaign wall-clock cap'
            t=time.perf_counter();u,w,details=scores(v,n,filters,cosines)
            saved[v]=(u,w);normalizers[v]=details
            print('filter',v,'nodes',n,'seconds',round(time.perf_counter()-t,3),flush=True)
        for v,j in active:
            c,z=rows[v,j];u,w=saved[v];ln2=arb(2).log();gamma=arb('0.45925');delta=arb('0.02844');slope=delta/gamma
            levels=list(map(arb,['0','1','1.25','1.6','2','2.6','3.5','5','8','15']))
            total=arb(0)
            for k in range(n):
                if j==0: ss=[delta-u[k],gamma-w[k]]
                elif j==9: ss=[slope*w[k]-u[k],w[k]-15*gamma]
                else: ss=[slope*w[k]-u[k],w[k]-levels[j]*gamma,levels[j+1]*gamma-w[k]]
                ss += [u[k]-saved[a][0][k] for a in c]
                assert len(ss)==len(z)
                exponent=sum((ball(a)*b for a,b in zip(z,ss)),arb(0))
                m2=2+2*cosines[k][0]
                total += m2*(ln2*exponent).exp()
            node_average=total/n;_,logB,threshold=plans[v,j]
            outer=rem(logB.exp(),2*beta,n);integral=widen(node_average,outer)
            status='certified' if integral<threshold else 'refuted' if integral>threshold else 'unresolved'
            result={'filter':v,'region':j,'nodes':n,'status':status,'node_average':node_average,
                    'outer_error':outer,'integral_enclosure':integral,'threshold':threshold,
                    'strict_gap':threshold-integral,'log_strip_bound':logB,'normalizers':{i:normalizers[i] for i in [v]+c}}
            report['results'].append(result);report['seconds']=time.perf_counter()-start
            output.write_text(json.dumps(encode(report),indent=2),encoding='utf-8')
            print('ROW',v,j,status,'integral',integral,'threshold',threshold,flush=True)
    report['complete']=len(report['results'])==len(pairs)
    report['seconds']=time.perf_counter()-start
    output.write_text(json.dumps(encode(report),indent=2),encoding='utf-8')
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--all',action='store_true');p.add_argument('--bits',type=int,default=160)
    p.add_argument('--max-seconds',type=int,default=600);a=p.parse_args()
    pairs=[(v,j) for v in range(43) for j in range(10)] if a.all else [(3,0),(3,1),(4,0),(4,9)]
    evaluate(pairs,a.source,a.output,a.bits,max_seconds=a.max_seconds)
