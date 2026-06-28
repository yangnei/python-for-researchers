# Master Course Outline — Learn Python

> Single source of truth. The student and teacher syllabi both derive from this.
> **5 core two-hour sessions** + 1 optional capstone session (~12 hours core, ~14 with the capstone).
> Each session covers **two paired topics** (Part A + Part B) around a mid-session break.

## How the topics are sequenced

A typical intro-Python course teaches roughly: functions/variables → conditionals → loops →
exceptions → libraries → unit tests → file I/O → regular expressions → OOP → assorted
"power-tools."

We **re-sequence and pair** for a fast adult learner. A strong self-learner clears one of those
topics in well under an hour, so stretching one across a two-hour session wastes the back half.
Instead each two-hour session bundles **two related topics** that share a through-line:

1. **Types → the type traps.** You can't reason about the traps until you know the types, and the
   traps are the whole reason this course exists — so they lead, together, on day one.
2. **Control flow → data structures.** Loops are most useful over the containers worth looping; a
   list of dicts is just a dataset.
3. **Functions → recursion.** Recursion is a function that calls itself, so it lands while function
   mechanics are fresh — and nested data (from S2) is the payoff.
4. **Exceptions → files & research data.** Surviving one dirty value scales straight into cleaning a
   whole CSV of them.
5. **Regex → modules & OOP.** The two "finishing" skills: clean any text, then organize code into
   modules and a small class.

The power-tools (comprehensions, generators, `*args`, type hints, the walrus) are folded into the
sessions where they naturally belong, not saved for the end.

## Design rules (from the e-learning pipeline)
- **Every session = two hours = two paired topics**, run **Part A → break → Part B → combined recap**.
- Each half is **Concept → Live Example → Practice**; practice is woven into both halves plus a short
  combined block (**~1 hour hands-on total**), packed because this learner moves fast.
- Every session has 4–6 learning objectives (≈2–3 per half); every objective is testable in that
  session's quiz.
- Every abstract idea ships with a runnable, education-flavored example.
- Difficulty rises monotonically; nothing is used before it's introduced (except clearly-flagged teasers).

---

## Session 1 — Running Python, Types & the Type Traps
*Part A — Running Python, Variables & Types · Part B — the Dynamic-Typing Traps (the core of the course)*

**Objectives**
1. Run Python interactively (REPL) and as a `.py` script; read a traceback without panic.
2. Use the core types (`int`, `float`, `str`, `bool`, `None`); do I/O with `input()`/`print()`,
   f-strings, and `int()`/`float()`/`str()` (remember `input()` is always a `str`).
3. Distinguish **value equality (`==`)** from **identity (`is`)**; predict `bool ⊂ int`
   (`True == 1`), `int`/`float`, and **float precision** (`0.1 + 0.2`).
4. Check types with `isinstance()` vs `type()`, handle `5 == "5"` vs `5 > "5"`, and reason about truthiness.

**Why it leads:** the whole course is built around the type traps (`==` vs `is`, `True == 1`,
`0.1 + 0.2`, `5 == "5"`). Front-loading them — right after the types they concern — means every
later session can assume the fluency.

---

## Session 2 — Control Flow & Data Structures
*Part A — Conditionals & Loops · Part B — list / tuple / dict / set*

**Objectives**
1. Write `if`/`elif`/`else` with comparison & logical operators and **chained comparisons**; use
   `and`/`or`/`not` correctly (short-circuit, operand-return); avoid `if x == True`.
2. Write `for`/`while` loops; control them with `break`/`continue`; mind `range` off-by-one;
   iterate Pythonically with `enumerate`/`zip` and the `while True:` validation loop.
3. Choose between `list`/`tuple`/`dict`/`set`; index, slice, and nest them; build list/dict
   **comprehensions**; sort with `sorted(key=…)`.
4. Reason about **mutability & aliasing** (copy vs reference, `[[0]*3]*3` shared rows).

**Trap focus:** `if x == True`, `range(1,5)` excludes 5, mutating a list while iterating it,
`range(len(...))` instead of `enumerate`/`zip`, and **aliasing** (`b = a` shares the list).

---

