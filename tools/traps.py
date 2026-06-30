"""Curated "predict, then reveal" traps — one source for three surfaces.

Each trap is a tiny piece of code whose result contradicts a beginner's
expectation. The same dataset is rendered three ways by the build tools:

  * the website     -> the code, the common (wrong) expectation, and a
                       click-to-reveal <details> with the real result + why;
  * the notebooks   -> the code in a runnable cell (run it to reveal the
                       result) with a collapsed "why";
  * the student PDF -> the code, result, and why shown inline (printed ref).

The *result* is never hand-written: `reveal()` runs `setup` then evaluates
`code`, so the answer shown is always what Python actually does. Keeping the
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
        {"setup": "a = [1, 2]\nb = [1, 2]",
         "code": "a is b",
         "expect": "True — the lists are equal",
         "why": "`==` compares VALUES; `is` compares IDENTITY (the object in memory). "
                "Two equal-looking lists are still different objects. Use `==` for values "
                "and keep `is` for `None`."},
        {"setup": "a = [1, 2]\nb = a\na.append(3)",
         "code": "b",
         "expect": "[1, 2] — we only touched a",
         "why": "`b = a` binds the SAME list, not a copy, so mutating through `a` shows up "
                "through `b`. Copy with `list(a)` or `a[:]`."},
        {"code": "True == 1",
         "expect": "False — they are different types",
         "why": "`bool` is a subclass of `int`: `True == 1` and `False == 0`."},
        {"code": "5 + True",
         "expect": "TypeError — you can't add a bool to an int",
         "why": "`True` acts as `1` (and `False` as `0`) in arithmetic, so `5 + True == 6`."},
        {"setup": "flags = [True, False, True, True]",
         "code": "sum(flags)",
         "expect": "an error, or 0",
         "why": "Summing booleans counts the `True`s — a handy way to count how many "
                "tests passed."},
        {"code": "0.1 + 0.2",
         "expect": "0.3",
         "why": "Floats are stored in binary, where 0.1 and 0.2 have no exact "
                "representation, so the tiny errors add up."},
        {"code": "0.1 + 0.2 == 0.3",
         "expect": "True",
         "why": "Because `0.1 + 0.2` is `0.30000000000000004`. Never test floats with `==`; "
                "use `math.isclose(a, b)`."},
        {"setup": "nan = float('nan')",
         "code": "nan == nan",
         "expect": "True — it is the very same value",
         "why": "`NaN` is defined to be equal to nothing, not even itself. Test it with "
                "`math.isnan(x)`."},
        {"code": "7 / 2",
         "expect": "3",
         "why": "`/` is always float (true) division. Use `//` for floor division."},
        {"code": "-7 // 2",
         "expect": "-3 (chop toward zero)",
         "why": "`//` floors toward negative infinity, not toward zero, so `-7 // 2 == -4`."},
        {"code": "5 == '5'",
         "expect": "True — same digit",
         "why": "Python does no automatic number/text conversion, so a number and a string "
                "are simply unequal (no error)."},
        {"code": "5 > '5'",
         "expect": "False (or maybe True)",
         "why": "Ordering a number against text raises TypeError — there is no sensible "
                "order. Convert first: `5 > int('5')`."},
        {"code": "[1, 2] == (1, 2)",
         "expect": "True — same elements",
         "why": "A list never equals a tuple, whatever the contents."},
        {"code": "type(True) is int",
         "expect": "True — bools are ints",
         "why": "`type()` is exact and `True`'s type is `bool`, not `int`. Use `isinstance` "
                "when you want subclass-aware checks."},
        {"code": "isinstance(True, int)",
         "expect": "False — it's a bool, not an int",
         "why": "`isinstance` respects subclassing, and `bool` IS a kind of `int`."},
        {"code": "bool('0')",
         "expect": "False — it's zero",
         "why": "Any NON-EMPTY string is truthy, including '0' and 'False'. Only the empty "
                "string is falsy."},
        {"code": "bool([])",
         "expect": "True — the list exists",
         "why": "Empty containers (`[]`, `{}`, `''`, `0`, `None`) are all falsy."},
        {"setup": "m = int('257')\np = int('257')",
         "code": "m is p",
         "expect": "True — same number",
         "why": "CPython pre-caches small ints (-5..256), so `is` accidentally looks True "
                "there; 257 built at runtime are separate objects. Compare values with `==`, "
                "never `is`."},
    ],
    # ---- Session 2 — Control flow & data structures ---------------------
    2: [
        {"code": "5 and 0",
         "expect": "True or False",
         "why": "`and`/`or` return one of the OPERANDS, not a bool: `and` yields the first "
                "falsy value (else the last), `or` the first truthy."},
        {"code": "list(range(1, 5))",
         "expect": "[1, 2, 3, 4, 5]",
         "why": "`range(start, stop)` stops BEFORE `stop`."},
        {"setup": "grid = [[0] * 3] * 3\ngrid[0][0] = 9",
         "code": "grid",
         "expect": "[[9, 0, 0], [0, 0, 0], [0, 0, 0]]",
         "why": "`[[0]*3]*3` makes three references to ONE inner row, so editing one edits "
                "all. Build with `[[0]*3 for _ in range(3)]`."},
        {"setup": "scores = [55, 92, 78]",
         "code": "all(s >= 60 for s in scores)",
         "expect": "True",
         "why": "`all()` is True only if EVERY item passes; 55 fails, so it's False."},
        {"setup": "d = {'Ana': 91}",
         "code": "d.get('Ben')",
         "expect": "KeyError",
         "why": "`.get()` returns `None` (or a default) for a missing key instead of raising "
                "— unlike `d['Ben']`."},
        {"setup": "nums = [1, 2, 3, 4]",
         "code": "nums[::-1]",
         "expect": "an error, or the same list",
         "why": "A slice with step -1 returns a reversed COPY — a common Python idiom."},
    ],
    # ---- Session 3 — Functions, scope & recursion -----------------------
    3: [
        {"setup": "def add(item, bag=[]):\n    bag.append(item)\n    return bag\nadd('apple')",
         "code": "add('banana')",
         "expect": "['banana'] — a fresh empty bag each call",
         "why": "A default value is created ONCE, at def time, so the same list persists "
                "across calls. Use `bag=None` then `bag = bag or []`."},
        {"setup": "def show(x):\n    print(x)",
         "code": "show(42) is None",
         "expect": "False — it clearly produced 42",
         "why": "Printing is not returning. A function with no `return` gives `None`."},
        {"setup": "funcs = [lambda: i for i in range(3)]",
         "code": "[f() for f in funcs]",
         "expect": "[0, 1, 2]",
         "why": "Closures capture the VARIABLE `i`, not its value; by call time the loop has "
                "left `i = 2`. Fix by binding it: `lambda i=i: i`."},
        {"setup": "def f(n):\n    return f(n - 1)",
         "code": "f(3)",
         "expect": "runs forever, or 0",
         "why": "Every recursive function needs a base case. Without one Python stops at its "
                "recursion limit (~1000 deep) with RecursionError."},
    ],
    # ---- Session 4 — Exceptions, files & research data ------------------
    4: [
        {"code": "int('3.0')",
         "expect": "3",
         "why": "`int()` parses INTEGER text only; '3.0' is not a valid int literal. "
                "Use `int(float('3.0'))`."},
        {"code": "round(2.5)",
         "expect": "3",
         "why": "Python uses banker's rounding (round half to EVEN): `round(2.5) == 2` but "
                "`round(3.5) == 4`. Watch this when summarising data."},
        {"code": "0.1 + 0.2 + 0.3 == 0.6",
         "expect": "True",
         "why": "Float error accumulates when you total measurements: 0.1+0.2+0.3 is "
                "0.6000000000000001. Compare sums with `math.isclose`, or round for display."},
        {"code": "int('1_000')",
         "expect": "ValueError",
         "why": "Python accepts underscores as digit separators, even inside `int()` text."},
    ],
    # ---- Session 5 — Regex, modules & OOP -------------------------------
    5: [
        {"setup": "gen = (n * n for n in range(3))\nfirst = list(gen)",
         "code": "list(gen)",
         "expect": "[0, 1, 4] again",
         "why": "A generator is one-shot: after the first full pass it is exhausted. "
                "Rebuild it, or store a list if you need it twice."},
        {"setup": "from dataclasses import dataclass\n\n@dataclass\nclass Pt:\n    x: int\n\np1 = Pt(1)\np2 = Pt(1)",
         "code": "p1 == p2",
         "expect": "False — two different objects",
         "why": "`@dataclass` writes an `__eq__` that compares fields, so equal-valued "
                "instances are `==` (even though `p1 is p2` is False)."},
        {"setup": "import re\nm = re.match(r'<(.+)>', '<a><b>')",
         "code": "m.group(1)",
         "expect": "'a'",
         "why": "`+` is greedy — it grabs as much as it can. Use `+?` for the shortest "
                "match: `r'<(.+?)>'`."},
        {"setup": "import re",
         "code": "bool(re.match(r'\\d+', 'abc123'))",
         "expect": "True — there are digits",
         "why": "`re.match` anchors at the START of the string. Use `re.search` to find a "
                "match anywhere."},
        {"setup": "class Dog:\n    tricks = []\n    def teach(self, t):\n        self.tricks.append(t)\n\na = Dog()\nb = Dog()\na.teach('sit')",
         "code": "b.tricks",
         "expect": "[] — b is a different dog",
         "why": "`tricks` is a CLASS variable shared by every instance. Give each its own in "
                "`__init__`: `self.tricks = []`."},
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
