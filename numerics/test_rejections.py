"""Bounded falsification checks for bad scalar/source certificates (stdlib)."""
import argparse
import copy
import json
import tempfile
from pathlib import Path
from verify_certificate import ROOT, check


def run(baseline):
    original = json.loads((ROOT/'data/candidate.json').read_text())
    tests = [
        ('nonpositive small-prime parameter', 'gamma', '0', 'Basic ranges'),
        ('nonpositive left block', 'l', '0', 'Basic ranges'),
        ('work exponent cannot exceed advertised exponent',
         'target_exponent', '0.48767228', 'Pure exponent absorption gap'),
        ('insufficient assumed finite-circle margin',
         'finite_moment_margin', '0.000001', 'Continuous moment transfer: other_low'),
        ('vanished bit-length guard reserve',
         'input_guard_coefficient', '1000000000', 'Guard and preliminary loss'),
        ('overstated common alias slack',
         'alias_margin', '0.00000001', 'Common alias margin: C1_coverage'),
        ('broken checksum transfer',
         'eta', '0.517', 'Continuous moment transfer: other_low'),
    ]
    results = []
    with tempfile.TemporaryDirectory(prefix='subset-sum-rejections-') as folder:
        path = Path(folder)/'bad.json'
        for name, parameter, value, expected in tests:
            data = copy.deepcopy(original)
            data['parameters'][parameter] = value
            path.write_text(json.dumps(data), encoding='utf-8')
            try:
                check(path, baseline)
            except ValueError as error:
                if str(error) != expected:
                    raise AssertionError(f'{name}: wrong rejection {error!s}') from error
                results.append({'test': name, 'status': 'rejected', 'reason': str(error)})
            else:
                raise AssertionError(f'{name}: invalid candidate accepted')
        # Alter only a harmless comment: row parsing still succeeds, authentication must fail.
        altered = Path(folder)/'altered.tex'
        altered.write_bytes(baseline.read_bytes()+b'\n% deliberately altered input\n')
        try:
            check(ROOT/'data/candidate.json', altered)
        except ValueError as error:
            if str(error) != 'Pinned baseline hash mismatch':
                raise
            results.append({'test': 'modified upstream bytes', 'status': 'rejected', 'reason': str(error)})
        else:
            raise AssertionError('Altered upstream bytes accepted')
    return {'status': 'PASS', 'checks': results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path, default=ROOT/'baseline/PROOF_0.4877.tex')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = json.dumps(run(args.baseline), indent=2)
    if args.output:
        args.output.write_text(result, encoding='utf-8')
    print(result)
