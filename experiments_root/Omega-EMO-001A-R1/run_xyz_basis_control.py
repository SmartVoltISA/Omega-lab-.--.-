#!/usr/bin/env python3
"""Ω-EMO-001A-R1: verified CIE 1931 color basis control."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

EXPECTED_MD5 = "17cca777db64b17170f06f67ce9d3ab7"


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load(path: Path):
    actual = md5(path)
    if actual != EXPECTED_MD5:
        raise RuntimeError(f"MD5 mismatch: expected {EXPECTED_MD5}, got {actual}")
    df = pd.read_csv(path, header=None)
    if df.shape != (471, 4):
        raise RuntimeError(f"Unexpected dataset shape: {df.shape}")
    wl = df.iloc[:, 0].to_numpy()
    X = df.iloc[:, 1:4].to_numpy(float)
    if not np.isfinite(X).all():
        raise RuntimeError("Non-finite value in verified XYZ dataset")
    return wl, X, actual


def metrics(X):
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    rank = int(np.linalg.matrix_rank(X))
    errors = {}
    for k in (1, 2, 3):
        Xk = (U[:, :k] * s[:k]) @ Vt[:k]
        errors[str(k)] = {
            "relative_fro_error": float(np.linalg.norm(X - Xk, "fro") / np.linalg.norm(X, "fro")),
            "max_abs_error": float(np.max(np.abs(X - Xk))),
            "rmse": float(np.sqrt(np.mean((X - Xk) ** 2))),
        }
    return rank, s, errors


def leave_one_out(X):
    out = {}
    for j in range(3):
        keep = [i for i in range(3) if i != j]
        A = X[:, keep]
        b = X[:, j]
        coef = np.linalg.lstsq(A, b, rcond=None)[0]
        pred = A @ coef
        out[str(j)] = {
            "kept_columns": keep,
            "relative_residual": float(np.linalg.norm(b - pred) / np.linalg.norm(b)),
            "max_abs_residual": float(np.max(np.abs(b - pred))),
            "coefficients": [float(v) for v in coef],
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--xyz", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    wl, X, checksum = load(args.xyz)
    rank, s, errors = metrics(X)

    C = X / X.sum(axis=1, keepdims=True)
    Cc = C - C.mean(axis=0, keepdims=True)
    c_rank, cs, c_errors = metrics(Cc)

    tests = {
        "checksum": checksum == EXPECTED_MD5,
        "shape": X.shape == (471, 3),
        "full_xyz_rank_three": rank == 3,
        "full_xyz_rank2_not_exact": errors["2"]["relative_fro_error"] > 1e-12,
        "chromaticity_simplex": float(np.max(np.abs(C.sum(axis=1) - 1.0))) < 1e-12,
        "chromaticity_affine_rank_two": c_rank == 2,
        "chromaticity_rank3_residual_negligible": c_errors["3"]["relative_fro_error"] < 1e-12,
    }
    if not all(tests.values()):
        raise RuntimeError(f"Invariant/test failure: {tests}")

    result = {
        "experiment": "Omega-EMO-001A-R1",
        "status": "EXECUTED",
        "dataset": {
            "file": args.xyz.name,
            "md5": checksum,
            "rows": int(len(X)),
            "wavelength_min": int(wl.min()),
            "wavelength_max": int(wl.max()),
        },
        "full_xyz": {
            "rank": rank,
            "singular_values": [float(v) for v in s],
            "singular_ratios_to_s1": [float(v / s[0]) for v in s],
            "errors": errors,
            "leave_one_out": leave_one_out(X),
        },
        "chromaticity_centered": {
            "rank": c_rank,
            "singular_values": [float(v) for v in cs],
            "singular_ratios_to_s1": [float(v / cs[0]) for v in cs],
            "errors": c_errors,
            "simplex_identity_max_abs": float(np.max(np.abs(C.sum(axis=1) - 1.0))),
        },
        "tests": tests,
        "interpretation_boundary": "Color-control result only; no universal Ω-basis claim.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
