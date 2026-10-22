"""Case 02 v0.5: finite projection model and document consistency checks.
This does not execute the integration acceptance scenarios.
"""
from pathlib import Path
import csv
import itertools
import re
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / 'artifacts'
OMS = ('UNKNOWN', 'OPEN', 'CLOSED_REFUND_REGISTERED', 'CLOSED_NO_REFUND')
WMS = ('UNKNOWN', 'PENDING', 'ACCEPTED', 'REJECTED')
PSP = ('UNKNOWN', 'PENDING', 'COMPLETED', 'FAILED')


def decide(o, w, p, flag=False):
    assert o in OMS and w in WMS and p in PSP
    known = p != 'UNKNOWN'
    if flag:
        return 'D01', 'NEEDS_RECONCILIATION'
    if ((w == 'REJECTED' and (known or o == 'CLOSED_REFUND_REGISTERED'))
            or (o == 'CLOSED_NO_REFUND' and (known or w == 'ACCEPTED'))):
        return 'D02', 'NEEDS_RECONCILIATION'
    if w == 'REJECTED':
        return 'D03', 'RETURN_REJECTED'
    if (w in ('UNKNOWN', 'PENDING')
            and (known or o in ('CLOSED_REFUND_REGISTERED', 'CLOSED_NO_REFUND'))):
        return 'D04', 'AWAITING_CONFIRMATION'
    if w == 'ACCEPTED' and p == 'COMPLETED':
        return 'D05', 'REFUND_ISSUED'
    if w == 'ACCEPTED' and p == 'FAILED':
        return 'D06', 'REFUND_FAILED'
    if w == 'ACCEPTED' and p == 'PENDING':
        return 'D07', 'REFUND_PROCESSING'
    if w == 'ACCEPTED' and p == 'UNKNOWN':
        return 'D08', 'REFUND_NOT_CONFIRMED'
    return 'D09', 'RETURN_IN_PROGRESS'


