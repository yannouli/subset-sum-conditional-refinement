"""Portable output-correspondence checks adapted from historical moment-audit.py.

Use after executing the full validator. This checks coverage, required thresholds,
strict ball separation and mathematical-output correspondence. It does not
replace the validator or independently prove the analytic quadrature theorem.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from flint import arb,ctx

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'verification/moments'))
from strip_probe import parse


def audit(path,rows,source_hash):
    d=json.loads(path.read_text(encoding='utf-8'))
    pairs=[(r['filter'],r['region']) for r in d['results']]
    assert len(pairs)==430 and len(set(pairs))==430 and set(pairs)==set(rows)
    assert d['complete'] and d['source_sha256']==source_hash
    for r in d['results']:
        m=arb('0.00025') if r['region']<2 else arb(17 if r['region']==9 else 4)
        expected=((arb('0.51613')-m)*arb(2).log()).exp()
        threshold=arb(r['threshold']);integral=arb(r['integral_enclosure'])
        assert threshold.overlaps(expected)
        assert integral.upper()<expected.lower()
        assert integral.upper()<threshold.lower()
        assert r['status']=='certified' and arb(r['strict_gap'])>0
        for n in r['normalizers'].values():
            assert arb(n['minimum_P_lower'])>0 and arb(n['Zfk'])>0 and arb(n['Zgk'])>0
            assert arb(n['P_inner_error'])>=0 and arb(n['Y_inner_error'])>=0
        assert arb(r['outer_error'])>=0
    for v,bounds in d['strip_bounds'].items():
        assert bounds['zero_free_proved'] and arb(bounds['q0'])<1
    return d


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for flag in ['source','reference','replay','output']:p.add_argument('--'+flag,type=Path,required=True)
    a=p.parse_args()
    if a.output.exists():raise FileExistsError('Choose a fresh output path; historical evidence is not overwritten')
    ctx.prec=160;ctx.threads=1
    filters,rows=parse(a.source);assert set(filters)==set(range(43))
    source_hash=hashlib.sha256(a.source.read_bytes()).hexdigest()
    reference=audit(a.reference,rows,source_hash);replay=audit(a.replay,rows,source_hash)
    by_pair=lambda d:{(r['filter'],r['region']):r for r in d['results']}
    original,fresh=by_pair(reference),by_pair(replay)
    mathematical_fields=['nodes','status','integral_enclosure','threshold','strict_gap','outer_error','node_average','log_strip_bound','normalizers']
    for pair in original:
        for key in mathematical_fields:assert original[pair][key]==fresh[pair][key],(pair,key)
    result={'status':'PASS','filters':43,'distinct_pairs':430,'all_strict_thresholds':True,
            'mathematical_output_fields_identical':True,'reference_seconds':reference['seconds'],'replay_seconds':replay['seconds'],
            'source_sha256':source_hash,'reference_sha256':hashlib.sha256(a.reference.read_bytes()).hexdigest(),
            'replay_sha256':hashlib.sha256(a.replay.read_bytes()).hexdigest(),
            'scope':'Correspondence/positivity/strict-gap check of full validated outputs; outside-Lean Python/FLINT/Arb and written-analysis trust.'}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
