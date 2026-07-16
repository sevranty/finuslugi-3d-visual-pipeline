#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path
from validation_lib import Result, broken_relative_paths, parse_args, read_json, repo_root, tracked_files, write_report

def main():
    args=parse_args(__doc__ or 'repository validator'); root=repo_root(); r=Result('repository')
    required=['.codex-plugin/plugin.json','README.md','AGENTS.md','CHANGELOG.md','RELEASE_CHECKLIST.md','LICENSE','assets/plugin-icon.png','assets/plugin-logo.png','assets/manifest.json','assets/checksums.sha256','skills/3d-visual-pipeline/SKILL.md','skills/3d-visual-pipeline/agents/openai.yaml']
    for rel in required:
        if not (root/rel).exists(): r.error(f'missing required path: {rel}')
    r.check('required-paths')
    plugin=read_json(root/'.codex-plugin/plugin.json')
    if plugin.get('name')!='3d-visual-pipeline': r.error('plugin name mismatch')
    if plugin.get('version')!='1.0.0': r.error('plugin version mismatch')
    if plugin.get('skills')!='./skills/': r.error('plugin skills path mismatch')
    if plugin.get('interface',{}).get('brandColor')!='#6B7280': r.error('neutral interface color mismatch')
    for key in ('composerIcon','logo'):
        value=plugin.get('interface',{}).get(key,'')
        if not value.startswith('./') or not (root/value[2:]).exists(): r.error(f'plugin {key} target missing')
    r.check('plugin-manifest')
    skill=(root/'skills/3d-visual-pipeline/SKILL.md').read_text(encoding='utf-8')
    if not skill.startswith('---\nname: 3d-visual-pipeline\n'): r.error('SKILL frontmatter name mismatch')
    r.check('skill-frontmatter')
    for p in tracked_files(root):
        rel=p.relative_to(root).as_posix()
        try: rel.encode('ascii')
        except UnicodeEncodeError: r.error(f'non-ASCII path: {rel}')
        if p.suffix.lower() in {'.docx','.pdf'}: r.error(f'forbidden document type: {rel}')
        if p.suffix.lower()=='.json':
            try: json.loads(p.read_text(encoding='utf-8'))
            except Exception as e: r.error(f'invalid JSON {rel}: {e}')
    r.check('path-and-json-integrity')
    for item in broken_relative_paths(root): r.error(f'broken relative path: {item}')
    r.check('relative-links')
    return write_report(root,args,r)
if __name__=='__main__': raise SystemExit(main())
