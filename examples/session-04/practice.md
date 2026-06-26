# Session 4 — Practice (25 min)

## Task 1 — Average two ways
Given `scores = [91, 58, 73, 64]`, compute the mean (a) with a manual loop and a running
total, and (b) with `sum(scores) / len(scores)`. Confirm they match.

## Task 2 — Pass/fail roster
With `names = ["Ana","Ben","Cara","Dev"]` and the scores above, use `zip` to print
`"<name>: PASS"` (score ≥ 60) or `"<name>: FAIL"`. Then count passes using `sum(...)`.

## Task 3 — Validation loop
Write a real `while True:` prompt that keeps asking for a score until the user types an
integer 0–100, then prints it. (Use `.isdigit()`.)

## Task 4 — Trap check
Why does this go wrong, and what's the fix?
```python
xs = [1, 2, 3, 4]
for x in xs:
    if x % 2 == 0:
        xs.remove(x)
print(xs)   # not [1, 3] — why?
```

---
## Solutions

```python
# Task 1
total = 0
for s in scores:
    total += s
print(total / len(scores), sum(scores) / len(scores))   # 71.5 71.5

# Task 2
for name, score in zip(names, scores):
    print(f"{name}: {'PASS' if score >= 60 else 'FAIL'}")
passes = sum(score >= 60 for score in scores)   # bools sum! (Session 2)
print("passes:", passes)                         # 3

# Task 3
while True:
    raw = input("Score 0–100: ")
    if raw.isdigit() and 0 <= int(raw) <= 100:
        print("Got", int(raw)); break
    print("Try again.")

# Task 4
# Removing while iterating shifts indices, so the loop skips elements.
# Fix: iterate a copy, or build a new list:
xs = [x for x in xs if x % 2 != 0]   # [1, 3]
```
