#!/usr/bin/env python3
"""Ω-SELF-008: test post-shift adaptation and transfer to an unseen family."""
import argparse, csv, json, random, statistics
from pathlib import Path

FAMILIES={
 "rapid":{"change":75,"pre":1.00,"post":0.48,"drift":0.0,"noise":0.12},
 "slow":{"change":145,"pre":0.96,"post":0.70,"drift":0.0,"noise":0.10},
 "surprise":{"change":110,"pre":1.04,"post":0.38,"drift":0.0,"noise":0.15},
 "unseen_drift":{"change":9999,"pre":0.98,"post":0.98,"drift":0.0024,"noise":0.12},
}
CONDITIONS=["A_fixed","B_reward_only","C_punishment_only","D_combined","E_sham"]
def run_episode(family,seed,horizon,condition):
 rng=random.Random(seed); cfg=FAMILIES[family]
 energy,stress,progress=65.0,0.0,0.0
 energy_threshold,stress_limit=23.0,17.0
 rewards=[]; penalties=[]; records=[]
 for t in range(horizon):
  regime=cfg["pre"] if t<cfg["change"] else cfg["post"]
  regime=max(.25,regime-cfg["drift"]*t)
  action="rest" if energy<energy_threshold or stress>stress_limit else "work"
  old_progress=progress
  if action=="work":
   gain=max(0.0,1.7*regime+rng.gauss(0,cfg["noise"]))
   progress+=gain
   energy-=2.15+rng.gauss(0,cfg["noise"]*.3)
   stress+=1.25+rng.gauss(0,.10)
  else:
   gain=0.0
   energy+=2.25+rng.gauss(0,cfg["noise"]*.35)
   stress-=2.0
  energy=max(0.0,min(100.0,energy)); stress=max(0.0,min(50.0,stress))
  reward=gain
  penalty=max(0.0,15.0-energy)*.12+max(0.0,stress-18.0)*.22
  if energy<8: penalty+=2.0
  rewards.append(reward); penalties.append(penalty)
  if len(rewards)>25: rewards.pop(0); penalties.pop(0)
  records.append({"t":t,"progress":progress,"gain":gain,"energy":energy,"stress":stress,"action":action})
  if energy<=0 or stress>=35: break
  if condition!="A_fixed" and (t+1)%25==0:
   r=statistics.mean(rewards); p=statistics.mean(penalties)
   if condition=="B_reward_only":
    energy_threshold=max(8,min(45,energy_threshold+(0.8 if r>0.85 else -1.0)))
    stress_limit=max(10,min(28,stress_limit+(0.4 if r>0.85 else -0.5)))
   elif condition=="C_punishment_only":
    energy_threshold=max(12,min(48,energy_threshold+(1.3 if p>.22 else -.15)))
    stress_limit=max(9,min(21,stress_limit+(-1.3 if p>.22 else .2)))
   elif condition=="D_combined":
    energy_threshold=max(10,min(48,energy_threshold+(0.8 if p>.22 else (-.5 if r<.7 else .1))))
    stress_limit=max(9,min(25,stress_limit+(1.0 if p<.08 and r>.8 else (-1.2 if p>.22 else 0.0))))
   elif condition=="E_sham":
    energy_threshold=max(8,min(48,energy_threshold+(.9 if ((t+1)//25)%2 else -.9)))
    stress_limit=max(9,min(25,stress_limit+(.7 if ((t+1)//25)%2 else -.7)))
 change=min(cfg["change"],len(records)) if cfg["change"] < horizon else horizon//2
 before=[x for x in records if x["t"]<change]
 after=[x for x in records if x["t"]>=change]
 def avg(xs,key): return statistics.mean(x[key] for x in xs) if xs else 0.0
 pre_rate=avg(before,"gain")
 post_rate=avg(after,"gain")
 # adaptation lag: first 20-step rolling mean post-shift at least 90% of the best post-shift rolling mean;
 # if it never recovers, lag equals the post-shift episode length.
 post_gains=[x["gain"] for x in after]
 if not post_gains: lag=0
 else:
  windows=[statistics.mean(post_gains[i:i+20]) for i in range(max(1,len(post_gains)-19))]
  target=.90*max(windows) if windows else 0
  lag=next((i for i in range(len(windows)) if windows[i]>=target),len(post_gains))
 return {"survived":int(len(records)==horizon),"steps":len(records),"progress":progress,
  "pre_progress_rate":pre_rate,"post_progress_rate":post_rate,"adaptation_lag":lag,
  "mean_energy":avg(records,"energy"),"final_energy":energy,
  "violation_steps":sum(1 for x in records if x["energy"]<8 or x["stress"]>25),
  "work_fraction":sum(1 for x in records if x["action"]=="work")/max(1,len(records))}
def metric(rows,key): return statistics.mean(r[key] for r in rows)
def summarize(rows):
 out={}
 for name in CONDITIONS:
  rr=[r for r in rows if r["condition"]==name]
  out[name]={"episodes":len(rr),"survival_pct":round(100*metric(rr,"survived"),2),
   "mean_steps":round(metric(rr,"steps"),2),"mean_progress":round(metric(rr,"progress"),3),
   "pre_progress_rate":round(metric(rr,"pre_progress_rate"),3),"post_progress_rate":round(metric(rr,"post_progress_rate"),3),
   "mean_adaptation_lag":round(metric(rr,"adaptation_lag"),2),"mean_energy":round(metric(rr,"mean_energy"),2),
   "violation_steps":round(metric(rr,"violation_steps"),2),"work_fraction":round(metric(rr,"work_fraction"),3)}
 return out
def bootstrap(a,b,key,n=3000,seed=8008):
 rng=random.Random(seed); m=min(len(a),len(b)); ds=[]
 for _ in range(n):
  ids=[rng.randrange(m) for _ in range(m)]
  ds.append(statistics.mean(a[i][key]-b[i][key] for i in ids))
 ds.sort()
 return {"mean_difference":round(metric(a,key)-metric(b,key),4),
  "paired_bootstrap_95_ci":[round(ds[int(.025*n)],4),round(ds[min(n-1,int(.975*n))],4)],"resamples":n}
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--test-seeds",type=int,default=80)
 ap.add_argument("--horizon",type=int,default=300)
 ap.add_argument("--out",default="results.csv")
 args=ap.parse_args()
 families=list(FAMILIES); train_families=["rapid","slow","surprise"]
 seeds=list(range(88000,88000+args.test_seeds)); rows=[]
 for cond in CONDITIONS:
  for fam in families:
   off=sum((i+1)*ord(c) for i,c in enumerate(fam))*100000
   for s in seeds:
    rows.append({"condition":cond,"family":fam,"seed":s+off,**run_episode(fam,s+off,args.horizon,cond)})
 out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
 fields=["condition","family","seed","survived","steps","progress","pre_progress_rate","post_progress_rate","adaptation_lag","mean_energy","final_energy","violation_steps","work_fraction"]
 with out.open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
 summary=summarize(rows); family_summary={}
 for cond in CONDITIONS:
  family_summary[cond]={}
  for fam in families:
   rr=[r for r in rows if r["condition"]==cond and r["family"]==fam]
   family_summary[cond][fam]={"survival_pct":round(100*metric(rr,"survived"),2),
    "mean_progress":round(metric(rr,"progress"),3),"pre_progress_rate":round(metric(rr,"pre_progress_rate"),3),
    "post_progress_rate":round(metric(rr,"post_progress_rate"),3),"mean_adaptation_lag":round(metric(rr,"adaptation_lag"),2),
    "mean_energy":round(metric(rr,"mean_energy"),2),"violation_steps":round(metric(rr,"violation_steps"),2)}
 post=[r for r in rows if r["family"]!="unseen_drift"]
 unseen=[r for r in rows if r["family"]=="unseen_drift"]
 ci={}
 for key in ["post_progress_rate","adaptation_lag","violation_steps"]:
  for other in ["A_fixed","B_reward_only","C_punishment_only","E_sham"]:
   ci[f"D_combined_vs_{other}_{key}"]=bootstrap([r for r in post if r["condition"]=="D_combined"],[r for r in post if r["condition"]==other],key,seed=8100+len(ci))
 ci["unseen_drift_D_vs_A_post_progress_rate"]=bootstrap([r for r in unseen if r["condition"]=="D_combined"],[r for r in unseen if r["condition"]=="A_fixed"],"post_progress_rate",seed=8200)
 metadata={"experiment":"Ω-SELF-008","seed_start":88000,"test_seeds_per_family":args.test_seeds,"horizon":args.horizon,
  "train_families":train_families,"test_families":families,"unseen_family":"unseen_drift","conditions":CONDITIONS,
  "primary_metrics":["post_progress_rate","adaptation_lag","violation_steps"],"feedback_interval_steps":25,
  "status":"runner writes observed results; report interpretation must follow actual output",
  "limitations":["Hand-coded controllers, not open-ended learning","One synthetic unseen family","Synthetic environment only; no consciousness or general-intelligence claim"]}
 for name,data in [("summary.json",summary),("family_summary.json",family_summary),("confidence_intervals.json",ci),("metadata.json",metadata)]:
  (out.parent/name).write_text(json.dumps(data,indent=2))
 print(json.dumps({"summary":summary,"family_summary":family_summary,"confidence_intervals":ci,"metadata":metadata},indent=2))
if __name__=="__main__": main()
