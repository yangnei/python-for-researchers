"""Curated "predict, then reveal" traps — one source for three surfaces.

Each trap is a tiny piece of code whose result contradicts a beginner's
expectation. The same dataset is rendered three ways by the build tools:

  * the website     -> the code, the common (wrong) expectation, and a
                       click-to-reveal <details> with the real result + why;
  * the notebooks   -> the code in a runnable cell (run it to reveal the
                       result) with a collapsed "why";
  * the student PDF -> the code, result, and why shown inline (printed ref).

The examples are grounded in the learner's world (students, scores, rosters,
survey cells, gradebooks) so the surprise lands on something concrete. The
*result* is never hand-written: `reveal()` runs `setup` then evaluates `code`,
so the answer shown is always what Python actually does. Keeping the
expression as the cell's last line means a notebook auto-displays it on run.

Schema per trap:  {"setup": <statements, optional>, "code": <one expression>,
                   "expect": <the naive expectation>, "why": <the explanation>}
"""
from __future__ import annotations

import contextlib
import io
import warnings


TRAPS: dict[int, list[dict]] = {
    # ---- Session 1 — Types & the dynamic-typing traps -------------------
    1: [
        {"setup": "ana_scores = [88, 91]\nben_scores = [88, 91]",
         "code": "ana_scores is ben_scores",
         "expect": "True — the two lists are identical",
         "why": "`==` compares VALUES (and `ana_scores == ben_scores` is True); `is` compares "
                "IDENTITY — whether they are the same object in memory. Ana's and Ben's lists "
                "just happen to match. Use `==` for values and keep `is` for `None`."},
        {"setup": "roster = ['Ana', 'Ben']\nbackup = roster\nroster.append('Cara')",
         "code": "backup",
         "expect": "['Ana', 'Ben'] — backup was taken before Cara",
         "why": "`backup = roster` does not copy: both names point at one list, so appending "
                "through `roster` shows up in `backup` too. Copy with `list(roster)` or "
                "`roster[:]`."},
        {"setup": "attended = True",
         "code": "attended == 1",
         "expect": "False — a yes/no flag isn't a number",
         "why": "`bool` is a subclass of `int`: `True == 1` and `False == 0`, which is why a "
                "spreadsheet's 1/0 lines up with Python's True/False."},
        {"setup": "base_score = 5\nbonus = True",
         "code": "base_score + bonus",
         "expect": "TypeError — you can't add a flag to a number",
         "why": "`True` acts as `1` (and `False` as `0`) in arithmetic — a quick way to add a "
                "bonus point for a flag."},
        {"setup": "passed = [True, False, True, True]",
         "code": "sum(passed)",
         "expect": "an error, or 0",
         "why": "Summing booleans counts the `True`s — a handy way to count how many students "
                "passed."},
        {"setup": "reading_a = 0.1\nreading_b = 0.2",
         "code": "reading_a + reading_b",
         "expect": "0.3",
         "why": "Floats are stored in binary, where 0.1 and 0.2 have no exact representation, "
                "so the tiny errors add up."},
        {"setup": "total = 0.1 + 0.2",
         "code": "total == 0.3",
         "expect": "True",
         "why": "Because `0.1 + 0.2` is `0.30000000000000004`. Never test measured values with "
                "`==`; use `math.isclose(a, b)`."},
        {"setup": "missing_score = float('nan')",
         "code": "missing_score == missing_score",
         "expect": "True — it is the very same value",
         "why": "`NaN` (a missing/invalid number) is defined to equal nothing, not even itself. "
                "Test it with `math.isnan(x)`."},
        {"setup": "points = 7",
         "code": "points / 2",
         "expect": "3",
         "why": "`/` is always float (true) division. Use `//` when you want a whole number."},
        {"setup": "net = -7",
         "code": "net // 2",
         "expect": "-3 (just chop off the decimal)",
         "why": "`//` floors toward negative infinity, not toward zero, so `-7 // 2 == -4`."},
        {"setup": "cell = '5'   # a value read from a CSV",
         "code": "cell == 5",
         "expect": "True — same digit",
         "why": "Python does no automatic text/number conversion, so a CSV string and a number "
                "are simply unequal (no error). Convert first: `int(cell) == 5`."},
        {"setup": "cell = '5'",
         "code": "5 > cell",
         "expect": "False (or maybe True)",
         "why": "Ordering a number against text raises TypeError — there is no sensible order. "
                "Convert first: `5 > int(cell)`."},
        {"setup": "as_list = [88, 91]\nas_tuple = (88, 91)",
         "code": "as_list == as_tuple",
         "expect": "True — same numbers",
         "why": "A list never equals a tuple, whatever the contents."},
        {"setup": "flag = True",
         "code": "type(flag) is int",
         "expect": "True — bools are ints",
         "why": "`type()` is exact, and `flag`'s type is `bool`, not `int`. Use `isinstance` when "
                "you want subclass-aware checks."},
        {"setup": "flag = True",
         "code": "isinstance(flag, int)",
         "expect": "False — it's a bool, not an int",
         "why": "`isinstance` respects subclassing, and `bool` IS a kind of `int`."},
        {"setup": "response = '0'   # what a respondent typed",
         "code": "bool(response)",
         "expect": "False — it's zero",
         "why": "Any NON-EMPTY string is truthy, including '0' and 'False'. Only the empty "
                "string is falsy — so convert survey text before testing it."},
        {"setup": "submissions = []",
         "code": "bool(submissions)",
         "expect": "True — the list exists",
         "why": "Empty containers (`[]`, `{}`, `''`, `0`, `None`) are all falsy, which is why "
                "`if submissions:` reads as 'are there any?'."},
        {"setup": "id_a = int('257')\nid_b = int('257')   # two IDs parsed from text",
         "code": "id_a is id_b",
         "expect": "True — same number",
         "why": "CPython pre-caches small ints (-5..256), so `is` accidentally looks True there; "
                "257 built at runtime are separate objects. Compare values with `==`, never "
                "`is`."},
    ],
    # ---- Session 2 — Control flow & data structures ---------------------
    2: [
        {"setup": "typed_name = ''   # the user left the box blank",
         "code": "typed_name or 'Anonymous'",
         "expect": "True or False",
         "why": "`or` returns the first truthy OPERAND (else the last), and `and` the first "
                "falsy — not a bool. This is the default-value idiom."},
        {"setup": "weeks = range(1, 5)",
         "code": "list(weeks)",
         "expect": "[1, 2, 3, 4, 5]",
         "why": "`range(start, stop)` stops BEFORE `stop`, so weeks 1–4 here."},
        {"setup": "gradebook = [[0] * 3] * 3   # 3 students x 3 assignments\ngradebook[0][0] = 9",
         "code": "gradebook",
         "expect": "only the first student's first score changes",
         "why": "`[[0]*3]*3` makes three references to ONE inner row, so editing one edits all. "
                "Build with `[[0]*3 for _ in range(3)]`."},
        {"setup": "scores = [55, 92, 78]",
         "code": "all(s >= 60 for s in scores)",
         "expect": "True",
         "why": "`all()` is True only if EVERY item passes; 55 fails, so it's False."},
        {"setup": "gpa = {'Ana': 3.9}",
         "code": "gpa.get('Ben')",
         "expect": "KeyError",
         "why": "`.get()` returns `None` (or a default) for a missing key instead of raising — "
                "unlike `gpa['Ben']`."},
        {"setup": "ranking = ['Ana', 'Ben', 'Cara']",
         "code": "ranking[::-1]",
         "expect": "an error, or the same list",
         "why": "A slice with step -1 returns a reversed COPY — a common Python idiom."},
    ],
    # ---- Session 3 — Functions, scope & recursion -----------------------
    3: [
        {"setup": "def enroll(name, roster=[]):\n    roster.append(name)\n    return roster\nenroll('Ana')",
         "code": "enroll('Ben')",
         "expect": "['Ben'] — a fresh empty roster each call",
         "why": "A default value is created ONCE, at def time, so the same list persists across "
                "calls. Use `roster=None` then `roster = roster or []`."},
        {"setup": "def show_score(s):\n    print(s)",
         "code": "show_score(91) is None",
         "expect": "False — it clearly produced 91",
         "why": "Printing is not returning. A function with no `return` gives `None`."},
        {"setup": "makers = [lambda: week for week in range(3)]",
         "code": "[make() for make in makers]",
         "expect": "[0, 1, 2]",
         "why": "Closures capture the VARIABLE `week`, not its value; by call time the loop has "
                "left `week = 2`. Fix by binding it: `lambda week=week: week`."},
        {"setup": "def countdown(n):\n    return countdown(n - 1)   # no base case!",
         "code": "countdown(3)",
         "expect": "runs forever, or 0",
         "why": "Every recursive function needs a base case. Without one Python stops at its "
                "recursion limit (~1000 deep) with RecursionError."},
    ],
    # ---- Session 4 — Exceptions, files & research data ------------------
    4: [
        {"setup": "cell = '3.0'   # a value from a CSV",
         "code": "int(cell)",
         "expect": "3",
         "why": "`int()` parses INTEGER text only; '3.0' is not a valid int literal. "
                "Use `int(float(cell))`."},
        {"setup": "measurement = 2.5",
         "code": "round(measurement)",
         "expect": "3",
         "why": "Python uses banker's rounding (round half to EVEN): `round(2.5) == 2` but "
                "`round(3.5) == 4`. Watch this when summarising data."},
        {"setup": "total = 0.1 + 0.2 + 0.3   # three measured values",
         "code": "total == 0.6",
         "expect": "True",
         "why": "Float error accumulates when you total measurements: 0.1+0.2+0.3 is "
                "0.6000000000000001. Compare sums with `math.isclose`, or round for display."},
        {"setup": "enrolment = '1_000'",
         "code": "int(enrolment)",
         "expect": "ValueError",
         "why": "Python accepts underscores as digit separators, even inside `int()` text."},
    ],
    # ---- Session 5 — Regex, modules & OOP -------------------------------
    5: [
        {"setup": "gpas = (s for s in [3.9, 1.8, 3.2])\nfirst_pass = list(gpas)",
         "code": "list(gpas)",
         "expect": "the same GPAs again",
         "why": "A generator is one-shot: after the first full pass it is exhausted. "
                "Rebuild it, or store a list if you need it twice."},
        {"setup": "from dataclasses import dataclass\n\n@dataclass\nclass Grade:\n    course: str\n    score: int\n\ng1 = Grade('ED101', 91)\ng2 = Grade('ED101', 91)",
         "code": "g1 == g2",
         "expect": "False — two different objects",
         "why": "`@dataclass` writes an `__eq__` that compares fields, so equal-valued grades "
                "are `==` (even though `g1 is g2` is False)."},
        {"setup": "import re\nm = re.match(r'\\[(.+)\\]', '[ED101][ED102]')",
         "code": "m.group(1)",
         "expect": "'ED101'",
         "why": "`+` is greedy — it grabs as much as it can. Use `+?` for the shortest match: "
                "`r'\\[(.+?)\\]'`."},
        {"setup": "import re",
         "code": "bool(re.match(r'\\d+', 'cohort2026'))",
         "expect": "True — there's a number in there",
         "why": "`re.match` anchors at the START of the string. Use `re.search` to find a match "
                "anywhere."},
        {"setup": "class Course:\n    students = []\n    def enroll(self, name):\n        self.students.append(name)\n\nart = Course()\nmath = Course()\nart.enroll('Ana')",
         "code": "math.students",
         "expect": "[] — math is a different course",
         "why": "`students` is a CLASS variable shared by every instance. Give each its own in "
                "`__init__`: `self.students = []`."},
    ],
}


