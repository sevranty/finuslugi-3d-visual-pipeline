# Asset governance

The registry is the only authority for production, regression, documentation, and public-distribution eligibility. A new asset requires stable ID, version, exact path, source, rights, approval, roles, public-distribution state, and SHA-256 in both `../../../assets/manifest.json` and `../../../assets/checksums.sha256`. Registry history is append-only. Validator: `../scripts/validate_asset_registry.py`.
