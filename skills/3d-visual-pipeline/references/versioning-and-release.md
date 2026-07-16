# Versioning and release

The plugin follows semantic versioning. Release identity must agree across `.codex-plugin/plugin.json`, `CHANGELOG.md`, `../../../release/1.0.0/validation-manifest.json`, release notes and intended tag `v1.0.0`.

## States

- `candidate` - source is under review; tag, tagged validation and Release URL are absent
- `tagged-validated` - an annotated tag exists and clean checkout validation passes on its exact target
- `published` - tagged validation passed and the public GitHub Release URL is recorded

Hosted CI status is independent from lifecycle state. A passed claim requires an exact commit and run URL. When no run exists, record `not_run`.

Published tags are immutable. A faulty release is deprecated and replaced, never moved or recreated.
