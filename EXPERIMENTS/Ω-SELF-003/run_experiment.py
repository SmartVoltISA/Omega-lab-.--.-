#!/usr/bin/env python3
"""Ω-SELF-003: feedback adaptation vs sham self-modification."""
import argparse
import numpy as np
import pandas as pd
CONDS=["A_reactive_noisy","B_self_model_fixed","C_feedback_self_modify","D_sham_self_modify","E_oracle_state"]
def run_experiment(n_seeds=1000,horizon=600):
 rows=[]
 for seed in range(n_seeds):
  rng=np.random.default_rng(seed+2603003); family=seed%4
  regime=np.zeros(horizon,dtype=int); state=int(rng.integers(0,2))
  if family==0:
   change=int(rng.integers(35,80))
   for t in range(horizon):
    if t>=change: state=1-state; change=t+int(rng.integers(35,80))
    regime[t]=state
  elif family==1:
   change=int(rng.integers(100,180))
   for t in range(horizon):
    if t>=change: state=1-state; change=t+int(rng.integers(100,180))
    regime[t]=state
  elif family==2:
   shift=int(rng.integers(180,420)); regime[:]=state; regime[shift:]=1-state
  else: regime[:]=state
  obs_noise=rng.normal(0,10,horizon); forage_noise=rng.normal(0,4,horizon)
  rest_noise=rng.normal(0,1,horizon); conserve_noise=rng.normal(0,1.8,horizon)
  cue=(regime+rng.normal(0,1,horizon))>0.6
  high=[11.,10.,12.,9.][family]; low=[3.5,4.5,2.5,5.][family]; initial=[42.,45.,38.,48.][family]
  for cond in CONDS:
   energy=initial; fatigue=.2; pred=initial; fatigue_belief=.2
   threshold=35.; rest_threshold=18.; changes=0; trace=[]; errors=[]; survival=horizon
   for t in range(horizon):
    obs=float(np.clip(energy+obs_noise[t],0,100))
    if cond=="A_reactive_noisy": perceived=obs
    elif cond=="E_oracle_state": perceived=energy
    else: perceived=float(np.clip(pred+.72*(obs-pred),0,100))
    if perceived<rest_threshold or fatigue>.95: action="rest"
    elif perceived<threshold: action="forage"
    elif cue[t] and perceived<62: action="forage"
    else: action="conserve"
    before=energy
    if action=="forage":
     energy+=(high if regime[t]==0 else low)+forage_noise[t]-6.5-2.6*fatigue; fatigue=min(1.5,fatigue+.15)
    elif action=="rest": energy+=3.5+rest_noise[t]; fatigue=max(0.,fatigue-.25)
    else: energy+=-1.2+conserve_noise[t]; fatigue=max(0.,fatigue-.04)
    energy=float(np.clip(energy,0,100))
    if cond in ("B_self_model_fixed","C_feedback_self_modify","D_sham_self_modify"):
     assumed=(high+low)/2
     if action=="forage": delta=assumed-6.5-2.6*fatigue_belief
     elif action=="rest": delta=3.5
     else: delta=-1.2
     pred=float(np.clip(perceived+delta,0,100)); errors.append(abs(pred-energy))
     fatigue_belief=float(np.clip(fatigue_belief+(.15 if action=="forage" else -.25 if action=="rest" else -.04),0,1.5))
     if cond=="C_feedback_self_modify":
      old=(threshold,rest_threshold)
      if action=="forage" and energy-before < -1.5: threshold=max(24,threshold-.35)
      if energy<24: rest_threshold=min(27,rest_threshold+.4)
      elif energy>55 and fatigue<.25: rest_threshold=max(14,rest_threshold-.1)
      if abs(threshold-old[0])+abs(rest_threshold-old[1])>1e-9: changes+=1
     elif cond=="D_sham_self_modify":
      old=(threshold,rest_threshold)
      if t%9==0: threshold=24+(t%7)*.7
      if t%13==0: rest_threshold=14+(t%5)*.8
      if abs(threshold-old[0])+abs(rest_threshold-old[1])>1e-9: changes+=1
    trace.append(energy)
    if energy<=0: survival=t+1; break
   a=np.asarray(trace)
   rows.append(dict(condition=cond,seed=seed,family=family,survival_steps=survival,
    survived_full_horizon=int(survival==horizon),final_energy=float(a[-1]),mean_energy=float(a.mean()),
    mean_prediction_error=float(np.mean(errors)) if errors else None,policy_changes=changes))
 return pd.DataFrame(rows)
def main():
 p=argparse.ArgumentParser(); p.add_argument("--seeds",type=int,default=1000); p.add_argument("--horizon",type=int,default=600); p.add_argument("--out",default="results.csv"); a=p.parse_args()
 d=run_experiment(a.seeds,a.horizon); d.to_csv(a.out,index=False)
 s=d.groupby("condition").agg(runs=("seed","count"),full_horizon_rate=("survived_full_horizon","mean"),mean_survival_steps=("survival_steps","mean"),sd_survival_steps=("survival_steps","std"),mean_final_energy=("final_energy","mean"),mean_energy=("mean_energy","mean"),mean_prediction_error=("mean_prediction_error","mean"),mean_policy_changes=("policy_changes","mean")).reset_index()
 s.to_csv(a.out.replace(".csv","_summary.csv"),index=False); print(s.to_string(index=False))
if __name__=="__main__": main()
