"""Orchestrator: run the daily pipeline end to end.

Stages run sequentially; any non-zero exit aborts the rest. Designed to be
invoked from GitHub Actions and from a local dev box equally.
"""
from __future__ import annotations

import subprocess
import sys

from common import ROOT, log


def step(label: str, script: str) -> None:
    log.info("===== %s =====", label)
    res = subprocess.run([sys.executable, f"scripts/{script}"], cwd=ROOT)
    if res.returncode != 0:
        raise SystemExit(f"step {label} failed (exit {res.returncode})")


def main():
    step("fetch",       "fetch.py")
    step("process",     "process.py")
    step("write_md",    "write_md.py")
    step("push_feishu", "push_feishu.py")
    log.info("pipeline done")


if __name__ == "__main__":
    main()
