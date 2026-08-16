"""Read-only security scanning boundary for SPACE.

The lab may inspect/quarantine artifacts, hash them, and optionally invoke an
explicitly configured antivirus executable. It never executes the inspected
artifact and never promotes it to trusted state by itself.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
from typing import Optional


@dataclass(frozen=True)
class ScanResult:
    verdict: str
    sha256: str
    size: int
    engine: str
    detail: str


class SecurityScanLab:
    def __init__(self, quarantine_dir: Path):
        self.quarantine_dir = Path(quarantine_dir)
        self.quarantine_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _hash(path: Path) -> str:
        digest = sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def quarantine(self, source: Path) -> Path:
        source = Path(source).resolve()
        if not source.is_file():
            raise ValueError("security scan input must be a regular file")
        target = self.quarantine_dir / source.name
        shutil.copy2(source, target)
        return target

    def inspect(self, path: Path, av_command: Optional[str] = None) -> ScanResult:
        path = Path(path).resolve()
        if not path.is_file():
            raise ValueError("security scan input must be a regular file")
        digest = self._hash(path)
        size = path.stat().st_size

        if av_command:
            # The executable is supplied by the trusted host configuration.
            # The scanned artifact is passed as data; it is never executed.
            proc = subprocess.run(
                [av_command, "--no-summary", str(path)],
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            )
            verdict = "CLEAN" if proc.returncode == 0 else "DETECTED"
            detail = (proc.stdout + proc.stderr).strip()[:4000]
            return ScanResult(verdict, digest, size, av_command, detail)

        return ScanResult(
            "UNSCANNED",
            digest,
            size,
            "metadata-only",
            "No antivirus engine configured; artifact remains quarantined.",
        )
