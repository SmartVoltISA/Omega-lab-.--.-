#!/usr/bin/env python3
"""Ω-SELF-001 toy pilot: functional self-model vs bounded self-modification.
Tests self-monitoring, NOT subjective consciousness.
Requires: numpy, pandas.
"""
from dataclasses import dataclass
import argparse, json
import numpy as np
import pandas as pd

@dataclass
class Result:
    condition: str
    seed: int
    survival_steps: int
    survived_full_horizon: int
    final_energy: float
    mean_energy: float
    actions_performed: int
    policy_changes: int
    prediction_error: float

def run_one(condition, seed, horizon=500, change_at=250):
    rng = np.random.default_rng(seed)
    energy, fatigue = 55.0, 0.0
    estimated_energy, estimated_fatigue = 55.0, 0.0
    forage_threshold, rest_threshold = 36.0, 22.0
    policy_changes, pred_errors = 0, []
    energy_trace, actions = [], 0
    regime = 0
    for t in range(horizon):
        if t == change_at:
            regime = 1
        cue = regime + rng.normal(0, 0.55)
        if condition == "A_reactive":
            if energy < 18: action = "rest"
            elif cue < 0.45 and energy > 34: action = "forage"
            elif energy < 42: action = "forage"
            else: action = "conserve"
        else:
            perceived_energy = estimated_energy + rng.normal(0, 2.5)
            perceived_fatigue = estimated_fatigue + rng.normal(0, 0.15)
            if perceived_energy < rest_threshold or perceived_fatigue > 0.9:
                action = "rest"
            elif perceived_energy < forage_threshold:
                action = "forage"
            elif cue < 0.4 and perceived_energy > 38:
                action = "forage"
            else: action = "conserve"
        before = energy
        if action == "forage":
            gain = (12.0 if regime == 0 else 5.0) + rng.normal(0, 4.0)
            energy += gain - 5.5 - 2.5*fatigue
            fatigue = min(1.5, fatigue + 0.12)
        elif action == "rest":
            energy += 3.5 + rng.normal(0, 1.0)
            fatigue = max(0.0, fatigue - 0.24)
        else:
            energy += (0.5 if regime == 0 else -1.0) + rng.normal(0, 1.4)
            fatigue = max(0.0, fatigue - 0.05)
        energy = float(np.clip(energy, 0, 100))
        energy_trace.append(energy); actions += 1
        if condition != "A_reactive":
            estimated_energy = float(np.clip(estimated_energy + (energy-before) + rng.normal(0, 1.2), 0, 100))
            estimated_fatigue = float(np.clip(fatigue + rng.normal(0, 0.08), 0, 1.5))
            pred_errors.append(abs(estimated_energy-energy))
            if condition == "C_self_modifying":
                old_f, old_r = forage_threshold, rest_threshold
                if action == "forage" and energy-before < 1.0:
                    forage_threshold = max(24.0, forage_threshold-0.8)
                elif energy < 30:
                    forage_threshold = min(46.0, forage_threshold+0.5)
                if energy < 16:
                    rest_threshold = min(30.0, rest_threshold+0.6)
                elif action == "rest" and energy > 45 and fatigue < 0.2:
                    rest_threshold = max(14.0, rest_threshold-0.2)
                if abs(old_f-forage_threshold)+abs(old_r-rest_threshold) > 1e-9:
                    policy_changes += 1
        if energy <= 0.0: break
    return Result(condition, seed, len(energy_trace), int(len(energy_trace)==horizon),
                  float(energy_trace[-1]), float(np.mean(energy_trace)), actions,
                  policy_changes, float(np.mean(pred_errors)) if pred_errors else float("nan"))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seeds",type=int,default=200)
    p.add_argument("--horizon",type=int,default=500)
    p.add_argument("--change-at",type=int,default=250)
    p.add_argument("--out",default="results.csv")
    a=p.parse_args()
    rows=[]
    for s in range(a.seeds):
        for ci,c in enumerate(["A_reactive","B_self_model","C_self_modifying"]):
            rows.append(run_one(c,s*1009+ci*1000003,a.horizon,a.change_at).__dict__)
    df=pd.DataFrame(rows); df.to_csv(a.out,index=False)
    summary=df.groupby("condition").agg(
      runs=("seed","count"),mean_survival_steps=("survival_steps","mean"),
      sd_survival_steps=("survival_steps","std"),
      full_horizon_rate=("survived_full_horizon","mean"),
      mean_final_energy=("final_energy","mean"),mean_energy=("mean_energy","mean"),
      mean_prediction_error=("prediction_error","mean"),
      mean_policy_changes=("policy_changes","mean")).reset_index()
    summary.to_csv(a.out.replace(".csv","_summary.csv"),index=False)
    with open(a.out.replace(".csv","_summary.json"),"w") as f:
        json.dump(summary.to_dict(orient="records"),f,indent=2)
    print(summary.to_string(index=False))
if __name__=="__main__": main()
