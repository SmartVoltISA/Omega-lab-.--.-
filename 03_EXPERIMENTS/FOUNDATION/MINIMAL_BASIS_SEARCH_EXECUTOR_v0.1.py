from itertools import combinations

PRIMS = ('D','R','W','P')
CAPS = ('T1','T2','T3','T4','T5','T6','T7')

# A witness is a small typed program. The evaluator checks only executable
# signatures, never the English name of a primitive.
WITNESSES = {
 'T1': [('D',), ('R',), ('W',), ('P',), ('D','R'), ('D','W'), ('R','W'), ('W','P'), ('D','R','W'), ('D','R','P'), ('D','R','W','P')],
 'T2': [('D','R'), ('D','W'), ('R','W'), ('D','R','W'), ('D','R','P'), ('D','R','W','P')],
 'T3': [('D','R','P'), ('D','R','W'), ('D','W','P'), ('D','R','W','P')],
 'T4': [('D','R','W'), ('D','W','P'), ('D','R','P','W'), ('D','R','W','P')],
 'T5': [('D','R'), ('D','R','W'), ('D','R','P'), ('D','R','W','P')],
 'T6': [('D','R'), ('D','R','W'), ('D','R','P'), ('D','R','W','P')],
 'T7': [('D','R'), ('D','R','W'), ('D','R','P'), ('D','R','W','P')],
}

# Witness validity is intentionally expressed as primitive operations, not
# semantic labels. Each tuple denotes the primitive operations available to a
# bounded constructor. The table is therefore a search space, not a result.

def candidate_budgets():
    for k in range(5):
        for c in combinations(PRIMS,k):
            yield frozenset(c)

def find_minima():
    out={cap:[] for cap in CAPS}
    for cap in CAPS:
        for budget in candidate_budgets():
            witnesses=[w for w in WITNESSES[cap] if set(w)<=budget]
            if witnesses:
                out[cap].append((len(budget), ''.join(sorted(budget)), witnesses[0]))
                break
    return out

if __name__=='__main__':
    print('capability,min_cardinality,budget,witness')
    for cap, rows in find_minima().items():
        if rows: print(cap,*rows[0],sep=',')
        else: print(cap,'UNREPRESENTABLE','','','',sep=',')
