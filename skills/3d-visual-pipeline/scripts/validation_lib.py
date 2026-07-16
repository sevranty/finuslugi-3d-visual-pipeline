from __future__ import annotations
import argparse, datetime as dt, hashlib, json, re, subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_PATH_RE = re.compile(r"`((?:\.\./|\./|skills/|assets/|release/|docs/)[A-Za-z0-9_./-]+(?:\.[A-Za-z0-9]+)?)`")

@dataclass
class Result:
    name: str
    checks: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    @property
    def ok(self): return not self.errors
    def check(self,x): self.checks.append(x)
    def error(self,x): self.errors.append(x)
    def warning(self,x): self.warnings.append(x)

def repo_root() -> Path: return Path(__file__).resolve().parents[3]
def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()
def read_json(path:Path): return json.loads(path.read_text(encoding='utf-8'))
def tracked_files(root:Path)->list[Path]:
    try:
        out=subprocess.run(['git','-C',str(root),'ls-files','-z'],check=True,capture_output=True).stdout
        return [root/p.decode() for p in out.split(b'\0') if p]
    except Exception:
        return [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
def parse_args(description:str):
    p=argparse.ArgumentParser(description=description); p.add_argument('--report',type=Path); p.add_argument('--no-report',action='store_true'); return p.parse_args()
def write_report(root:Path,args,result:Result):
    payload={'validator':result.name,'status':'pass' if result.ok else 'fail','checks':result.checks,'warnings':result.warnings,'errors':result.errors,'timestamp_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    if not args.no_report:
        path=args.report or root/'validation'/'runtime'/f'{result.name}.json'; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print(f"[{'PASS' if result.ok else 'FAIL'}] {result.name}")
    for x in result.warnings: print('WARNING:',x)
    for x in result.errors: print('ERROR:',x)
    return 0 if result.ok else 1
def resolve_doc_path(document:Path, link:str, root:Path)->Path|None:
    clean=link.split('#',1)[0].strip()
    if not clean or clean.startswith(('http://','https://','mailto:','#')): return None
    if clean.startswith('/'): return root/clean.lstrip('/')
    return (document.parent/clean).resolve()
def broken_relative_paths(root:Path, documents:Iterable[Path]|None=None)->list[str]:
    errors=[]
    for doc in documents or root.rglob('*.md'):
        if '.git' in doc.parts: continue
        text=doc.read_text(encoding='utf-8')
        for link in MARKDOWN_LINK_RE.findall(text)+CODE_PATH_RE.findall(text):
            target=resolve_doc_path(doc,link,root)
            if target is not None and not target.exists(): errors.append(f'{doc.relative_to(root)}: {link}')
    return errors
