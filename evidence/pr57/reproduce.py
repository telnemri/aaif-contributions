#!/usr/bin/env python3
"""Rerun the pinned kit and a synthetic contribution-discovery probe."""

import argparse
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile

PIN = "25a47f6f9deeed4a6f6d43b6d8393205d0bc494f"


def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    return {"command": command, "exit_code": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    checkout = args.checkout.resolve()
    # Keep the venv executable path. Resolving its symlink loses the venv.
    python = str(args.python.absolute())
    head = run(["git", "rev-parse", "HEAD"], checkout)
    if head["exit_code"] or head["stdout"].strip() != PIN:
        parser.error(f"checkout HEAD must equal {PIN}")
    before = run(["git", "status", "--porcelain", "--untracked-files=no"], checkout)
    if before["exit_code"] or before["stdout"]:
        parser.error("checkout must have no tracked changes")
    kit = checkout / "test-kit"
    manifest = {str(p.relative_to(checkout)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(kit.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}
    result = {"source_sha": PIN, "environment": {
        "platform": platform.platform(), "machine": platform.machine(),
        "python": run([python, "--version"], checkout),
        "packages": run([python, "-m", "pip", "freeze"], checkout)},
        "input_sha256": manifest, "checks": {}}
    for name, command in {
        "reference": [python, "test-kit/run.py"],
        "naive_negative_control": [python, "test-kit/run.py", "--reader", "naive", "--expect-fail"],
        "regeneration": [python, "test-kit/generate.py", "--check"],
    }.items():
        result["checks"][name] = run(command, checkout)
    with tempfile.TemporaryDirectory(prefix="aaif-pr57-") as temporary:
        root = Path(temporary)
        shutil.copytree(kit, root / "test-kit", ignore=shutil.ignore_patterns("__pycache__"))
        copied_kit = root / "test-kit"
        probe = copied_kit / "contributions" / "review-probe"
        shutil.copytree(copied_kit / "TEMPLATE", probe)
        fixture = copied_kit / "cases" / "effects-ticket-id-changed"
        for name in ("records.otlp.json", "basis.json"):
            shutil.copyfile(fixture / name, probe / name)
        # Deliberately wrong answer: a checked example must fail comparison.
        (probe / "expected.json").write_text('{"diagnostic": "must fail if discovered"}\n')
        result["probe"] = {"description": "Copied template plus existing synthetic inputs; intentionally wrong expected answer.",
                           "under_contributions": run([python, "test-kit/run.py"], root)}
        shutil.move(str(probe), str(copied_kit / "cases" / "review-probe"))
        result["probe"]["under_cases"] = run([python, "test-kit/run.py"], root)
    result["tracked_status_after"] = run(["git", "status", "--porcelain", "--untracked-files=no"], checkout)
    final_manifest = {name: hashlib.sha256((checkout / name).read_bytes()).hexdigest()
                      for name in manifest}
    result["inputs_unchanged"] = manifest == final_manifest
    checks_passed = all(c["exit_code"] == 0 for c in result["checks"].values())
    probe_confirmed = (result["probe"]["under_contributions"]["exit_code"] == 0
                       and "review-probe" not in result["probe"]["under_contributions"]["stdout"]
                       and result["probe"]["under_cases"]["exit_code"] == 1
                       and "DIFF review-probe" in result["probe"]["under_cases"]["stdout"])
    clean = (result["tracked_status_after"]["exit_code"] == 0
             and not result["tracked_status_after"]["stdout"] and result["inputs_unchanged"])
    result["review_checks_passed"] = checks_passed and probe_confirmed and clean
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"checks_passed": checks_passed, "probe_confirmed": probe_confirmed,
                      "source_unchanged": clean, "output": str(args.output)}, indent=2))
    return 0 if result["review_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
