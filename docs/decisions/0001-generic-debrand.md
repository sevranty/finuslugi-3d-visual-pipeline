# ADR 0001 — Generic public identity

## Decision

The active repository tree uses a generic plugin and skill identity, neutral repository-authored visual assets, configurable accents, and a dedicated validator that rejects legacy organization-specific identifiers from the distribution surface.

## Constraints

Published historical tags remain immutable. The validator scans the active tracked tree and deliberately excludes the Git object database.
