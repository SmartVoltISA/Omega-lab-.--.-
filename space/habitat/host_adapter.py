"""Read-only host adapters for the SPACE habitat."""
from __future__ import annotations
import os, platform, shutil, subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class HostSnapshot:
    os: str; kernel: str; architecture: str; cpu_count: int | None; ram_bytes: int | None; storage_free_bytes: int | None
    gpus: tuple[dict[str, Any], ...]; network_interfaces: tuple[str, ...]; bluetooth: tuple[str, ...]; usb: tuple[str, ...]
    cameras: tuple[str, ...]; audio_devices: tuple[str, ...]; displays: tuple[str, ...]

class HostAdapter:
    """Portable, conservative discovery. Missing OS facilities become empty."""
    def _ram(self) -> int | None:
        try:
            for line in Path("/proc/meminfo").read_text().splitlines():
                if line.startswith("MemTotal:"): return int(line.split()[1]) * 1024
        except (OSError, ValueError): pass
        return None
    def _names(self, path: str) -> tuple[str, ...]:
        try: return tuple(sorted(p.name for p in Path(path).iterdir()))
        except OSError: return tuple()
    def _gpus(self) -> tuple[dict[str, Any], ...]:
        try:
            out = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader,nounits"], capture_output=True, text=True, timeout=2, check=False)
            if out.returncode == 0:
                return tuple({"vendor":"nvidia", "name": n.strip(), "vram_mib": int(m.strip())} for n, m in (line.split(",", 1) for line in out.stdout.splitlines()))
        except (OSError, ValueError, subprocess.SubprocessError): pass
        return tuple()
    def snapshot(self) -> dict[str, Any]:
        dev = self._names("/dev"); root = shutil.disk_usage("/")
        snap = HostSnapshot(platform.system(), platform.release(), platform.machine(), os.cpu_count(), self._ram(), root.free, self._gpus(),
            self._names("/sys/class/net"), self._names("/sys/class/bluetooth"), self._names("/sys/bus/usb/devices"),
            tuple(x for x in dev if x.startswith("video")), tuple(x for x in dev if x.startswith("snd")), self._names("/sys/class/drm"))
        return asdict(snap)
