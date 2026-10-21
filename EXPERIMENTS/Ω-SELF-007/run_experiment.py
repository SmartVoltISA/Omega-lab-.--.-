#!/usr/bin/env python3
"""Omega SELF-007: two-signal reward/punishment with outcome feedback."""
import argparse, csv, json, random, statistics
from pathlib import Path
FAMILIES={
 'rapid': {'shift':65,'pre':1.0,'post':0.62,'drift':0.0,'noise':0.12},
 'slow': {'shift':145,'pre':0.94,'post':0.76,'drift':0.0,'noise':0.09},
 'surprise': {'shift':110,'pre':1.05,'post':0.48,'drift':0.0,'noise':0.14},
 'unseen_drift': {'shift':9999,'pre':0.98,'post':0.98,'drift':0.0018,'noise':0.11},
}
def episode(family, seed, horizon, condition):
    rng=random.Random(seed); cfg=FAMILIES[family]
    energy,stress,progress=65.0,0.0,0.0
    survived_steps=0; energy_sum=0.0; work_steps=0
    energy_threshold=23.0; stress_limit=17.0
    recent_reward=[]; recent_punishment=[]
    for t in range(horizon):
        regime=cfg['pre'] if t<cfg['shift'] else cfg['post']
        regime=max(0.30,regime-cfg['drift']*t)
        action='rest' if energy<energy_threshold or stress>stress_limit else 'work'
        if action=='work':
            gain=max(0.0,1.65*regime+rng.gauss(0,cfg['noise']))
            progress+=gain; energy-=2.0+rng.gauss(0,cfg['noise']*0.35)
            stress+=1.20+rng.gauss(0,0.10); work_steps+=1
        else:
            gain=0.0; energy+=2.4+rng.gauss(0,cfg['noise']*0.40); stress-=2.0
        energy=min(100.0,max(0.0,energy)); stress=min(50.0,max(0.0,stress))
        reward=gain
        punishment=max(0.0,18.0-energy)*0.15+max(0.0,stress-20.0)*0.25
        if energy<10.0: punishment+=1.5
        recent_reward.append(reward); recent_punishment.append(punishment)
        if len(recent_reward)>25: recent_reward.pop(0); recent_punishment.pop(0)
        survived_steps+=1; energy_sum+=energy
        if energy<=0.0 or stress>=35.0: break
        if condition in ('B_reward_only','D_whip_and_carrot') and (t+1)%25==0:
            r=statistics.mean(recent_reward); p=statistics.mean(recent_punishment)
            if condition=='B_reward_only':
                energy_threshold=max(8.0,min(45.0,energy_threshold+(0.7 if r>0.9 else -1.0)))
                stress_limit=max(10.0,min(28.0,stress_limit+(0.3 if r>0.9 else -0.4)))
            else:
                energy_threshold=max(12.0,min(48.0,energy_threshold+(0.7 if p>0.25 else (-0.8 if r<0.85 else 0.15))))
                stress_limit=max(10.0,min(25.0,stress_limit+(1.0 if p<0.10 and r>0.85 else (-1.5 if p>0.25 else 0.0))))
        elif condition=='C_punishment_only' and (t+1)%25==0:
            p=statistics.mean(recent_punishment)
            energy_threshold=max(18.0,min(48.0,energy_threshold+(1.5 if p>0.20 else -0.1)))
            stress_limit=max(9.0,min(20.0,stress_limit+(-1.5 if p>0.20 else 0.2)))
        elif condition=='E_sham_feedback' and (t+1)%25==0:
            energy_threshold=max(8.0,min(48.0,energy_threshold+(0.8 if (t//25)%2==0 else -0.8)))
            stress_limit=max(10.0,min(25.0,stress_limit+(-0.6 if (t//25)%2==0 else 0.6)))
    return {'survived':int(survived_steps==horizon),'steps':survived_steps,'progress':progress,
            'mean_energy':energy_sum/max(1,survived_steps),'final_energy':energy,'work_fraction':work_steps/max(1,survived_steps)}
def eval_condition(name,families,seeds,horizon):
    out=[]
    for fam in families:
        offset=sum((i+1)*ord(c) for i,c in enumerate(fam))*100000
        for seed in seeds: out.append({'condition':name,'family':fam,'seed':seed+offset,**episode(fam,seed+offset,horizon,name)})
    return out
def score(rows):
    return .70*(statistics.mean(r['progress'] for r in rows)/250.0)+.20*statistics.mean(r['survived'] for r in rows)+.10*(statistics.mean(r['mean_energy'] for r in rows)/100.0)
def summarize(rows):
    result={}
    for name in sorted(set(r['condition'] for r in rows)):
        rr=[r for r in rows if r['condition']==name]
        result[name]={'episodes':len(rr),'full_survival_pct':round(100*statistics.mean(r['survived'] for r in rr),2),
          'mean_survival_steps':round(statistics.mean(r['steps'] for r in rr),2),'mean_task_progress':round(statistics.mean(r['progress'] for r in rr),2),
          'mean_energy':round(statistics.mean(r['mean_energy'] for r in rr),2),'final_energy':round(statistics.mean(r['final_energy'] for r in rr),2),
          'work_fraction':round(statistics.mean(r['work_fraction'] for r in rr),3),'descriptive_score':round(score(rr),5)}
    return result
def bootstrap(a,b,n=3000,seed=7007,key='progress'):
    rng=random.Random(seed); m=min(len(a),len(b)); diffs=[]
    for _ in range(n):
        ix=[rng.randrange(m) for _ in range(m)]
        diffs.append(statistics.mean(a[i][key]-b[i][key] for i in ix))
    diffs.sort()
    return {'mean_difference':round(statistics.mean(x[key] for x in a)-statistics.mean(x[key] for x in b),3),
            'paired_bootstrap_95_ci':[round(diffs[int(.025*n)],3),round(diffs[min(n-1,int(.975*n))],3)],'resamples':n}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--test-seeds',type=int,default=60); ap.add_argument('--horizon',type=int,default=250); ap.add_argument('--out',default='results.csv'); args=ap.parse_args()
    test_fams=['rapid','slow','surprise','unseen_drift']; conditions=['A_fixed','B_reward_only','C_punishment_only','D_whip_and_carrot','E_sham_feedback']
    seeds=list(range(81000,81000+args.test_seeds)); rows=[]
    for name in conditions: rows+=eval_condition(name,test_fams,seeds,args.horizon)
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['condition','family','seed','survived','steps','progress','mean_energy','final_energy','work_fraction']); w.writeheader(); w.writerows(rows)
    summary=summarize(rows); families={}
    for name in conditions:
        families[name]={}
        for fam in test_fams:
            rr=[r for r in rows if r['condition']==name and r['family']==fam]
            families[name][fam]={'full_survival_pct':round(100*statistics.mean(r['survived'] for r in rr),2),
              'mean_task_progress':round(statistics.mean(r['progress'] for r in rr),2),'mean_energy':round(statistics.mean(r['mean_energy'] for r in rr),2),
              'work_fraction':round(statistics.mean(r['work_fraction'] for r in rr),3)}
    primary={name:[r for r in rows if r['condition']==name] for name in conditions}
    ci={'D_vs_A_progress':bootstrap(primary['D_whip_and_carrot'],primary['A_fixed'],seed=7011),
        'D_vs_B_progress':bootstrap(primary['D_whip_and_carrot'],primary['B_reward_only'],seed=7012),
        'D_vs_C_progress':bootstrap(primary['D_whip_and_carrot'],primary['C_punishment_only'],seed=7013)}
    metadata={'experiment':'Ω-SELF-007','seed':81000,'test_families':test_fams,'unseen_family':'unseen_drift','test_seeds_per_family':args.test_seeds,
      'horizon':args.horizon,'conditions':conditions,'reward_signal':'incremental useful task progress','punishment_signal':'low-energy and high-stress penalties',
      'feedback_interval_steps':25,'initial_thresholds_shared':True,'method':'hand-coded feedback-rule comparison; not open-ended learning',
      'limitations':['Toy hand-coded environment and controllers','Only one designed unseen family','All conditions reached 100% survival','Not evidence of consciousness or general intelligence']}
    for name,data in [('summary.json',summary),('family_summary.json',families),('confidence_intervals.json',ci),('metadata.json',metadata)]:
        (out.parent/name).write_text(json.dumps(data,indent=2))
    print(json.dumps({'primary_summary':{k:summary[k] for k in conditions},'family_summary':families,'confidence_intervals':ci,'metadata':metadata},indent=2))
if __name__=='__main__': main()
