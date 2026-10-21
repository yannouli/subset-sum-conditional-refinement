"""Check a fixed scalar certificate, independently of the floating search.

This checks a conditional parameter/certificate refinement, not an implementation
of Subset Sum or the inherited continuous moment inequalities.
"""
import argparse,hashlib,json,re,time
from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING
from fractions import Fraction as Q
from pathlib import Path
from rational_bounds import Bounds,binary_log,entropy

ROOT=Path(__file__).resolve().parent
def require(condition,message):
    if not condition:raise ValueError(message)

def read_source(file):
    data=file.read_bytes();text=data.decode('utf-8');filters={};rows={}
    for line in text.splitlines():
        a=[s.strip() for s in line.split('&')]
        if len(a)!=4 or not a[0].isdigit():continue
        v=int(a[0]);reg=re.fullmatch(r'\$\\rho_\{(\d+)\}\$',a[1])
        if reg:
            region=int(reg[1]);z=[Q(s.strip()) for s in a[3].replace('\\','').split(',')]
            cons=[] if not a[2] else [int(s.strip()) for s in a[2].split(',')]
            require((v,region) not in rows,'Duplicate certificate')
            require(len(z)==len(cons)+(3 if 1<=region<=8 else 2),'Certificate dimension')
            require(len(set(cons))==len(cons) and v not in cons and all(0<=u<43 for u in cons),'Comparison indices')
            require(all(s>=0 for s in z) and sum(z)<=Q('418.36'),'Multiplier signs/budget')
            lower=[Q(s) for s in ['1','1.25','1.6','2','2.6','3.5','5','8','15']]
            require(z[0]>=(1 if region==0 else 1/lower[region-1]),'Domination multiplier')
            rows[v,region]=z
        elif re.fullmatch(r'\d+\.\d+',a[1]):
            coeff=[Q(s.strip()) for field in a[2:] for s in field.replace('\\','').split(',')]
            require(v not in filters,'Duplicate filter')
            require(len(coeff)==16 and all(abs(x)<=2 for x in coeff),'Filter coefficients')
            kap=Q(a[1]);require(1<=kap<=2,'Power range');filters[v]=(kap,coeff)
    require(set(filters)==set(range(43)),'Filter coverage')
    require(set(rows)=={(v,j) for v in range(43) for j in range(10)},'All430regions')
    return hashlib.sha256(data).hexdigest(),rows,filters

def shown(value):
    b=Bounds.exact(value)
    def dec(x,rounding):
        with localcontext() as c:
            c.prec=32;c.rounding=rounding
            return str(Decimal(x.numerator)/Decimal(x.denominator))
    return {'lower':dec(b.low,ROUND_FLOOR),'upper':dec(b.high,ROUND_CEILING)}

