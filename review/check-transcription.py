import sys,re,pathlib
from fractions import Fraction
sys.path.insert(0,str(pathlib.Path('subset-sum-speedrun/moment-review').resolve()))
from strip_probe import parse
f,r=parse(pathlib.Path('C:/Users/yanni/Desktop/SubsetSum-Speedrun-2026-10-21/upstream/ed-startup-2026-10-21/kapila-pinned-PROOF.tex'))
s=pathlib.Path('subset-sum-speedrun/lean-review/DataBridge.lean').read_text(encoding='utf8')
rat=lambda text:[Fraction(int(a),int(b)) for a,b in re.findall(r'\((-?\d+) / (\d+) : Rat\)',text)]
lines=[l for l in s.split('def expectedFilters')[1].split('def expectedCertificates')[0].splitlines() if l.startswith('\u27e8')]
assert len(lines)==43
for v,line in enumerate(lines):assert rat(line)==[f[v][0]]+f[v][1][0]+f[v][1][1],v
lines=[l for l in s.split('def expectedCertificates')[1].split('theorem filter_transcription')[0].splitlines() if l.startswith('\u27e8')]
seen=[]
for line in lines:
 m=re.match('\u27e8'+r'(\d+), (\d+), \[([^\]]*)\],',line);v,j=int(m[1]),int(m[2]);c=[int(x) for x in m[3].split(',') if x.strip()]
 assert (c,rat(line))==r[v,j];seen.append((v,j))
assert seen==[(v,j) for v in range(43) for j in range(10)]
print('Independent parsing confirms all 43 filters and 430 ordered certificate transcriptions')
