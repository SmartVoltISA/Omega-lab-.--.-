#!/usr/bin/env python3
"""Ω-BASIS-002 minimal state/time control.

Synthetic stationary processes only. The purpose is to test whether an explicit
clock coordinate is required when the declared state already contains all
variables needed by the transition law.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np


def rank_of(X):
    return int(np.linalg.matrix_rank(X))


def one_step_linear_error(X):
    A = np.column_stack([np.ones(len(X)-1), X[:-1]])
    y = X[1:]
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    return float(np.mean((y-pred)**2)), coef


def fit_with_time(X):
    t = np.arange(len(X)-1, dtype=float)
    A = np.column_stack([np.ones(len(t)), X[:-1], t])
    y = X[1:]
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    return float(np.mean((y-pred)**2)), coef


def entropy_binary(values):
    vals, counts = np.unique(values, return_counts=True)
    p = counts / counts.sum()
    return float(-(p*np.log2(p)).sum())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=5000)
    ap.add_argument('--seed', type=int, default=20260813)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)

    # M0: independent 3-state observations. State dimension is tested directly.
    m0 = rng.integers(0, 3, size=args.n)

    # M1: stationary deterministic binary flip. No clock is needed once state is known.
    m1 = np.empty(args.n, dtype=int)
    m1[0] = 0
    for i in range(args.n-1):
        m1[i+1] = 1 - m1[i]

    # M2: stationary Markov chain with fixed transition probability.
    m2 = np.empty(args.n, dtype=int)
    m2[0] = 0
    for i in range(args.n-1):
        m2[i+1] = m2[i] if rng.random() < 0.8 else 1-m2[i]

    # M3: explicitly time-dependent process. State alone is insufficient because
    # the transition probability changes at the declared midpoint.
    m3 = np.empty(args.n, dtype=int)
    m3[0] = 0
    for i in range(args.n-1):
        p_stay = 0.9 if i < args.n//2 else 0.6
        m3[i+1] = m3[i] if rng.random() < p_stay else 1-m3[i]

    models = {'M0_static': m0, 'M1_deterministic': m1, 'M2_stationary_markov': m2, 'M3_time_dependent': m3}
    result = {'experiment':'Omega-BASIS-002','status':'EXECUTED','n':args.n,'seed':args.seed,'models':{}}

    for name, x in models.items():
        state_matrix = np.column_stack([x[:-1]])
        mse_state, coef_state = one_step_linear_error(x.astype(float)[:,None])
        mse_time, coef_time = fit_with_time(x.astype(float)[:,None])
        shuffled = x.copy()
        rng.shuffle(shuffled)
        mse_shuffle, _ = one_step_linear_error(shuffled.astype(float)[:,None])
        result['models'][name] = {
            'state_rank': rank_of(state_matrix),
            'state_values': sorted(set(map(int, x))),
            'state_entropy_bits': entropy_binary(x),
            'one_step_mse_state_only': mse_state,
            'one_step_mse_state_plus_time': mse_time,
            'time_coefficient': float(coef_time[-1]),
            'one_step_mse_time_shuffled': mse_shuffle,
        }

    # Pre-registered sanity expectations. These are not scientific claims.
    result['checks'] = {
        'M1_time_coefficient_near_zero': abs(result['models']['M1_deterministic']['time_coefficient']) < 1e-12,
        'M2_time_coefficient_small': abs(result['models']['M2_stationary_markov']['time_coefficient']) < 0.01,
        'M3_time_coefficient_nonzero': abs(result['models']['M3_time_dependent']['time_coefficient']) > 1e-8,
    }
    if not all(result['checks'].values()):
        raise RuntimeError('Prerequisite sanity check failed; inspect model implementation before interpretation.')

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
