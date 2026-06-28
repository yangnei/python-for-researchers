"""
Session 1 — Running Python, Types & the Type Traps
Run me:  python3 demo.py
Two halves — (A) Running Python, Variables & Types; (B) The Dynamic-Typing Traps.
Predict each block, then run it.
"""

# ======================================================================
# PART A — Running Python, Variables & Types
# ======================================================================

# --- 1. Variables are labels on objects ---------------------------------
n = 30          # int
mean = 3.7      # float
name = "Ada"    # str
passed = True   # bool
missing = None  # NoneType

print(name, "->", type(name))
print(mean, "->", type(mean))
print("passed?", passed, "| missing?", missing)

# `=` is an action, not a math claim. Re-pointing a label is fine:
n = n + 1
print("n is now", n)

# Parallel assignment: the right side is built first, then unpacked left.
x, y = 1, 2
x, y = y, x                 # the Pythonic swap — no temp variable needed
print("after swap:", x, y)             # 2 1
big = 1_000_000            # underscores are just visual separators in numbers
print("big =", big)                    # 1000000


# --- 2. input() is ALWAYS a string --------------------------------------
# (Hard-coded here so the file runs without typing; the trap is real.)
raw = "5"                 # imagine this came from input()
print('"5" + "3" =', raw + "3")          # '53'  <- string concatenation!
print("int + int =", int(raw) + 3)       # 8     <- convert first


# --- 3. f-strings: clean formatting -------------------------------------
score = 87.456
print(f"{name} scored {score:.1f}")      # one decimal -> 87.5
print(f"big number: {1234567:,}")        # 1,234,567
print(f"as percent: {0.873:.1%}")        # 87.3%
print(f"{score=}")                       # self-documenting: score=87.456 (great for debugging)


# --- 4. Strings are objects with methods --------------------------------
full = "ada  LOVELACE"
print("title:", full.title())            # 'Ada  Lovelace'
print("upper:", name.upper(), "| len:", len(name))   # ADA 3
print("words:", "one two three".split())  # ['one', 'two', 'three']
print("'da' in name?", "da" in name)      # True — `in` tests membership


# --- 5. Casting (type conversion) ---------------------------------------
print("int('42')   =", int("42"))
print("float('3.1')=", float("3.1"))
print("int(3.9)    =", int(3.9), "(truncates!)")
print("round(3.9)  =", round(3.9))


# --- 6. A tiny real program: years to graduation ------------------------
def years_to_graduation(credits_done: int, credits_needed: int, per_year: int) -> float:
    remaining = credits_needed - credits_done
    return remaining / per_year          # / always gives a float

print("Years left:", years_to_graduation(60, 120, 30))   # 2.0


# --- 7. Reading a traceback ---------------------------------------------
# Uncomment the next line to SEE an error on purpose, then read the LAST line:
# age = int("thirty")   # ValueError: invalid literal for int() with base 10: 'thirty'


# ======================================================================
# PART B — The Dynamic-Typing Traps
# ======================================================================

import math

print("=== 1. == vs is ===")
a = [1, 2]; b = [1, 2]
print("a == b :", a == b)          # True  (same value)
print("a is b :", a is b)          # False (different objects)
print("id(a) == id(b)?", id(a) == id(b))   # False — `is` is really an id() check
c = a
print("a is c :", a is c)          # True  (c is an alias for a)

x = None
print("x is None :", x is None)    # True  (correct way to test None)

print("\n=== 2. Booleans are integers ===")
print("True == 1 :", True == 1)            # True
print("5 + True  :", 5 + True)             # 6
print("sum([T,F,T]):", sum([True, False, True]))  # 2  (counts Trues)
# Note: Python prints a SyntaxWarning here ("is with int literal") — that warning
# IS the lesson: don't use `is` to compare values. We do it once to show the result.
print("True is 1 :", True is 1)            # False (value equal, not same object)
print("isinstance(True, int):", isinstance(True, int))  # True

print("\n=== 3. int vs float / division ===")
print("3 == 3.0 :", 3 == 3.0)      # True
print("7 / 2    :", 7 / 2)         # 3.5  (always float)
print("7 // 2   :", 7 // 2)        # 3
print("-7 // 2  :", -7 // 2)       # -4   (floors toward -inf)

print("\n=== 4. Float precision (and the NaN oddity) ===")
print("0.1 + 0.2          :", 0.1 + 0.2)            # 0.30000000000000004
print("0.1 + 0.2 == 0.3   :", 0.1 + 0.2 == 0.3)     # False
print("math.isclose(...)  :", math.isclose(0.1 + 0.2, 0.3))  # True  <- the fix
nan = float("nan")
print("nan == nan         :", nan == nan)           # False! NaN equals nothing, not even itself
print("math.isnan(nan)    :", math.isnan(nan))      # True   <- the right test

print("\n=== 5. Comparing across types ===")
print('5 == "5" :', 5 == "5")      # False (no error)
try:
    print(5 > "5")
except TypeError as e:
    print('5 > "5"  : TypeError ->', e)

print("\n=== 6. Sequences compare element-by-element ===")
print("[1,2] == [1,2] :", [1, 2] == [1, 2])   # True
print("[1,2] == (1,2) :", [1, 2] == (1, 2))   # False (list vs tuple)
print("(1,2) < (1,3)  :", (1, 2) < (1, 3))    # True
print("'apple'<'banana':", "apple" < "banana")  # True

print("\n=== 7. type vs isinstance ===")
print("isinstance(5,(int,float)):", isinstance(5, (int, float)))  # True
print("type(True) is int        :", type(True) is int)            # False
print("isinstance(True, int)    :", isinstance(True, int))        # True

print("\n=== 8. Truthiness ===")
for v in (0, 0.0, "", [], {}, None, "0", [0], "False"):
    print(f"bool({v!r:>7}) = {bool(v)}")

print("\n=== 9. The small-int cache (an implementation detail — never rely on it) ===")
m = 256; p = 256
print("256 cached    :", m is p)        # True  — CPython pre-caches small ints (-5..256)
m = int("257"); p = int("257")          # built at runtime, so NOT folded to one object
print("257 runtime   :", m is p)        # False — outside the cache, separate objects
print("but 257 == 257:", m == p)        # True  — value is equal; identity is not
# Lesson: this is why you compare values with ==, never identities with `is`.
