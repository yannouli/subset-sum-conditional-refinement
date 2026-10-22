"""Portable counterpart of historical review/check-transcription.py.

Compare the authenticated primary tables with every generated Lean record.
This is a data-transcription check, not a Lean proof or an integral validator.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'verification/moments'))
from strip_probe import parse


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,required=True)
    p.add_argument('--lean-data',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if a.output.exists(): raise FileExistsError('Choose a fresh output path; historical evidence is not overwritten')
    filters,rows=parse(a.source)
    text=a.lean_data.read_text(encoding='utf-8')
    rat=lambda s:[Fraction(int(x),int(y)) for x,y in re.findall(r'\((-?\d+) / (\d+) : Rat\)',s)]
    lines=[s for s in text.split('def expectedFilters')[1].split('def expectedCertificates')[0].splitlines() if s.startswith('\u27e8')]
    assert len(lines)==43
    for v,line in enumerate(lines):
        assert rat(line)==[filters[v][0]]+filters[v][1][0]+filters[v][1][1],v
    lines=[s for s in text.split('def expectedCertificates')[1].split('theorem filter_transcription')[0].splitlines() if s.startswith('\u27e8')]
    seen=[]
    for line in lines:
        m=re.match('\u27e8'+r'(\d+), (\d+), \[([^\]]*)\],',line)
        assert m is not None
        v,j=int(m[1]),int(m[2]);c=[int(x) for x in m[3].split(',') if x.strip()]
        assert (c,rat(line))==rows[v,j],(v,j)
        seen.append((v,j))
    assert seen==[(v,j) for v in range(43) for j in range(10)]
    result={'status':'PASS','filters':43,'ordered_distinct_pairs':430,
            'source_sha256':hashlib.sha256(a.source.read_bytes()).hexdigest(),
            'lean_data_sha256':hashlib.sha256(a.lean_data.read_bytes()).hexdigest(),
            'scope':'Exact primary-source versus Lean transcription; not integral or complete algorithm verification.'}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
