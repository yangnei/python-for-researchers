# Master Course Outline — Python for an Education Researcher

> Single source of truth. The student and teacher syllabi both derive from this.
> 9 core one-hour sessions + 1 optional capstone hour = **8–10 hours**.

## How this maps to CS50P

CS50P teaches in this order: 0 Functions/Variables · 1 Conditionals · 2 Loops · 3 Exceptions
· 4 Libraries · 5 Unit Tests · 6 File I/O · 7 Regular Expressions · 8 OOP · 9 Et Cetera.

We **re-sequence** for an adult learner: we pull the dynamic-typing fundamentals forward into
Session 2 (CS50 scatters them across weeks 0/1/8/9), and we fold the "Et Cetera" power-tools
(comprehensions, generators, `*args`, type hints) into the sessions where they naturally belong
instead of dumping them at the end. Each session below lists the CS50P week(s) it draws from.

## Design rules (from the e-learning pipeline)
- Every session = one hour, structured **Concept → Live Example → Practice → Traps → Summary**.
- Every session has 2–4 learning objectives; every objective is testable in that session's quiz.
- Every abstract idea ships with a runnable, education-flavored example.
- Difficulty rises monotonically; nothing is used before it's introduced (except clearly-flagged teasers).

---

## Session 1 — Running Python, Variables & Types *(CS50P W0)*
**Objectives**
1. Run Python both interactively (REPL) and as a `.py` script; read a traceback without panic.
2. Use variables and the core built-in types: `int`, `float`, `str`, `bool`, `None`.
3. Do I/O with `input()`/`print()`, format with f-strings, and convert types with `int()`/`float()`/`str()`.

**Key idea the beginner misses:** `input()` *always* returns a `str`; numbers from users must be converted.

---

## Session 2 — The Dynamic-Typing Traps (THE CORE SESSION) *(CS50P W0/W1/W9)*
**Objectives**
1. Distinguish **value equality (`==`)** from **identity (`is`)** and know when each is correct.
2. Predict results when mixing numeric types: `bool` ⊂ `int`, `int`/`float`, and **float precision**.
3. Check types correctly with `isinstance()` vs `type()`, and reason about truthiness.

**This is the session the whole course is built around** — it front-loads every trap in the
learner's brief (`==` vs `is`, `True == 1`, `3 == 3.0`, `0.1 + 0.2`, `5 == "5"` vs `5 > "5"`,
sequence comparison, `isinstance`). Everything later assumes this fluency.

---

## Session 3 — Conditionals & Boolean Logic *(CS50P W1)*
**Objectives**
1. Write `if`/`elif`/`else`; use comparison and logical operators and **chained comparisons**.
2. Use `and`/`or`/`not` correctly, including **short-circuit** behavior and operand-return semantics.
3. Refactor nested conditionals into clean Pythonic form (ternary, early `return`, `match`/`case`).

**Trap focus:** `if x == True`, `is None` vs `== None`, `and`/`or` returning a value (not a bool).

---

## Session 4 — Loops & Iteration *(CS50P W2)*
**Objectives**
1. Write `for` and `while` loops; control them with `break`, `continue`, and the loop-`else`.
2. Iterate the Pythonic way with `range`, `enumerate`, and `zip` instead of index juggling.
3. Build the `while True:` input-validation pattern used throughout the rest of the course.

**Trap focus:** off-by-one in `range`, mutating a list while iterating it, `for/else`.

---

## Session 5 — Data Structures: list, tuple, dict, set *(CS50P W2/W6/W9)*
**Objectives**
1. Choose between `list`, `tuple`, `dict`, and `set`; index, slice, and nest them.
2. Sort with `sorted(..., key=...)` and lambdas; build **list/dict comprehensions**.
3. Reason about **mutability & aliasing** (copy vs reference, shallow vs deep copy).

**Trap focus:** aliasing (`b = a`), `list * n` shared rows, mutable default arguments (preview),
element-by-element sequence comparison, set deduplication of survey data.

---

## Session 6 — Functions, Scope & Reusability *(CS50P W0/W9)*
**Objectives**
1. Define functions with positional, keyword, default, `*args`, and `**kwargs` parameters.
2. Explain scope (LEGB), `return` vs `print`, and avoid the `UnboundLocalError`/`global` trap.
3. Document with docstrings and annotate with **type hints** (and know hints aren't enforced).

**Trap focus:** the **mutable default argument** bug, late-binding closures, implicit `None` return.

---

## Session 7 — Exceptions & Defensive Code *(CS50P W3/W5)*
**Objectives**
1. Handle errors with `try`/`except`/`else`/`finally`; raise `ValueError` etc. deliberately.
2. Validate real, messy human/research input robustly (EAFP "ask forgiveness" style).
3. Use `assert` and write a first `pytest` test for a function.

**Trap focus:** bare `except:`, catching too broadly, swallowing errors silently.

---

## Session 8 — Files, Libraries & Research Data *(CS50P W4/W6)*
**Objectives**
1. Read/write text with `open`/`with`; understand file modes and why `with` matters.
2. Load and write **CSV** survey/gradebook data with `csv.DictReader`/`DictWriter`; touch `json`.
3. `import` standard-library tools a researcher reaches for (`statistics`, `random`, `datetime`,
   `pathlib`) and install a third-party package with `pip` (guided `pandas` teaser).

**Trap focus:** `"w"` silently overwrites, forgotten `newline=""`/`\n`, file encoding.

---

## Session 9 — Organizing Code: Regex, Modules, OOP & "Pythonic" *(CS50P W5/W7/W8/W9)*
**Objectives**
1. Clean and validate strings with regular expressions (`re.search`, groups, raw strings).
2. Split code into modules; model a domain entity with a small **class** (`__init__`, `__str__`, `@property`).
3. Recognize and apply the "Pythonic" power-tools recap: comprehensions, `enumerate`/`zip`,
   generators/`yield`, `map`/`filter`, the walrus `:=`.

**Trap focus:** `.` matches any char in regex, forgetting raw strings, `self` confusion.

---

## Session 10 (Optional) — Capstone Project *(integrative)*
**Objective:** Independently build one small, end-to-end program on a real-ish education dataset.
Default brief: **"Gradebook & Survey Analyzer"** — read a CSV of students + Likert responses,
clean and validate it, compute summary statistics, flag at-risk students, and write a report CSV.
Alternative briefs are listed in `assessments/capstone-project.md`.

---

## Coverage check (every CS50P topic lands somewhere)
| CS50P Week | Where it lives here |
|---|---|
| 0 Functions, Variables | S1, S6 |
| 1 Conditionals | S3 (+ traps in S2) |
| 2 Loops | S4, S5 |
| 3 Exceptions | S7 |
| 4 Libraries | S8 |
| 5 Unit Tests | S7 (+ S9 modules) |
| 6 File I/O | S8 (+ data structures S5) |
| 7 Regular Expressions | S9 |
| 8 OOP | S9 |
| 9 Et Cetera (sets, comprehensions, `*args`, type hints, generators, `map`/`filter`) | S5, S6, S9 |

## Scaling to the time budget
- **Exactly 8 hours:** merge S8+S9's lighter halves, drop the `pandas` teaser and regex depth.
- **9 hours:** run S1–S9 as written (recommended).
- **10 hours:** add S10 capstone.
