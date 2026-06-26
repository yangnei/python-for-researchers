---
marp: true
title: "Session 9 — Regex, Modules, OOP & Pythonic"
paginate: true
---

# Session 9
## Regex · Modules · OOP · "Pythonic"

Clean text, organize code, and write like the experts.

---

## Regular expressions — clean & validate text

```python
import re
re.search(r"\d+", "id 42")      # finds "42"  (or None)
re.fullmatch(r"\d{5}", zipcode) # whole string is 5 digits?
re.sub(r"\s+", " ", messy)      # collapse whitespace
```

🧠 Like search-and-filter in a corpus / qualitative coding — but it matches *form*, not meaning.

---

## Regex tokens (the survival set)

| Token | Means |
|---|---|
| `.` | **any** char (not just a dot!) |
| `\d \w \s` | digit / word-char / whitespace |
| `+ * ?` | 1+, 0+, 0-or-1 |
| `{m,n}` | between m and n |
| `^ $` | start / end |
| `[abc] [^abc]` | in set / not in set |
| `(...)` | capture group |

⚠️ Always use **raw strings** `r"..."`; escape a literal dot as `\.`.

---

## Groups: extract pieces

```python
m = re.search(r"([A-Z]{2})(\d{4})", "ED1234")
m.group(0)   # "ED1234" (whole match)
m.group(1)   # "ED"     (dept)
m.group(2)   # "1234"   (number)
```

---

## Modules — split your code

```python
# grades.py
def letter_grade(score): ...

# analysis.py
from grades import letter_grade
import statistics
```

A `.py` file is a module. The `if __name__ == "__main__":` block runs only when the
file is executed directly, not when imported.

---

## OOP — model a domain entity

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self._gpa = gpa
    def __str__(self):
        return f"{self.name} ({self._gpa})"
```

🧠 A class is an *operational definition*: the attributes + behaviors that "count" as a Student.
`self` = "this particular student."

---

## @property — validate on set

```python
class Student:
    ...
    @property
    def gpa(self):
        return self._gpa
    @gpa.setter
    def gpa(self, value):
        if not 0 <= value <= 4:
            raise ValueError("gpa must be 0–4")
        self._gpa = value
```

Looks like an attribute (`s.gpa = 3.9`), but defends its own integrity.

---

## "Pythonic" power-tools (recap tour)

```python
[s.name for s in students]            # comprehension
for i, s in enumerate(students): ...  # index + item
for a, b in zip(xs, ys): ...          # parallel
list(map(str.upper, words))           # apply fn to all
list(filter(lambda s: s.gpa >= 3.5, students))
```

---

## Generators & walrus

```python
def big_scores(rows):
    for r in rows:
        yield int(r["score"])     # one at a time, low memory

if (n := len(scores)) > 30:        # assign + test in one step
    print(f"{n} students")
```

A generator is iterated **once**; great for data too big for memory.

---

## Your turn

`examples/session-09/practice.md`:
1. Validate a student email / extract an ID with regex.
2. Build the `Student` class with a validating `@property`.
3. Rewrite a loop as a comprehension; write one generator.

---

## Traps recap

- Regex `.` matches anything; forget `r"..."` → backslash chaos.
- `self` is just "this instance" — not magic.
- A generator exhausts after one pass.
- Don't use regex where `.split()`/`.strip()` is clearer.

## Summary
You can clean text, organize code into modules/classes, and write idiomatic Python.
**Next (optional):** the capstone — put it all together.
