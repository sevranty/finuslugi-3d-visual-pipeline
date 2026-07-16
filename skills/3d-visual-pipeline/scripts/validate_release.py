#!/usr/bin/env python3
from __future__ import annotations

import re
from typing import Any

from validation_lib import Result, parse_args, read_json, repo_root, write_report

VERSION = "1.0.0"
TAG = "v1.0.0"
LEGACY_TAG = "v0.2.0"
LEGACY_TARGET = "3d2cdea9f651f7641ec1f805519a777f013dd6ec"
ALLOWED_STATES = {"candidate", "tagged-validated", "published"}
HEX_SHA = re.compile(r"^[0-9a-f]{40}$")


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    state = manifest.get("status")

    if manifest.get("version") != VERSION or manifest.get("intended_tag") != TAG:
        errors.append("release manifest not aligned")
    if state not in ALLOWED_STATES:
        errors.append("release status invalid")

    hosted = manifest.get("hosted_ci", {})
    hosted_status = hosted.get("status")
    if hosted_status not in {"not_run", "passed", "failed"}:
        errors.append("hosted CI status invalid")
    if hosted_status == "passed":
        if not hosted.get("run_url") or not HEX_SHA.fullmatch(str(hosted.get("commit_sha", ""))):
            errors.append("hosted CI pass lacks run URL or exact commit")

    tag_target = manifest.get("tag_target")
    release_url = manifest.get("release_url")
    tagged = manifest.get("tagged_validation")

    if state == "candidate":
        if tag_target is not None or release_url is not None or tagged is not None:
            errors.append("candidate contains publication evidence")

    if state in {"tagged-validated", "published"}:
        if not HEX_SHA.fullmatch(str(tag_target or "")):
            errors.append("tag target missing or invalid")
        if not isinstance(tagged, dict) or tagged.get("status") != "pass":
            errors.append("tagged validation is not pass")
        elif tagged.get("checkout_sha") != tag_target:
            errors.append("tagged validation is not bound to tag target")

    if state == "tagged-validated" and release_url is not None:
        errors.append("tagged-validated state contains release URL")
    if state == "published":
        expected_suffix = f"/releases/tag/{TAG}"
        if not isinstance(release_url, str) or not release_url.endswith(expected_suffix):
            errors.append("published state lacks canonical release URL")

    legacy = manifest.get("legacy_release", {})
    if legacy.get("tag") != LEGACY_TAG or legacy.get("target") != LEGACY_TARGET:
        errors.append("legacy release boundary changed")
    if legacy.get("immutable") is not True:
        errors.append("legacy release must remain immutable")

    return errors


def main() -> int:
    args = parse_args(__doc__ or "release validator")
    root = repo_root()
    result = Result("release")

    plugin = read_json(root / ".codex-plugin/plugin.json")
    manifest = read_json(root / f"release/{VERSION}/validation-manifest.json")

    if plugin.get("version") != VERSION:
        result.error("plugin version not aligned")
    for error in validate_manifest(manifest):
        result.error(error)

    for path in [
        f"release/{VERSION}/RELEASE_NOTES.md",
        "CHANGELOG.md",
        "README.md",
        "RELEASE_CHECKLIST.md",
    ]:
        text = (root / path).read_text(encoding="utf-8")
        if VERSION not in text:
            result.error(f"version absent from {path}")

    result.check("version-and-publication-contract")
    return write_report(root, args, result)


if __name__ == "__main__":
    raise SystemExit(main())
