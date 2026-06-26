"""
Session 4 — Loops & Iteration
Run me:  python3 demo.py
"""

names = ["Ana", "Ben", "Cara", "Dev"]
scores = [91, 58, 73, 64]

# --- 1. for + range vs for over elements --------------------------------
print("range(1,5) =", list(range(1, 5)))   # [1,2,3,4]  stop excluded!

total = 0
for s in scores:               # iterate elements directly (preferred)
    total += s
print("class total:", total, "| average:", total / len(scores))

# --- 2. enumerate: index + value ----------------------------------------
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# --- 3. zip: two lists in lockstep --------------------------------------
for name, score in zip(names, scores):
    print(f"{name}: {'PASS' if score >= 60 else 'FAIL'}")

# --- 4. break / continue -------------------------------------------------
print("\nfirst failing student:")
for name, score in zip(names, scores):
    if score >= 60:
        continue               # skip the passers
    print(" ->", name)
    break                      # stop at the first failure

# --- 5. TRAP: modifying a list while iterating --------------------------
nums = [1, 2, 3, 4, 5, 6]
# BAD: nums.remove(x) inside `for x in nums` skips elements.
# GOOD: build a new list.
evens_removed = [x for x in nums if x % 2 != 0]
print("\nodds only:", evens_removed)        # [1, 3, 5]

# --- 6. The validation loop (simulated input) ---------------------------
def to_valid_score(raw):
    """Return int 0..100 or None — the logic inside a while-True prompt."""
    return int(raw) if raw.isdigit() and 0 <= int(raw) <= 100 else None

for raw in ["150", "abc", "84"]:
    print(raw, "->", to_valid_score(raw))   # None, None, 84
