#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np

def generate(model, n, seed):
    rng=np.random.default_rng(seed); x=np.empty(n,dtype=int); x[0]=0
    if model=='M1':
        for i in range(n-1): x[i+1]=1-x[i]
    elif model=='M2':
        for i in range(n-1): x[i+1]=x[i] if rng.random()<0.8 else 1-x[i]
    elif model=='M3':
        for i in range(n-1):
            p=0.9 if i < n//2 else 0.6
            x[i+1]=x[i] if rng.random()<p else 1-x[i]
    return x

def probs(train_x, train_y, regimes=None, eps=1e-9):
    if regimes is None:
        counts=np.zeros((2,2));
        for a,b in zip(train_x,train_y): counts[a,b]+=1
        return (counts[:,1]+eps)/(counts.sum(1)+2*eps)
    counts=np.zeros((2,2,2))
    for a,b,r in zip(train_x,train_y,regimes): counts[r,a,b]+=1
    return (counts[:,:,1]+eps)/(counts.sum(2)+2*eps)

def score(y,p):
    p=np.clip(p,1e-12,1-1e-12)
    nll=float(np.mean(-(y*np.log(p)+(1-y)*np.log(1-p))))
    brier=float(np.mean((p-y)**2))
    return nll,brier

def one_seed(model,seed,n=5000):
    x=generate(model,n,seed); y=x[1:]; state=x[:-1]; regime=(np.arange(n-1)>=n//2).astype(int)
    # deterministic stratified split: each regime alternates train/test by local index parity
    train=np.zeros(n-1,dtype=bool)
    for r in (0,1):
        idx=np.flatnonzero(regime==r); train[idx[::2]]=True
    test=~train
    pa=probs(state[train],y[train]); pb=probs(state[train],y[train],regime[train])
    pA=pa[state[test]]; pB=pb[regime[test],state[test]]
    a=score(y[test],pA); b=score(y[test],pB)
    # shuffle regime labels only for training; test remains original
    shuf_reg=regime[train].copy(); rng=np.random.default_rng(seed+99991); rng.shuffle(shuf_reg)
    pbs=probs(state[train],y[train],shuf_reg); pBS=score(y[test],pbs[regime[test],state[test]])
    return {'seed':seed,'A_nll':a[0],'B_nll':b[0],'A_brier':a[1],'B_brier':b[1],'BminusA_nll':b[0]-a[0],'BminusA_brier':b[1]-a[1],'shuffle_B_nll':pBS[0],'shuffle_BminusA_nll':pBS[0]-a[0]}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--n',type=int,default=5000); ap.add_argument('--seeds',type=int,default=100); args=ap.parse_args()
    out={'experiment':'Omega-BASIS-002-R2','status':'EXECUTED','n':args.n,'models':{}}
    rng=np.random.default_rng(20260813); seeds=[int(v) for v in rng.integers(0,2**31-1,size=args.seeds)]
    for m in ('M1','M2','M3'):
        rows=[one_seed(m,s,args.n) for s in seeds]
        out['models'][m]={'rows':rows}
        for k in ('BminusA_nll','BminusA_brier','shuffle_BminusA_nll'):
            v=np.array([r[k] for r in rows]); out['models'][m][k]={'mean':float(v.mean()),'sd':float(v.std(ddof=1)),'min':float(v.min()),'max':float(v.max())}
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
