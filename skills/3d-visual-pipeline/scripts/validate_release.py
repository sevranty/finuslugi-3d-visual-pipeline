#!/usr/bin/env python3
from __future__ import annotations
from validation_lib import Result, parse_args, read_json, repo_root, write_report
VERSION='1.0.0'; TAG='v1.0.0'
def main():
    args=parse_args(__doc__ or 'release validator'); root=repo_root(); r=Result('release')
    plugin=read_json(root/'.codex-plugin/plugin.json'); manifest=read_json(root/f'release/{VERSION}/validation-manifest.json')
    if plugin.get('version')!=VERSION: r.error('plugin version not aligned')
    if manifest.get('version')!=VERSION or manifest.get('intended_tag')!=TAG: r.error('release manifest not aligned')
    for path in [f'release/{VERSION}/RELEASE_NOTES.md','CHANGELOG.md','README.md','RELEASE_CHECKLIST.md']:
        text=(root/path).read_text(encoding='utf-8')
        if VERSION not in text: r.error(f'version absent from {path}')
    if manifest.get('status') not in {'candidate','pass'}: r.error('release status must be candidate or pass')
    r.check('version-and-publication-contract'); return write_report(root,args,r)
if __name__=='__main__': raise SystemExit(main())
