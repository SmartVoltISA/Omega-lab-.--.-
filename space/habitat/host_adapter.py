"""Read-only host adapters for the SPACE habitat.

These adapters discover the host environment without granting the organism
implicit authority to control it. Protected I/O remains behind GuardianIO.
"""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class HostSnapshot:
    os: str
    kernel: str
    architecture: str
    cpu_count: int | None
    ram_bytes: int | None
    storage_free_bytes: int | None
    gpus: tuple[dict[str, Any], ...]
    network_interfaces: tuple[str, ...]
    bluetooth: tuple[str, ...]
    usb: tuple[str, ...]
    cameras: tuple[str, ...]
    audio_devices: tuple[str, ...]
    displays: tuple[str, ...]

class HostAdapter:
    """Portable, conservative discovery. Missing OS facilities become empty."""

    def _ram(self) -> int | None:
        try:
            if Path("/proc/meminfo").exists():
                for line in Path("/proc/meminfo").read_text().splitlines():
                    if line.startswith("MemTotal:"):
                        return int(line.split()[1]) * 1024
        except (OSError, ValueError):
            pass
        return None

    def _interfaces(self) -> tuple[str, ...]:
        try:
            return tuple(sorted(p.name for p in Path("/sys/class/net").iterdir()))
        except OSError:
            return tuple()

    def _names(self, path: str) -> tuple[str, ...]:
        try:
            return tuple(sorted(p.name for p in Path(path).iterdir()))
        except OSError:
            return tuple()

    def _gpus(self) -> tuple[dict[str, Any], ...]:
        # nvidia-smi is optional; failure is intentionally non-fatal.
        try:
            out = subprocess.run(
                ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader,nounits"],
                capture_output=True, text=True, timeout=2, check=False,
            )
            if out.returncode == 0:
                result = []
                for line in out.stdout.splitlines():
                    name, memory = [x.strip() for x in line.split(",", 1)]
                    result.append({"vendor": "nvidia", "name": name, "vram_mib": int(memory)})
                return tuple(result)
        except (OSError, ValueError, subprocess.SubprocessError):
            pass
        return tuple()

    def snapshot(self) -> dict[str, Any]:
        root = shutil.disk_usage("/")
        cameras = self._names("/dev")
        cameras = tuple(x for x in cameras if x.startswith("video"))
        audio = tuple(x for x in cameras if x.startswith("snd"))
        bluetooth = self._names("/sys/class/bluetooth")
        usb = self._names("/sys/bus/usb/devices")
        displays = self._names("/sys/class/drm")
        snap = HostSnapshot(
            os=platform.system(), kernel=platform.release(), architecture=platform.machine(),
            cpu_count=os.cpu_count(), ram_bytes=self._ram(), storage_free_bytes=root.free,
            gpus=self._gpus(), network_interfaces=self._interfaces(), bluetooth=bluetooth,
            usb=usb, cameras=cameras, audio_devices=audio, displays=displays,
        )
        return asdict(snap)
