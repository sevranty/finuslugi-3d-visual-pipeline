# Repository Instructions

## Scope

This repository contains one skill-only Codex plugin for Finuslugi 3D visual production.

## Source of truth

- Runtime order and non-negotiable behavior: `skills/finuslugi-3d-visual-pipeline/SKILL.md`.
- Detailed rules: files in `skills/finuslugi-3d-visual-pipeline/references/`.
- Machine-readable contracts: files in `skills/finuslugi-3d-visual-pipeline/assets/schemas/`.
- Regression cases: files in `skills/finuslugi-3d-visual-pipeline/evals/`.

Do not duplicate detailed rules in multiple files. Keep `SKILL.md` concise and link to the canonical reference.

## File rules

- Use ASCII-only paths and filenames.
- Store text as UTF-8.
- Do not commit temporary generations, caches, or credentials.
- Keep style versions explicit in headings and source maps.
- Record system-level behavior changes in `CHANGELOG.md`.

## Brand rules

- Use `assets/finuslugi-base.png` on white or light backgrounds.
- Use `assets/finuslugi-inverted.png` on red or dark backgrounds.
- Use `#FF0508` as the Finuslugi and MOEX brand red.
- Do not redraw or regenerate the logo inside an AI image.

## Development workflow

1. Work in a dedicated branch.
2. Update the relevant canonical file only.
3. Add or update an eval case for behavior changes.
4. Run:

```bash
python3 skills/finuslugi-3d-visual-pipeline/scripts/validate_repository.py
```

5. Open a Draft PR. Do not merge without a separate lifecycle decision.
