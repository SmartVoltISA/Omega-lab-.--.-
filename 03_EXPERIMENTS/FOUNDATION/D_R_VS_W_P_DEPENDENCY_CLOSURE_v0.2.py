from dataclasses import dataclass
from typing import FrozenSet, Tuple

@dataclass(frozen=True)
class Term:
    op: str
    args: Tuple['Term', ...] = ()
    deps: FrozenSet[str] = frozenset()

    def closure(self):
        out = set(self.deps)
        for a in self.args:
            out.update(a.closure())
        return frozenset(out)


def atom(name, primitive):
    return Term(name, deps=frozenset({primitive}))


def op(name, *args):
    return Term(name, args=tuple(args))

# Explicit constructors. No constructor silently grants distinction,
# relation, will, prohibition, state, time, or memory.
RULES = {
    'D+R': {
        'T1': lambda: op('pair', atom('a','D'), atom('b','D')),
        'T2': lambda: op('boundary', atom('inside','D'), atom('outside','D'), atom('link','R')),
        'T3': lambda: op('constraint', atom('source','R'), atom('target','R')),
        'T4': lambda: op('select', atom('candidate_set','D'), atom('criterion','R'),),
        'T5': lambda: op('transition', atom('pre','R'), atom('post','R')),
        'T6': lambda: op('trace', atom('current','R'), atom('prior','R')),
        'T7': lambda: op('cycle', atom('state_a','R'), atom('state_b','R'), atom('guard','D')),
    },
    'W+P': {
        'T1': lambda: op('pair', atom('a','W'), atom('b','W')),
        'T2': lambda: op('boundary', atom('inside','P'), atom('outside','P')),
        'T3': lambda: op('constraint', atom('target','P')),
        'T4': lambda: op('select', atom('candidate','W'), atom('restriction','P')),
        'T5': lambda: op('transition', atom('pre','W'), atom('post','P')),
        'T6': lambda: op('trace', atom('current','W'), atom('prior','P')),
        'T7': lambda: op('cycle', atom('state_a','W'), atom('state_b','P'), atom('guard','P')),
    },
}

# Required semantic resources for the target capabilities. These are not
# asserted to be metaphysical truths; they define the operational test.
REQUIRED = {
    'T1': frozenset({'D'}),
    'T2': frozenset({'D','R'}),
    'T3': frozenset({'D','R'}),
    'T4': frozenset({'D','R','W'}),
    'T5': frozenset({'D','R'}),
    'T6': frozenset({'D','R'}),
    'T7': frozenset({'D','R'}),
}

PRIMITIVES = {'D+R': frozenset({'D','R'}), 'W+P': frozenset({'W','P'})}


def classify(model, cap):
    term = RULES[model][cap]()
    used = term.closure()
    budget = PRIMITIVES[model]
    missing_from_budget = used - budget
    required_missing = REQUIRED[cap] - budget
    if missing_from_budget:
        return 'IMPORTED', used, missing_from_budget
    if not required_missing:
        return 'DIRECT', used, frozenset()
    # A construction that uses only the declared budget but lacks a capability
    # resource is only a candidate derivation; it cannot be called direct.
    return 'DERIVED_CANDIDATE', used, required_missing


def run():
    print('model,capability,status,primitive_closure,missing')
    for model in ('D+R','W+P'):
        for cap in ('T1','T2','T3','T4','T5','T6','T7'):
            status, used, missing = classify(model,cap)
            print(model,cap,status,','.join(sorted(used)),','.join(sorted(missing)),sep=',')

if __name__ == '__main__':
    run()
