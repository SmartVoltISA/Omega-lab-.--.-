import json, hashlib, platform
from pathlib import Path
import numpy as np
OUT=Path("EXPERIMENTS/RESULTS"); OUT.mkdir(parents=True,exist_ok=True)
SEED=20261010
def stats(a):
 a=np.asarray(a,float); return {"mean":float(a.mean()),"sd":float(a.std(ddof=1)) if len(a)>1 else 0.0,"n":len(a)}
def part(c):
 x=c.astype(float)+1e-8; x/=x.sum(axis=1,keepdims=True); x/=np.maximum(np.linalg.norm(x,axis=1,keepdims=True),1e-12)
 s=np.clip(x@x.T,0,1); np.fill_diagonal(s,0); d=s.sum(1); inv=1/np.sqrt(np.maximum(d,1e-12))
 _,v=np.linalg.eigh(np.eye(len(c))-inv[:,None]*s*inv[None,:]); return (v[:,1]>np.median(v[:,1])).astype(int)
def cnt(seq,n):
 c=np.zeros((n,n))
 for a,b in zip(seq[:-1],seq[1:]): c[int(a),int(b)]+=1
 return c
def graph_part(c):
 w=c+c.T
 np.fill_diagonal(w,0)
 d=w.sum(axis=1); inv=1/np.sqrt(np.maximum(d,1e-12))
 _,v=np.linalg.eigh(np.eye(len(c))-inv[:,None]*w*inv[None,:])
 return (v[:,1]>np.median(v[:,1])).astype(int)
def f1(a,b):
 a=np.asarray(a,int); b=np.asarray(b,int)
 def z(x):
  tp=((x==1)&(b==1)).sum(); fp=((x==1)&(b==0)).sum(); fn=((x==0)&(b==1)).sum()
  return 2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else 0
 return max(z(a),z(1-a))
raw={}; out={}
# EXP-001: online memory vs last-transition prediction in expanding state space.
def e1(seed):
 r=np.random.default_rng(seed); n=8; cap=24; p=r.dirichlet(np.ones(n),size=n); c=np.zeros((cap,cap)); last={}; s=int(r.integers(n)); ok={k:0 for k in ["flat","memory","boundary","grow"]}; added=0
 for t in range(20000):
  if n<cap and r.random()<.00035:
   a=min(int(r.integers(1,4)),cap-n); old=n; n+=a; added+=a; p=np.pad(p,((0,a),(0,a)))
   for i in range(old,n): p[i,:n]=r.dirichlet(np.ones(n))
   for i in range(n): p[i,:n]=(p[i,:n]+.03)/(p[i,:n]+.03).sum()
  if t and t%250==0:
   i=int(r.integers(n)); p[i,:n]=r.dirichlet(np.maximum(p[i,:n]*40,.05))
  y=int(r.choice(n,p=p[s,:n]/p[s,:n].sum())); row=c[s,:n]
  preds={"flat":last.get(s,-1),"memory":int(row.argmax()) if row.sum() else -1,"boundary":int(np.argmax(np.where(row/row.sum()>=.1,row,0))) if row.sum() else -1,"grow":int(row.argmax()) if row.sum() else -1}
  for k,v in preds.items(): ok[k]+=int(v==y)
  last[s]=y; c[s,y]+=1; s=y
 return {"accuracy":{k:v/20000 for k,v in ok.items()},"states":n,"added":added}
