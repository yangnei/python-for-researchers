"""
Session 1 — Running Python, Variables & Types
Run me:  python3 demo.py
Read each block, then change ONE thing and predict the output before re-running.
"""

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


# --- 4. Casting (type conversion) ---------------------------------------
print("int('42')   =", int("42"))
print("float('3.1')=", float("3.1"))
print("int(3.9)    =", int(3.9), "(truncates!)")
print("round(3.9)  =", round(3.9))


# --- 5. A tiny real program: years to graduation ------------------------
def years_to_graduation(credits_done: int, credits_needed: int, per_year: int) -> float:
    remaining = credits_needed - credits_done
    return remaining / per_year          # / always gives a float

print("Years left:", years_to_graduation(60, 120, 30))   # 2.0


# --- 6. Reading a traceback ---------------------------------------------
# Uncomment the next line to SEE an error on purpose, then read the LAST line:
# age = int("thirty")   # ValueError: invalid literal for int() with base 10: 'thirty'
