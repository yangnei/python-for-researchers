---
marp: true
title: "Session 4 — Exceptions, Files & Research Data"
paginate: true
---

# Session 4
## Exceptions, Files & Research Data

*Learn Python — a two-hour session, in two halves.*

**Part A:** Exceptions & Defensive Code  ·  **Part B:** Files, Libraries & Research Data

---

# Part A
## Exceptions & Defensive Code

---

## try / except

```python
try:
    n = int(value)
except ValueError:
    n = None        # handle the bad case
```

When code might fail at runtime, wrap it. The `except` catches the named error.

---

## Common exception types

| Exception | Happens when |
|---|---|
| `ValueError` | right type, bad value: `int("N/A")` |
| `TypeError` | wrong type: `5 > "5"` |
| `KeyError` | missing dict key: `d["nope"]` |
| `IndexError` | bad list index: `xs[99]` |
| `ZeroDivisionError` | `x / 0` |
| `FileNotFoundError` | `open("missing.csv")` |

---

## try / except / else / finally

```python
try:
    n = int(value)
except ValueError:
    print("not a number")
else:
    print("ok:", n)      # only if NO exception
finally:
    print("always runs")  # cleanup
```

---

## Raise your own

```python
def clean_likert(n):
    if not 1 <= n <= 5:
        raise ValueError(f"{n} not in 1–5")
    return n
```

`raise` throws an exception on purpose — caller decides how to handle it.

---

## EAFP vs LBYL

```python
# LBYL — "look before you leap"
if value.isdigit():
    n = int(value)

# EAFP — "easier to ask forgiveness" (Pythonic)
try:
    n = int(value)
except ValueError:
    n = None
```

Both valid. EAFP shines when "checking first" is hard or racy.

---

## assert (developer check, not validation)

```python
assert len(scores) > 0, "scores must not be empty"
```

For *your* sanity checks while developing. Can be disabled (`python -O`),
so **never** use `assert` to validate untrusted input — use `raise`.

---

## A first test with pytest

```python
# clean.py
def clean_likert(n):
    if not 1 <= n <= 5:
        raise ValueError("1–5 only")
    return n

# test_clean.py
import pytest
from clean import clean_likert

def test_valid():    assert clean_likert(3) == 3
def test_invalid():
    with pytest.raises(ValueError):
        clean_likert(9)
```
Run: `pytest`

---

## Your turn

`examples/session-04/practice.md`:
1. `safe_int(value)` returning int or None.
2. Clean a dirty survey list, collecting good values + a rejection log.
3. Write one `pytest` test.

---

## Traps recap

- **Never** bare `except:` — name the exception.
- Don't catch too broadly or swallow errors silently.
- `assert` ≠ input validation (use `raise`).
- Catch the *specific* error you expect.

## Summary
You can validate messy input and fail loudly when you should.
**Next:** *Part B of this session* — files & research data.

---

# Part B
## Files, Libraries & Research Data

---

## Opening files with `with`

```python
with open("notes.txt") as f:
    text = f.read()
# file auto-closes here, even if the code crashes
```

`with` = a context manager: sets up and tears down the resource for you.
Always prefer it to a bare `open()`/`close()`.

---

## File modes (mind the trap)

| Mode | Meaning |
|---|---|
| `"r"` | read (default) |
| `"w"` | write — **truncates the file to empty first!** |
| `"a"` | append |
| `"r+"` | read + write |

⚠️ Open the wrong file with `"w"` → its contents are gone.

---

## Reading text

```python
with open("notes.txt") as f:
    whole = f.read()           # one big string
    # or
    for line in f:             # line by line (memory-friendly)
        print(line.rstrip())
```

⚠️ A file object is exhausted after one pass — re-open to read again.

---

## CSV in, as dicts 🧠

```python
import csv
with open("students.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["score"])   # row is a dict keyed by header
```

`csv.DictReader` turns each row into a dict — your "list of dicts" dataset from Session 4.
(`newline=""` avoids blank rows on Windows.)

---

## CSV out

```python
with open("summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "score"])
    w.writeheader()
    w.writerow({"name": "Ana", "score": 91})
```

---

## Libraries a researcher reaches for

```python
import statistics
statistics.mean(xs); statistics.median(xs); statistics.stdev(xs)

import random
random.choice(xs); random.randint(1, 6); random.shuffle(xs)

from datetime import date
date.today()

from pathlib import Path
Path("students.csv").exists()
```

`pip install <package>` for third-party libs.

---

## The pandas teaser (your next course)

```python
import pandas as pd
df = pd.read_csv("students.csv")
df["score"].describe()      # count, mean, std, min, quartiles, max
df.groupby("major")["score"].mean()
```

Everything you did by hand today — in three lines.
We learned the fundamentals *underneath* it first.

---

## Your turn

`examples/session-04/practice.md` (uses `survey.csv`):
1. Read `students.csv`; print class mean with `statistics.mean`.
2. Compute per-item survey means; write `survey_summary.csv`.

---

## Traps recap

- `"w"` silently overwrites — be sure of the filename.
- `csv` module → open with `newline=""`.
- Files exhaust after one read; re-open to re-read.
- Specify `encoding="utf-8"` for non-ASCII text.

## Summary
You can load, summarize, and write real research data.
**Next:** Regular expressions, modules & OOP.
