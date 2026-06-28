"""
Session 2 — Control Flow & Data Structures
Run me:  python3 demo.py
Two halves — (A) Control Flow: Conditionals & Loops; (B) Data Structures: list, tuple, dict, set.
Predict each block, then run it.
"""

# ======================================================================
# PART A — Control Flow: Conditionals & Loops
# ======================================================================

# --- 1. Conditionals + chained comparison -------------------------------
def letter_grade(score):
    if not 0 <= score <= 100:        # chained comparison
        return "Invalid"
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

for s in [95, 90, 89.999, 72, 60, 59, 120]:
    print(f"{s:>7} -> {letter_grade(s)}")

# --- 2. and / or return an operand (short-circuit) ----------------------
print("\n5 and 0   =", 5 and 0)        # 0
print("'' or N/A =", "" or "N/A")      # N/A
name = "" or "Anonymous"               # default-value idiom
print("name      =", name)

# truthiness instead of == True
submitted = ["essay.pdf"]
if submitted:                          # not  if len(submitted) > 0
    print("Has submissions")

# --- 3. Loops: iterate elements, range, break/continue ------------------
names  = ["Ana", "Ben", "Cara", "Dev"]
scores = [91, 58, 73, 64]

print("\nrange(1,5) =", list(range(1, 5)))   # [1,2,3,4] — stop excluded!
print("'Ben' in names:", "Ben" in names)     # True — membership test, no loop needed

total = 0
for s in scores:
    total += s
print("average:", total / len(scores))

# --- 4. enumerate + zip (no index juggling) -----------------------------
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

for name, score in zip(names, scores):
    print(f"{name}: {'PASS' if score >= 60 else 'FAIL'}")

print("passes:", sum(s >= 60 for s in scores))   # bools sum! (Session 2)

# --- 5. any / all: did ALL pass? did ANY fail? --------------------------
print("\nall passed?", all(s >= 60 for s in scores))   # False
print("any failed?", any(s < 60 for s in scores))      # True

# --- 6. break / continue + the for...else clause ------------------------
# `else` on a loop runs ONLY if the loop finished WITHOUT hitting `break`.
print("\nfirst failing student:")
for name, score in zip(names, scores):
    if score < 60:
        print(" -> found:", name)
        break
else:
    print(" -> nobody failed")     # would run only if no break happened

# --- 7. The validation loop (simulated input) ---------------------------
def to_valid_score(raw):
    """The logic inside a `while True:` prompt: int 0..100 or None."""
    return int(raw) if raw.isdigit() and 0 <= int(raw) <= 100 else None

print("\nvalidation:", [to_valid_score(x) for x in ["150", "abc", "84"]])  # None,None,84


# ======================================================================
# PART B — Data Structures: list, tuple, dict, set
# ======================================================================

import copy
from collections import Counter, defaultdict

# --- 1. A list of dicts is a tidy dataset -------------------------------
roster = [
    {"name": "Ana",  "major": "Education",  "score": 91},
    {"name": "Ben",  "major": "Psychology", "score": 58},
    {"name": "Cara", "major": "Education",  "score": 73},
    {"name": "Dev",  "major": "Sociology",  "score": 64},
]

# --- 2. Slicing + star-unpacking ----------------------------------------
xs = [10, 20, 30, 40]
print("xs[1:3]:", xs[1:3], "| xs[-1]:", xs[-1], "| xs[::-1]:", xs[::-1])
first, *rest = xs                 # grab the head; *rest soaks up the tail
*lead, last = xs                  # or the other way round
print("first:", first, "| rest:", rest, "| last:", last)

# --- 3. Sorting by a key (and a tuple key for tie-breaks) ---------------
top = sorted(roster, key=lambda s: s["score"], reverse=True)
print("\nRanked:", [s["name"] for s in top])
# Sort by major (A->Z), then by score (high->low) within each major:
by_major_then_score = sorted(roster, key=lambda s: (s["major"], -s["score"]))
print("major then score:", [(s["major"], s["name"]) for s in by_major_then_score])
print("top scorer:", max(roster, key=lambda s: s["score"])["name"])   # max with key=

# --- 4. Comprehensions (list, dict, AND set) ----------------------------
name_to_score = {s["name"]: s["score"] for s in roster}      # dict comp
passers = [s["name"] for s in roster if s["score"] >= 60]    # filtered list
majors = {s["major"] for s in roster}                        # set comp (unique)
print("\nmap:", name_to_score)
print("passers:", passers)
print("distinct majors:", majors)

# --- 5. dict methods: .get() and .items() -------------------------------
print("\nget present:", name_to_score.get("Ana"))            # 91
print("get missing:", name_to_score.get("Zoe", "n/a"))       # default, no KeyError
for name, score in name_to_score.items():                    # iterate key+value
    print(f"  {name} = {score}")

# --- 6. Grouping: setdefault, defaultdict, and Counter ------------------
buckets = defaultdict(list)        # auto-creates an empty list per new key
for s in roster:
    buckets["pass" if s["score"] >= 60 else "fail"].append(s["name"])
print("\nbuckets:", dict(buckets))
print("majors tally:", Counter(s["major"] for s in roster))  # counts in one line

# --- 7. Merging dicts (two ways) ----------------------------------------
defaults = {"scale": 100, "passing": 60}
overrides = {"passing": 50}
print("\nmerged {**a,**b}:", {**defaults, **overrides})      # later wins
print("merged a | b    :", defaults | overrides)             # Python 3.9+ union

# --- 8. Sets: dedup + set algebra ---------------------------------------
took_stats = {"Ana", "Ben", "Cara"}
took_python = {"Ana", "Dev"}
print("\nboth courses:", took_stats & took_python)           # intersection
print("either course:", took_stats | took_python)            # union
print("stats only:   ", took_stats - took_python)            # difference
print("exactly one:  ", took_stats ^ took_python)            # symmetric difference

# --- 9. Tuples + zip(*...) to transpose ---------------------------------
matrix = [(1, 2, 3), (4, 5, 6)]      # 2 rows x 3 cols
print("\ntransposed:", list(zip(*matrix)))   # [(1,4),(2,5),(3,6)] — rows<->cols

# --- 10. TRAP: aliasing -------------------------------------------------
a = [1, 2, 3]
b = a                 # alias — SAME list
a.append(4)
print("\nalias b:", b)          # [1, 2, 3, 4]  (changed!)

c = a.copy()          # independent shallow copy
a.append(5)
print("copy c:", c)             # [1, 2, 3, 4]  (unaffected)

# Nested data needs deepcopy:
grid_bad = [[0] * 3] * 3        # 3 refs to ONE row
grid_bad[0][0] = 9
print("shared-row grid:", grid_bad)   # [[9,0,0],[9,0,0],[9,0,0]]  😱
grid_ok = [[0] * 3 for _ in range(3)]
grid_ok[0][0] = 9
print("independent grid:", grid_ok)   # [[9,0,0],[0,0,0],[0,0,0]]
_ = copy.deepcopy(grid_ok)            # deepcopy duplicates every nested level