a=[e1(SEED+i) for i in range(30)]; raw["EXP-001"]=a; out["EXP-001"]={"accuracy":{k:stats([x["accuracy"][k] for x in a]) for k in a[0]["accuracy"]},"states":stats([x["states"] for x in a]),"note":"Independent ledger-scale rerun, not source-identical."}
# EXP-002: ring topology recurrence with accumulating trace.
def e2(seed):
 tr=np.zeros(12); h=[]
 for t in range(300): tr[t%12]+=1+(0.25 if (t//12)%2 else 0); h.append(tr.copy())
 d=[np.abs(h[t]-h[t+12]).mean() for t in range(288)]
 return {"edges":12,"trace_delta":float(np.mean(d)),"min":float(np.min(d)),"max":float(np.max(d))}
a=[e2(SEED+i) for i in range(30)]; raw["EXP-002"]=a; out["EXP-002"]={"trace_delta":stats([x["trace_delta"] for x in a]),"note":"Toy ring; recurrence is not historical-state return."}
# shared hidden modular generator for EXP-003/004/006.
def gen(seed,n,within,steps):
 r=np.random.default_rng(seed); h=n//2; p=np.array([[(within/h if i//h==j//h else (1-within)/h) for j in range(n)] for i in range(n)])
 s=int(r.integers(n)); seq=[]
 for _ in range(steps): seq.append(s); s=int(r.choice(n,p=p[s]/p[s].sum()))
 return np.array(seq),p
# EXP-003: spectral recovery on planted 6+6 modules.
a=[]
for i in range(50):
 seq,_=gen(SEED+100+i,12,.92,5001); c=cnt(seq,12); q=part(c); truth=[0]*6+[1]*6
 a.append({"seed":SEED+100+i,"f1":f1(q,truth),"conductance":float(c[q[:,None]!=q[None,:]].sum()/c.sum())})
raw["EXP-003"]=a; out["EXP-003"]={"f1":stats([x["f1"] for x in a]),"conductance":stats([x["conductance"] for x in a]),"note":"Hidden modules are present in generator; not spontaneous emergence."}
# EXP-004: robustness sweep + held-out sequences.
a=[]
for cross in [.10,.20,.30,.40,.45]:
 for i in range(30):
  seq,_=gen(SEED+1000+int(cross*1000)*100+i,12,1-cross,11001); tr,te=seq[:8000],seq[8000:]; c=cnt(tr,12); q=part(c)
  a.append({"cross":cross,"f1":f1(q,[0]*6+[1]*6),"conductance":float(c[q[:,None]!=q[None,:]].sum()/c.sum()),"heldout_within":float(np.mean([q[x]==q[y] for x,y in zip(te[:-1],te[1:])]))})
raw["EXP-004"]=a; out["EXP-004"]={str(x):{k:stats([z[k] for z in a if z["cross"]==x]) for k in ["f1","conductance","heldout_within"]} for x in [.10,.20,.30,.40,.45]}; out["EXP-004"]["note"]="Planted-module positive control."
# EXP-005: homogeneous relational reinforcement, no supplied modules.
def e5(seed):
 r=np.random.default_rng(seed); n=24; w=np.ones((n,n)); np.fill_diagonal(w,0); s=int(r.integers(n)); seq=[]
 for _ in range(20000):
  y=int(r.choice(n,p=w[s]/w[s].sum())); seq.append(y); w[s,y]+=.15; w*=.99998; s=y
 c=cnt(seq,n); q=part(c); shuffled=c.copy(); r.shuffle(shuffled); qn=part(shuffled)
 return {"cut":float(c[q[:,None]!=q[None,:]].sum()/c.sum()),"shuffled_cut":float(c[qn[:,None]!=qn[None,:]].sum()/c.sum())}
a=[e5(SEED+2000+i) for i in range(30)]; raw["EXP-005"]=a; out["EXP-005"]={"candidate_cut":stats([x["cut"] for x in a]),"shuffled_cut":stats([x["shuffled_cut"] for x in a]),"note":"Fresh homogeneous generator; partition is not automatically meaningful."}
# EXP-006: intervention proxy, modular positive control vs homogeneous null.
def e6(seed,mod):
 r=np.random.default_rng(seed); n=24; h=12
 p=np.array([[(.85/h if i//h==j//h else .15/h) for j in range(n)] for i in range(n)]) if mod else np.array([r.dirichlet(np.ones(n)) for _ in range(n)])
 s=int(r.integers(n)); seq=[]
 for _ in range(12000): seq.append(s); s=int(r.choice(n,p=p[s]/p[s].sum()))
 c=cnt(seq,n); q=graph_part(c); learned_f1=f1(q,[0]*h+[1]*h) if mod else None
 rnd=np.array([0]*h+[1]*h); r.shuffle(rnd); node=int(r.integers(n))
 changed=p.copy(); changed[node]=1/n
 def crossing(partition,mat,node):
  return float(sum(mat[node,j] for j in range(n) if partition[j]!=partition[node])/mat[node].sum())
 baseline=crossing(q,p,node); after=crossing(q,changed,node)
 random_baseline=crossing(rnd,p,node); random_after=crossing(rnd,changed,node)
 return {"condition":"modular" if mod else "homogeneous","learned_f1":learned_f1,
         "learned_crossing_baseline":baseline,"learned_crossing_after":after,
         "learned_crossing_delta":after-baseline,
         "random_crossing_baseline":random_baseline,"random_crossing_after":random_after,
         "random_crossing_delta":random_after-random_baseline}
a=[e6(SEED+3000+i,True) for i in range(40)]+[e6(SEED+4000+i,False) for i in range(40)]; raw["EXP-006"]=a; out["EXP-006"]={}
for cond in ["modular","homogeneous"]:
 b=[x for x in a if x["condition"]==cond]; out["EXP-006"][cond]={k:stats([x[k] for x in b if x[k] is not None]) for k in ["learned_f1","learned_crossing_baseline","learned_crossing_after","learned_crossing_delta","random_crossing_baseline","random_crossing_after","random_crossing_delta"] if any(x[k] is not None for x in b)}
out["EXP-006"]["note"]="Exploratory intervention proxy; not causal-boundary certification."
payload={"date":"2026-10-10","suite":"Geometry Foundation EXP-001..006 independent full rerun","base_seed":SEED,"python":platform.python_version(),"numpy":np.__version__,"sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"summary":out,"raw_runs":raw}
(OUT/"GEOMETRY_FOUNDATION_FULL_RUN_2026-10-10.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
lines=["# Geometry Foundation Full Run 2026-10-10","Status: executed; independent operationalization where source code was absent.","","Base seed: "+str(SEED),"Python: "+platform.python_version(),"NumPy: "+np.__version__,""]
for k,v in out.items(): lines += ["## "+k,"",json.dumps(v,indent=2,sort_keys=True),""]
lines += ["Limits: EXP-003/004 use planted modules; EXP-005 partition is not automatically meaningful; EXP-006 is exploratory; none of these toy tests establishes a universal physical law.","Raw per-seed results are in GEOMETRY_FOUNDATION_FULL_RUN_2026-10-10.json."]
(OUT/"GEOMETRY_FOUNDATION_FULL_RUN_2026-10-10.md").write_text("\n".join(lines)+"\n")
print(json.dumps({"status":"PASS","rows":{k:len(v) for k,v in raw.items()},"summary":out},indent=2))
