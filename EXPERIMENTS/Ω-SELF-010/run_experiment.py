#!/usr/bin/env python3
"""Ω-SELF-010: model-based transfer, analogy cues, and safe probing."""
import argparse, csv, json, math, random, statistics
from pathlib import Path
CONDS=['A_no_memory','B_episode_replay','C_similarity_only','D_model_based_probe','E_random_probe']
FAMILIES=['hot_surface','pressurized_vessel','unseen_electrical']
PARAMS={'hot_surface':{'scale':1.0,'offset':0.0,'noise':.055,'base_hazard':.40},'pressurized_vessel':{'scale':.72,'offset':.18,'noise':.075,'base_hazard':.42},'unseen_electrical':{'scale':.61,'offset':.25,'noise':.085,'base_hazard':.44}}
def clip(x,a=0,b=1): return max(a,min(b,x))
def episode(seed,cond,family,steps=120):
 rng=random.Random(seed); p=PARAMS[family]; latent=clip(p['base_hazard']+rng.gauss(0,.08)); risk_model=.35; uncertainty=.38
 score=0.; incidents=0; unsafe=0; probes=0; avoided=0; model_errors=[]
 for t in range(steps):
  cue=clip(p['scale']*latent+p['offset']+rng.gauss(0,p['noise']))
  if rng.random()<.09: latent=clip(latent+rng.choice([-.22,.18,.28])+rng.gauss(0,.04))
  else: latent=clip(latent+rng.gauss(0,.025))
  if cond=='D_model_based_probe': estimate=clip((cue-p['offset'])/p['scale'])
  else: estimate=cue
  uncertain=abs(estimate-risk_model)>.15 or uncertainty>.22
  if cond=='A_no_memory': action='touch'
  elif cond=='B_episode_replay': action='avoid' if cue>.62 else 'touch'
  elif cond=='C_similarity_only': action='probe' if cue>.50 else 'touch'
  elif cond=='D_model_based_probe': action='probe' if uncertain else ('avoid' if estimate>.58 else 'touch')
  else: action='probe' if rng.random()<.35 else 'touch'
  if action=='probe':
   probes+=1; observed=clip(latent+rng.gauss(0,.045)); error=abs(observed-estimate); model_errors.append(error)
   risk_model=.72*risk_model+.28*observed; uncertainty=max(.035,uncertainty*.78+error*.12); score+=.30
   if observed>.58: avoided+=1
  elif action=='avoid': avoided+=1; score-=.12; uncertainty=min(.5,uncertainty+.015)
  else:
   if latent>.58:
    incidents+=1; unsafe+=1; score-=2.2
    if cond in ('B_episode_replay','C_similarity_only','D_model_based_probe'):
     risk_model=.8*risk_model+.2*latent; uncertainty=max(.03,uncertainty*.88)
   else: score+=1.0
 model_error=abs(risk_model-latent)
 return {'condition':cond,'family':family,'seed':seed,'score':score,'incidents':incidents,'unsafe_actions':unsafe,'probe_count':probes,'avoid_count':avoided,'probe_rate':probes/steps,'model_error':model_error,'uncertainty_final':uncertainty,'final_latent_risk':latent}
def mean(rows,k): return statistics.mean(r[k] for r in rows)
def paired_ci(a,b,key,n=4000,seed=1010):
 rng=random.Random(seed); d=[]; m=min(len(a),len(b))
 for _ in range(n): d.append(statistics.mean(a[i][key]-b[i][key] for i in (rng.randrange(m) for _ in range(m))))
 d.sort(); return {'difference':round(mean(a,key)-mean(b,key),4),'ci95':[round(d[int(.025*n)],4),round(d[min(n-1,int(.975*n))],4)],'resamples':n}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--seeds',type=int,default=240); ap.add_argument('--steps',type=int,default=120); ap.add_argument('--out',default='results.csv'); args=ap.parse_args()
 rows=[]
 for ci,c in enumerate(CONDS):
  for fi,f in enumerate(FAMILIES):
   for s in range(args.seeds): rows.append(episode(1010000+ci*100000+fi*10000+s,c,f,args.steps))
 out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('w',newline='') as fp:
  w=csv.DictWriter(fp,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
 summary={}; family={}
 for c in CONDS:
  rr=[r for r in rows if r['condition']==c]
  summary[c]={k:round(mean(rr,k),4) for k in ['score','incidents','unsafe_actions','probe_count','probe_rate','model_error','uncertainty_final']}
  family[c]={}
  for f in FAMILIES:
   fr=[r for r in rr if r['family']==f]
   family[c][f]={k:round(mean(fr,k),4) for k in ['score','incidents','probe_rate','model_error','uncertainty_final']}
 held=[r for r in rows if r['family']=='unseen_electrical']; ci={}
 for baseline in ['A_no_memory','B_episode_replay','C_similarity_only','E_random_probe']:
  for k in ['score','incidents','model_error']:
   ci[f'D_model_based_probe_vs_{baseline}_{k}']=paired_ci([r for r in held if r['condition']=='D_model_based_probe'],[r for r in held if r['condition']==baseline],k,seed=1020+len(ci))
 meta={'experiment':'Ω-SELF-010','seeds_per_condition_family':args.seeds,'steps_per_episode':args.steps,'conditions':CONDS,'families':FAMILIES,'held_out_family':'unseen_electrical','primary_metrics':['incidents','score','model_error','probe_rate'],'design':'safe probes provide non-injurious evidence; direct-contact harms are simulated; family cue scales differ','limitations':['Synthetic environment; manually specified cue transforms','Model-based condition receives the correct family transform, so this is an oracle-normalization benchmark, not autonomous discovery','One held-out family; no evidence of general intelligence or consciousness']}
 for name,data in [('summary.json',summary),('family_summary.json',family),('confidence_intervals.json',ci),('metadata.json',meta)]: (out.parent/name).write_text(json.dumps(data,indent=2))
 print(json.dumps({'summary':summary,'family_summary':family,'confidence_intervals':ci,'metadata':meta},indent=2))
if __name__=='__main__': main()
