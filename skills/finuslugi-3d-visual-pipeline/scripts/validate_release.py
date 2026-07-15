#!/usr/bin/env python3
"""Validate the Finuslugi 3D Visual Pipeline 0.2.0 release candidate."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

VERSION = "0.2.0"
TAG = f"v{VERSION}"
SHA_RE = re.compile(r"^[a-f0-9]{40}$")
SEMVER_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
FORBIDDEN_SUFFIXES = {".docx", ".pdf", ".env", ".pem", ".p12", ".pfx", ".key"}
IGNORED_PARTS = {".git", "__pycache__", ".pytest_cache"}


def parse_args() -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=default_root)
    parser.add_argument("--report", type=Path, default=None)
    return parser.parse_args()


def read_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"Missing file: {path}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON: {path}: {exc}")
    return None


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"Missing file: {path}")
    except UnicodeDecodeError as exc:
        errors.append(f"File is not UTF-8 text: {path}: {exc}")
    return ""


def git_head(root: Path) -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return "unknown"


def run_command(command: list[str], root: Path, errors: list[str], label: str) -> None:
    try:
        completed = subprocess.run(command, cwd=root, capture_output=True, text=True)
    except FileNotFoundError as exc:
        errors.append(f"{label} could not start: {exc}")
        return
    if completed.returncode != 0:
        output = "\n".join(part.strip() for part in (completed.stdout, completed.stderr) if part.strip())
        errors.append(f"{label} failed with exit code {completed.returncode}: {output}")


def validate_required_files(root: Path, errors: list[str]) -> None:
    required = [
        ".codex-plugin/plugin.json",
        "README.md",
        "CHANGELOG.md",
        "RELEASE_CHECKLIST.md",
        "release/0.2.0/RELEASE_NOTES.md",
        "release/0.2.0/validation-manifest.json",
        "skills/finuslugi-3d-visual-pipeline/SKILL.md",
        "skills/finuslugi-3d-visual-pipeline/references/installation.md",
        "skills/finuslugi-3d-visual-pipeline/references/versioning-and-release.md",
        "skills/finuslugi-3d-visual-pipeline/references/compatibility.md",
        "skills/finuslugi-3d-visual-pipeline/scripts/smoke_test_installation.py",
        "skills/finuslugi-3d-visual-pipeline/scripts/validate_release.py",
    ]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"Required release file is missing: {relative}")


def validate_plugin(root: Path, errors: list[str]) -> None:
    manifest = read_json(root / ".codex-plugin/plugin.json", errors)
    if not isinstance(manifest, dict):
        return
    if manifest.get("name") != "finuslugi-3d-visual-pipeline":
        errors.append("Plugin name is not canonical")
    version = manifest.get("version")
    if version != VERSION or not isinstance(version, str) or SEMVER_RE.fullmatch(version) is None:
        errors.append(f"Plugin version must be {VERSION}")
    if manifest.get("skills") != "./skills/":
        errors.append("Plugin skills path must be ./skills/")
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        errors.append("Plugin interface metadata is missing")
        return
    if interface.get("brandColor") != "#FF0508":
        errors.append("Plugin brand color must be #FF0508")
    for key in ("composerIcon", "logo"):
        value = interface.get(key)
        if not isinstance(value, str) or not value.startswith("./"):
            errors.append(f"Plugin interface {key} must be a ./ relative path")
        elif not (root / value[2:]).is_file():
            errors.append(f"Plugin interface asset does not exist: {value}")


def validate_version_alignment(root: Path, errors: list[str]) -> None:
    changelog = read_text(root / "CHANGELOG.md", errors)
    if f"## {VERSION} - 2026-07-15" not in changelog:
        errors.append(f"CHANGELOG.md lacks the {VERSION} release heading")
    release_notes = read_text(root / f"release/{VERSION}/RELEASE_NOTES.md", errors)
    if VERSION not in release_notes or TAG not in release_notes:
        errors.append("Release notes must mention the version and intended tag")
    policy = read_text(
        root / "skills/finuslugi-3d-visual-pipeline/references/versioning-and-release.md",
        errors,
    )
    for marker in (VERSION, TAG, "semantic versioning", "Rollback", "Deprecation"):
        if marker.lower() not in policy.lower():
            errors.append(f"Versioning and release policy lacks marker: {marker}")


def validate_release_manifest(root: Path, errors: list[str]) -> None:
    manifest = read_json(root / f"release/{VERSION}/validation-manifest.json", errors)
    if not isinstance(manifest, dict):
        return
    if manifest.get("manifest_version") != "1.0":
        errors.append("Release validation manifest version must be 1.0")
    if manifest.get("release_version") != VERSION:
        errors.append("Release validation manifest release_version mismatch")
    if manifest.get("intended_tag") != TAG:
        errors.append("Release validation manifest intended_tag mismatch")
    base_sha = manifest.get("release_base_sha")
    if not isinstance(base_sha, str) or SHA_RE.fullmatch(base_sha) is None:
        errors.append("Release validation manifest requires a full release_base_sha")
    upstream = manifest.get("upstream_merge_commits")
    if not isinstance(upstream, dict):
        errors.append("Release validation manifest requires upstream_merge_commits")
    else:
        required_issues = {"F3D-001-002-003", "F3D-005", "F3D-006", "F3D-007", "F3D-004"}
        if set(upstream) != required_issues:
            errors.append("Release validation manifest upstream merge set is incomplete")
        for key, value in upstream.items():
            if not isinstance(value, str) or SHA_RE.fullmatch(value) is None:
                errors.append(f"Invalid upstream merge SHA for {key}")
    validators = manifest.get("validators")
    required_validators = {
        "repository",
        "runtime",
        "assets",
        "visual-regression",
        "installation-smoke",
        "release",
    }
    if not isinstance(validators, dict) or set(validators) != required_validators:
        errors.append("Release validation manifest validator set is incomplete")
    elif any(value not in {"pass", "self"} for value in validators.values()):
        errors.append("Release validation manifest contains a non-passing validator state")
    publication = manifest.get("publication")
    if not isinstance(publication, dict):
        errors.append("Release validation manifest publication state is missing")
    else:
        if publication.get("source_release_state") != "ready-for-merge":
            errors.append("Source release state must be ready-for-merge")
        if publication.get("tag_state") != "pending" or publication.get("github_release_state") != "pending":
            errors.append("Tag and GitHub Release must remain pending before release PR merge")


def validate_readme(root: Path, errors: list[str]) -> None:
    readme = read_text(root / "README.md", errors)
    markers = [
        VERSION,
        "installation.md",
        "smoke_test_installation.py",
        "validate_release.py",
        "runtime-capabilities",
        "asset-governance",
        "visual regression",
    ]
    for marker in markers:
        if marker.lower() not in readme.lower():
            errors.append(f"README.md lacks release marker: {marker}")


def validate_checklist(root: Path, errors: list[str]) -> None:
    checklist = read_text(root / "RELEASE_CHECKLIST.md", errors)
    required_checked = [
        "F3D#1 architecture merged",
        "F3D#2 canonical skill merged",
        "F3D#3 style packs and source traceability merged",
        "F3D#5 deterministic repository validation merged",
        "F3D#6 runtime capability contract merged",
        "F3D#7 governed asset registry and rights states merged",
        "F3D#4 golden set and visual regression merged",
        "Plugin manifest version is `0.2.0`",
        "Installation smoke test passes",
        "Release validator passes",
    ]
    for item in required_checked:
        if f"- [x] {item}" not in checklist:
            errors.append(f"Release checklist item is not checked: {item}")
    for pending in (
        "Annotated tag `v0.2.0` created",
        "GitHub Release `v0.2.0` published",
        "Installation smoke test repeated from immutable tag",
    ):
        if f"- [ ] {pending}" not in checklist:
            errors.append(f"Pre-merge publication item must remain pending: {pending}")


def validate_public_repository(root: Path, errors: list[str]) -> None:
    forbidden_files: list[str] = []
    suspicious_files: list[str] = []
    private_key_marker = "-----BEGIN " + "PRIVATE KEY-----"
    prefixed_private_key_markers = [
        "-----BEGIN " + prefix + " PRIVATE KEY-----"
        for prefix in ("RSA", "OPENSSH", "EC", "DSA")
    ]
    secret_patterns = [
        re.compile(r"ghp_[A-Za-z0-9]{36}"),
        re.compile(r"github_pat_[A-Za-z0-9_]{40,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"sk-[A-Za-z0-9]{24,}"),
    ]
    validator_path = Path("skills/finuslugi-3d-visual-pipeline/scripts/validate_release.py")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES or path.name.startswith(".env"):
            forbidden_files.append(relative.as_posix())
        if relative == validator_path or path.stat().st_size > 2_000_000:
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if private_key_marker in text or any(marker in text for marker in prefixed_private_key_markers):
            suspicious_files.append(relative.as_posix())
            continue
        if any(pattern.search(text) for pattern in secret_patterns):
            suspicious_files.append(relative.as_posix())

    if forbidden_files:
        errors.append(f"Forbidden public repository files: {', '.join(sorted(forbidden_files))}")
    if suspicious_files:
        errors.append(f"Potential secrets found in: {', '.join(sorted(set(suspicious_files)))}")


def main() -> int:
    args = parse_args()
    root = args.repo_root.resolve()
    errors: list[str] = []
    checks: list[str] = []

    validate_required_files(root, errors)
    checks.append("release-required-files")
    validate_plugin(root, errors)
    checks.append("release-plugin-manifest")
    validate_version_alignment(root, errors)
    checks.append("release-version-alignment")
    validate_release_manifest(root, errors)
    checks.append("release-validation-manifest")
    validate_readme(root, errors)
    checks.append("release-readme")
    validate_checklist(root, errors)
    checks.append("release-checklist")
    validate_public_repository(root, errors)
    checks.append("release-public-repository-scan")

    run_command(
        [sys.executable, "skills/finuslugi-3d-visual-pipeline/scripts/smoke_test_installation.py"],
        root,
        errors,
        "Installation smoke test",
    )
    checks.append("release-installation-smoke")

    commit = git_head(root)
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    report = args.report or root / "validation/runtime/release-report.json"
    if not report.is_absolute():
        report = root / report
    report.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "report_version": "1.0",
        "run_id": f"{now.strftime('%Y%m%dT%H%M%SZ')}-{commit[:8] if commit != 'unknown' else 'nogit'}-release",
        "timestamp": now.isoformat().replace("+00:00", "Z"),
        "head_sha": commit,
        "release_version": VERSION,
        "status": "pass" if not errors else "fail",
        "passed_checks": checks,
        "errors": errors,
    }
    report.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"[{'PASS' if not errors else 'FAIL'}] Release validation {VERSION}")
    print(f"HEAD: {commit}")
    print(f"Checks: {len(checks)}")
    print(f"Errors: {len(errors)}")
    print(f"Report: {report}")
    for error in errors:
        print(f"ERROR: {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
