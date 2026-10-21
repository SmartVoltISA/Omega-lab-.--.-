#!/usr/bin/env python3
"""Ω-SELF-004: bounded random policy search with held-out evaluation.
Requires numpy and pandas. Synthetic control experiment; not a consciousness test.
"""
import argparse,json
import numpy as np
import pandas as pd
FAMILIES=['rapid_changes','slow_changes','surprise_shift','stable']
def make_env(seed,family,horizon):
 r=np.random.default_rng(seed); z=np.zeros(horizon,dtype=int); state=int(r.integers(0,2))
 if family in (0,1):
  step=int(r.integers(35,80) if family==0 else r.integers(100,180))
  for t in range(horizon):
   if t>=step:
    state=1-state; step=t+int(r.integers(35,80) if family==0 else r.integers(100,180))
   z[t]=state
 elif family==2:
  shift=int(r.integers(180,420)); z[:]=state; z[shift:]=1-state
 else: z[:]=state
 return {'regime':z,'obs':r.normal(0,10,horizon),'forage':r.normal(0,4,horizon),'rest':r.normal(0,1,horizon),'conserve':r.normal(0,1.8,horizon),'cue':(z+r.normal(0,1,horizon))>0.6,'high':[11.,10.,12.,9.][family],'low':[3.5,4.5,2.5,5.][family],'initial':[42.,45.,38.,48.][family],'family':family}
def episode(e,policy,horizon,adaptive=False):
 energy=float(e['initial']); fatigue=.2; th,rt=map(float,policy); trace=[]
 for t in range(horizon):
  seen=float(np.clip(energy+e['obs'][t],0,100))
  if seen<rt or fatigue>.95: action='rest'
  elif seen<th: action='forage'
  elif e['cue'][t] and seen<62: action='forage'
  else: action='conserve'
  before=energy
  if action=='forage': energy+=(e['high'] if e['regime'][t]==0 else e['low'])+e['forage'][t]-6.5-2.6*fatigue; fatigue=min(1.5,fatigue+.15)
  elif action=='rest': energy+=3.5+e['rest'][t]; fatigue=max(0.,fatigue-.25)
  else: energy+=-1.2+e['conserve'][t]; fatigue=max(0.,fatigue-.04)
  energy=float(np.clip(energy,0,100)); trace.append(energy)
  if adaptive:
   if action=='forage' and energy-before < -1.5: th=max(24.,th-.35)
   if energy<24: rt=min(27.,rt+.4)
   elif energy>55 and fatigue<.25: rt=max(14.,rt-.1)
  if energy<=0: break
 a=np.asarray(trace); return {'survival_steps':len(a),'survived_full_horizon':int(len(a)==horizon),'final_energy':float(a[-1]),'mean_energy':float(a.mean()),'score':float(len(a)/horizon*.75+a.mean()/100*.25)}
def evaluate(pol,envs,horizon): return np.mean([episode(e,pol,horizon)['score'] for e in envs])
def main():
 p=argparse.ArgumentParser(); p.add_argument('--seeds',type=int,default=400); p.add_argument('--train-seeds',type=int,default=40); p.add_argument('--candidates',type=int,default=20); p.add_argument('--horizon',type=int,default=400); p.add_argument('--out',default='results.csv'); p.add_argument('--search-seed',type=int,default=404); a=p.parse_args()
 train=[make_env(100000+f*10000+i,f,a.horizon) for f in range(4) for i in range(max(1,a.train_seeds//4))]
 test=[make_env(9000000+i*13,i%4,a.horizon) for i in range(a.seeds)]
 rng=np.random.default_rng(a.search_seed); cand=[(35.,18.)]+[(float(rng.uniform(24,48)),float(rng.uniform(14,30))) for _ in range(a.candidates-1)]
 scored=[(evaluate(x,train,a.horizon),x) for x in cand]; scored.sort(key=lambda x:x[0],reverse=True); best_score,best=scored[0]
 cond={'A_fixed_baseline':((35.,18.),False),'B_handcoded_feedback':((35.,18.),True),'C_search_selected':(best,False),'D_random_candidate_control':(cand[-1],False)}
 rows=[]
 for i,e in enumerate(test):
  for name,(pol,ad) in cond.items(): rows.append(dict(condition=name,seed=i,family=FAMILIES[e['family']],policy_threshold=pol[0],policy_rest_threshold=pol[1],**episode(e,pol,a.horizon,ad)))
 d=pd.DataFrame(rows); d.to_csv(a.out,index=False)
 s=d.groupby('condition').agg(runs=('seed','count'),full_horizon_rate=('survived_full_horizon','mean'),mean_survival_steps=('survival_steps','mean'),sd_survival_steps=('survival_steps','std'),mean_final_energy=('final_energy','mean'),mean_energy=('mean_energy','mean'),mean_score=('score','mean')).reset_index(); s.to_csv(a.out.replace('.csv','_summary.csv'),index=False)
 f=d.groupby(['family','condition']).agg(full_horizon_rate=('survived_full_horizon','mean'),mean_survival_steps=('survival_steps','mean'),mean_score=('score','mean')).reset_index(); f.to_csv(a.out.replace('.csv','_families.csv'),index=False)
 meta={'experiment':'Ω-SELF-004','status':'PILOT / needs replication','search_seed':a.search_seed,'training_environment_count':len(train),'test_environment_count':len(test),'candidate_count':len(cand),'selected_policy':{'energy_threshold':best[0],'rest_threshold':best[1]},'best_training_score':best_score,'train_test_seeds_disjoint':True,'families':FAMILIES,'note':'Search algorithm is experimenter-written; this tests bounded parameter search, not spontaneous invention.'}
 with open(a.out.replace('.csv','_metadata.json'),'w') as h: json.dump(meta,h,indent=2)
 print('selected',best,'training score',best_score); print(s.to_string(index=False)); print(f.to_string(index=False))
if __name__=='__main__': main()
