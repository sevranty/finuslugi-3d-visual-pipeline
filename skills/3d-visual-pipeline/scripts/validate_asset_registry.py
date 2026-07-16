#!/usr/bin/env python3
from __future__ import annotations
import re
from validation_lib import Result, parse_args, read_json, repo_root, sha256_file, tracked_files, write_report
VISUAL={'.png','.svg','.jpg','.jpeg','.webp','.gif'}
def main():
    args=parse_args(__doc__ or 'asset validator'); root=repo_root(); r=Result('asset-registry')
    manifest=read_json(root/'assets/manifest.json'); entries=manifest.get('assets',[]); by_path={e.get('path'):e for e in entries}
    checksum_lines=(root/'assets/checksums.sha256').read_text(encoding='utf-8').splitlines(); checks={line.split('  ',1)[1]:line.split('  ',1)[0] for line in checksum_lines if '  ' in line}
    visuals=[p.relative_to(root).as_posix() for p in tracked_files(root) if p.suffix.lower() in VISUAL]
    if set(visuals)!=set(by_path):
        for p in sorted(set(visuals)-set(by_path)): r.error(f'unregistered visual: {p}')
        for p in sorted(set(by_path)-set(visuals)): r.error(f'manifest path missing: {p}')
    for path,e in by_path.items():
        p=root/path
        if not p.exists(): continue
        actual=sha256_file(p)
        if e.get('sha256')!=actual: r.error(f'manifest checksum mismatch: {path}')
        if checks.get(path)!=actual: r.error(f'checksum file mismatch: {path}')
        if e.get('source_status')!='repository-authored': r.error(f'non-generic source status: {path}')
        if e.get('rights_status')!='cleared' or e.get('approval_status')!='approved' or e.get('public_distribution_status')!='approved': r.error(f'asset not publicly cleared: {path}')
    r.check('inventory-and-checksums'); return write_report(root,args,r)
if __name__=='__main__': raise SystemExit(main())
