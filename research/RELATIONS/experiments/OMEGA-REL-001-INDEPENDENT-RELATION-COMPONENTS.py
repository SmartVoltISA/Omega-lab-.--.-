from itertools import product

ALPHABET = (-1, 0, 1)

# Baseline: relation is completely specified by two directional response values.
states = list(product(ALPHABET, repeat=2))

# Any candidate quantity that is a function of the pair is derived, not independent.
derived = {
    "sum": lambda a, b: a + b,
    "product": lambda a, b: a * b,
    "difference": lambda a, b: a - b,
    "absolute_difference": lambda a, b: abs(a - b),
}

print("OMEGA-REL-001 BASELINE")
print("alphabet:", ALPHABET)
print("number of directional states:", len(states))
print("states:", states)

for name, fn in derived.items():
    values = {fn(*s) for s in states}
    print(f"derived {name}: {sorted(values)}")

# Controlled hidden-state extension.
# Two relations have identical observable directional responses (+,+),
# but different internal modes. Their future behavior differs.
R1 = {"r_ab": 1, "r_ba": 1, "m": 0}
R2 = {"r_ab": 1, "r_ba": 1, "m": 1}

def future_response(R):
    return 1 if R["m"] == 0 else -1

same_pair = (R1["r_ab"], R1["r_ba"]) == (R2["r_ab"], R2["r_ba"])
different_future = future_response(R1) != future_response(R2)

print("\nCONTROLLED HIDDEN-STATE TEST")
print("same observable pair:", same_pair)
print("future R1:", future_response(R1))
print("future R2:", future_response(R2))
print("different future:", different_future)

assert same_pair and different_future

print("\nRESULT")
print("1. The two-component stateless model has exactly 9 qualitative states.")
print("2. Any quantity that is a function of (r_ab, r_ba) is derived, not independent.")
print("3. An independent third component requires identical pairs with different reproducible future behavior.")
print("4. The controlled hidden-state extension satisfies that criterion, but the hidden state was explicitly introduced.")
print("5. Therefore this experiment does NOT establish a third fundamental component.")
print("6. Next target: test whether such hidden relational state emerges from existing minimal Ω dynamics without explicit insertion.")
