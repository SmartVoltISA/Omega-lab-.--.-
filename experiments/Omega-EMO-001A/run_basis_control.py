#!/usr/bin/env python3
"""Ω-EMO-001A physical color basis control.

No external downloads are performed by this script. Input datasets are supplied
locally so the exact files and checksums used for a run are explicit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

EXPECTED_MD5 = {
    "CIE1931_XYZ": "17cca777db64b17170f06f67ce9d3ab7",
    "CIE2006_LMS": "27c74cc0f98edecadc02fc71f540b116",
}


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_dataset(path: Path, expected_md5: str):
    actual = md5(path)
    if actual != expected_md5:
        raise RuntimeError(f"MD5 mismatch for {path}: expected {expected_md5}, got {actual}")
    df = pd.read_csv(path, header=None)
    if df.shape[1] != 4:
        raise RuntimeError(f"Expected 4 columns in {path}, got {df.shape[1]}")
    wavelengths = df.iloc[:, 0].to_numpy()
    X = df.iloc[:, 1:4].to_numpy(dtype=float)
    input_nan_count = int(np.isnan(X).sum())
    return wavelengths, X, input_nan_count, actual


def svd_metrics(X: np.ndarray):
    if not np.isfinite(X).all():
        raise RuntimeError("Non-finite values remain after input handling")
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    rank = int(np.linalg.matrix_rank(X))
    errors = {}
    for k in (1, 2, 3):
        Xk = (U[:, :k] * s[:k]) @ Vt[:k, :]
        errors[str(k)] = {
            "relative_fro_error": float(np.linalg.norm(X - Xk, "fro") / np.linalg.norm(X, "fro")),
            "max_abs_error": float(np.max(np.abs(X - Xk))),
            "rmse": float(np.sqrt(np.mean((X - Xk) ** 2))),
        }
    return rank, s, errors


def leave_one_out(X: np.ndarray):
    result = {}
    for j in range(3):
        keep = [i for i in range(3) if i != j]
        A = X[:, keep]
        b = X[:, j]
        coef = np.linalg.lstsq(A, b, rcond=None)[0]
        pred = A @ coef
        denom = np.sum((b - b.mean()) ** 2)
        r2 = float(1 - np.sum((b - pred) ** 2) / denom) if denom else float("nan")
        result[str(j)] = {
            "kept_columns": keep,
            "coefficients": [float(v) for v in coef],
            "relative_residual": float(np.linalg.norm(b - pred) / np.linalg.norm(b)),
            "max_abs_residual": float(np.max(np.abs(b - pred))),
            "r2": r2,
        }
    return result


def analyze(name: str, wavelengths: np.ndarray, X: np.ndarray, input_nan_count: int, checksum: str, nan_to_zero: bool):
    if nan_to_zero:
        X = np.nan_to_num(X, nan=0.0)
    rank, s, errors = svd_metrics(X)
    return {
        "name": name,
        "rows": int(len(X)),
        "wavelength_min": int(wavelengths.min()),
        "wavelength_max": int(wavelengths.max()),
        "input_nan_count": input_nan_count,
        "nan_to_zero": nan_to_zero,
        "md5": checksum,
        "rank": rank,
        "singular_values": [float(v) for v in s],
        "singular_ratios_to_s1": [float(v / s[0]) for v in s],
        "errors": errors,
        "leave_one_out": leave_one_out(X),
    }


def analyze_chromaticity(wavelengths, X, checksum):
    X = np.nan_to_num(X, nan=0.0)
    denom = X.sum(axis=1, keepdims=True)
    if np.any(denom == 0):
        raise RuntimeError("Chromaticity normalization encountered a zero row sum")
    C = X / denom
    # Chromaticity has an affine 2-D constraint Cx+Cy+Cz=1. Centering makes
    # the intrinsic affine dimension testable by ordinary linear rank.
    Cc = C - C.mean(axis=0, keepdims=True)
    rank, s, errors = svd_metrics(Cc)
    return {
        "name": "CIE1931_chromaticity_centered",
        "rows": int(len(C)),
        "wavelength_min": int(wavelengths.min()),
        "wavelength_max": int(wavelengths.max()),
        "md5": checksum,
        "normalization": "XYZ / (X+Y+Z)",
        "centered_before_rank": True,
        "rank": rank,
        "singular_values": [float(v) for v in s],
        "singular_ratios_to_s1": [float(v / s[0]) for v in s],
        "errors": errors,
        "simplex_identity_max_abs": float(np.max(np.abs(C.sum(axis=1) - 1.0))),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--xyz", required=True, type=Path)
    ap.add_argument("--lms", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    xyz_w, xyz_X, xyz_nan, xyz_md5 = load_dataset(args.xyz, EXPECTED_MD5["CIE1931_XYZ"])
    lms_w, lms_X, lms_nan, lms_md5 = load_dataset(args.lms, EXPECTED_MD5["CIE2006_LMS"])

    xyz = analyze("CIE1931_XYZ", xyz_w, xyz_X, xyz_nan, xyz_md5, False)
    lms = analyze("CIE2006_LMS", lms_w, lms_X, lms_nan, lms_md5, True)
    chrom = analyze_chromaticity(xyz_w, xyz_X, xyz_md5)

    # Basic invariants/tests required by the protocol.
    tests = {
        "xyz_checksum": xyz_md5 == EXPECTED_MD5["CIE1931_XYZ"],
        "lms_checksum": lms_md5 == EXPECTED_MD5["CIE2006_LMS"],
        "xyz_rank_three": xyz["rank"] == 3,
        "lms_rank_three": lms["rank"] == 3,
        "chromaticity_centered_rank_two": chrom["rank"] == 2,
        "chromaticity_sum_identity": chrom["simplex_identity_max_abs"] < 1e-12,
        "xyz_rank2_not_exact": xyz["errors"]["2"]["relative_fro_error"] > 1e-12,
        "lms_rank2_not_exact": lms["errors"]["2"]["relative_fro_error"] > 1e-12,
    }
    if not all(tests.values()):
        raise RuntimeError(f"Invariant/test failure: {tests}")

    result = {
        "experiment": "Omega-EMO-001A",
        "status": "EXECUTED",
        "datasets": {
            "CIE1931_XYZ": xyz,
            "CIE2006_LMS": lms,
            "CIE1931_chromaticity_centered": chrom,
        },
        "tests": tests,
        "interpretation_boundary": "Color-control result only; no claim about a universal Ω basis, information, or emotion.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
