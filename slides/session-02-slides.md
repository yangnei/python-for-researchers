---
marp: true
title: "Session 2 — Control Flow & Data Structures"
paginate: true
---

# Session 2
## Control Flow & Data Structures

*Learn Python — a two-hour session, in two halves.*

**Part A:** Control Flow: Conditionals & Loops  ·  **Part B:** Data Structures

---

# Part A
## Control Flow: Conditionals & Loops

---

## Part 1 — Conditionals

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
```

Indentation defines the block. Only the **first** true branch runs.

---

## Comparison + chained comparisons

`==`  `!=`  `<`  `<=`  `>`  `>=`

```python
0 <= score <= 100      # chained — reads like math
```

🧠 No need for `score >= 0 and score <= 100` — chain it.

---

## Logical operators (and the gotcha)

```python
passed and submitted     # both
late or excused          # either
not flagged              # negate
```

**Short-circuit:** `a and b` skips `b` if `a` is falsy.
And `and`/`or` return an **operand, not a bool**:

```python
5 and 0        # ?  ← predict, then reveal in Traps below
"" or "N/A"    # the default-value idiom
```

So write `if x:` — never `if x == True`.

---

## Part 2 — Loops

```python
for s in scores:          # each element directly
    print(s)

for i in range(5):        # 0,1,2,3,4
    print(i)

while not done:           # repeat until a condition flips
    ...
```

⚠️ `range(1, 5)` → `1,2,3,4` — **stop is excluded** (off-by-one!).

---

## break / continue

```python
for x in data:
    if x is None:
        continue          # skip this one
    if x == "STOP":
        break             # leave the loop entirely
    process(x)
```

---

## Stop juggling indices: enumerate & zip

```python
for i, name in enumerate(names):       # index + value
    print(i, name)

for name, score in zip(names, scores): # two lists together
    print(name, score)
```

🧠 If you write `range(len(x))`, stop — use `enumerate`/`zip`.

---

## The validation loop (you'll reuse this everywhere)

```python
while True:
    raw = input("Score 0–100: ")
    if raw.isdigit() and 0 <= int(raw) <= 100:
        score = int(raw)
        break
    print("Try again.")
```

---

## Your turn

`examples/session-02/practice.md`:
1. Grade-band classifier — test the boundaries (89.999 / 90 / 90.001).
2. Average a roster and label each student PASS/FAIL with `zip`.
3. A robust "ask until valid" loop.

---

## Traps recap

- `if x == True` → just `if x:`; use `x is None` (not `== None`).
- `=` (assign) vs `==` (compare) — classic typo.
- `range(1, 5)` excludes 5; test your boundaries.
- Don't modify a list while looping it; prefer `enumerate`/`zip` over `range(len(...))`.

*(More in the cheat sheet: `match`/`case`, the ternary, `for/else`.)*

## Summary
You can branch and repeat cleanly.
**Next:** *Part B of this session* — data structures.

---

# Part B
## Data Structures

---

## Four containers, four jobs

| Type | Syntax | Mutable? | Use for |
|---|---|---|---|
| `list` | `[1, 2, 3]` | yes | ordered, changing collection |
| `tuple` | `(1, 2)` | no | fixed record / coordinates |
| `dict` | `{"k": v}` | yes | key → value lookup |
| `set` | `{1, 2, 3}` | yes | unique items |

---

## Lists & slicing

```python
xs = [10, 20, 30, 40]
xs[0]      # 10     xs[-1]   # 40 (last)
xs[1:3]    # [20, 30]   (stop excluded)
xs[:2]     # [10, 20]
xs[::-1]   # reversed
xs.append(50); xs.sort()      # mutate in place
```

⚠️ `xs.sort()` returns **None** — it sorts in place. Use `sorted(xs)` for a new list.

---

## Dicts = labeled records

```python
student = {"name": "Ana", "gpa": 3.9}
student["name"]              # "Ana"
student.get("major", "N/A")  # safe access with default
student["major"] = "Ed"      # add/update
for key, val in student.items(): ...
```

---

## A list of dicts = a dataset 🧠

```python
roster = [
    {"name": "Ana", "score": 91},
    {"name": "Ben", "score": 58},
]
```

Each dict = a **row/respondent**; each key = a **variable/column**.
This is your tidy dataset until pandas shows up (Session 4).

---

## Sets: unique, fast membership

```python
answers = ["yes", "no", "yes", "maybe", "no"]
set(answers)            # {'yes', 'no', 'maybe'}  — dedup
"yes" in set(answers)   # True, very fast
```

Great for "distinct responses" and "have I seen this ID?"

---

## Comprehensions

```python
[s["score"] for s in roster]                 # list
[s for s in roster if s["score"] >= 60]      # with filter
{s["name"]: s["score"] for s in roster}      # dict
{s["score"] // 10 for s in roster}           # set of score-decades
```

Read as: *expr, for each item, (optionally) if condition.*

---

## Sorting with a key

```python
sorted(roster, key=lambda s: s["score"])               # ascending
sorted(roster, key=lambda s: s["score"], reverse=True) # descending
```

`lambda s: s["score"]` = "sort by the score field."

---

## TRAP: aliasing (labels, not boxes)

```python
a = [1, 2, 3]
b = a                # SAME list
a.append(4)
b                    # ?  😱  ← predict (see Traps below)

b = a.copy()         # ✅ independent copy
```

`[[0]*3]*3` makes 3 references to ONE row — use `[[0]*3 for _ in range(3)]`.

---

## Your turn

`examples/session-02/practice.md`:
1. Build the roster (list of dicts); sort by score.
2. `{name: score}` dict comprehension.
3. Group students into pass/fail buckets.
4. Demonstrate the aliasing trap and fix it.

---

## Traps recap

- `=` aliases; use `.copy()` / `copy.deepcopy()`.
- `.sort()` returns None (in place); `sorted()` returns new.
- list ≠ tuple even with same contents (Session 2).
- `dict.get(key, default)` avoids `KeyError`.

## Summary
You can store, look up, dedup, sort, and reshape data.
**Next:** Functions, scope & recursion.
