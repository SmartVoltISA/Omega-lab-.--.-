from dataclasses import dataclass
from itertools import combinations
from hashlib import sha256

@dataclass(frozen=True)
class State:
    tape: tuple
    head: int
    control: int

@dataclass(frozen=True)
class Rule:
    src: int
    read: int
    dst: int
    write: int
    move: int

# Neutral finite machine: control state and tape-head position are separate.
# No target capability is encoded in the transition semantics.
def step(s, rules):
    read=s.tape[s.head % len(s.tape)]
    rs=[r for r in rules if (r.src, r.read)==(s.control, read)]
    if not rs: return None
    r=rs[0]
    tape=list(s.tape)
    tape[s.head % len(tape)]=r.write
    return State(tuple(tape), (s.head+r.move)%len(tape), r.dst)

def run(rules, tape=(0,1,0,1), limit=12):
    s=State(tuple(tape),0,0)
    trace=[s]
    for _ in range(limit):
        n=step(s,rules)
        if n is None: break
        trace.append(n); s=n
    return trace

def signatures(trace):
    states={(x.tape,x.head,x.control) for x in trace}
    return {
        'difference': len({x.tape for x in trace})>1,
        'repeat_state': len(states)<len(trace),
        'termination': len(trace)<13,
        'multiple_positions': len({x.head for x in trace})>1,
        'multiple_control': len({x.control for x in trace})>1,
    }

def machine_space():
    rules=[Rule(src,read,dst,write,move)
           for src in range(2) for read in range(2)
           for dst in range(2) for write in range(2)
           for move in (-1,0,1)]
    for k in (1,2):
        yield from combinations(rules,k)

def fingerprint(trace):
    raw=';'.join(f'{s.tape}|{s.head}|{s.control}' for s in trace)
    return sha256(raw.encode()).hexdigest()

if __name__=='__main__':
    counts={k:0 for k in ('difference','repeat_state','termination','multiple_positions','multiple_control')}
    examples={}; total=0
    for rules in machine_space():
        total+=1; tr=run(rules); sig=signatures(tr)
        for k,v in sig.items():
            if v:
                counts[k]+=1
                examples.setdefault(k,(rules,fingerprint(tr),len(tr)))
    print('machines=',total)
    for k in counts: print(k,counts[k])
    for k,v in examples.items(): print('example',k,v)
