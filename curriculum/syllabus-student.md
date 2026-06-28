# Learn Python — Student Syllabus

Welcome. This is a fast, ~12-hour path (five two-hour sessions, **each covering two topics**) from
"never coded" to "I can write a real Python program to wrangle my research data." It's re-ordered
for you and front-loaded with the language quirks that trip people up.

**How each 2-hour session runs:** two halves around a short break. Each half is Concept (≈22 min) →
I code, you watch (≈12 min) → **you code (≈25 min)**, then a combined recap + quiz at the end. The
practice is the biggest part on purpose — you learn by typing. You will *type every example yourself*.

**What you need:** Python 3.11+, VS Code (or any editor), and this folder. Open the matching
`slides/`, `examples/`, and `cheatsheets/` file for each session. (A full **PDF** of the course
is downloadable from the website, and every session is also a **Jupyter notebook** you can run in
the browser — no install.)

---

## The 5 sessions (2 hours each, two topics per session)

| # | Title | You'll be able to… | Files |
|---|---|---|---|
| 1 | **Running Python, Types & the Type Traps** | Run code, use `int/float/str/bool/None` & f-strings; tell `==` from `is`, predict `True==1` / `0.1+0.2` / `5=="5"`, check types right | `slides/session-01` · `examples/session-01` |
| 2 | **Control Flow & Data Structures** | `if/elif/else`, chained comparisons, `for`/`while`, `enumerate`/`zip`; `list/tuple/dict/set`, comprehensions, sorting, aliasing | `slides/session-02` · `examples/session-02` |
| 3 | **Functions, Scope & Recursion** | Write reusable functions, `*args/**kwargs`, type hints, dodge the mutable-default bug; write functions that call themselves, trace the call stack, recurse over nested data | `slides/session-03` · `examples/session-03` |
| 4 | **Exceptions, Files & Research Data** | Validate messy input with `try/except` + a first test; read/write CSV survey data, use `statistics`/`datetime`, `pip install`, pandas teaser | `slides/session-04` · `examples/session-04` |
| 5 | **Regular Expressions, Modules & OOP** | Validate, extract, and clean real text with regex; import modules, build a small class with `@property`, use generators/`map`/`filter`/walrus | `slides/session-05` · `examples/session-05` |
| 6 | **Capstone (optional)** | Build a Gradebook & Survey Analyzer end-to-end | `assessments/capstone-project` |

Session 1's **type traps** (Part B) are the most load-bearing material in the course — if you
deeply master one half, make it that one.

---

## Your standing toolkit (open these any time)
- **`cheatsheets/traps-and-gotchas.md`** — every quirk, with the wrong vs right way. *Keep this open.*
- **`cheatsheets/quick-reference.md`** — syntax you'll forget (slicing, f-strings, comprehensions).
- **`cheatsheets/glossary.md`** — plain-language definitions of every term.

## How to study (specific to this material)
1. **Type, don't read.** Re-type every example in `examples/`; change one thing and predict the result *before* you run it.
2. **Predict-then-run on traps.** For Session 1's Part B especially, guess the output, then run. The surprise *is* the lesson.
3. **Do both halves' practice.** Each session is sized for a fast learner — aim to finish Part A and Part B, not just the first few tasks.
4. **Keep a "bugs I hit" log.** When you get a traceback, write the last line + your fix. You'll build your own personalized cheat sheet.
5. **Connect to what you know.** Every topic maps to research methods/stats (see `connection-map.md`). Lean on those bridges.

## What "done" looks like
You finish the capstone (S6) or, at minimum, complete every session's practice and score the
per-session quizzes in `assessments/`. The real test: you can open a messy CSV of your own data and
write a short script that summarizes it without copying from anyone.

## Scope (so you're not surprised)
This makes you a confident *programmer who handles research data*. It is **not** a full data-science
course — pandas, plotting, and statistical modeling get a taste, not a deep dive. Those are the
natural next step once these fundamentals are solid.
