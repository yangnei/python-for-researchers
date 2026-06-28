# Session 5 — Practice: Regex, Modules & OOP

This 2-hour session has two halves. Do **Part A** after the first topic, **Part B** after the second. Predict every output before you run it.

## Part A — Regular Expressions & Text Cleaning

Always use raw strings `r"..."`. Predict each result before running.

### Task 1 — Validate
Write `valid_university_email(addr)` returning `True` only for `something@something.edu`.
Test: `"ana@university.edu"`, `"ana@gmail.com"`, `"a@b.edu.evil.com"`.

### Task 2 — Extract with groups
From `"Course ED1234 meets Tue"`, pull the department (`ED`) and number (`1234`) using one
regex with two capture groups.

### Task 3 — Clean
Collapse all runs of whitespace in `"  too    much\t space "` to single spaces and trim.

### Task 4 — Mine free text
From a list of open-ended responses, count how often each `#hashtag` appears
(use `re.findall(r"#(\w+)", text)` and `collections.Counter`).

### Task 5 — Reformat
Turn `"Curie, Marie"` into `"Marie Curie"` with a single regex + groups.

### Task 6 — Judgment
Give one task where a plain string method (`.split()`, `.strip()`, `.replace()`) is the better,
clearer choice than a regex.

### Bonus — Pythonic idiom drill
Cover the `# ->` answers, predict each line, then run.

```python
import re
m = re.search(r"(?P<year>\d{4})", "class of 2026")
print(m.group("year"), m.groupdict())   # -> 2026 {'year': '2026'}   (named groups)
print(re.split(r"\s*,\s*", "a, b ,c")) # -> ['a', 'b', 'c']        (split on commas + spaces)
```

## Part B — Modules, OOP & the Pythonic Toolkit

Files in this folder: `grades.py` (a module you import), `demo.py` (worked example).

### Task 1 — Use a module
From a new file, `from grades import letter_grade, class_average` and call both. Why does the
`if __name__ == "__main__":` block in `grades.py` NOT run when you import it?

### Task 2 — A class with a validating property
Build `Student(name, gpa)` with:
- `__str__` → `"Ana: 3.9 (Good)"`,
- `standing()` → `"Good"` if gpa ≥ 2.0 else `"Probation"`,
- a `@property` setter for `gpa` that raises `ValueError` outside 0–4.
Prove the setter rejects `5.0`.

### Task 3 — Inheritance
Add `GradStudent(Student)` that also stores an `advisor` and uses `super().__init__(...)`.
Override `__str__` to append the advisor.

### Task 4 — The Pythonic toolkit
Given a roster of `Student`s:
1. names in good standing (list comprehension),
2. uppercase names (`map`),
3. at-risk students (`filter`),
4. mean gpa via a **generator** that `yield`s each gpa — then show the generator is empty on a
   second pass.

### Bonus — Pythonic idiom drill
Cover the `# ->` answers, predict each line, then run.

```python
from dataclasses import dataclass

@dataclass                           # auto __init__, __repr__, __eq__
class Point:
    x: int
    y: int
print(Point(1, 2), Point(1, 2) == Point(1, 2))   # -> Point(x=1, y=2) True

def head(v):
    match v:                         # structural pattern matching (3.10+)
        case [first, *_]: return first
        case _: return None
print(head([9, 8]), head(5))         # -> 9 None
```

---

## Solutions

### Part A — Regular Expressions & Text Cleaning

See `demo.py` in this folder — it implements all six. Key lines:

```python
re.fullmatch(r"\w+@\w+\.edu", addr) is not None      # 1 (fullmatch anchors both ends)
m = re.search(r"([A-Z]{2})(\d{4})", s); m.group(1), m.group(2)   # 2
re.sub(r"\s+", " ", messy).strip()                   # 3
from collections import Counter; Counter(re.findall(r"#(\w+)", text))   # 4
m = re.search(r"^(.+),\s*(.+)$", s); f"{m.group(2)} {m.group(1)}"      # 5
```
Task 6: splitting `"a,b,c"` on commas is just `"a,b,c".split(",")` — no regex needed.
Reach for regex only when the pattern is genuinely variable (digits, optional parts, anchors).
```
```
Trap reminder: `.` matches **any** character — use `\.` for a literal dot, and never forget the
`r"..."` prefix or your backslashes become Python escape sequences.

### Part B — Modules, OOP & the Pythonic Toolkit

See `demo.py` — it implements Tasks 2–4. Key points:

```python
@property
def gpa(self): return self._gpa
@gpa.setter
def gpa(self, v):
    if not 0 <= v <= 4: raise ValueError(...)
    self._gpa = v

class GradStudent(Student):
    def __init__(self, name, gpa, advisor):
        super().__init__(name, gpa)
        self.advisor = advisor

[s.name for s in roster if s.gpa >= 2.0]          # comprehension
list(map(lambda s: s.name.upper(), roster))        # map
[s.name for s in filter(lambda s: s.gpa < 2.0, roster)]   # filter
def gpas(rs):
    for s in rs: yield s.gpa                        # generator (exhausts after one pass)
```
Task 1: the `__name__` guard is only `"__main__"` when the file is **run directly**; on `import`
its `__name__` is `"grades"`, so the demo block is skipped — that's how a file can be both a
runnable script and an importable module.
