#!/usr/bin/env python3
from __future__ import annotations
import json, shutil, tempfile
from pathlib import Path
from validation_lib import repo_root

def main():
    root=repo_root(); plugin=json.loads((root/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
    assert plugin['name']=='3d-visual-pipeline' and plugin['version']=='1.0.0' and plugin['skills']=='./skills/'
    source=root/'skills/3d-visual-pipeline'
    with tempfile.TemporaryDirectory() as td:
        target=Path(td)/'.agents/skills/3d-visual-pipeline'; target.parent.mkdir(parents=True); shutil.copytree(source,target)
        assert (target/'SKILL.md').exists() and (target/'agents/openai.yaml').exists()
    print('[PASS] installation-smoke'); return 0
if __name__=='__main__': raise SystemExit(main())
