# Per-Session Quizzes (with answer keys)

Each quiz is ~6 questions (about three per half), ~8 minutes, given at the end of the session.
Every question maps to a session objective. **Teacher:** ask the student to *predict* code output
before they run it — the surprise is the assessment. Answers are at the end of each session block.

---

## Session 1 — Running Python, Types & the Type Traps
*Part A — Variables & Types*
1. What type does `input("x: ")` return, always?
2. What does `"5" + "3"` evaluate to? How do you get `8`? And what is `int(3.9)`?

*Part B — The Dynamic-Typing Traps*
3. `a = [1,2]; b = [1,2]` — is `a == b`? is `a is b`? Why?
4. What is `True + True`? Why?
5. Is `0.1 + 0.2 == 0.3` True or False? How should you compare them?
6. What does `5 == "5"` give? What about `5 > "5"`?

**Answers:** 1. `str`. 2. `"53"`; use `int("5") + int("3")`; `int(3.9)` is `3` (truncates).
3. `==` True (same value), `is` False (different objects). 4. `2` (bool is a subclass of int).
5. False; use `math.isclose(0.1+0.2, 0.3)` (or round). 6. `False`; `5 > "5"` raises `TypeError`
(can't order int vs str).

---

## Session 2 — Control Flow & Data Structures
*Part A — Conditionals & Loops*
1. Rewrite `if x >= 90 and x < 100:` using a chained comparison.
2. What is `5 and 0`? What is `0 or "hi"`? Why aren't they `True`/`False`?
3. What does `list(range(1, 5))` produce?

*Part B — Data Structures*
4. Which are mutable: list, tuple, dict, set?
5. `a = [1,2]; b = a; a.append(3)` — what is `b`? Why?
6. (Practical) Write a one-line dict comprehension mapping each name in `names` to `0`.

**Answers:** 1. `if 90 <= x < 100:`. 2. `0` and `"hi"` — `and`/`or` return an operand, not a bool.
3. `[1, 2, 3, 4]` (5 excluded). 4. list, dict, set are mutable; tuple is not. 5. `[1, 2, 3]` —
`b` is an alias for the same list. 6. `{n: 0 for n in names}`.

---

## Session 3 — Functions, Scope & Recursion
*Part A — Functions & Scope*
1. What's the difference between `return` and `print`?
2. Why is `def f(x, items=[])` dangerous? What's the fix?
3. What does a function with no `return` statement return? Are type hints enforced at runtime?

*Part B — Recursion*
4. What two parts must every recursive function have?
5. What error comes from a base case that's never reached, and why doesn't Python just keep going?
6. Why is recursion a natural fit for nested data (a list of lists, or nested JSON)?

**Answers:** 1. `return` hands a value to the caller; `print` only displays. 2. The default list is
created once and persists across calls; use `items=None` then create inside. 3. `None`; and no —
type hints are documentation (`mypy` checks them optionally). 4. A **base case** (stops) and a
**recursive case** (calls itself on a smaller input, toward the base case). 5. `RecursionError` —
Python has no tail-call optimization, so each pending call keeps a stack frame until the limit
(~1000). 6. The data is *defined in terms of itself* (a list may contain lists), so a function
defined in terms of itself mirrors its shape and can reach every level.

---

## Session 4 — Exceptions, Files & Research Data
*Part A — Exceptions*
1. Which exception does `int("N/A")` raise? Wrap `int(value)` so it returns `None` on failure.
2. Why is a bare `except:` dangerous?
3. When should you use `raise` vs `assert`?

*Part B — Files & Data*
4. What does opening a file in `"w"` mode do to existing contents? Why prefer `with open(...)`?
5. After `csv.DictReader`, what type is each row?
6. CSV values read from a file are what type — and what must you do with numbers?

**Answers:** 1. `ValueError`; `try: return int(value) except (ValueError, TypeError): return None`.
2. It catches everything (even Ctrl+C and your own typos) and can hide bugs. 3. `raise` to validate
real/untrusted input; `assert` for developer sanity checks (can be disabled). 4. Truncates it to
empty immediately; `with` auto-closes even if the code crashes. 5. A `dict` keyed by the header
row. 6. Strings; convert with `int()`/`float()`.

---

## Session 5 — Regular Expressions, Modules & OOP
*Part A — Regular Expressions*
1. In regex, what does `.` match? How do you match a literal dot?
2. Why write regex patterns as raw strings `r"..."`?
3. What does `re.search` return when there's no match, and what must you do before `.group()`?

*Part B — Modules & OOP*
4. In a class, what is `self`?
5. What happens if you iterate a generator twice?
6. Why doesn't a module's `if __name__ == "__main__":` block run when you `import` it?

**Answers:** 1. Any character (except newline); use `\.` for a literal dot. 2. So backslashes
aren't treated as Python string escapes. 3. It returns `None`; check `if m:` before `m.group()` or
you'll hit an `AttributeError`. 4. The current instance ("this particular object"). 5. The second
pass is empty — a generator is exhausted after one iteration. 6. On import, `__name__` is the
module's name, not `"__main__"`, so the block is skipped.

---

## Scoring guide (formative, not graded)
- **All correct, explained why:** ready for the capstone.
- **Right answer, fuzzy why:** re-do that session's `traps-and-gotchas` rows.
- **Wrong on Session 1 Part B items:** revisit the type traps before continuing — they're load-bearing.
