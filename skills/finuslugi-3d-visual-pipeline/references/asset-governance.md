# Asset Governance

The asset registry is the only authority for deciding whether a binary or visual reference may be used in production, regression, documentation, or public distribution.

## Collections

- `brand-assets`: canonical supplied logos and interface assets.
- `anchors-modern-flat`: approved Modern Flat regression anchors.
- `anchors-silver-gold`: approved Silver-Gold regression anchors.
- `anchors-obsidian-gold`: approved Obsidian Gold regression anchors.
- `anti-patterns`: deliberately rejected fixtures linked to diagnostic codes.
- `exploratory`: quarantined research references that are never canonical style sources.

A directory name does not grant approval. Every usable file requires an active manifest entry.

## Admission contract

A new asset is admitted only when the same PR provides:

1. stable `asset_id` and semantic version;
2. exact repository path;
3. collection membership and asset type;
4. source, owner, and license scope;
5. approval, rights, lifecycle, and public-distribution states;
6. allowed and prohibited roles;
7. SHA-256 in both `assets/manifest.json` and `assets/checksums.sha256`;
8. review decision and manifest-history event.

Unregistered binary files are rejected.

## Rights and approval gates

Production use requires:

- `lifecycle_status=active`;
- `approval_status=approved`;
- `rights_status=cleared`;
- a role listed in `allowed_roles`;
- no matching role in `prohibited_roles`.

Public golden-set use additionally requires `public_distribution_status=approved`.

`pending`, `blocked`, `candidate`, `rejected`, `internal-only`, and `quarantine` are stop states for public golden admission.

## Logo rules

- White or light background: `finuslugi-logo-base`.
- Red or dark background: `finuslugi-logo-inverted`.
- Add logos after the generative pass.
- Do not generate, redraw, recolor, distort, crop, or use a logo as a style reference.
- An AI-generated logo is a critical `LOGO_ERROR` and cannot be repaired by scoring.

## Anchor rules

An anchor represents one versioned style pack and one declared regression purpose. It must not contain unlicensed third-party content, exact personal identity without permission, generated pseudo-logos, or unreviewed text.

Approved anchors and exploratory references are stored in different collections. Moving a file between collections requires a new review event; renaming the folder is insufficient.

## Anti-pattern rules

Every anti-pattern entry records:

- one primary diagnostic code;
- visible defect description;
- style pack or general contract affected;
- rejection reason;
- rights state;
- the positive rule it proves.

Anti-patterns are never production eligible.

## Replacement and deprecation

1. Add the replacement as a new asset version and checksum.
2. Set `supersedes` to the prior stable asset ID/version.
3. Mark the previous entry `deprecated` before removal.
4. Add a manifest-history event with old and new checksums.
5. Update affected eval cases and documentation.
6. Remove a file only in a later PR after no active contract references it.

History is append-only. Do not rewrite earlier events.

## Machine contracts

- Registry: `../../../assets/manifest.json`.
- Checksums: `../../../assets/checksums.sha256`.
- History: `../../../assets/manifest-history.json`.
- Schema: `../assets/schemas/asset-manifest.schema.json`.
- Validator: `../scripts/validate_asset_registry.py`.
