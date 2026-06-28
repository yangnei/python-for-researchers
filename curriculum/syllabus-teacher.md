# Learn Python — TEACHER Edition

Everything in the student syllabus, **plus** the instructor scaffolding: a minute-by-minute clock
for each two-hour session, transition scripts (how to move between blocks without dead air), predicted
misconceptions for *this* learner, Socratic prompts (DeepTutor-style — ask, don't tell), and an
explicit **"if you're behind, cut this"** line per session.

Each two-hour session covers **two topics** — **Part A** and **Part B** — around a mid-session
break. That's the point of the format: a fast learner clears a topic in under an hour, so we pair
two related topics per session instead of stretching one thin.

## How to read this document
Each session has:
- **Covers** — the two topics (Part A / Part B) this session bundles.
- **Pre-flight** — what to have open/ready before the student arrives.
- **The clock** — a 120-minute breakdown: Part A, a break, Part B, then a combined recap. Keep a timer visible. The numbers are targets, not law.
- **Transitions** — short scripted lines to hand off cleanly between blocks.
- **Predicted misconceptions** — where THIS learner (expert in research, novice in code) will stumble.
- **Socratic prompts** — questions to ask instead of explaining; let them derive it.
- **Cut line** — the first thing to drop if you're running over.

## Universal pacing principles (this learner is fast)
- **Talk less than you want to.** He reads fast and abstracts well. Default to "here's the rule, here's the trap, now you try."
- **Protect — and fill — the practice time.** Roughly **an hour of hands-on** per session, split across the two halves plus a short combined block. It's packed on purpose: he finishes individual tasks quickly, so each half carries *more* tasks rather than more minutes. If concept overruns, steal from your own talking, never from his typing.
- **Predict-then-run is the engine, especially the Session 1 traps.** Always have him *commit to an answer out loud* before running. The cognitive surprise is the teaching moment.
- **Two topics, one through-line.** Each pairing shares a thread (types→the type traps; functions→recursion; exceptions→dirty file data). Name the thread at the Part A→B handoff so the session feels like one arc, not two.
- **Don't pad.** Each clock is tight by design. If he's ahead, give him the next practice task or a stretch goal, not more talking.
- **Carry a running "misconceptions log"** (DeepTutor "learning memory"): note every trap he hit this session; re-surface it as a 60-second warm-up next session.

---

## SESSION 1 — Running Python, Types & the Type Traps
**Covers:** Part A — Running Python, Variables & Types; Part B — the Dynamic-Typing Traps (the most important material in the course).
**Pre-flight:** terminal + VS Code open; `examples/session-01/` ready; a deliberately broken line staged to show a traceback; `cheatsheets/traps-and-gotchas.md` open for Part B.

**The clock (120 min)**
- **0:00–0:06 — Orientation.** Why Python, why this re-ordered path, how a two-hour session works (two halves, one break). Don't oversell; he wants to start.
- **0:06–0:26 — Part A concept.** REPL vs script; `python file.py`. Variables as *labels on objects* (Connection Map #1). The five core types; `type(x)`. `input()` → always `str`. f-strings. `int()/float()/str()`.
- **0:26–0:48 — Part A live + you-try.** Build `greet.py` then "years to graduation" together; trigger and *read* one traceback (last line first). Then he starts `examples/session-01/practice.md` Part A (GPA reporter, age bucket, the string-concatenation trap).
- **0:48–0:56 — Break.**
- **0:56–1:22 — Part B concept + demo (predict-then-run).** This is the heart of the course; tell him so. `==` vs `is` (value vs identity, Connection Map #3) with a mutable-list demo and `is None`; `bool ⊂ int` (`True == 1`, `sum([T,F,T])`, Connection Map #4); **float precision** `0.1 + 0.2` → `math.isclose` (Connection Map #5); `5 == "5"` is `False` but `5 > "5"` raises; `isinstance` vs `type`; truthiness. He predicts every line *out loud* before you run it.
- **1:22–1:48 — Part B you-try.** `examples/session-01/practice.md` Part B: the predict-the-output gauntlet, then `clean_score()` handling int/float/str (and rejecting `bool`).
- **1:48–1:56 — Traps recap (both halves).** `input()` → string; `int(3.9)` truncates; `==` vs `is`; never `==` raw floats. Hand him the trap cheat sheet as his permanent reference.
- **1:56–2:00 — Summary + quiz. Next:** control flow & data structures.

**Transitions**
- A concept→live: *"Enough theory — watch me make these mistakes so you don't have to."*
- A→B (the thread): *"You now know the five types. Here's the catch: Python lets them mix in ways that surprise everyone. Cover the right column and predict each line."*
- B→recap: *"These eight traps are 80% of week-one bugs. Let's name them once more, then they're yours."*

**Predicted misconceptions (this learner)**
- Expects `input()` to give a number → `"5" + "3" == "53"`.
- Thinks `=` asserts equality (math habit). Reinforce label-on-object now; it pays off in Part B and in Session 2's aliasing.
- Assumes `is` is a stylistic `==` — nail it with the mutable-list demo.
- Trusts `==` on floats out of stats habit ("I round anyway") — stress the *cause* is binary storage, not data.
- Over-generalizes the `TypeError` and thinks `5 == "5"` errors too. It returns `False` — show it.

**Socratic prompts**
- "What type do you think `input()` hands back? How could we check?" (→ `type(...)`)
- "Two students, same 3.7 GPA. `==`? `is`? Why?"
- "If `0.1 + 0.2` isn't `0.3`, is the bug in the data or in the computer? How would you test 'close enough'?"
- "`5 == '5'` is False, fine. So why does `5 > '5'` *crash*?"

**Cut line:** drop the small-int-cache and `nan` wrinkles, and the years-to-graduation demo; **never** cut the Part B `==`/`is`, float, and `isinstance` core or its practice.

---

## SESSION 2 — Control Flow & Data Structures
**Covers:** Part A — Conditionals & Loops; Part B — list / tuple / dict / set.
**Pre-flight:** `examples/session-02/`; a messy nested-`if` staged for the refactor; `Ctrl+C` ready for the infinite-loop demo; a "list of dicts = tidy dataset" diagram (Connection Map #6).

**The clock (120 min)**
- **0:00–0:06 — Warm-up.** S1 traps recap (60-sec quiz from your log).
- **0:06–0:30 — Part A concept.** `if/elif/else`; **chained comparisons** (`90 <= x < 100` — reads like math); `and/or/not`, short-circuit, `and/or` return an *operand*; `while` (+ infinite-loop demo); `for ... in`; `range` (off-by-one!); `break`/`continue`; the `while True: … break` validation pattern; **`enumerate`/`zip`** as the antidote to `range(len(...))`.
- **0:30–0:52 — Part A live + you-try.** A Likert→label classifier (chained comparison + early `return`); sum/average a roster two ways (index vs `enumerate`/`zip`); a robust "ask until valid" loop. He then starts `examples/session-02/practice.md` Part A (grade-band classifier — test every boundary — and the validation loop).
- **0:52–1:00 — Break.**
- **1:00–1:24 — Part B concept + live.** `list`(mutable)/`tuple`(immutable)/`dict`(key→value)/`set`(unique); indexing & **slicing**; nesting → **list of dicts = a dataset**; list/dict comprehensions; `sorted(key=lambda …)`. Live: build a roster as a list of dicts, sort by score, dedupe answers with a `set`, rewrite a loop as a comprehension.
- **1:24–1:48 — Part B you-try.** `examples/session-02/practice.md` Part B: group by grade band into a dict, `{name: average}` in one comprehension, slice/sort tasks, and the **aliasing** bug then its fix.
- **1:48–1:56 — Traps recap (both halves).** `if x == True` (just `if x`); `range(1,5)` excludes 5; **mutating a list while looping it**; `range(len(...))` vs `enumerate`/`zip`; **aliasing** (`b = a` shares the list) and `[[0]*3]*3` shared rows.
- **1:56–2:00 — Summary + quiz. Next:** functions, scope & recursion.

**Transitions**
- A concept→live: *"Watch me turn an ugly five-level `if` into three readable lines — then loop a whole roster."*
- A→B (the thread): *"You can loop over data now. Next: the containers worth looping — and a list of dicts is just a tidy dataset, rows as dicts, keys as your variables."*
- B→recap: *"One last thing that bites everyone — assignment doesn't copy. Watch `b` change when I never touched it."*

**Predicted misconceptions**
- Writes `if score >= 90 and score < 100` — show chaining `90 <= score < 100`.
- Boundary errors (`>=` vs `>`) at cutoffs — make him test 89.999 / 90 / 90.001.
- `range(len(x))` index habit (from R/SPSS vectorized thinking) — push `enumerate`/`zip`.
- Removes items from a list *while iterating it* → demo the bug, then iterate a copy / build a new list.
- **Aliasing** is the big one — expects `b = a` to copy. Show `a.append(...)` changing `b`; tie to S1 "label on object."

**Socratic prompts**
- "`x = 5 and 0` — what's `x`? Why isn't it `True`/`False`?"
- "You need both the position and the value. What's cleaner than indexing?"
- "`b = a; a.append(99)` — what's in `b`? Why? (Labels, not boxes.)"
- "Survey gave duplicate free-text answers. What structure removes duplicates for free?"

**Cut line:** drop `match/case`, `for/else`, and deep-copy/`[[0]*3]*3`; keep chained comparisons, `enumerate`/`zip`, the validation loop, comprehensions, and aliasing basics.

---

## SESSION 3 — Functions, Scope & Recursion
**Covers:** Part A — Functions, Scope & Reusability; Part B — Recursion.
**Pre-flight:** `examples/session-03/`; the **mutable-default-arg** demo staged (Part A headline); a nested-JSON-shaped dict staged for `deep_sum`, and the `runaway` overflow + `sys.getrecursionlimit()` queued for Part B.

**The clock (120 min)**
- **0:00–0:06 — Warm-up.** S2 traps recap (aliasing, mutate-while-iterating).
- **0:06–0:28 — Part A concept.** `def`; parameters (positional/keyword/default, `*args`/`**kwargs`); `return` vs `print`; scope (LEGB), `global` and why to avoid it; docstrings; **type hints** ("not enforced; `mypy` checks them"). Keyword-only args and a one-line decorator if time allows.
- **0:28–0:52 — Part A live + you-try.** Refactor S2 inline code into `class_average`/`letter_grade`; then the **mutable-default bug** live (`def add(x, bag=[])` accumulating) → fix with `bag=None`. He starts `examples/session-03/practice.md` Part A (a small grade-functions library with hints/docstrings; reproduce-then-fix the mutable default).
- **0:52–1:00 — Break.**
- **1:00–1:24 — Part B concept + live.** The two parts: a **base case** and a **recursive case** that moves toward it. Trace `factorial(3)` as a stack that builds then unwinds; recursion vs iteration; the cost (each pending call is a frame; **no tail-call optimization**, limit ≈ 1000). Live: `countdown`/`factorial`, then `deep_sum` over nested data (the payoff a single loop can't reach), then a `RecursionError` read together. Mention `@lru_cache`.
- **1:24–1:48 — Part B you-try.** `examples/session-03/practice.md` Part B: recursive sum, `flatten`, `depth`, and the two trap-fixes (missing base case; forgetting to `return` the recursive call).
- **1:48–1:56 — Traps recap (both halves).** Mutable default; forgetting `return` (function/ recursion returns `None`); `UnboundLocalError`; unreachable base case → stack overflow; recursion isn't free.
- **1:56–2:00 — Summary + quiz. Next:** exceptions, files & research data.

**Transitions**
- A concept→live: *"This next bug has burned every Python programmer once. Watch the list keep growing across calls."*
- A→B (the thread): *"A function can call other functions. The mind-bender: it can call *itself*. That's exactly the tool for data defined in terms of itself — nested data."*
- B live→you-try: *"Say the base case out loud before you write the function — that's where the bugs hide."*

**Predicted misconceptions**
- Won't believe the default list persists until shown twice; then explain defaults evaluate *once, at definition*.
- Thinks a function that `print`s has "returned" the value → show `x = show(...)` is `None`.
- Expects type hints to enforce types → show `add("a","b")` still runs.
- Writes the recursive case but forgets to `return` it → silent `None`.
- From a vectorized stats background, may not see when recursion beats a loop → the nested-data demo is the "aha"; and may assume recursion is a free swap → show the limit.

**Socratic prompts**
- "I called `add(1)` three times and the list keeps growing. When does `bag=[]` actually run?"
- "`print` vs `return` — which lets the *next* function use the result?"
- "What's the smallest input where the answer is obvious without recursing? That's your base case."
- "Your data is a list that can contain lists. What kind of function matches a thing defined in terms of itself?"

**Cut line:** drop decorators/closures in Part A and the `depth`/string-reverse tasks in Part B; **never** cut the mutable-default demo or `deep_sum` on nested data.

---

## SESSION 4 — Exceptions, Files & Research Data
**Covers:** Part A — Exceptions & Defensive Code; Part B — Files, Libraries & Research Data.
**Pre-flight:** `examples/session-04/` with `students.csv` + `survey.csv`; a dirty list ("N/A", "", "7" on a 1–5 scale) staged; confirm `pip` works and have `pandas` ready for the teaser.

**The clock (120 min)**
- **0:00–0:06 — Warm-up.** S3 traps recap (mutable default; forgotten `return`).
- **0:06–0:28 — Part A concept.** Errors vs exceptions; `try/except/else/finally`; common types (`ValueError`, `KeyError`, `FileNotFoundError`); `raise ValueError(...)`; a custom exception subclass; **EAFP** vs LBYL; `assert` (a developer check, can be disabled — not input validation).
- **0:28–0:52 — Part A live + you-try.** Harden `safe_int()`/`clean_likert()` against blanks/"N/A"/out-of-range; a first `pytest.raises` test. He starts `examples/session-04/practice.md` Part A (validate a raw response list into clean values + a rejection log; add a `raise`).
- **0:52–1:00 — Break.**
- **1:00–1:24 — Part B concept + live.** `open`/`with` (auto-close); modes (`r/w/a`; **`w` overwrites!**); **CSV** via `csv.DictReader`/`DictWriter` (rows as dicts → ties to S2); `json`; researcher stdlib (`statistics`, `datetime`, `pathlib`). Live: read `students.csv` → list of dicts, class mean with `statistics.mean`, write a summary CSV; then the **`pandas` teaser** ("same thing in three lines — that's your next course").
- **1:24–1:48 — Part B you-try.** `examples/session-04/practice.md` Part B: per-item survey means skipping dirty values, write `survey_summary.csv`, mean score by major; the exception skills from Part A do the cleaning.
- **1:48–1:56 — Traps recap (both halves).** Bare `except:`; swallowing errors; `"w"` destroys data; forgotten `newline=""`; reading a file twice (cursor at end).
- **1:56–2:00 — Summary + quiz. Next:** regular expressions, modules & OOP.

**Transitions**
- A concept→live: *"Your real survey data WILL have 'N/A' in a numeric column. Let's write code that shrugs it off."*
- A→B (the thread): *"You can now survive one bad value. Real data is a *file full* of them — let's open a real CSV and clean it with exactly these moves."*
- Teaser framing: *"Everything you just did by hand, pandas does in three lines — your next course, not today's. Now you know what it's doing underneath."*

**Predicted misconceptions**
- Reaches for `if/else` (LBYL) everywhere; introduce EAFP as the Pythonic default, but be honest both are valid.
- Writes bare `except:` — show why `except ValueError:` is safer.
- Confuses `raise` with `return`, and `assert` with input validation.
- Opens with `"w"` to read and wonders why the file is empty; stress mode meanings.
- Expects to iterate a file object twice without re-opening; show the exhausted cursor.

**Socratic prompts**
- "User typed 'seven' instead of 7. Catch it *before* (`if`) or *after* (`try`)? Trade-offs?"
- "Why is a bare `except:` dangerous? What might you swallow?"
- "Why does `with` matter even if your program crashes? What does it guarantee?"

**Cut line:** drop the custom exception and `pytest` (use `assert`) in Part A, and the `pandas`/`json` teaser in Part B; keep `try/except` validation and `csv.DictReader/Writer`.

---

## SESSION 5 — Regular Expressions, Modules & OOP
**Covers:** Part A — Regular Expressions & Text Cleaning; Part B — Modules, OOP & the Pythonic Toolkit.
**Pre-flight:** `examples/session-05/`; messy free-text, emails, and "Last, First" names staged for Part A; `grades.py` + the `Student` class and the generator-exhaustion demo staged for Part B; regex101 open.

**The clock (120 min)**
- **0:00–0:06 — Warm-up.** S4 traps recap (bare `except:`; `"w"` overwrites).
- **0:06–0:28 — Part A concept.** Why regex for a researcher (validate/extract/clean/qualitative-coding, Connection Map #9). **Raw strings** `r"..."`. Survival tokens (`. \d \w \s + * ? {m,n} ^ $ [] () |`); `.` matches *any* char (use `\.`). The four functions: `search`/`fullmatch`/`findall`/`sub`; capture groups (and named groups).
- **0:28–0:52 — Part A live + you-try.** Validate an email (`fullmatch`), extract dept+number with groups, collapse whitespace with `sub`, count `#hashtags` with `findall`. He starts `examples/session-05/practice.md` Part A (email validator, extract codes, hashtag count, the `"Last, First"` flip, and one case where `.split()` beats regex).
- **0:52–1:00 — Break.**
- **1:00–1:24 — Part B concept + live.** Modules: move grade functions to `grades.py`, `import`, the `if __name__ == "__main__":` guard. OOP: a small `Student` class — `__init__`, `self`, a method, `__str__`, a validating `@property` setter (Connection Map #10), brief inheritance with `super()`; `@dataclass` for the free `__repr__`/`__eq__`.
- **1:24–1:48 — Part B you-try.** `examples/session-05/practice.md` Part B: build the validating `Student`, add `GradStudent(super())`, then a tour-by-doing of the Pythonic toolkit (comprehension, `map`/`filter`, a generator + its one-pass exhaustion, the walrus `:=`).
- **1:48–1:56 — Traps recap (both halves).** Forgot `r"..."`; `re.search` returns `None` → guard before `.group()`; `self` confusion; a generator exhausts after one pass; over-using a class where a dict/function fits.
- **1:56–2:00 — Summary + quiz; course wrap. Next:** the capstone project.

**Transitions**
- A concept→live: *"Four functions cover almost everything: search, fullmatch, findall, sub. Every pattern is a raw string, no exceptions."*
- A→B (the thread): *"You can now clean any string. Last step: organize your code so it's reusable — functions into modules, then data-plus-behavior into a class."*
- Modules→OOP: *"Functions in a file is reuse. A class bundles the data *and* the rules that guard it."*

**Predicted misconceptions**
- Forgets raw strings → backslash chaos. Always `r"..."`.
- Calls `.group()` on a `None` result → teach the `if m:` guard.
- `self` looks magical — it's just "this particular instance."
- Treats a generator like a list (iterates once) → show the second pass is empty.
- Reaches for a class when a function or dict would do — name when OOP earns its keep.

**Socratic prompts**
- "You want every response mentioning a theme. Is that a *form* match (regex) or a *meaning* match (human coding)? What can regex actually catch?"
- "Why does `re.search(...).group()` crash when there's no match? (Same shape as `5 > '5'` weeks ago.)"
- "Your operational definition of 'student' — what attributes and rules belong to it? That's your class."
- "A million rows won't fit in memory. What does `yield` give you that a list doesn't?"

**Cut line:** drop named groups / `re.VERBOSE` in Part A and `@dataclass`/`match`-`case` in Part B; compress the toolkit tour to comprehensions + `enumerate`/`zip`. Keep validate+extract+`sub`, modules, and the validating class.

---

## SESSION 6 (Optional) — Capstone
**Role shift:** you stop teaching and start *coaching*. He drives; you ask questions and unblock.
- **0:00–0:15 — Brief & plan.** He restates the goal and sketches the steps aloud (pseudocode). You only check the plan is sound.
- **0:15–1:05 — Build.** He codes the Gradebook & Survey Analyzer (`assessments/capstone-project.md`). Intervene only when stuck >3 min; prefer a question over an answer.
- **1:05–1:13 — Break.**
- **1:13–1:45 — Build, continued.** Finish the report CSV, then one stretch goal (a `Student` class, a regex validation, or the recursive nested-data total).
- **1:45–1:55 — Review.** Walk his code for the course's traps (identity, aliasing, mutable defaults, bare `except:`). Praise readability.
- **1:55–2:00 — Debrief & next steps.** Point to pandas/visualization as the genuine next course.

**Coaching prompts:** "What's your data structure?" · "What happens if that cell is blank?" · "Is that comparing value or identity?" · "Could that be one comprehension?"

---

## Instructor's running checklist (use across all sessions)
- [ ] Timer visible; both halves get real hands-on time; the break is honored.
- [ ] The Part A→B thread named out loud, so two topics feel like one arc.
- [ ] Misconceptions log updated after each session; warm-up next session pulls from it.
- [ ] Every trap demoed via **predict-then-run**, not narration.
- [ ] Each new concept hooked to the **Connection Map** before syntax.
- [ ] Student typed everything himself; you talked less than half the session.
- [ ] End-of-session quiz given; capstone kept in view as the destination.
