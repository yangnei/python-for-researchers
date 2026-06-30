---
marp: true
title: "Session 5 — Regular Expressions, Modules & OOP"
paginate: true
---

# Session 5
## Regular Expressions, Modules & OOP

*Learn Python — a two-hour session, in two halves.*

**Part A:** Regular Expressions & Text Cleaning  ·  **Part B:** Modules, OOP & the Pythonic Toolkit

---

# Part A
## Regular Expressions & Text Cleaning

---

## Why a researcher cares

- Validate IDs, emails, dates before they pollute your data.
- Extract structured bits from free text (codes, names, numbers).
- Clean and normalize open-ended survey responses.
- A first pass at **qualitative coding** (find every response matching a pattern).

🧠 Like search-and-filter over a corpus — but it matches *form*, not meaning.

---

## Always use raw strings

```python
import re
re.search(r"\d+", "id 42")     # r"..." = raw string
```

Without `r"..."`, Python eats the backslashes (`\d` → error/garbage).
**Rule:** every regex pattern is a raw string.

---

## The survival tokens

| Token | Matches |
|---|---|
| `.` | **any** char (except newline) |
| `\d \w \s` | digit / word-char / whitespace |
| `\D \W \S` | the negations |
| `+ * ?` | 1+, 0+, 0-or-1 |
| `{m}` `{m,n}` | exactly m / between m and n |
| `^ $` | start / end of string |
| `[abc]` `[^abc]` | any in set / none in set |
| `(...)` | capture group |
| `a\|b` | a or b |

---

## The `.` trap

```python
re.search(r".", "a.b").group()    # 'a'  — ANY char, not a dot!
re.search(r"\.", "a.b").group()   # '.'  — escape it for a literal dot
```

Escape the specials when you mean them literally: `\. \^ \$ \* \+ \? \( \) \[ \] \{ \} \|`

---

## The four functions you need

```python
re.search(pattern, s)     # first match ANYWHERE -> match or None
re.fullmatch(pattern, s)  # the WHOLE string must match -> validation
re.findall(pattern, s)    # list of ALL matches
re.sub(pattern, repl, s)  # replace matches -> cleaning
```

`re.IGNORECASE` flag for case-insensitive: `re.search(p, s, re.IGNORECASE)`.

---

## Validate (fullmatch anchors both ends)

```python
def valid_university_email(addr):
    return re.fullmatch(r"\w+@\w+\.edu", addr) is not None

valid_university_email("ana@university.edu")   # True
valid_university_email("ana@gmail.com")        # False
valid_university_email("ana@@x.edu")           # False
```

---

## Extract with capture groups

```python
m = re.search(r"([A-Z]{2})(\d{4})", "Course ED1234 meets Tue")
m.group(0)   # "ED1234"  whole match
m.group(1)   # "ED"      dept
m.group(2)   # "1234"    number
```

`m` is `None` if nothing matched — check before `.group()`.

---

## Clean & mine free text

```python
re.sub(r"\s+", " ", messy).strip()        # collapse whitespace
re.findall(r"#(\w+)", "love #python #stats")   # ['python', 'stats']

from collections import Counter
Counter(re.findall(r"#(\w+)", corpus))    # theme frequencies
```

Reformat with groups: `re.sub(r"^(.+),\s*(.+)$", r"\2 \1", "Curie, Marie")` → `"Marie Curie"`.

---

## When NOT to use regex

```python
"a,b,c".split(",")     # simple split — no regex needed
"  hi  ".strip()       # trim — no regex needed
text.replace("X", "Y") # fixed substring — no regex needed
```

Regex shines for *variable* patterns. For fixed strings, plain methods read better.

---

## Your turn

`examples/session-05/practice.md`:
1. Email validator. 2. Extract dept+number. 3. Collapse whitespace.
4. Count hashtags across responses. 5. Flip `"Last, First"`. 6. One case to use `.split()` instead.

---

## Traps recap

- `.` matches **any** char — use `\.` for a literal dot.
- Forgetting `r"..."` breaks your backslashes.
- `re.search` returns `None` on no match — guard before `.group()`.
- Don't use regex where a string method is clearer.

## Summary
You can validate, extract, and clean real-world text.
**Next:** *Part B of this session* — modules, OOP & the Pythonic toolkit.

---

# Part B
## Modules, OOP & the Pythonic Toolkit

---

## Modules: split your code into files

```python
# grades.py
def letter_grade(score): ...
def class_average(scores): ...

# analysis.py
from grades import letter_grade, class_average
```

A `.py` file is a **module**. `import` reuses its functions elsewhere → no copy-paste.

---

## The `__main__` guard

```python
# grades.py
if __name__ == "__main__":
    print(letter_grade(85))   # runs ONLY when you execute grades.py directly
```

On `import grades`, `__name__` is `"grades"`, so the block is skipped.
One file can be both a runnable script *and* an importable library.

---

## OOP: model a domain entity

```python
class Student:
    def __init__(self, name, gpa):   # constructor
        self.name = name
        self.gpa = gpa
    def __str__(self):               # how it prints
        return f"{self.name} ({self.gpa})"

ana = Student("Ana", 3.9)
print(ana)        # Ana (3.9)
```

🧠 A class is an *operational definition*: the attributes + behaviors that "count" as a Student.
`self` = "this particular student."

---

## @property: validate on assignment

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

`ana.gpa = 5.0` now raises — the object defends its own integrity.

---

## Inheritance

```python
class GradStudent(Student):
    def __init__(self, name, gpa, advisor):
        super().__init__(name, gpa)    # reuse parent setup
        self.advisor = advisor
    def __str__(self):
        return super().__str__() + f" — {self.advisor}"
```

`GradStudent` *is a* `Student` plus extra. `super()` calls the parent.

---

## The Pythonic toolkit (recap tour)

```python
[s.name for s in roster if s.gpa >= 2.0]   # comprehension (from S4)
list(map(lambda s: s.name.upper(), roster))# map: apply to all
list(filter(lambda s: s.gpa < 2.0, roster))# filter: keep matches
for i, s in enumerate(roster): ...          # index + item
for a, b in zip(names, scores): ...         # parallel
```

---

## Generators & walrus

```python
def gpas(students):
    for s in students:
        yield s.gpa          # one value at a time — low memory on big data

g = gpas(roster)
list(g)   # ?
list(g)   # ?  ← run it twice — what changes? (Traps below)

if (n := len(roster)) > 30:   # walrus := : assign + test in one step
    print(f"{n} students")
```

---

## Your turn

`examples/session-05/practice.md`:
1. Import from `grades.py`. 2. Build the validating `Student` class.
3. Add `GradStudent` with `super()`. 4. Comprehension + `map` + `filter` + a generator.

---

## Traps recap

- `self` is just "this instance" — not magic.
- A generator iterates **once**, then it's empty.
- The `__main__` guard keeps imported modules from running their demo code.
- Don't reach for a class when a function or dict will do.

## Summary
You can structure code into modules and classes and write idiomatic Python.
**Next (optional):** the capstone — put it all together.

**Next:** the capstone project.
