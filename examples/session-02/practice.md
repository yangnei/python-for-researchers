# Session 2 — Practice: Control Flow & Data Structures

This 2-hour session has two halves. Do **Part A** after the first topic, **Part B** after the second. Predict every output before you run it.

## Part A — Control Flow: Conditionals & Loops

### Task 1 — Grade-band classifier
Write `letter_grade(score)` returning A/B/C/D/F (90/80/70/60 cutoffs), `"Invalid"` outside 0–100.
**Test the boundaries:** 90, 89.999, 0, 100, -5, 101.

### Task 2 — Boolean logic
1. What is `5 and 0`? `"" or "N/A"`? Why aren't they `True`/`False`?
2. Rewrite `if attended == True:` the Pythonic way.

### Task 3 — Average + pass/fail (loops)
Given `names = ["Ana","Ben","Cara","Dev"]` and `scores = [91, 58, 73, 64]`:
1. Compute the mean with a loop and a running total.
2. Use `zip` to print `"<name>: PASS"` (≥60) or `"<name>: FAIL"`.
3. Count the passes with `sum(s >= 60 for s in scores)`.

### Task 4 — Validation loop
Write a real `while True:` prompt that keeps asking until the user types an integer 0–100.

### Task 5 — Trap check
Why does this skip elements, and what's the fix?
```python
xs = [1, 2, 3, 4]
for x in xs:
    if x % 2 == 0:
        xs.remove(x)
```

### Bonus — Pythonic idiom drill
Cover the `# ->` answers, predict each line, then run.

```python
nums = [80, 92, 45]
print(all(n >= 60 for n in nums))    # -> False   (45 fails)
print(any(n >= 90 for n in nums))    # -> True    (92 passes)
print(92 in nums, 60 in nums)        # -> True False
```

## Part B — Data Structures: list, tuple, dict, set

Start from:
```python
roster = [
    {"name": "Ana", "score": 91}, {"name": "Ben", "score": 58},
    {"name": "Cara", "score": 73}, {"name": "Dev", "score": 64},
]
```

### Task 1 — Rank
Print names sorted by score, highest first.

### Task 2 — Map (dict comprehension)
Build `{name: score}` in one line.

### Task 3 — Group
Build `{"pass": [...names...], "fail": [...names...]}` using a loop.

### Task 4 — Dedup
From `["A","B","A","C","B"]`, get the distinct values and how many there are.

### Task 5 — Aliasing
Show that `b = roster` then `roster.append({...})` also changes `b`. Then make `b` an
independent copy so it doesn't. (Hint: nested dicts → `copy.deepcopy`.)

### Bonus — Pythonic idiom drill
Cover the `# ->` answers, predict each line, then run.

```python
head, *tail = [10, 20, 30, 40]
print(head, tail)                    # -> 10 [20, 30, 40]   (star-unpacking)
print({"a": 1} | {"b": 2})           # -> {'a': 1, 'b': 2}  (dict union, 3.9+)
print({1, 2, 3} & {2, 3, 4})         # -> {2, 3}            (set intersection)
print(list(zip(*[(1, 2), (3, 4)])))  # -> [(1, 3), (2, 4)]  (transpose)
```

---

## Solutions

### Part A — Control Flow: Conditionals & Loops

```python
# 1
def letter_grade(score):
    if not 0 <= score <= 100: return "Invalid"
    for cutoff, g in [(90,"A"),(80,"B"),(70,"C"),(60,"D")]:
        if score >= cutoff: return g
    return "F"
# 90->A, 89.999->B, 0->F, 100->A, -5->Invalid, 101->Invalid

# 2
# 5 and 0 -> 0 ; "" or "N/A" -> "N/A"  (and/or return an operand, not a bool)
result = "pass" if attended else "absent"     # and just `if attended:`

# 3
total = 0
for s in scores: total += s
print(total / len(scores))                    # 71.5
for name, score in zip(names, scores):
    print(f"{name}: {'PASS' if score >= 60 else 'FAIL'}")
print("passes:", sum(s >= 60 for s in scores))   # 3

# 4
while True:
    raw = input("Score 0–100: ")
    if raw.isdigit() and 0 <= int(raw) <= 100:
        print("Got", int(raw)); break
    print("Try again.")

# 5  Removing while iterating shifts indices, so elements get skipped.
xs = [x for x in xs if x % 2 != 0]            # build a new list instead -> [1, 3]
```

### Part B — Data Structures: list, tuple, dict, set

```python
# 1
print([s["name"] for s in sorted(roster, key=lambda s: s["score"], reverse=True)])
# ['Ana', 'Cara', 'Dev', 'Ben']

# 2
name_to_score = {s["name"]: s["score"] for s in roster}

# 3
groups = {"pass": [], "fail": []}
for s in roster:
    groups["pass" if s["score"] >= 60 else "fail"].append(s["name"])

# 4
vals = ["A","B","A","C","B"]
distinct = set(vals); print(distinct, len(distinct))   # {'A','B','C'} 3

# 5
import copy
b = roster                       # alias
roster.append({"name": "Eve", "score": 80})
# b now also has Eve. To stay independent:
b = copy.deepcopy(roster)        # changes to roster no longer touch b
```
