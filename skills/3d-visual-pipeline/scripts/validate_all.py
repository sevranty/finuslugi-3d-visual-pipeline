#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the complete 3DP validation set")
    parser.add_argument("--report-dir", default="validation/runtime")
    args = parser.parse_args()

    root = repo_root()
    report_dir = root / args.report_dir
    if report_dir.exists():
        shutil.rmtree(report_dir)
    report_dir.mkdir(parents=True)

    py = sys.executable
    scripts = root / "skills/3d-visual-pipeline/scripts"
    tests = root / "skills/3d-visual-pipeline/tests"
    commands = [
        ("repository", [py, str(scripts / "validate_repository.py"), "--report", str(report_dir / "repository.json")]),
        ("runtime-contract", [py, str(scripts / "validate_runtime_contract.py"), "--report", str(report_dir / "runtime.json")]),
        ("asset-registry", [py, str(scripts / "validate_asset_registry.py"), "--report", str(report_dir / "assets.json")]),
        ("visual-regression", [py, str(scripts / "validate_visual_regression.py"), "--report", str(report_dir / "visual.json")]),
        ("installation-smoke", [py, str(scripts / "smoke_test_installation.py")]),
        ("release", [py, str(scripts / "validate_release.py"), "--report", str(report_dir / "release.json")]),
        ("debrand", [py, str(scripts / "validate_debrand.py"), "--report", str(report_dir / "debrand.json")]),
        ("unittest", [py, "-m", "unittest", "discover", "-s", str(tests), "-p", "test_*.py"]),
    ]

    results = []
    failed = False
    for name, command in commands:
        completed = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
        results.append(
            {
                "name": name,
                "command": command,
                "exit_code": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "status": "pass" if completed.returncode == 0 else "fail",
            }
        )
        failed = failed or completed.returncode != 0
        print(f"{name}: {'PASS' if completed.returncode == 0 else 'FAIL'}")

    summary = {
        "project_id": "3D_VISUAL_PIPELINE",
        "short_id": "3DP",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "fail" if failed else "pass",
        "results": results,
    }
    (report_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