def main():
    dictionary = list(csv.DictReader((ART / 'status-mapping.csv').open()))
    assert len(dictionary) == 9
    keys = [(r['contract_version'], r['source_system'], r['object_type'],
             r['raw_status'], r['inspection_result']) for r in dictionary]
    assert len(set(keys)) == len(keys)
    assert all(r['mapping_version'] == '0.3' and r['contract_version'] == '1'
               for r in dictionary)
    expected_terminals = {
        ('OMS', 'COMPLETED', ''), ('OMS', 'CLOSED_NO_REFUND', ''),
        ('WMS', 'COMPLETED', 'ACCEPTED'), ('WMS', 'COMPLETED', 'REJECTED'),
        ('PSP', 'FAILED', '')}
    terminals = {(r['source_system'], r['raw_status'], r['inspection_result'])
                 for r in dictionary if r['is_terminal'] == 'true'}
    assert terminals == expected_terminals
    assert all(r['is_terminal'] in ('true', 'false') for r in dictionary)
    for source, states in [('OMS', OMS), ('WMS', WMS), ('PSP', PSP)]:
        assert {r['target_value'] for r in dictionary if r['source_system'] == source} == set(states) - {'UNKNOWN'}
    table = '| Source / object | Raw status | Required result | Target fact | Terminal | Meaning |\n|---|---|---|---|---|---|\n'
    for r in dictionary:
        table += (f"| {r['source_system']} / {r['object_type']} | {r['raw_status']} | "
                  f"{r['inspection_result'] or '(absent)'} | {r['target_dimension']}={r['target_value']} | "
                  f"{r['is_terminal']} | {r['meaning']} |\n")
    spec = ART / 'specification.md'
    text = spec.read_text()
    text, count = re.subn(r'<!-- dictionary:start -->.*?<!-- dictionary:end -->',
                         '<!-- dictionary:start -->\n' + table + '<!-- dictionary:end -->',
                         text, flags=re.S)
    assert count == 1
    spec.write_text(text)
    # Manually specified outcomes, independent of enumerator output.
    examples = [
        (('CLOSED_NO_REFUND', 'REJECTED', 'UNKNOWN'), ('D03', 'RETURN_REJECTED')),
        (('CLOSED_NO_REFUND', 'ACCEPTED', 'UNKNOWN'), ('D02', 'NEEDS_RECONCILIATION')),
        (('OPEN', 'ACCEPTED', 'COMPLETED'), ('D05', 'REFUND_ISSUED')),
        (('OPEN', 'PENDING', 'FAILED'), ('D04', 'AWAITING_CONFIRMATION')),
        (('CLOSED_REFUND_REGISTERED', 'UNKNOWN', 'UNKNOWN'), ('D04', 'AWAITING_CONFIRMATION')),
        (('OPEN', 'PENDING', 'UNKNOWN'), ('D09', 'RETURN_IN_PROGRESS')),
        (('OPEN', 'ACCEPTED', 'UNKNOWN'), ('D08', 'REFUND_NOT_CONFIRMED')),
        (('OPEN', 'ACCEPTED', 'FAILED'), ('D06', 'REFUND_FAILED')),
        (('OPEN', 'ACCEPTED', 'PENDING'), ('D07', 'REFUND_PROCESSING'))]
    for inputs, expected in examples:
        assert decide(*inputs) == expected, inputs
    output = []
    coverage = Counter()
    for o, w, p in itertools.product(OMS, WMS, PSP):
        rule, result = decide(o, w, p)
        coverage[rule] += 1
        flagged_rule, flagged_result = decide(o, w, p, True)
        assert flagged_rule == 'D01' and flagged_result == 'NEEDS_RECONCILIATION'
        if result == 'REFUND_ISSUED':
            assert w == 'ACCEPTED' and p == 'COMPLETED' and o != 'CLOSED_NO_REFUND'
        if result == 'RETURN_REJECTED':
            assert w == 'REJECTED' and p == 'UNKNOWN' and o != 'CLOSED_REFUND_REGISTERED'
        if o == 'CLOSED_NO_REFUND' and p != 'UNKNOWN':
            assert result == 'NEEDS_RECONCILIATION'
        if w == 'REJECTED' and p != 'UNKNOWN':
            assert result == 'NEEDS_RECONCILIATION'
        output.append([o, w, p, rule, result, str(rule == 'D02').lower(), flagged_rule, flagged_result])
    assert len({r[4] for r in output}) == 8
    assert len(output) == 64 and set(coverage) == {f'D{i:02}' for i in range(2, 10)}
    with (ART / 'decision-combinations.csv').open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['return_state', 'inspection_state', 'refund_state',
                         'rule_without_flag', 'projection_without_flag', 'creates_flag',
                         'rule_with_flag', 'projection_with_flag'])
        writer.writerows(output)
    acceptance = (ART / 'acceptance-scenarios.md').read_text()
    ids = re.findall(r'^\| (AC-\d+) \|', acceptance, re.M)
    assert ids == [f'AC-{i:02}' for i in range(1, 113)]
    lengths = {}
    for lang in ('en', 'ru'):
        post = (ROOT / f'post.{lang}.md').read_text().strip()
        lengths[lang] = len(post)
        assert len(post) < 3000 and '112' in post
        assert 'REFUND_ISSUED' in post and '#SystemIntegration' in post
    # Ensure every projection result has a bilingual display row.
    display = (ART / 'display-mapping.md').read_text()
    assert all(f'| {r[4]} |' in display for r in output)
    report = f'''# Model and Document Validation

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.5  
Language: en  
Status: Draft

## Purpose
Report executed finite-model and document checks separately from specified integration behavior.

## Executed checks
- Parsed 9 dictionary rows; keys unique; contract/mapping versions and 5 terminal mappings checked.
- Generated the embedded dictionary from the CSV; verified projected state sets match the model domains.
- Enumerated 64 state tuples with no reconciliation flag and 64 D01 overrides: 128 model inputs.
- Checked success prerequisites, rejection prerequisites, no-refund contradictions, and 9 independent input/expected-result examples.
- All nine rules exercised (D01 through flag cases); eight distinct projection enums. D02–D09 counts: {dict(sorted(coverage.items()))}.
- Verified AC-01 through AC-112 are present once and in order. These are not executed acceptance tests.
- Checked every model result has a display mapping and draft relative links resolve.
- Post lengths including case URL: EN {lengths['en']}; RU {lengths['ru']} characters.
- Checked authored Markdown, CSV, and Python for prohibited dash characters.

## Not verified by this script
Transport, identity validation, event ingestion, concurrency, persistence, dispatch, clocks, escalation, and re-baseline have specified expectations but no integration implementation was executed. PDF layout validation is recorded separately in pdf-validation.md. This script does not verify remote publication status.

---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
'''
    (ART / 'validation-report.md').write_text(report)
    for path in ROOT.rglob('*'):
        if not path.is_file() or path.suffix not in ('.md', '.csv', '.py'):
            continue
        content = path.read_text()
        assert chr(0x2014) not in content, path
        if path.suffix in ('.md', '.csv'):
            assert 'REFUND_' + 'COMPLETED' not in content, path
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', content):
                if '://' not in target and not target.startswith('#'):
                    assert (path.parent / target.split('#')[0]).exists(), (path, target)
    print(f'PASS: 128 model inputs, 9 independent examples, 112 scenario IDs; posts {lengths}')


if __name__ == '__main__':
    main()
