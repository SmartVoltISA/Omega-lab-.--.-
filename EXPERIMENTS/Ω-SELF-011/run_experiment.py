#!/usr/bin/env python3
"""Ω-SELF-011: consequence-aware probing, uncertainty, and model revision."""
import argparse, csv, json, math, random, statistics
from pathlib import Path

CONDS=['A_no_memory','B_surface_replay','C_similarity_probe','D_uncertainty_revision','E_random_probe','F_model_only']
FAMILIES=['hot_surface','pressurized_vessel','unseen_electrical']
PARAMS={'hot_surface':(1.0,0.0,.05),'pressurized_vessel':(.72,.18,.07),'unseen_electrical':(.61,.25,.085)}
def clip(x,lo=0.,hi=1.): return max(lo,min(hi,x))
def episode(seed,cond,family,steps=140):
 rng=random.Random(seed); scale,offset,noise=PARAMS[family]
 latent=clip(.38+rng.gauss(0,.09)); model_scale=1.0; model_offset=0.0; uncertainty=.34
 score=0.; incidents=0; probes=0; work=0; revisions=0; prediction_errors=[]; calib=[]
 # The first 12 steps are safe calibration opportunities; no harmful contact occurs.
 for t in range(steps):
  latent=clip(latent+rng.gauss(0,.035)+(rng.choice([-.12,.16]) if rng.random()<.04 else 0))
  cue=clip(scale*latent+offset+rng.gauss(0,noise))
  if t<12:
   observed=clip(latent+rng.gauss(0,.035)); calib.append((cue,observed)); probes+=1; score-=.12
   if len(calib)>=3:
    # Fit a simple affine cue transform by least squares from non-injurious calibration data.
    xs=[x for x,y in calib]; ys=[y for x,y in calib]
    xm=statistics.mean(xs); ym=statistics.mean(ys)
    den=sum((x-xm)**2 for x in xs)
    if den>1e-6:
     new_scale=sum((x-xm)*(y-ym) for x,y in calib)/den
     new_offset=ym-new_scale*xm
     if cond in ('D_uncertainty_revision','F_model_only'):
      model_scale=max(.2,min(2.0,new_scale)); model_offset=max(-.4,min(.6,new_offset))
   continue
  if cond=='A_no_memory': estimate=cue; u=.4; action='touch'
  elif cond=='B_surface_replay':
   estimate=cue; u=.25; action='avoid' if cue>.62 else 'touch'
  elif cond=='C_similarity_probe':
   estimate=cue; u=.3; action='probe' if cue>.48 else 'touch'
  elif cond in ('D_uncertainty_revision','F_model_only'):
   estimate=clip(model_scale*cue+model_offset); u=uncertainty
   if cond=='D_uncertainty_revision' and (u>.19 or estimate>.53): action='probe'
   elif cond=='F_model_only': action='avoid' if estimate>.62 else 'touch'
   else: action='avoid' if estimate>.58 else 'touch'
  else:
   estimate=cue; u=.35; action='probe' if rng.random()<.34 else 'touch'
  predicted=estimate
  if action=='probe':
   probes+=1; obs=clip(latent+rng.gauss(0,.04)); err=abs(obs-predicted); prediction_errors.append(err)
   score-=.12
   if cond=='D_uncertainty_revision':
    # Revise mapping when prediction misses the observation; bounded online affine correction.
    residual=obs-predicted
    if err>.10:
     revisions+=1
     model_offset=clip(model_offset+.20*residual,-.4,.6)
     model_scale=clip(model_scale+.04*residual*(cue-.5),.2,2.0)
    uncertainty=clip(.78*uncertainty+.22*err,.025,.5)
   elif cond=='F_model_only':
    uncertainty=clip(.96*uncertainty+.04*err,.025,.5)
   if obs>.58: action='avoid'
   else: action='touch'
  if action=='avoid':
   score-=.18
  elif action=='touch':
   work+=1
   if latent>.58:
    incidents+=1; score-=2.0
    # Direct-contact outcome updates the model only in D; no direct-contact update for other variants.
    if cond=='D_uncertainty_revision':
     residual=latent-predicted
     revisions+=1
     model_offset=clip(model_offset+.12*residual,-.4,.6)
     uncertainty=clip(uncertainty+.06,.025,.5)
   else: score+=1.
  # Reward model accuracy after every safe observation, never using hidden latent as an observation.
 model_error=abs(clip(model_scale*cue+model_offset)-latent)
 return {'condition':cond,'family':family,'seed':seed,'score':score,'incidents':incidents,'work_actions':work,'probe_count':probes,'probe_rate':probes/steps,'revisions':revisions,'prediction_error':statistics.mean(prediction_errors) if prediction_errors else 0.,'final_model_error':model_error,'uncertainty_final':uncertainty,'final_risk':latent}
def avg(rows,k): return statistics.mean(r[k] for r in rows)
def ci_pair(a,b,key,n=4000,seed=1111):
 rng=random.Random(seed); m=min(len(a),len(b)); ds=[]
 for _ in range(n): ds.append(statistics.mean(a[i][key]-b[i][key] for i in (rng.randrange(m) for _ in range(m))))
 ds.sort(); return {'difference':round(avg(a,key)-avg(b,key),4),'ci95':[round(ds[int(.025*n)],4),round(ds[min(n-1,int(.975*n))],4)],'resamples':n}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--seeds',type=int,default=240); ap.add_argument('--steps',type=int,default=140); ap.add_argument('--out',default='results.csv'); args=ap.parse_args()
 rows=[]
 for ci,c in enumerate(CONDS):
  for fi,f in enumerate(FAMILIES):
   for s in range(args.seeds): rows.append(episode(1101100+ci*100000+fi*10000+s,c,f,args.steps))
 out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('w',newline='') as fp:
  w=csv.DictWriter(fp,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
 summary={}; family={}
 keys=['score','incidents','work_actions','probe_count','probe_rate','revisions','prediction_error','final_model_error','uncertainty_final','final_risk']
 for c in CONDS:
  rr=[r for r in rows if r['condition']==c]
  summary[c]={k:round(avg(rr,k),4) for k in keys}
  family[c]={}
  for f in FAMILIES:
   fr=[r for r in rr if r['family']==f]
   family[c][f]={k:round(avg(fr,k),4) for k in keys}
 held=[r for r in rows if r['family']=='unseen_electrical']; ci={}
 for baseline in ['A_no_memory','B_surface_replay','C_similarity_probe','E_random_probe','F_model_only']:
  for k in ['score','incidents','final_model_error']:
   ci[f'D_uncertainty_revision_vs_{baseline}_{k}']=ci_pair([r for r in held if r['condition']=='D_uncertainty_revision'],[r for r in held if r['condition']==baseline],k,seed=1120+len(ci))
 meta={'experiment':'Ω-SELF-011','seeds_per_condition_family':args.seeds,'steps_per_episode':args.steps,'conditions':CONDS,'families':FAMILIES,'held_out_family':'unseen_electrical','calibration_steps':12,'primary_metrics':['incidents','score','probe_rate','final_model_error','final_risk'],'safety_note':'harmful actions occur only inside the simulator; calibration probes are non-injurious','limitations':['Synthetic environment and hand-coded policies','Simple affine model','One held-out family','No claim of consciousness or general intelligence']}
 for name,data in [('summary.json',summary),('family_summary.json',family),('confidence_intervals.json',ci),('metadata.json',meta)]: (out.parent/name).write_text(json.dumps(data,indent=2))
 print(json.dumps({'summary':summary,'family_summary':family,'confidence_intervals':ci,'metadata':meta},indent=2))
if __name__=='__main__': main()
