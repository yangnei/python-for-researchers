"""
Session 3 — Conditionals & Boolean Logic
Run me:  python3 demo.py
"""

# --- 1. if / elif / else with chained comparison ------------------------
def letter_grade(score):
    if not 0 <= score <= 100:          # chained comparison
        return "Invalid"
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

for s in [95, 90, 89.999, 72, 60, 59, 120]:
    print(f"{s:>7} -> {letter_grade(s)}")

# --- 2. and / or return a value (short-circuit) -------------------------
print("\n5 and 0 =", 5 and 0)          # 0
print("0 or 'hi' =", 0 or "hi")        # hi
name = "" or "Anonymous"               # default-value idiom
print("name =", name)

# --- 3. truthiness instead of == True ----------------------------------
submitted = ["essay.pdf"]
if submitted:                          # ✅ not  if len(submitted) > 0
    print("Has submissions")

# --- 4. Likert classifier with early return ----------------------------
def likert_label(n):
    labels = {5: "Strongly agree", 4: "Agree", 3: "Neutral",
              2: "Disagree", 1: "Strongly disagree"}
    return labels.get(n, "Invalid")    # dict-as-switch (preview of S5)

print("\n", likert_label(5), "|", likert_label(9))

# --- 5. ternary & match -------------------------------------------------
score = 72
print("\nstatus:", "pass" if score >= 60 else "fail")

def route(cmd):
    match cmd:
        case "start": return "running"
        case "stop" | "halt": return "stopped"
        case _: return "unknown"
print(route("halt"), route("nope"))
