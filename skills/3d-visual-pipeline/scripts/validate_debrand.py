#!/usr/bin/env python3
from __future__ import annotations
import json, re
from pathlib import Path
from validation_lib import Result, parse_args, read_json, repo_root, tracked_files, write_report

def blocked_tokens():
    cyr=lambda seq: ''.join(chr(x) for x in seq)
    return [
        ''.join(['fin','us','lugi']),
        cyr([1092,1080,1085,1091,1089,1083,1091,1075,1080]),
        ''.join(['mo','ex']),
        cyr([1084,1086,1089,1082,1086,1074,1089,1082,1072,1103,32,1073,1080,1088,1078,1072]),
        ''.join(['f','d','s']),
        ''.join(['f','3','d']),
        ''.join(['ff','05','08']),
    ]
def scan(root:Path):
    errors=[]; tokens=blocked_tokens(); text_suffix={'.md','.json','.yaml','.yml','.py','.svg','.txt'}
    for p in tracked_files(root):
        rel=p.relative_to(root).as_posix(); low=rel.lower()
        for token in tokens:
            if token in low: errors.append(f'blocked path token in {rel}')
        if p.suffix.lower() in text_suffix:
            try: text=p.read_text(encoding='utf-8').lower()
            except UnicodeDecodeError: continue
            for token in tokens:
                if token in text: errors.append(f'blocked text token in {rel}')
    return sorted(set(errors))
def main():
    args=parse_args(__doc__ or 'debrand validator'); root=repo_root(); r=Result('debrand')
    for e in scan(root): r.error(e)
    plugin=read_json(root/'.codex-plugin/plugin.json')
    if plugin.get('name')!='3d-visual-pipeline': r.error('generic plugin identity missing')
    if plugin.get('interface',{}).get('brandColor')!='#6B7280': r.error('neutral interface color missing')
    if (root/'skills/3d-visual-pipeline').exists() is False: r.error('generic skill path missing')
    r.check('active-tree-scan'); return write_report(root,args,r)
if __name__=='__main__': raise SystemExit(main())
