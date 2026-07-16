# Release Checklist - 1.0.0

## Identity

- [x] Repository, plugin, skill and commands use `3d-visual-pipeline`
- [x] Skill path is `skills/3d-visual-pipeline`
- [x] Project SHORT_ID is `3DP`
- [x] Plugin version is `1.0.0`
- [x] Validation context is `3dp/validation`

## Governance

- [x] `TASK.md` defines the local execution contract
- [x] ADR 0002 defines the WebFactoryOS orchestration boundary
- [x] One repository-local execution Issue Form remains
- [x] No runtime, package, workflow or network dependency on WebFactoryOS exists

## Debrand

- [x] Active tracked tree contains no blocked organization identifiers, URLs, filenames, asset IDs or fixed palette marker
- [x] Generic repository-authored visual assets are registered and checksummed
- [x] Style contracts are organization-neutral
- [x] New active previous project IDs are rejected outside narrow historical evidence

## Validation

Run one local command matching CI:

```bash
python3 skills/3d-visual-pipeline/scripts/validate_all.py --report-dir validation/runtime
```

- [ ] Exact candidate HEAD validation passes
- [ ] Hosted GitHub Actions result is recorded as pass, fail or not run
- [ ] Full diff review has no P0-P2 findings
- [ ] Unresolved review threads are zero

## Publication

Current factual state: `candidate`

- [ ] Annotated tag `v1.0.0` created on the approved release commit
- [ ] Full validation repeated from a clean immutable-tag checkout
- [ ] Manifest moved to `tagged-validated` with exact tag target and checkout SHA
- [ ] Public GitHub Release published from checked-in notes
- [ ] Manifest moved to `published` with canonical Release URL
- [ ] Closure evidence merged

The historical `v0.2.0` tag and Release remain immutable.