"""Orchestrator: run the daily pipeline end to end.

Stages run sequentially; any non-zero exit aborts the rest. Designed to be
invoked from GitHub Actions and from a local dev box equally.
"""
from __future__ import annotations

import subprocess
import sys

from common import ROOT, log


def step(label: str, script: str, fatal: bool = True) -> None:
    log.info("===== %s =====", label)
    res = subprocess.run([sys.executable, f"scripts/{script}"], cwd=ROOT)
    if res.returncode != 0:
        if fatal:
            raise SystemExit(f"step {label} failed (exit {res.returncode})")
        log.warning("step %s failed (exit %d) — non-fatal, continuing",
                    label, res.returncode)


def main():
    step("fetch papers",      "fetch.py")
    step("process papers",    "process.py")
    step("write paper md",    "write_md.py")
    step("fetch news",        "fetch_news.py")
    step("process news",      "process_news.py")
    step("write news md",     "write_news_md.py")
    # repos: best-effort — GitHub search rate-limits shouldn't kill the run
    step("fetch repos",       "fetch_repos.py",   fatal=False)
    step("process repos",     "process_repos.py", fatal=False)
    step("write repos md",    "write_repos_md.py", fatal=False)
    step("push feishu",       "push_feishu.py")
    log.info("pipeline done")


if __name__ == "__main__":
    main()
