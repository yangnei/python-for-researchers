"""
Session 9 — Regex, Modules, OOP & "Pythonic"
Run me from this folder:  python3 demo.py
"""
import re
from grades import letter_grade, class_average   # importing our own module


# --- 1. Regex: validate & extract --------------------------------------
def valid_university_email(addr: str) -> bool:
    # one-or-more word chars, @, domain, ending .edu  (raw string!)
    return re.fullmatch(r"\w+@\w+\.edu", addr) is not None

print(valid_university_email("ana@harvard.edu"))   # True
print(valid_university_email("ana@gmail.com"))     # False

m = re.search(r"([A-Z]{2})(\d{4})", "Course ED1234 meets Tue")
print("dept:", m.group(1), "| number:", m.group(2))   # ED 1234

messy = "too    much   space"
print(re.sub(r"\s+", " ", messy))                   # "too much space"


# --- 2. OOP: a Student with a validating property ----------------------
class Student:
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa            # goes through the setter (validates!)

    def __str__(self) -> str:
        return f"{self.name}: {self.gpa} ({self.standing()})"

    def standing(self) -> str:
        return "Good" if self.gpa >= 2.0 else "Probation"

    @property
    def gpa(self) -> float:
        return self._gpa

    @gpa.setter
    def gpa(self, value: float):
        if not 0 <= value <= 4:
            raise ValueError(f"gpa {value} not in 0–4")
        self._gpa = value


ana = Student("Ana", 3.9)
print(ana)                         # uses __str__
try:
    ana.gpa = 5.0                  # rejected by the setter
except ValueError as e:
    print("rejected:", e)


# --- 3. Pythonic power-tools -------------------------------------------
roster = [Student("Ana", 3.9), Student("Ben", 1.8), Student("Cara", 3.2)]

good = [s.name for s in roster if s.gpa >= 2.0]        # comprehension
print("good standing:", good)

for i, s in enumerate(roster, start=1):                # enumerate
    print(i, s.name)

names = list(map(lambda s: s.name.upper(), roster))    # map
print("upper:", names)


# --- 4. Generator: one value at a time (memory-friendly) ---------------
def gpas(students):
    for s in students:
        yield s.gpa

g = gpas(roster)
print("mean gpa:", round(class_average(list(g)), 2))
# A generator is exhausted after one pass:
print("second pass:", list(g))     # []  <- already consumed


# --- 5. Reusing the imported module ------------------------------------
print("letter for 85:", letter_grade(85))
