#!/usr/bin/env python3
"""Ω-SELF-002: self-model calibration vs bounded self-modification.
Requires numpy and pandas. Tests functional monitoring, not consciousness.
"""
import argparse
import numpy as np
import pandas as pd

CONDITIONS = ["A_reactive_noisy","B_calibrated_self_model",
              "C_miscalibrated_self_model","D_self_modifying","E_oracle_state"]

def run_experiment(n_seeds=1000, horizon=600):
    rows=[]
    for seed in range(n_seeds):
        rng=np.random.default_rng(seed+2601021)
        regime=np.zeros(horizon,dtype=int); state=0
        for t in range(horizon):
            if t in (120,240,360,480): state=1-state
            regime[t]=state
        # Shared exogenous streams make condition comparisons paired by seed.
        obs_noise=rng.normal(0,10,size=horizon)
        forage_noise=rng.normal(0,4.0,size=horizon)
        rest_noise=rng.normal(0,1.0,size=horizon)
        conserve_noise=rng.normal(0,1.8,size=horizon)
        cue_noise=rng.normal(0,1.0,size=horizon)
        cue=(regime+cue_noise)>0.6
        for cond in CONDITIONS:
            energy,fatigue=42.0,0.2
            predicted_energy,fatigue_belief=42.0,0.2
            threshold,rest_threshold=35.0,18.0
            policy_changes=0; trace=[]; pred_errors=[]; survival=horizon
            for t in range(horizon):
                observed=float(np.clip(energy+obs_noise[t],0,100))
                if cond=="A_reactive_noisy": perceived=observed
                elif cond=="E_oracle_state": perceived=energy
                else:
                    gain=0.72 if cond!="C_miscalibrated_self_model" else 0.18
                    perceived=float(np.clip(predicted_energy+gain*(observed-predicted_energy),0,100))
                if perceived<rest_threshold or fatigue>0.95: action="rest"
                elif perceived<threshold: action="forage"
                elif cue[t] and perceived<62: action="forage"
                else: action="conserve"
                before=energy
                if action=="forage":
                    y=(11.0 if regime[t]==0 else 3.5)+forage_noise[t]
                    energy += y-6.5-2.6*fatigue
                    fatigue=min(1.5,fatigue+0.15)
                elif action=="rest":
                    energy += 3.5+rest_noise[t]; fatigue=max(0.0,fatigue-0.25)
                else:
                    energy += -1.2+conserve_noise[t]; fatigue=max(0.0,fatigue-0.04)
                energy=float(np.clip(energy,0,100))
                if cond in ("B_calibrated_self_model","C_miscalibrated_self_model","D_self_modifying"):
                    if action=="forage":
                        assumed_yield=7.25 if cond!="C_miscalibrated_self_model" else 12.5
                        pred_delta=assumed_yield-6.5-2.6*fatigue_belief
                    elif action=="rest": pred_delta=3.5
                    else: pred_delta=-1.2
                    predicted_energy=float(np.clip(perceived+pred_delta,0,100))
                    pred_errors.append(abs(predicted_energy-energy))
                    fatigue_belief=float(np.clip(fatigue_belief+(0.15 if action=="forage" else -0.25 if action=="rest" else -0.04),0,1.5))
                    if cond=="D_self_modifying":
                        old=(threshold,rest_threshold)
                        if action=="forage" and energy-before < -1.5: threshold=max(24.0,threshold-0.35)
                        if energy<24: rest_threshold=min(27.0,rest_threshold+0.4)
                        elif energy>55 and fatigue<0.25: rest_threshold=max(14.0,rest_threshold-0.1)
                        if abs(threshold-old[0])+abs(rest_threshold-old[1])>1e-9: policy_changes+=1
                trace.append(energy)
                if energy<=0: survival=t+1; break
            a=np.asarray(trace)
            rows.append({"condition":cond,"seed":seed,"survival_steps":survival,
              "survived_full_horizon":int(survival==horizon),"final_energy":float(a[-1]),
              "mean_energy":float(a.mean()),"mean_prediction_error":float(np.mean(pred_errors)) if pred_errors else None,
              "policy_changes":policy_changes})
    return pd.DataFrame(rows)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seeds",type=int,default=1000)
    p.add_argument("--horizon",type=int,default=600)
    p.add_argument("--out",default="results.csv")
    a=p.parse_args()
    df=run_experiment(a.seeds,a.horizon); df.to_csv(a.out,index=False)
    s=df.groupby("condition").agg(runs=("seed","count"),
      full_horizon_rate=("survived_full_horizon","mean"),
      mean_survival_steps=("survival_steps","mean"),
      sd_survival_steps=("survival_steps","std"),
      mean_final_energy=("final_energy","mean"),mean_energy=("mean_energy","mean"),
      mean_prediction_error=("mean_prediction_error","mean"),
      mean_policy_changes=("policy_changes","mean")).reset_index()
    s.to_csv(a.out.replace(".csv","_summary.csv"),index=False)
    print(s.to_string(index=False))
if __name__=="__main__": main()
