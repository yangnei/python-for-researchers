# Session 4 — Practice: Exceptions, Files & Research Data

This 2-hour session has two halves. Do **Part A** after the first topic, **Part B** after the second. Predict every output before you run it.

## Part A — Exceptions & Defensive Code

### Task 1 — `safe_int`
Write `safe_int(value)` returning `int(value)` or `None` on failure. Test on
`"42"`, `"N/A"`, `""`, `None`, `3.0`.

### Task 2 — Clean a survey column
Given `raw = ["5","3","N/A","7","","1","two","4"]`, produce:
- `clean` — list of valid Likert ints (1–5), and
- `rejected` — list of `(value, reason)` pairs.
Use a `clean_likert(n)` that **raises** `ValueError` for out-of-range or non-ints.

### Task 3 — Write a test
Put `clean_likert` in `clean.py` and write `test_clean.py` with pytest:
one passing case and one `pytest.raises(ValueError)` case. Run `pytest`.

### Task 4 — Discuss
Why is `except:` (bare) dangerous? Give one error it would hide that you'd rather see.

### Bonus — Pythonic idiom drill
Cover the `# ->` answers, predict each line, then run.

```python
class LikertError(ValueError):       # your own exception type
    pass
print(issubclass(LikertError, ValueError))   # -> True  (so `except ValueError` still catches it)

try:
    assert 1 == 2, "values differ"   # assert: cheap internal sanity check
except AssertionError as e:
    print(e)                         # -> values differ
```

## Part B — Files, Libraries & Research Data

Files provided: `students.csv`, `survey.csv`.

### Task 1 — Read & summarize students
Read `students.csv` with `csv.DictReader`. Remember the values are **strings** — convert
`score` to `int`. Print the class mean and median with the `statistics` module.

### Task 2 — Mean by major
Build `{major: mean_score}`. (Hint: `dict.setdefault(key, []).append(...)`.)

### Task 3 — Clean & summarize the survey
`survey.csv` has `"N/A"` and blanks in numeric columns. For each `q*` item, compute the
mean of the **valid** values only, and how many were valid. Write `survey_summary.csv`
with columns `item,mean,n_valid`.

### Task 4 — pandas teaser (optional)
If `pandas` is installed: `pd.read_csv("students.csv")["score"].describe()`. Compare the
mean to your hand-computed one.

### Trap check
What happens if you accidentally open `students.csv` with mode `"w"` before reading it?

### Bonus — Pythonic idiom drill
Cover the `# ->` answers, predict each line, then run.

```python
import json
s = json.dumps({"n": 3, "ok": True})
print(s)                             # -> {"n": 3, "ok": true}   (Python True -> JSON true)
print(json.loads(s)["ok"])           # -> True                   (and back to a Python bool)
```

---

## Solutions

### Part A — Exceptions & Defensive Code

```python
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def clean_likert(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"{n!r} not an int")
    if not 1 <= n <= 5:
        raise ValueError(f"{n} outside 1–5")
    return n

raw = ["5","3","N/A","7","","1","two","4"]
clean, rejected = [], []
for r in raw:
    try:
        clean.append(clean_likert(safe_int(r)))
    except ValueError as e:
        rejected.append((r, str(e)))
print(clean)      # [5, 3, 1, 4]
print(rejected)   # [('N/A', ...), ('7', ...), ('', ...), ('two', ...)]
```

```python
# test_clean.py
import pytest
from clean import clean_likert
def test_ok():   assert clean_likert(3) == 3
def test_bad():
    with pytest.raises(ValueError):
        clean_likert(9)
```

Task 4: a bare `except:` also catches `KeyboardInterrupt` (Ctrl+C) and `NameError`
from your own typos — so a misspelled variable would be silently swallowed instead of
showing you the bug. Always catch the specific exception you expect.

### Part B — Files, Libraries & Research Data

See `demo.py` in this folder — it implements Tasks 1–3 exactly. Key lines:

```python
scores = [int(s["score"]) for s in students]     # convert strings!
statistics.mean(scores)                           # 75.5

by_major = {}
for s in students:
    by_major.setdefault(s["major"], []).append(int(s["score"]))

def to_int(x):
    try: return int(x)
    except (ValueError, TypeError): return None   # handles N/A and ""
```

Trap: opening with `"w"` **truncates the file to empty immediately** — your data is gone
before you ever read it. Use `"r"` (the default) to read.
