#!/usr/bin/env python3
from __future__ import annotations
from validation_lib import Result, parse_args, read_json, repo_root, write_report

def main():
    args=parse_args(__doc__ or 'visual validator'); root=repo_root(); r=Result('visual-regression')
    cases=read_json(root/'skills/3d-visual-pipeline/evals/visual-cases.json').get('cases',[])
    accepted={}; rejected=0
    for case in cases:
        p=root/case['asset']
        if not p.exists(): r.error(f'missing visual case asset: {case["asset"]}'); continue
        text=p.read_text(encoding='utf-8')
        if '<svg' not in text or 'viewBox=' not in text: r.error(f'invalid SVG fixture: {case["asset"]}')
        if case['expected']=='accept': accepted[case['style_id']]=accepted.get(case['style_id'],0)+1
        elif case['expected']=='reject' and case.get('diagnostic'): rejected+=1
    for style in ['modern-flat','silver-gold','obsidian-gold']:
        if accepted.get(style,0)<1: r.error(f'missing accepted fixture for {style}')
    if rejected<1: r.error('missing rejected diagnostic fixture')
    r.check('style-and-negative-cases'); return write_report(root,args,r)
if __name__=='__main__': raise SystemExit(main())
