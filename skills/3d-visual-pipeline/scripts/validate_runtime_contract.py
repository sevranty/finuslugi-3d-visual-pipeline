#!/usr/bin/env python3
from __future__ import annotations
from validation_lib import Result, parse_args, read_json, repo_root, write_report

def main():
    args=parse_args(__doc__ or 'runtime validator'); root=repo_root(); r=Result('runtime-contract')
    schema=read_json(root/'skills/3d-visual-pipeline/assets/schemas/runtime-capabilities.schema.json')
    cases=read_json(root/'skills/3d-visual-pipeline/evals/runtime-cases.json')
    allowed={'supported','unsupported','unknown'}
    if schema.get('title')!='Runtime Capability Profile': r.error('runtime schema title mismatch')
    for profile in cases.get('profiles',[]):
        if not profile.get('profile_id'): r.error('runtime profile missing id')
        for cap,state in profile.get('capabilities',{}).items():
            if state not in allowed: r.error(f'invalid capability state: {cap}={state}')
    text=(root/'skills/3d-visual-pipeline/references/runtime-capabilities.md').read_text(encoding='utf-8')
    for cap in ['generate','reference-conditioned','edit','deliver']:
        if f'`{cap}`' not in text: r.error(f'missing capability vocabulary: {cap}')
    r.check('schema-and-profiles'); return write_report(root,args,r)
if __name__=='__main__': raise SystemExit(main())
