"""Immutable anchor for the Ω-Lab foundation.

The Guardian keeps a pinned Git blob identity for the active foundation. A
foundation mismatch is a security failure: the request is never allowed to
cross the Guardian boundary until the foundation is restored and re-verified.
"""
from __future__ import annotations

from pathlib import Path
import subprocess

FOUNDATION_PATH = Path("00_CORE/OMEGA_FOUNDATION_ARCHITECTURE_v1.1.md")
FOUNDATION_GIT_BLOB_SHA = "6d5649a0ebe86226dd8c35d4009cff3bbc27dd44"


def foundation_integrity_ok(root: Path | None = None) -> bool:
    root = root or Path.cwd()
    path = root / FOUNDATION_PATH
    if not path.is_file():
        return False
    try:
        actual = subprocess.check_output(
            ["git", "hash-object", str(path)], cwd=root, text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return False
    return actual == FOUNDATION_GIT_BLOB_SHA


def protected_foundation_identity() -> dict[str, str]:
    return {"path": str(FOUNDATION_PATH), "git_blob_sha": FOUNDATION_GIT_BLOB_SHA}
