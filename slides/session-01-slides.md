---
marp: true
title: "Session 1 — Running Python, Types & the Type Traps"
paginate: true
---

# Session 1
## Running Python, Types & the Type Traps

*Learn Python — a two-hour session, in two halves.*

**Part A:** Running Python, Variables & Types  ·  **Part B:** The Dynamic-Typing Traps

---

# Part A
## Running Python, Variables & Types

---

## Why Python (for you)

- Free, readable, the lingua franca of research computing.
- Glue between your data, your stats, and your writing.
- Today: from zero to "I ran a program."

> Mantra for the whole course: **readability wins**.

---

## Two ways to run Python

1. **REPL** — type `python3`, get `>>>`, run one line at a time. Great for experiments.
2. **Script** — save `hello.py`, run `python3 hello.py`. Great for real work.

```python
# hello.py
print("Hello, researcher")
```

---

## Variables = labels on objects

```python
n = 30          # an int
mean = 3.7      # a float
name = "Ada"    # a str
passed = True   # a bool
missing = None  # "no value"
```

`=` is an **action** ("stick this label on that object"), **not** a math equation.
So `n = n + 1` is fine.

🧠 In stats you name quantities (`n`, `α`). Same idea — but the name can be re-pointed.

---

## The 5 core types

| Type | Example | Think |
|---|---|---|
| `int` | `30` | counts |
| `float` | `3.7` | measurements |
| `str` | `"Ada"` | text |
| `bool` | `True`/`False` | flags |
| `NoneType` | `None` | missing |

`type(x)` tells you which.

---

## Input & output

```python
name = input("Your name: ")        # ⚠️ ALWAYS a str
age  = int(input("Your age: "))    # convert right away
print("Hi", name, "— age", age)
```

**The #1 week-one trap:** `input()` gives you text.
`"5" + "3"` is `"53"`, not `8`.

---

## f-strings (use these)

```python
score = 87.456
print(f"{name} scored {score:.1f}")   # one decimal
print(f"{1234567:,}")                  # 1,234,567
print(f"{0.873:.1%}")                  # 87.3%
```

Cleaner than `+` concatenation and no type errors.

---

## Type conversion (casting)

```python
int("42")     # 42
float("3.14") # 3.14
str(42)       # "42"
int(3.9)      # 3   (truncates, doesn't round!)
round(3.9)    # 4
```

`int(input(...))` = read text, convert to number, in one step.

---

## Reading a traceback (don't panic)

```text
Traceback (most recent call last):
  File "x.py", line 3, in <module>
    age = int(input("Age: "))
ValueError: invalid literal for int() with base 10: 'thirty'
```

**Read the LAST line first.** It names the problem: `ValueError`, and the bad value `'thirty'`.

---

## Live demo & your turn

- Live: `greet.py`, then a "years to graduation" calculator. We'll break it once on purpose.
- You: `examples/session-01/practice.md` — build a GPA-or-BMI style script.

---

## Traps recap

- `input()` → **always a string**; convert with `int()`/`float()`.
- `print(a, b)` (comma → spaces) vs `print(a + b)` (must be same type).
- `int(3.9)` truncates to `3`; use `round()` to round.

## Summary
You can run code, name values, convert types, format output, and read an error.
**Next:** *Part B of this session* — the dynamic-typing traps.

---

# Part B
## The Dynamic-Typing Traps

---

## A name is just a label

Python won't lock a name to a type — it can point at an `int` now and a
`str` later. That freedom is powerful, but it creates **traps** where the
result contradicts your intuition.

> This half is hands-on. Every rule below has a one-line, runnable trap in
> **Traps — predict, then run** at the bottom of the page. Predict first,
> then reveal.

---

## `==` value, `is` identity

- `==` asks "same value?" — almost always what you want.
- `is` asks "same object?" — use it only for `None` (and `True`/`False`).
- `b = a` does **not** copy: both names point at one list, so mutating `a`
  shows through `b`. Copy with `list(a)` or `a[:]`.

🧠 Same GPA = `==`. Same student = `is`.

---

## Booleans are integers

- `bool` is a *subtype* of `int`, so `True` behaves as `1` and `False` as `0`.
- That means `5 + True` works, and `sum(flags)` counts how many are `True`.
- Identity still differs, and `isinstance(True, int)` is true while
  `type(True) is int` is not.

🧠 Dummy coding (1/0) baked right into the language.

---

## Numbers: int, float, division

- `/` **always** returns a float (`4 / 2` is `2.0`); `//` floors **toward −∞**.
- `3 == 3.0` compares by value, but decimals are stored in **binary**, so
  `0.1 + 0.2` is not exactly `0.3`.
- Never test two floats with `==` — use `math.isclose(a, b)`. (You already
  never compare two measured scores for exact equality; same instinct.)

---

## Comparing across types

- `==` / `!=` across types returns `False` and never crashes.
- `<` / `>` across incompatible types raises **TypeError** — the computer can
  ask "same?" but can't *rank* text against numbers.
- A list and a tuple with the same contents are **never equal**; sequences
  compare element by element.

---

## Truthiness

- Falsy: `0  0.0  ""  []  {}  set()  None`. Truthy: everything else —
  including `"0"`, `"False"`, and `[0]`.
- Idiom: `if scores:` rather than `if len(scores) > 0:`.
- But convert user text first — `"0"` is truthy.

---

## Now spring the traps

Open **Traps — predict, then run** below: ~18 one-line traps. For each one,
**say your prediction out loud, then run it** to reveal the real result and
the reason behind it.

Then in `examples/session-01/practice.md`: write `clean_score(value)` that
accepts `5`, `5.0`, or `"5"` and returns a float, rejecting nonsense — safely.

**Next:** Control flow & data structures.