def check(certificate,baseline):
    start=time.perf_counter();data=json.loads(certificate.read_text());p={k:Q(v) for k,v in data['parameters'].items()}
    digest,rows,filters=read_source(baseline)
    require(digest==data['baseline_sha256'],'Pinned baseline hash mismatch')
    require(data['construction']=='filter3_boundary_split','Unexpected construction')
    t,e,a,m,g,l=[p[k] for k in ['tau','eta','a','mu','gamma','l']];r=1-m-l
    ep,zeta,guard,alias_margin,finite,target=[p[k] for k in ['epsilon','zeta','input_guard_coefficient','alias_margin','finite_moment_margin','target_exponent']]
    require(0<a<Q(1,4) and 0<m<1 and 0<t<Q(1,2) and Q(1,2)<e<1
            and 0<g<1 and 0<l<1,'Basic ranges')
    require(ep>0 and zeta>0 and guard>0 and alias_margin>0 and finite>0,'Accuracy/margin ranges')
    ha,h2,hb=entropy(a),entropy(2*a),entropy(Q(1,2)-a)
    delta_collision=(e-m*binary_log(3)/2)/2
    gaps={
      'C1_coverage':h2/2-g,
      'C2_left_list':t-l-(ha-g)*m,
      'C3_right_classes':t-r-(1-g)*m,
      'C4_pairs':t-1+m-(ha+hb-g)*m+e,
      'C5_right_masks':2*t-Q(1,2)-hb*m,
      'C6_left_map':t-l,'C6_right_map':t-r,'C6_right_positive':r,
      'C7_sampled_map':l-m*(1-2*a),
      'C8_reduction':e-m*binary_log(3)/2,
      'A7_block_classes':t-m,
      'A7_right_key_sort':2*t-Q(1,2)-r-zeta,
      'A7_small_prime':2*t-Q(1,2)-zeta-g*m/2,
      'prime_generation':t-e/2,
      'S2_sampled_size':Q(1,2)-m*(1-2*a),
      'S3_layer_size':1-2*a-h2/2-ha,
      'left_masks_cheaper':hb-ha,
      'A4_guard_collision':delta_collision-1/guard,
      'A5_remove_bad_halves':delta_collision-(Q(1,2)-t+zeta),
      'A5_density_threshold':Q('0.013')-(Q(1,2)-t+zeta),
    }
    for name,value in gaps.items():require(Bounds.exact(value).low>alias_margin,f'Common alias margin: {name}')
    require(zeta+1/guard<alias_margin,'Guard and preliminary loss')
    D=e-t;G=2*t-e;D0=Q('.02844');G0=Q('.45925');e0=Q('.51613')
    require(D>0 and 0<G<G0,'New budgets and q')
    q=G/G0;K=D/q-D0;da=D/G-D0/G0
    require(K>0 and da>0 and K==G0*da and 0<D/G<Q(1,4),'Transfer prerequisites')
    z30,z31=rows[3,0],rows[3,1]
    require(z30[:2]==[Q('17.211'),Q('27.1977')],'Special low data')
    require(z31[:3]==[Q('7.7547'),Q(0),Q(0)],'Special band data/zero lower multiplier')
    max_other=max(rows[v,0][0] for v in range(43) if v!=3)
    max_band=max(rows[v,1][0] for v in range(43))
    require(max_other==Q('10.6428') and max_band==Q('8.4537'),'Global maxima')
    margin_other=Q('.00025')+e-e0-max_other*K
    special_shift=z30[0]*(D-D0)+z30[1]*(G-G0)
    margin_special=Q('.00025')+e-e0-special_shift
    margin_band=Q('.00025')+e-e0-max_band*Q('1.25')*K
    margin_middle=Q(4)+e-e0-Q('418.36')*15*K
    margin_tail=Q(17)+e-e0-Q('418.36')*256*da
    moments={'other_low':margin_other,'special3_low':margin_special,'all_first_bands_including_extended3':margin_band,'rho2_to_rho8':margin_middle,'rho9':margin_tail}
    for name,value in moments.items():require(value>finite,f'Continuous moment transfer: {name}')
    new_sum=Q('418.36')*(1+da);require(new_sum<419,'New multiplier sum')
    error=finite-(18+6*419)*ep;work=t+20*ep
    require(error>0,'Mean-square error exponent');require(work<target,'Pure exponent absorption gap')
    require(t<Q('.48767595') and work<Q('.4876759502'),'Actual internal improvement, not display slack')
    return dict(status='PASS: exact scalar certificate under explicit inherited assumptions',
        assumptions=data['inherited_assumptions'],baseline_sha256=digest,
        finite_source_checks=dict(filters=len(filters),certificates=len(rows),special_lower_multiplier_zero=True),
        alias_gaps={k:shown(v) for k,v in gaps.items()},moment_margins={k:shown(v) for k,v in moments.items()},
        budgets={k:shown(v) for k,v in dict(Delta=D,Gamma=G,q=q,K=K,delta_slope=da,special_low_shift=special_shift,new_sum_bound=new_sum).items()},
        error_exponent=shown(error),work_exponent=shown(work),target_exponent=shown(target),absorption_gap=shown(target-work),
        limitation='Does not execute or prove a complete Subset Sum solver, certify the original continuous integrals, or establish site Lean verification.',seconds=time.perf_counter()-start)

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--certificate',type=Path,default=ROOT/'data/candidate.json');ap.add_argument('--baseline',type=Path,default=ROOT/'baseline/PROOF_0.4877.tex');ap.add_argument('--output',type=Path);args=ap.parse_args()
    result=check(args.certificate,args.baseline);out=json.dumps(result,indent=2)
    if args.output:args.output.write_text(out,encoding='utf-8')
    print(out)
