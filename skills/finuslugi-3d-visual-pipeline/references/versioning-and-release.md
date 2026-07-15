# Versioning and Release

The plugin uses semantic versioning.

## Version classes

- **Patch** `x.y.Z`: documentation corrections, validator fixes, or fixture repairs that do not change the public workflow contract.
- **Minor** `x.Y.0`: backward-compatible capabilities, style packs, schemas, runtime routes, governed collections, or eval coverage.
- **Major** `X.0.0`: incompatible Scene Specification, manifest, skill invocation, packaging, or lifecycle changes.

Style packs retain independent `major.minor` versions. Asset entries use full semantic versions. Machine manifests and schemas declare their own versions.

## Version alignment

Before release, the following must agree:

- `.codex-plugin/plugin.json` version;
- `CHANGELOG.md` release heading;
- `release/<version>/validation-manifest.json`;
- release notes;
- intended Git tag `v<version>`.

## Release process

1. Start a release branch from an immutable validated `main` commit.
2. Update plugin metadata and changelog.
3. Add installation, compatibility, release notes, and validation manifest.
4. Run smoke, repository, runtime, asset, visual, and release validators.
5. Review the exact release-candidate HEAD.
6. Merge the release PR by the approved method.
7. Create annotated tag `v<version>` on the merge commit.
8. Publish GitHub Release from that tag with the checked-in release notes.
9. Verify repository installation from the immutable tag.

A GitHub Release must not point to a branch head or a pre-merge synthetic commit.

## Compatibility policy

Release `0.2.0` supports:

- skill-only Codex plugin packaging;
- repository-scoped Agent Skills discovery through `.agents/skills` fallback;
- Python 3.10 or newer for validators;
- image runtimes matching the capability contract;
- ChatGPT image-generation and Nano Banana-style profiles as contract examples.

Tool capability states remain runtime observations and are not guaranteed by this plugin version.

## Deprecation

- Mark a public contract deprecated in documentation and changelog before removal.
- Keep deprecated asset entries and manifest history until no active release references them.
- Minor releases may add warnings but cannot remove backward-compatible fields.
- Breaking removals require a major version.

## Rollback

Rollback means reinstalling the last accepted immutable tag. Do not force-move a published release tag. A faulty tag is deprecated in release notes and replaced by a new patch version.

## Release limitations

The repository can prepare and merge an exact release candidate independently of the GitHub API used to publish tags and Release objects. When the connected tool cannot create them, record the limitation and retain the release issue until the external publication step is completed.
