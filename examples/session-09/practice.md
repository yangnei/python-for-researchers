# Session 9 — Practice (25 min)

## Task 1 — Regex
1. Write `valid_university_email(addr)` → `True` only for `something@something.edu`.
2. Given `"Course ED1234 meets Tue"`, extract the department (`ED`) and number (`1234`)
   with one regex and capture groups.
3. Collapse runs of whitespace in `"too    much   space"` to single spaces.

## Task 2 — A Student class
Build `Student(name, gpa)` with:
- a `__str__` that prints `"Ana: 3.9 (Good)"`,
- a `standing()` method (`"Good"` if gpa ≥ 2.0 else `"Probation"`),
- a `@property` setter for `gpa` that raises `ValueError` outside 0–4.
Prove the setter rejects `5.0`.

## Task 3 — Pythonic
Given a roster of `Student`s:
1. List the names in good standing (comprehension).
2. Compute the mean gpa with a **generator** that yields each gpa.
3. Show that the generator is empty on a second pass.

---
## Solutions
See `demo.py` in this folder — it implements all three tasks. Key bits:

```python
re.fullmatch(r"\w+@\w+\.edu", addr) is not None
m = re.search(r"([A-Z]{2})(\d{4})", text); m.group(1), m.group(2)
re.sub(r"\s+", " ", messy)

@property
def gpa(self): return self._gpa
@gpa.setter
def gpa(self, v):
    if not 0 <= v <= 4: raise ValueError(...)
    self._gpa = v

good = [s.name for s in roster if s.gpa >= 2.0]
def gpas(students):
    for s in students: yield s.gpa
```
Remember: a generator yields lazily and **exhausts after one pass** — `list(g)` twice
gives the data then `[]`.
