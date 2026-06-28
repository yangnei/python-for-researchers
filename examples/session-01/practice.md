# Session 1 — Practice: Types & the Type Traps

This 2-hour session has two halves. Do **Part A** after the first topic, **Part B** after the second. Predict every output before you run it.

## Part A — Running Python, Variables & Types

Type each solution yourself. Predict output before running. Solutions at the bottom.

### Task 1 — Warm-up REPL
In the REPL (`python3`), check the type of: `42`, `42.0`, `"42"`, `True`, `None`, `7/2`, `7//2`.
*What surprises you?* (Hint: `7/2`.)

### Task 2 — GPA reporter (`gpa.py`)
Ask for a name and a GPA (a decimal). Print:
`"<name>'s GPA is <gpa to 2 decimals>, which is <87.5%> of a 4.0 scale."`

### Task 3 — Survey age bucket (`age.py`)
Ask for an age (integer). Print the age, and the age in "months lived" (age × 12).
Then deliberately type `twenty` instead of a number and **read the traceback's last line.**

### Task 4 — Stretch: the string trap
Without converting, what does `input("a: ") + input("b: ")` print if you type `2` then `3`?
Now fix it so it prints `5`.

### Bonus — Pythonic idiom drill
Cover the `# ->` answers, predict each line, then run.

```python
a, b = 1, 2
a, b = b, a;          print(a, b)        # -> 2 1   (swap, no temp variable)
print(f"{a + b = }")                     # -> a + b = 3   (self-documenting f-string)
print("CS50".lower(), "  hi ".strip())   # -> cs50 hi
print("@" in "ana@uni.edu", len("data")) # -> True 4   (membership + length)
```

## Part B — The Dynamic-Typing Traps

### Predict-the-output gauntlet
For each line, write *why* (one sentence). Predict, then run to check.

```python
True + True            # 2     — bools are ints; True is 1
3 == 3.0               # True  — numbers compare by value
0.1 + 0.2 == 0.3       # False — binary float rounding
5 == "5"               # False — different types, no error
5 > "5"                # 💥    — can't ORDER int vs str
[1,2] == (1,2)         # False — list vs tuple are different types
bool("0")              # True  — non-empty string is truthy
x=[1]; y=x; x.append(2); y   # [1,2] — y is an alias of x
```

### Build `clean_score()`
Write a function that safely turns a value into a float on a 0–100 scale:

```python
def clean_score(value):
    """
    Accept 87, 87.0, or "87" and return 87.0 (a float).
    - Reject anything outside 0..100 with a clear message (return None).
    - Compare floats safely (no exact ==).
    """
```
Test it on: `87`, `87.0`, `"87"`, `"eighty"`, `120`, `True`.
*What does `True` do, and why? (Hint: bool is an int...)*

### Bonus — Pythonic idiom drill
Cover the `# ->` answers, predict each line, then run.

```python
x = int("257"); y = int("257")
print(x == y, x is y)                # -> True False   (equal value, different objects)
print(float("nan") == float("nan"))  # -> False        (NaN equals nothing, not even itself)
```

---

## Solutions

### Part A — Running Python, Variables & Types

```python
# Task 2 — gpa.py
name = input("Name: ")
gpa = float(input("GPA: "))
print(f"{name}'s GPA is {gpa:.2f}, which is {gpa/4:.1%} of a 4.0 scale.")

# Task 3 — age.py
age = int(input("Age: "))
print(f"You are {age} years old, about {age*12} months.")
# Typing "twenty" -> ValueError: invalid literal for int() with base 10: 'twenty'

# Task 4
# "2" + "3" -> "23"  (string concatenation)
a = int(input("a: ")); b = int(input("b: "))
print(a + b)          # 5
```

### Part B — The Dynamic-Typing Traps

```python
import math

def clean_score(value):
    # Reject bools explicitly — they'd sneak through as ints (True == 1).
    if isinstance(value, bool):
        print(f"Rejected {value!r}: looks like a flag, not a score.")
        return None
    try:
        score = float(value)              # handles int, float, and numeric strings
    except (ValueError, TypeError):
        print(f"Rejected {value!r}: not a number.")
        return None
    if not 0 <= score <= 100:
        print(f"Rejected {value!r}: out of range 0–100.")
        return None
    return score

for v in [87, 87.0, "87", "eighty", 120, True]:
    print(v, "->", clean_score(v))
# 87->87.0, 87.0->87.0, "87"->87.0, "eighty"->None, 120->None, True->None
```
Key lesson: `float(True)` is `1.0`, so without the explicit bool check a flag would
pass as a valid score. This is the `bool ⊂ int` trap in a real function.
