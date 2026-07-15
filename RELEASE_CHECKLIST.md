# Release Checklist — 0.2.0

## Architecture and behavior

- [x] F3D#1 architecture merged.
- [x] F3D#2 canonical skill merged.
- [x] F3D#3 style packs and source traceability merged.
- [x] F3D#5 deterministic repository validation merged.
- [x] F3D#6 runtime capability contract merged.
- [x] F3D#7 governed asset registry and rights states merged.
- [x] F3D#4 golden set and visual regression merged.

## Packaging

- [x] Plugin manifest version is `0.2.0`.
- [x] Plugin manifest resolves `./skills/`.
- [x] Canonical `SKILL.md` is discoverable.
- [x] Brand assets referenced by plugin metadata exist and match checksums.
- [x] Installation documentation covers plugin and repository-scoped skill modes.
- [x] Compatibility, rollback, and deprecation policies are documented.

## Validation

- [x] Repository validator passes.
- [x] Runtime contract validator passes.
- [x] Asset registry validator passes.
- [x] Visual regression validator passes.
- [x] Installation smoke test passes.
- [x] Release validator passes.
- [x] Negative fixtures are rejected.
- [x] Exact release-candidate HEAD is reviewed.

## Public repository

- [x] No internal FDS source DOCX/PDF files are committed.
- [x] No secrets or private keys are committed.
- [x] No personal-data dataset is included.
- [x] Public visual fixtures are repository-authored or owner-supplied and rights-cleared for this repository.
- [x] Trademark limitations are explicit.

## Publication

- [x] Release PR merged to `main`.
- [ ] Annotated tag `v0.2.0` created on the release merge commit.
- [ ] GitHub Release `v0.2.0` published from checked-in release notes.
- [ ] Installation smoke test repeated from immutable tag.

The final three publication items require a GitHub API surface that can create tags and Release objects. They are not represented as completed until that operation is actually available and executed.
