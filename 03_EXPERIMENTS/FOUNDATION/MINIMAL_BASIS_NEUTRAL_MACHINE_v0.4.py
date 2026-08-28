from dataclasses import dataclass
from itertools import combinations, product
from hashlib import sha256

@dataclass(frozen=True)
class State:
    tape: tuple
    pc: int
    regs: tuple

@dataclass(frozen=True)
class Rule:
    src: int
    read: int
    dst: int
    write: int
    move: int

# Fully neutral machine. Primitive labels are data only; no capability names.
# A program is a finite rule table over binary symbols.

def step(s, rules):
    key=(s.pc, s.tape[s.pc % len(s.tape)])
    rs=[r for r in rules if (r.src,r.read)==key]
    if not rs:return None
    r=rs[0]
    tape=list(s.tape); tape[s.pc % len(tape)]=r.write
    return State(tuple(tape),(s.pc+r.move)%len(tape),s.regs)

def run(rules, tape=(0,1,0,1), limit=12):
    s=State(tuple(tape),0,())
    trace=[s]
    for _ in range(limit):
        n=step(s,rules)
        if n is None:break
        trace.append(n);s=n
    return trace

def signatures(trace):
    if not trace:return {}
    tapes=[x.tape for x in trace]
    pcs=[x.pc for x in trace]
    return {
      'difference': len(set(tapes))>1,
      'repeat_state': len(set((x.tape,x.pc) for x in trace)) < len(trace),
      'termination': len(trace)<13,
      'multiple_positions': len(set(pcs))>1,
    }

def machine_space():
    # Small exhaustive neutral search. Rule tables are encoded as data.
    rules=[]
    for src in range(2):
      for read in range(2):
       for dst in range(2):
        for write in range(2):
         for move in (-1,0,1): rules.append(Rule(src,read,dst,write,move))
    for k in (1,2):
      for rs in combinations(rules,k): yield rs

def fingerprint(trace):
    raw=';'.join(f'{s.tape}|{s.pc}' for s in trace)
    return sha256(raw.encode()).hexdigest()

if __name__=='__main__':
    counts={k:0 for k in ('difference','repeat_state','termination','multiple_positions')}
    examples={}
    total=0
    for rules in machine_space():
        total+=1
        tr=run(rules)
        sig=signatures(tr)
        for k,v in sig.items():
            if v:
                counts[k]+=1; examples.setdefault(k,(rules,fingerprint(tr),len(tr)))
    print('machines=',total)
    for k in counts:print(k,counts[k])
    for k,v in examples.items():print('example',k,v)