def reveal(trap: dict) -> str:
    """Run setup, evaluate the trap's expression, return the real result (or error)."""
    ns: dict = {}
    setup = trap.get("setup", "")
    if setup:
        exec(setup, ns)  # noqa: S102 — trusted, in-repo trap code
    with warnings.catch_warnings(record=True) as caught, contextlib.redirect_stdout(io.StringIO()):
        warnings.simplefilter("always")
        try:
            out = repr(eval(trap["code"], ns))  # noqa: S307 — trusted trap code
        except Exception as exc:  # the result IS sometimes an exception (that's the lesson)
            out = f"{type(exc).__name__}: {exc}"
    if caught:
        msg = str(caught[0].message).splitlines()[0]
        out += f"   (Python also warns: {caught[0].category.__name__}: {msg})"
    return out


def display_code(trap: dict) -> str:
    """The code a learner sees: any setup lines, then the expression to predict."""
    setup = trap.get("setup", "").strip()
    return f"{setup}\n{trap['code']}" if setup else trap["code"]


if __name__ == "__main__":  # quick self-check: print every trap's real result
    for n, traps in TRAPS.items():
        print(f"\n===== Session {n} ({len(traps)} traps) =====")
        for i, t in enumerate(traps, 1):
            print(f"  {i:>2}. {t['code']:<34} -> {reveal(t)}")
