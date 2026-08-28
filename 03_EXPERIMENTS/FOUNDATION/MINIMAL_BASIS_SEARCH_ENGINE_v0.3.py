from dataclasses import dataclass
from itertools import product

PRIMS=('D','R','W','P')
MAX_DEPTH=3

@dataclass(frozen=True)
class Term:
    kind:str
    args:tuple=()

# Neutral constructors only. No constructor is named after a target capability.
# The evaluator observes traces after execution rather than embedding T1..T7.
KINDS=('ATOM','PAIR','MAP','ITER','FILTER')

def atoms(budget):
    return [Term('ATOM',(p,)) for p in sorted(budget)]

def gen_terms(budget, depth):
    if depth==1: return atoms(budget)
    prev=gen_terms(budget, depth-1)
    out=list(prev)
    for k in KINDS[1:]:
        for a in prev: out.append(Term(k,(a,)))
        for a,b in product(prev, repeat=2): out.append(Term(k,(a,b)))
    seen=set(); r=[]
    for t in out:
        if t not in seen: seen.add(t); r.append(t)
    return r

def primitive_closure(t):
    if t.kind=='ATOM': return frozenset((t.args[0],))
    s=set()
    for a in t.args:s.update(primitive_closure(a))
    return frozenset(s)

def eval_term(t, env=None, fuel=8):
    if fuel<=0:return ()
    if t.kind=='ATOM': return (('atom',t.args[0]),)
    traces=[]
    for a in t.args: traces.extend(eval_term(a,env,fuel-1))
    if t.kind=='PAIR': return tuple(traces)+(('pair',len(t.args)),)
    if t.kind=='MAP': return tuple(traces)+(('map',len(t.args)),)
    if t.kind=='FILTER': return tuple(traces)+(('filter',len(t.args)),)
    if t.kind=='ITER': return tuple(traces)+(('iter',len(t.args)),)
    return tuple(traces)

def signatures(trace):
    # Purely observational signatures; no target-capability names.
    tags=[x[0] for x in trace]
    return {
      'branch_like': tags.count('filter')>0,
      'successor_like': tags.count('map')>0,
      'retained_like': tags.count('pair')>0 and len(trace)>1,
      'repeat_like': tags.count('iter')>0,
      'composed_like': len(set(tags))>1,
    }

def search(budget):
    seen={}
    for d in range(1,MAX_DEPTH+1):
        for t in gen_terms(budget,d):
            tr=eval_term(t)
            for sig,v in signatures(tr).items():
                if v and sig not in seen: seen[sig]=(d,t,primitive_closure(t),tr)
    return seen

if __name__=='__main__':
    for k in range(5):
        from itertools import combinations
        for b in combinations(PRIMS,k):
            r=search(b)
            print('budget=', ''.join(b) or 'EMPTY','signatures=',sorted(r))
