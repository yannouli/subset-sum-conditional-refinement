"""Bounded floating-point discovery only. Never a certificate or a solver theorem."""
import json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

ROOT=Path(__file__).resolve().parent
BASE=np.array([.48767595,.51612858,.008145205148,.475442899283,.060035950245,.483780402235])
D0=.02844;G0=.45925;E0=.51613
SCALE=np.array([1e-5,1e-5,1e-5,1e-4,1e-4,1e-5])
def entropy(a):return -a*np.log2(a)-(1-a)*np.log2(1-a)

def constraints(x,family):
    tau,eta,a,mu,g,l=x;r=1-mu-l
    ha,h2,hb=entropy(a),entropy(2*a),entropy(.5-a)
    D=eta-tau;G=2*tau-eta;K=D*G0/G-D0;da=K/G0;q=G/G0
    v=[h2/2-g,tau-l-(ha-g)*mu,tau-r-(1-g)*mu,
       tau-1+mu-(ha+hb-g)*mu+eta,2*tau-.5-hb*mu,
       tau-l,tau-r,r,l-mu*(1-2*a),eta-mu*np.log2(3)/2,
       .5-mu*(1-2*a),1-2*a-h2/2-ha,hb-ha,tau-mu,
       .25-D/G,q,1-q,K,da]
    # Explicit positive margins, with much smaller epsilon/guard reserved below.
    v=np.array(v)-1e-9
    if family=='uniform':m0=.00025+eta-E0-17.211*K
    else:m0=.00025+eta-E0-10.6428*K # max c0 excluding filter3
    m1=.00025+eta-E0-8.4537*1.25*K
    middle=4+eta-E0-418.36*15*K
    tail=17+eta-E0-418.36*256*da
    extra=.00025+eta-E0-(17.211*(D-D0)+27.1977*(G-G0))
    margins=[m0,m1,middle,tail]
    if family=='split_filter3':margins.append(extra)
    return np.r_[1e5*v,1e4*(np.array(margins)-1e-7),419-418.36*(1+da)]

def main():
    rng=np.random.default_rng(20261021);records=[];start=time.perf_counter()
    bounds=[(.48,.48996),(.51,.52),(.005,.012),(.46,.49),(.04,.08),(.47,.49)]
    scaled_bounds=[((lo-b)/s,(hi-b)/s) for (lo,hi),b,s in zip(bounds,BASE,SCALE)]
    for family in ['uniform','split_filter3']:
        for j in range(12):
            if time.perf_counter()-start>30:break
            init=np.zeros(6) if j==0 else rng.normal(size=6)*.5
            t0=time.perf_counter()
            res=minimize(lambda z:(BASE+SCALE*z)[0]/1e-5,init,method='SLSQP',bounds=scaled_bounds,
                constraints=[{'type':'ineq','fun':lambda z:constraints(BASE+SCALE*z,family)}],
                options={'ftol':1e-11,'maxiter':400})
            x=BASE+SCALE*res.x;v=constraints(x,family)
            records.append(dict(family=family,start=j,success=bool(res.success),message=res.message,
                parameters={k:format(float(t),'.16g') for k,t in zip(['tau','eta','a','mu','gamma','l'],x)},
                minimum_scaled_slack=float(v.min()),nfev=res.nfev,nit=res.nit,seconds=time.perf_counter()-t0))
            print(family,j,res.success,format(x[0],'.13f'),v.min(),flush=True)
    result={'classification':'FLOATING DISCOVERY ONLY, NOT CERTIFIED','seed':20261021,'seconds':time.perf_counter()-start,'runs':records}
    (ROOT/'evidence/discovery.json').write_text(json.dumps(result,indent=2),encoding='utf-8')

if __name__=='__main__':main()
