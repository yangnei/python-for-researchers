# Session 3 — Practice (25 min)

## Task 1 — Grade-band classifier
Write `letter_grade(score)` returning A/B/C/D/F (90/80/70/60 cutoffs).
**Test the boundaries:** what does 90 return? 89.999? 0? 100? -5? 101?

## Task 2 — Likert validator
Write `is_valid_likert(n)` that returns `True` only for the integers 1–5.
Make sure `is_valid_likert(3.0)`, `is_valid_likert("3")`, and `is_valid_likert(True)`
all behave sensibly. *(Recall Session 2: what is `True` here?)*

## Task 3 — Refactor
This is ugly. Rewrite it in two lines using truthiness and a ternary:
```python
if attended == True:
    if score >= 60:
        result = "pass"
    else:
        result = "fail"
else:
    result = "absent"
```

---
## Solutions

```python
# Task 1
def letter_grade(score):
    if not 0 <= score <= 100:
        return "Invalid"
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"
# 90->A, 89.999->B, 0->F, 100->A, -5->Invalid, 101->Invalid

# Task 2
def is_valid_likert(n):
    # reject bools (True would pass as int 1) and non-ints
    return isinstance(n, int) and not isinstance(n, bool) and 1 <= n <= 5
# is_valid_likert(3.0) -> False (it's a float)
# is_valid_likert("3") -> False (it's a str)
# is_valid_likert(True) -> False (explicitly excluded)

# Task 3
result = ("pass" if score >= 60 else "fail") if attended else "absent"
```
