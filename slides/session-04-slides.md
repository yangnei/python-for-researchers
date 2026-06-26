---
marp: true
title: "Session 4 — Loops & Iteration"
paginate: true
---

# Session 4
## Loops & Iteration

Do something many times — the Pythonic way.

---

## while loops

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

⚠️ Forget to change the condition → **infinite loop**. Kill it with **Ctrl+C**.

---

## for loops + range

```python
for i in range(5):        # 0,1,2,3,4
    print(i)

for x in [10, 20, 30]:    # each element directly
    print(x)
```

`range(1, 5)` → `1,2,3,4` — **stop is excluded** (off-by-one!).
`range(0, 10, 2)` → `0,2,4,6,8`.

---

## break & continue

```python
for x in data:
    if x is None:
        continue          # skip this one
    if x == "STOP":
        break             # leave the loop entirely
    process(x)
```

---

## The validation loop (you'll reuse this everywhere)

```python
while True:
    raw = input("Score 0–100: ")
    if raw.isdigit() and 0 <= int(raw) <= 100:
        score = int(raw)
        break
    print("Try again.")
```

---

## Stop juggling indices: enumerate & zip

```python
for i, name in enumerate(names):     # index + value
    print(i, name)

for name, score in zip(names, scores):   # two lists together
    print(name, score)
```

🧠 If you write `range(len(x))`, stop — `enumerate`/`zip` is cleaner.

---

## Your turn

`examples/session-04/practice.md`:
1. Average a list of scores (no `sum()` — use a loop), then with `sum()/len()`.
2. Walk `names` and `scores` together; print "name: PASS/FAIL".
3. Robust "ask until valid" prompt.

---

## Traps recap

- `range(1, 5)` excludes 5.
- **Don't modify a list while looping it** — iterate a copy or build a new list.
- Prefer `enumerate`/`zip` over `range(len(...))`.
- Infinite loop? Ctrl+C.

## Summary
You can repeat work, control loops, and iterate cleanly.
**Next:** the containers you loop *over* — lists, dicts, sets.
