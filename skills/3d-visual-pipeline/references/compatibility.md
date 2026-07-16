# Compatibility

Version `1.0.0` supports skill-only plugin packaging, repository-scoped skill discovery, Python 3.10 or newer, and image runtimes matching the declared capability contract.

Runtime capabilities are observed, not assumed. The pipeline must stop or disclose a fallback when the requested generation or editing capability is unavailable.

Exact identity preservation is not guaranteed by a generative runtime. Requests requiring exact likeness need sufficient source evidence and an explicit supported edit route.
