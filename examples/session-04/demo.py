"""
Session 4 — Exceptions, Files & Research Data
Run me:  python3 demo.py
Two halves — (A) Exceptions & Defensive Code; (B) Files, Libraries & Research Data.
Predict each block, then run it.
"""

# ======================================================================
# PART A — Exceptions & Defensive Code
# ======================================================================

# --- 1. try / except: convert what you can ------------------------------
def safe_int(value):
    """Return int(value) or None if it can't be parsed."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

for v in ["42", "N/A", "", None, "7"]:
    print(f"safe_int({v!r}) = {safe_int(v)}")

# --- 2. Your own exception type, and raising it -------------------------
class LikertError(ValueError):
    """Raised when a value isn't a valid 1–5 Likert response."""

def clean_likert(n):
    """Return n if it's a valid 1–5 Likert int, else raise LikertError."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise LikertError(f"{n!r} is not an integer")
    if not 1 <= n <= 5:
        raise LikertError(f"{n} is outside 1–5")
    return n

# --- 3. clean a dirty survey column, keeping a rejection log ------------
raw_responses = ["5", "3", "N/A", "7", "", "1", "two", "4"]
clean, rejected = [], []
for r in raw_responses:
    n = safe_int(r)
    try:
        clean.append(clean_likert(n))        # may raise LikertError
    except LikertError as e:                 # catching the base ValueError works too
        rejected.append((r, str(e)))

print("\nclean:", clean)
print("rejected:")
for original, why in rejected:
    print(f"  {original!r}: {why}")

# --- 4. Exception chaining: keep the original cause with `raise ... from` -
def parse_score(text):
    try:
        return int(text)
    except ValueError as e:
        raise LikertError(f"bad score {text!r}") from e   # preserves the __cause__

try:
    parse_score("oops")
except LikertError as e:
    print("\nraised:", e, "| caused by:", repr(e.__cause__))

# --- 5. else / finally ---------------------------------------------------
def parse(value):
    try:
        n = int(value)
    except ValueError:
        return "bad"
    else:
        return f"ok:{n}"          # only when no exception
    finally:
        pass                       # cleanup would go here (e.g., close a file)

print("\n", parse("10"), parse("x"))

# --- 6. assert: a cheap internal sanity check ---------------------------
def mean(xs):
    assert xs, "mean() needs at least one value"   # AssertionError if xs is empty
    return sum(xs) / len(xs)

print("mean:", mean([2, 4, 6]))

# --- 7. TRAP: bare except hides real bugs (don't do this) ---------------
# try:
#     risky()
# except:            # ❌ catches EVERYTHING, even Ctrl+C and typos
#     pass           # ❌ and silently swallows the error
# Always: except SpecificError as e: ...


# ======================================================================
# PART B — Files, Libraries & Research Data
# ======================================================================

import csv
import json
import statistics
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent     # so it works no matter where you run it

# --- 1. Read a CSV into a list of dicts ---------------------------------
with open(HERE / "students.csv", newline="") as f:
    students = list(csv.DictReader(f))   # each row is a dict keyed by header

print("rows read:", len(students))
print("first row:", students[0])

# CSV values are STRINGS — convert numbers (recall Session 1!)
scores = [int(s["score"]) for s in students]
print("class mean:", statistics.mean(scores))
print("class stdev:", round(statistics.stdev(scores), 2))
print("majors tally:", Counter(s["major"] for s in students))   # quick frequency count

# --- 2. Group by major, mean score -------------------------------------
by_major = {}
for s in students:
    by_major.setdefault(s["major"], []).append(int(s["score"]))
major_means = {m: round(statistics.mean(v), 1) for m, v in by_major.items()}
print("means by major:", major_means)

# --- 3. Write a summary CSV --------------------------------------------
with open(HERE / "students_summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["major", "mean_score", "n"])
    w.writeheader()
    for major, vals in by_major.items():
        w.writerow({"major": major, "mean_score": round(statistics.mean(vals), 1),
                    "n": len(vals)})
print("wrote students_summary.csv")

# --- 4. JSON: serialize a Python object to text and back ----------------
snapshot = {"n": len(students), "mean": statistics.mean(scores), "by_major": major_means}
(HERE / "snapshot.json").write_text(json.dumps(snapshot, indent=2))   # pathlib write
restored = json.loads((HERE / "snapshot.json").read_text())           # pathlib read
print("\nJSON round-trip ok?", restored == snapshot)

# --- 5. Survey: per-item means, skipping dirty values -------------------
def to_int(x):
    try:
        return int(x)
    except (ValueError, TypeError):
        return None        # handles "N/A" and "" (this session, Part A)

with open(HERE / "survey.csv", newline="") as f:
    rows = list(csv.DictReader(f))

items = [c for c in rows[0] if c != "respondent"]
item_means = {}
for item in items:
    vals = [to_int(r[item]) for r in rows]
    vals = [v for v in vals if v is not None]      # drop missing
    item_means[item] = round(statistics.mean(vals), 2)
print("\nper-item survey means:", item_means)

# Two files open at once in a single `with` (read source, write report together):
with open(HERE / "survey.csv", newline="") as src, \
     open(HERE / "survey_summary.csv", "w", newline="") as out:
    rows = list(csv.DictReader(src))
    w = csv.DictWriter(out, fieldnames=["item", "mean", "n_valid"])
    w.writeheader()
    for item in items:
        valid = [to_int(r[item]) for r in rows if to_int(r[item]) is not None]
        w.writerow({"item": item, "mean": round(statistics.mean(valid), 2),
                    "n_valid": len(valid)})
print("wrote survey_summary.csv")

# --- 6. pathlib: discover files without hard-coding names ---------------
csvs = sorted(p.stem for p in HERE.glob("*.csv"))   # .stem = filename without extension
print("\nCSV files here:", csvs)