## Session 3 — Functions, Scope & Recursion
*Part A — Functions, Scope & Reusability · Part B — Recursion*

**Objectives**
1. Define functions with positional, keyword, default, `*args`, and `**kwargs` parameters.
2. Explain scope (LEGB) and `return` vs `print`; document with docstrings and **type hints**
   (and know hints aren't enforced); dodge the `UnboundLocalError`/`global` trap.
3. Write a recursive function with a correct **base case** and **recursive case**; trace the
   **call stack**; convert between recursion and iteration; know recursion's cost (`RecursionError`,
   no tail-call optimization, limit ≈ 1000).
4. Apply recursion to **naturally nested data** (nested lists/dicts/JSON) where one loop is awkward.

**Trap focus:** the **mutable default argument** bug; forgetting to `return` (function or recursive
call returns `None`); an unreachable base case → stack overflow.

---

## Session 4 — Exceptions, Files & Research Data
*Part A — Exceptions & Defensive Code · Part B — Files, Libraries & Research Data*

**Objectives**
1. Handle errors with `try`/`except`/`else`/`finally`; `raise` deliberately; validate messy
   human/research input the EAFP way; use `assert` and write a first `pytest` test.
2. Read/write text with `open`/`with` and understand file modes (why `"w"` is dangerous).
3. Load and write **CSV** survey/gradebook data with `csv.DictReader`/`DictWriter`; touch `json`.
4. `import` the researcher's stdlib (`statistics`, `datetime`, `pathlib`), `pip install` a package,
   and meet `pandas` in a guided teaser.

**Trap focus:** bare `except:`, swallowing errors, `"w"` silently overwrites, forgotten
`newline=""`, reading a file twice.

---

## Session 5 — Regular Expressions, Modules & OOP
*Part A — Regular Expressions & Text Cleaning · Part B — Modules, OOP & the Pythonic Toolkit*

**Objectives**
1. Write patterns with raw strings and the core tokens; use `re.search`/`fullmatch`/`findall`/`sub`
   to validate, extract (capture groups), and clean real research text.
2. Split code into modules and `import` them; understand the `if __name__ == "__main__":` guard.
3. Model a domain entity with a small **class** (`__init__`, `self`, `__str__`, a validating
   `@property`, brief inheritance with `super()`).
4. Apply the **Pythonic toolkit**: comprehensions, `map`/`filter`, `enumerate`/`zip`,
   generators/`yield`, the walrus `:=`.

**Trap focus:** forgetting `r"..."`, `.` matches any char, `re.search` returns `None`, `self`
confusion, a generator exhausts after one pass, over-using a class where a function/dict fits.

---

## Session 6 (Optional) — Capstone Project *(integrative)*
**Objective:** independently build one small, end-to-end program on a real-ish education dataset.
Default brief: **"Gradebook & Survey Analyzer"** — read a CSV of students + Likert responses,
clean and validate it, compute summary statistics, flag at-risk students, and write a report CSV.
Alternative briefs are listed in `assessments/capstone-project.md`.

---

## Coverage check (every core topic lands somewhere)
| Topic | Where it lives now |
|---|---|
| Running Python, variables & types | S1 Part A |
| The dynamic-typing traps (`==`/`is`, floats, `bool⊂int`, `isinstance`) | S1 Part B |
| Conditionals | S2 Part A |
| Loops | S2 Part A (iterating data in S2 Part B) |
| Data structures (list/tuple/dict/set) | S2 Part B |
| Functions, scope & reuse | S3 Part A |
| Recursion | S3 Part B (nested data ties to S2 Part B) |
| Exceptions & unit tests | S4 Part A |
| Files & libraries (CSV, `statistics`, `pandas` teaser) | S4 Part B |
| Regular expressions | S5 Part A |
| Modules & OOP | S5 Part B |
| Power-tools (comprehensions, `*args`, type hints, generators, `map`/`filter`, walrus) | S2, S3, S5 |

## Scaling to the time budget
- **~10 hours:** drop the Pythonic-toolkit tour in S5 Part B and the `pandas`/`json` teaser in S4;
  keep both halves' core of every session.
- **~12 hours:** run S1–S5 as written, two hours each (recommended).
- **~14 hours:** add the S6 capstone.
