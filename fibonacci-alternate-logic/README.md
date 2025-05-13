# Fibonacci Series Generator (Alternate Logic)

This Python script generates the Fibonacci series using an alternate logic by maintaining two separate variables (`pre1` and `pre2`) and updating them on odd and even iterations respectively.

## 🔢 Example Output
1
1
2
3
5
8
13
21


## 🧠 Logic Overview

- `pre1` and `pre2` are initialized to 1.
- If `i == 1 or 2`, print `1`.
- If `i > 2` and `i` is **odd**, update `pre1 = pre1 + pre2` and print it.
- If `i > 2` and `i` is **even**, update `pre2 = pre2 + pre1` and print it.

This approach offers a unique and clear alternate way to compute Fibonacci numbers.

## 📂 How to Run

```bash
python fibonacci.py

