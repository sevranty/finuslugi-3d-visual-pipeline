# Installation

## Repository checkout

Run from the repository root:

```bash
mkdir -p .agents/skills
cp -R skills/3d-visual-pipeline .agents/skills/3d-visual-pipeline
python3 skills/3d-visual-pipeline/scripts/smoke_test_installation.py
```

## Immutable release

After publication, use the exact release tag rather than a branch name:

```bash
git checkout --detach v1.0.0
python3 skills/3d-visual-pipeline/scripts/validate_all.py --report-dir validation/runtime
mkdir -p .agents/skills
cp -R skills/3d-visual-pipeline .agents/skills/3d-visual-pipeline
python3 skills/3d-visual-pipeline/scripts/smoke_test_installation.py
```

A release is not fully validated until the complete command succeeds from a clean checkout of the immutable tag.
