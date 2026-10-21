"""Fetch one pinned upstream input, verify bytes, and keep it outside Git.

Optional network step; the exact checker itself never accesses the network.
"""
import argparse
import hashlib
from pathlib import Path
from urllib.request import urlopen

REVISION = '44c34961b56784c220a6e913cc068d57dc37c5a3'
URL = f'https://raw.githubusercontent.com/a-kapila/maths-proofs/{REVISION}/subset-sum/PROOF_0.4877.tex'
SHA256 = 'b397531cc5997e88c439d5290774861b46a34aa32d9cd71fa7dcced130359298'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).resolve().parent/'baseline/PROOF_0.4877.tex')
    args = parser.parse_args()
    with urlopen(URL, timeout=30) as response:
        data = response.read(5_000_001)
    if len(data) > 5_000_000 or hashlib.sha256(data).hexdigest() != SHA256:
        raise ValueError('Downloaded baseline does not match pinned bytes; no file written')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(data)
    print(f'Pinned baseline verified: {SHA256}\n{args.output}')
