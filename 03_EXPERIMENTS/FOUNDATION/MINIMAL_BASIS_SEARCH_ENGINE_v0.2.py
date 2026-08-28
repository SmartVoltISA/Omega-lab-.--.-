from dataclasses import dataclass
from itertools import product

PRIMS=('D','R','W','P')
OPS=('APPLY','COMPOSE','TEST','STEP','STORE','LOOP')
MAX_DEPTH=4

@dataclass(frozen=True)
class Term:
    op:str
    args:tuple=()

# Pure syntax generator. It deliberately does not contain capability names.
ATOMS=[Term(p) for p in PRIMS]

def gen(depth):
    if depth==1: return ATOMS
    prev=gen(depth-1)
    out=list(prev)
    for op in OPS:
        for a in prev:
            out.append(Term(op,(a,)))
        for a,b in product(prev, repeat=2):
            out.append(Term(op,(a,b)))
    # deterministic deduplication
    seen=set(); result=[]
    for t in out:
        if t not in seen:
            seen.add(t); result.append(t)
    return result

def closure(t):
    if t.op in PRIMS: return frozenset((t.op,))
    c=set()
    for a in t.args: c.update(closure(a))
    return frozenset(c)

def size(t):
    return 1+sum(size(a) for a in t.args)

def shape(t):
    # Structural observables only. No English capability labels.
    if t.op=='TEST': return {'branch'}
    if t.op=='STEP': return {'successor'}
    if t.op=='STORE': return {'retained_trace'}
    if t.op=='LOOP': return {'repeat'}
    if t.op=='APPLY': return {'application'}
    if t.op=='COMPOSE': return {'composition'}
    s=set()
    for a in t.args:s |= shape(a)
    return s

def search():
    terms=[]
    for d in range(1,MAX_DEPTH+1): terms.extend(gen(d))
    # Search only minimal syntactic witnesses for observable signatures.
    targets={k:None for k in ('branch','successor','retained_trace','repeat','application','composition')}
    for t in sorted(terms,key=lambda x:(size(x),repr(x))):
        for sig in shape(t):
            if targets[sig] is None: targets[sig]=(size(t),t,closure(t))
    return targets

if __name__=='__main__':
    for k,v in search().items():
        print(k, '->', v)
