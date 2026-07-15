#!/usr/bin/env python3
"""Validate the Finuslugi 3D visual pipeline repository using Python stdlib only."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


SEMVER_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
STYLE_VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+$")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_PATH_RE = re.compile(
    r"`((?:\.\./|\./|references/|assets/|evals/|scripts/)[A-Za-z0-9_./-]+(?:\.[A-Za-z0-9]+)?)`"
)


@dataclass
class ValidationResult:
    checks: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def check(self, name: str) -> None:
        self.checks.append(name)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


def parse_args() -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=default_root,
        help="Repository root. Defaults to the root inferred from this script.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Explicit report path. Defaults to validation/<run-id>/report.json.",
    )
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Do not write a JSON report.",
    )
    return parser.parse_args()


def read_text(path: Path, result: ValidationResult) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        result.error(f"Missing file: {path}")
    except UnicodeDecodeError as exc:
        result.error(f"File is not valid UTF-8: {path}: {exc}")
    return None


def read_json(path: Path, result: ValidationResult) -> Any | None:
    text = read_text(path, result)
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        result.error(f"Invalid JSON: {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}")
        return None


def get_git_head(repo_root: Path) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return os.environ.get("GITHUB_SHA", "unknown")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_ascii(value: str) -> bool:
    try:
        value.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


def validate_required_paths(repo_root: Path, result: ValidationResult) -> None:
    required = [
        ".codex-plugin/plugin.json",
        "README.md",
        "AGENTS.md",
        "CHANGELOG.md",
        "LICENSE",
        "assets/finuslugi-base.png",
        "assets/finuslugi-inverted.png",
        "assets/manifest.json",
        "assets/checksums.sha256",
        "skills/finuslugi-3d-visual-pipeline/SKILL.md",
        "skills/finuslugi-3d-visual-pipeline/agents/openai.yaml",
        "skills/finuslugi-3d-visual-pipeline/references/style-selection.md",
        "skills/finuslugi-3d-visual-pipeline/references/style-modern-flat.md",
        "skills/finuslugi-3d-visual-pipeline/references/style-silver-gold.md",
        "skills/finuslugi-3d-visual-pipeline/references/style-obsidian-gold.md",
        "skills/finuslugi-3d-visual-pipeline/references/diagnostic-codes.md",
        "skills/finuslugi-3d-visual-pipeline/assets/schemas/scene-spec.schema.json",
        "skills/finuslugi-3d-visual-pipeline/assets/schemas/output-manifest.schema.json",
        "skills/finuslugi-3d-visual-pipeline/evals/cases.json",
        "skills/finuslugi-3d-visual-pipeline/evals/expected-behavior.md",
        "skills/finuslugi-3d-visual-pipeline/scripts/validate_repository.py",
    ]
    for relative in required:
        if not (repo_root / relative).exists():
            result.error(f"Required path does not exist: {relative}")
    result.check("required-paths")


def validate_ascii_paths(repo_root: Path, result: ValidationResult) -> None:
    ignored_parts = {".git", "__pycache__"}
    for path in repo_root.rglob("*"):
        relative = path.relative_to(repo_root)
        if any(part in ignored_parts for part in relative.parts):
            continue
        if not is_ascii(relative.as_posix()):
            result.error(f"Non-ASCII repository path: {relative.as_posix()}")
    result.check("ascii-paths")


def validate_plugin_manifest(repo_root: Path, result: ValidationResult) -> None:
    path = repo_root / ".codex-plugin/plugin.json"
    data = read_json(path, result)
    if not isinstance(data, dict):
        return

    required = ["name", "version", "description", "author", "repository", "license", "skills", "interface"]
    for key in required:
        if key not in data:
            result.error(f"plugin.json missing key: {key}")

    if data.get("name") != "finuslugi-3d-visual-pipeline":
        result.error("plugin.json name must be finuslugi-3d-visual-pipeline")
    if not isinstance(data.get("version"), str) or not SEMVER_RE.fullmatch(data["version"]):
        result.error("plugin.json version must use semantic versioning x.y.z")
    if data.get("skills") != "./skills/":
        result.error("plugin.json skills must be ./skills/")

    interface = data.get("interface")
    if not isinstance(interface, dict):
        result.error("plugin.json interface must be an object")
    else:
        if interface.get("brandColor") != "#FF0508":
            result.error("plugin.json interface.brandColor must be #FF0508")
        for key in ["displayName", "shortDescription", "longDescription", "developerName"]:
            if not isinstance(interface.get(key), str) or not interface[key].strip():
                result.error(f"plugin.json interface.{key} must be a non-empty string")
        for asset_key in ["composerIcon", "logo"]:
            value = interface.get(asset_key)
            if not isinstance(value, str) or not value.startswith("./"):
                result.error(f"plugin.json interface.{asset_key} must be a ./ relative path")
            elif not (repo_root / value[2:]).exists():
                result.error(f"plugin.json interface.{asset_key} target does not exist: {value}")

    changelog = read_text(repo_root / "CHANGELOG.md", result)
    if changelog is not None and isinstance(data.get("version"), str):
        if data["version"] not in changelog:
            result.error(f"CHANGELOG.md does not mention plugin version {data['version']}")

    result.check("plugin-manifest")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if len(lines) < 4 or lines[0].strip() != "---":
        return None
    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return metadata
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return None


def validate_skill_frontmatter(repo_root: Path, result: ValidationResult) -> None:
    path = repo_root / "skills/finuslugi-3d-visual-pipeline/SKILL.md"
    text = read_text(path, result)
    if text is None:
        return
    metadata = parse_frontmatter(text)
    if metadata is None:
        result.error("SKILL.md must begin with closed YAML frontmatter")
        return
    if metadata.get("name") != "finuslugi-3d-visual-pipeline":
        result.error("SKILL.md frontmatter name is incorrect")
    description = metadata.get("description", "")
    if len(description) < 40:
        result.error("SKILL.md frontmatter description is too short")
    if "reference" not in description.lower() or "image" not in description.lower():
        result.error("SKILL.md description must describe reference-to-image use")
    result.check("skill-frontmatter")


def extract_style_metadata(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for key in ["style_id", "version", "status", "source_status"]:
        match = re.search(rf"^\s*{re.escape(key)}:\s*[\"']?([^\n\"']+)[\"']?\s*$", text, re.MULTILINE)
        if match:
            values[key] = match.group(1).strip()
    return values


def validate_style_packs(repo_root: Path, result: ValidationResult) -> None:
    base = repo_root / "skills/finuslugi-3d-visual-pipeline/references"
    expected = {
        "style-modern-flat.md": ("modern-flat", "2.1"),
        "style-silver-gold.md": ("silver-gold", "3.1"),
        "style-obsidian-gold.md": ("obsidian-gold", "1.0"),
    }
    for filename, (style_id, version) in expected.items():
        text = read_text(base / filename, result)
        if text is None:
            continue
        metadata = extract_style_metadata(text)
        if metadata.get("style_id") != style_id:
            result.error(f"{filename}: expected style_id {style_id}, found {metadata.get('style_id')!r}")
        if metadata.get("version") != version:
            result.error(f"{filename}: expected version {version}, found {metadata.get('version')!r}")
        if not STYLE_VERSION_RE.fullmatch(metadata.get("version", "")):
            result.error(f"{filename}: version must use x.y format")
        if not metadata.get("status"):
            result.error(f"{filename}: status is required")

    obsidian = read_text(base / "style-obsidian-gold.md", result)
    if obsidian is not None:
        for marker in ["#000000", "15-25%", "The background is black.", "obsidian stone", "no HDR"]:
            if marker not in obsidian:
                result.error(f"style-obsidian-gold.md missing canonical marker: {marker}")

    silver = read_text(base / "style-silver-gold.md", result)
    if silver is not None:
        for marker in ["70-85%", "15-30%", "matte or satin", "chrome"]:
            if marker not in silver:
                result.error(f"style-silver-gold.md missing canonical marker: {marker}")

    modern = read_text(base / "style-modern-flat.md", result)
    if modern is not None:
        for marker in ["#FF0508", "10%", "15% vertical", "10% horizontal", "photorealism"]:
            if marker not in modern:
                result.error(f"style-modern-flat.md missing canonical marker: {marker}")

    result.check("style-packs")


def resolve_doc_path(document: Path, link: str, repo_root: Path) -> Path | None:
    clean = link.split("#", 1)[0].strip()
    if not clean or clean.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if clean.startswith("/"):
        return repo_root / clean.lstrip("/")
    return (document.parent / clean).resolve()


def validate_relative_links(repo_root: Path, result: ValidationResult) -> None:
    for document in repo_root.rglob("*.md"):
        if ".git" in document.parts:
            continue
        text = read_text(document, result)
        if text is None:
            continue
        links = list(MARKDOWN_LINK_RE.findall(text)) + list(CODE_PATH_RE.findall(text))
        for link in links:
            target = resolve_doc_path(document, link, repo_root)
            if target is None:
                continue
            if not target.exists():
                relative_document = document.relative_to(repo_root)
                result.error(f"Broken relative path in {relative_document}: {link}")
    result.check("relative-links")


def validate_asset_manifest(repo_root: Path, result: ValidationResult) -> None:
    manifest_path = repo_root / "assets/manifest.json"
    data = read_json(manifest_path, result)
    if not isinstance(data, dict):
        return
    assets = data.get("assets")
    if not isinstance(assets, list) or not assets:
        result.error("assets/manifest.json must contain a non-empty assets array")
        return

    ids: set[str] = set()
    checksum_lines: dict[str, str] = {}
    checksum_text = read_text(repo_root / "assets/checksums.sha256", result)
    if checksum_text is not None:
        for line in checksum_text.splitlines():
            if not line.strip():
                continue
            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                result.error(f"Invalid checksum line: {line}")
                continue
            checksum_lines[parts[1].strip()] = parts[0].strip()

    for entry in assets:
        if not isinstance(entry, dict):
            result.error("Asset manifest entries must be objects")
            continue
        asset_id = entry.get("asset_id")
        path_value = entry.get("path")
        checksum = entry.get("sha256")
        if not isinstance(asset_id, str) or not asset_id:
            result.error("Asset entry missing asset_id")
            continue
        if asset_id in ids:
            result.error(f"Duplicate asset_id: {asset_id}")
        ids.add(asset_id)
        if not isinstance(path_value, str) or not path_value:
            result.error(f"Asset {asset_id} missing path")
            continue
        asset_path = repo_root / path_value
        if not asset_path.exists():
            result.error(f"Asset {asset_id} file does not exist: {path_value}")
            continue
        if not isinstance(checksum, str) or not SHA256_RE.fullmatch(checksum):
            result.error(f"Asset {asset_id} has invalid sha256")
            continue
        actual = sha256_file(asset_path)
        if actual != checksum:
            result.error(f"Asset {asset_id} checksum mismatch: expected {checksum}, got {actual}")
        if checksum_lines.get(path_value) != checksum:
            result.error(f"assets/checksums.sha256 is missing or inconsistent for {path_value}")
        for key in ["allowed_roles", "approval_status", "public_distribution_status", "owner", "source_note"]:
            if key not in entry:
                result.error(f"Asset {asset_id} missing governance field: {key}")

    result.check("asset-manifest")


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return True


def validate_schema_instance(instance: Any, schema: dict[str, Any], location: str = "$") -> list[str]:
    errors: list[str] = []

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{location}: expected constant {schema['const']!r}, got {instance!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{location}: value {instance!r} is not in enum {schema['enum']!r}")

    expected_type = schema.get("type")
    if isinstance(expected_type, str) and not type_matches(instance, expected_type):
        errors.append(f"{location}: expected type {expected_type}, got {type(instance).__name__}")
        return errors

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{location}: missing required property {key!r}")
        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                errors.extend(validate_schema_instance(value, properties[key], f"{location}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{location}: additional property is not allowed: {key!r}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{location}: expected at least {schema['minItems']} items")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{location}: expected at most {schema['maxItems']} items")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in instance]
            if len(serialized) != len(set(serialized)):
                errors.append(f"{location}: items must be unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(instance):
                errors.extend(validate_schema_instance(item, item_schema, f"{location}[{index}]"))

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{location}: string is shorter than {schema['minLength']}")
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.fullmatch(pattern, instance) is None:
            errors.append(f"{location}: value {instance!r} does not match pattern {pattern!r}")
        if schema.get("format") == "date-time":
            try:
                dt.datetime.fromisoformat(instance.replace("Z", "+00:00"))
            except ValueError:
                errors.append(f"{location}: value {instance!r} is not an ISO date-time")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{location}: value {instance} is below minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{location}: value {instance} is above maximum {schema['maximum']}")

    return errors


def validate_schemas_and_fixtures(repo_root: Path, result: ValidationResult) -> None:
    base = repo_root / "skills/finuslugi-3d-visual-pipeline"
    pairs = [
        (
            base / "assets/schemas/scene-spec.schema.json",
            base / "evals/fixtures/valid/scene-spec.json",
            [base / "evals/fixtures/invalid/scene-spec-style-version-missing.json"],
        ),
        (
            base / "assets/schemas/output-manifest.schema.json",
            base / "evals/fixtures/valid/output-manifest.json",
            [base / "evals/fixtures/invalid/output-manifest-delivery-missing.json"],
        ),
    ]

    for schema_path, valid_path, invalid_paths in pairs:
        schema = read_json(schema_path, result)
        valid_instance = read_json(valid_path, result)
        if not isinstance(schema, dict) or valid_instance is None:
            continue
        errors = validate_schema_instance(valid_instance, schema)
        if errors:
            result.error(f"Valid fixture failed {schema_path.name}: {'; '.join(errors)}")
        for invalid_path in invalid_paths:
            invalid_instance = read_json(invalid_path, result)
            if invalid_instance is None:
                continue
            invalid_errors = validate_schema_instance(invalid_instance, schema)
            if not invalid_errors:
                result.error(f"Invalid fixture unexpectedly passed {schema_path.name}: {invalid_path.name}")

    result.check("schemas-and-fixtures")


def validate_eval_cases(repo_root: Path, result: ValidationResult) -> None:
    path = repo_root / "skills/finuslugi-3d-visual-pipeline/evals/cases.json"
    data = read_json(path, result)
    if not isinstance(data, dict):
        return
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        result.error("evals/cases.json must contain a non-empty cases array")
        return

    ids: set[str] = set()
    positive_styles: set[str] = set()
    negative_names: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            result.error("Each eval case must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not re.fullmatch(r"EV-[0-9]{3}", case_id):
            result.error(f"Invalid eval case ID: {case_id!r}")
            continue
        if case_id in ids:
            result.error(f"Duplicate eval case ID: {case_id}")
        ids.add(case_id)
        if case.get("kind") not in {"positive", "negative"}:
            result.error(f"{case_id}: kind must be positive or negative")
        expected = case.get("expected")
        if not isinstance(expected, list) or not expected or not all(isinstance(item, str) and item for item in expected):
            result.error(f"{case_id}: expected must be a non-empty string array")
        if case.get("kind") == "positive" and isinstance(case.get("style"), str):
            positive_styles.add(case["style"])
        if case.get("kind") == "negative" and isinstance(case.get("name"), str):
            negative_names.add(case["name"])

    for required_style in {"modern-flat@2.1", "silver-gold@3.1", "obsidian-gold@1.0"}:
        if required_style not in positive_styles:
            result.error(f"Missing positive eval case for {required_style}")
    if "Delivery regression" not in negative_names:
        result.error("Missing delivery regression negative eval")
    if "Generated logo rejection" not in negative_names:
        result.error("Missing generated-logo negative eval")

    result.check("eval-cases")


def write_report(
    repo_root: Path,
    explicit_path: Path | None,
    result: ValidationResult,
    head_sha: str,
    command: list[str],
) -> Path:
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    run_id = f"{now.strftime('%Y%m%dT%H%M%SZ')}-{head_sha[:8] if head_sha != 'unknown' else 'nogit'}"
    report_path = explicit_path or repo_root / "validation" / run_id / "report.json"
    if not report_path.is_absolute():
        report_path = repo_root / report_path
    report_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "report_version": "1.0",
        "run_id": run_id,
        "timestamp": now.isoformat().replace("+00:00", "Z"),
        "head_sha": head_sha,
        "command": command,
        "status": "pass" if result.ok else "fail",
        "passed_checks": result.checks,
        "warnings": result.warnings,
        "errors": result.errors,
    }
    report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report_path


def validate(repo_root: Path) -> ValidationResult:
    result = ValidationResult()
    validate_required_paths(repo_root, result)
    validate_ascii_paths(repo_root, result)
    validate_plugin_manifest(repo_root, result)
    validate_skill_frontmatter(repo_root, result)
    validate_style_packs(repo_root, result)
    validate_relative_links(repo_root, result)
    validate_asset_manifest(repo_root, result)
    validate_schemas_and_fixtures(repo_root, result)
    validate_eval_cases(repo_root, result)
    return result


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    result = validate(repo_root)
    head_sha = get_git_head(repo_root)

    report_path: Path | None = None
    if not args.no_report:
        report_path = write_report(repo_root, args.report, result, head_sha, sys.argv)

    status = "PASS" if result.ok else "FAIL"
    print(f"[{status}] Finuslugi 3D visual pipeline repository validation")
    print(f"Repository: {repo_root}")
    print(f"HEAD: {head_sha}")
    print(f"Checks: {len(result.checks)}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Errors: {len(result.errors)}")
    if report_path is not None:
        print(f"Report: {report_path}")
    for warning in result.warnings:
        print(f"WARNING: {warning}")
    for error in result.errors:
        print(f"ERROR: {error}")

    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
