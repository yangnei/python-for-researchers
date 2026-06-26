---
marp: true
title: "Session 3 — Conditionals & Boolean Logic"
paginate: true
---

# Session 3
## Conditionals & Boolean Logic

Make decisions; write them the Pythonic way.

---

## if / elif / else

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

Indentation defines the block. `elif` = "else if". Only the **first** true branch runs.

---

## Comparison operators

`==`  `!=`  `<`  `<=`  `>`  `>=`

```python
score == 100      # equal (VALUE — recall Session 2)
score != 0
0 <= score <= 100 # chained! reads like math
```

🧠 No need for `score >= 0 and score <= 100` — chain it.

---

## Logical operators

```python
passed and submitted     # both
late or excused          # either
not flagged              # negate
```

**Short-circuit:** `a and b` skips `b` if `a` is falsy; `a or b` skips `b` if `a` is truthy.

---

## `and`/`or` return a VALUE, not a bool

```python
5 and 0        # 0      (and → first falsy / last)
0 or "hi"      # "hi"   (or → first truthy / last)
name = user_input or "Anonymous"   # default-value idiom
```

So don't write `if x == True` — just `if x:`.

---

## The Likert classifier (live)

```python
def likert_label(n):
    if n == 5: return "Strongly agree"
    if n == 4: return "Agree"
    if n == 3: return "Neutral"
    if n == 2: return "Disagree"
    if n == 1: return "Strongly disagree"
    return "Invalid"
```

Early `return` → no nesting needed.

---

## Ternary & match

```python
status = "pass" if score >= 60 else "fail"   # ternary

match command:                                # Python 3.10+
    case "start":      run()
    case "stop"|"halt": halt()    # multiple values
    case _:            unknown()  # default (_ = wildcard)
```

---

## Your turn

`examples/session-03/practice.md`:
1. Grade-band classifier — test the boundaries (89.999 / 90 / 90.001).
2. `is_valid_likert(n)` → only 1–5 integers are valid.

---

## Traps recap

- `if x == True` → just `if x:`.
- Use `x is None`, not `x == None`.
- `=` (assign) vs `==` (compare) — a classic typo.
- Test your **boundaries**; `>=` vs `>` decides a grade.

## Summary
You can branch cleanly, chain comparisons, and use boolean values directly.
**Next:** Loops — do something many times.
