## 🎯Day 4 Core Idea

Messy code can work once.

Clean code can be:

- read
- debugged
- reused
- tested
- explained
- uploaded to GitHub
- used inside an ML project

Day 4 is where you stop writing “one-time code” and start writing code like a future ML engineer.

## ⚖️ The most important Day 4 rule: one function, one responsibility
- Naming: code should explain itself
- Docstrings: small explanations inside functions

```
def calculate_average_score(scores):
    """Calculate the average score from a list of numeric scores."""
    return sum(scores) / len(scores)
```
- Simple config: avoid magic values everywhere

Bad:
```
df = pd.read_csv("data.csv")
print(df["age"].mean())
print(df["income"].mean())
```
- The file path and column names are hardcoded inside the logic.

Better :
```
DATA_PATH = "data.csv"
AGE_COLUMN = "age"
INCOME_COLUMN = "income"


df = pd.read_csv(DATA_PATH)
print(df[AGE_COLUMN].mean())
print(df[INCOME_COLUMN].mean())
```
- requirements.txt
    - A repo without requirements.txt is harder to reproduce.



---

## Why main() matters

This part may look strange at first:
``` python
if __name__ == "__main__":
    main()
```

It means:

- Only run main() when this file is executed directly.
- Do not automatically run it when this file is imported.

Example:

### data_utils.py
```python
def clean_data(df):

    return df.dropna()
print("Cleaning started")
```

If another file imports this:
```
import data_utils
```
Python will immediately run:

print("Cleaning started")

That is called an import-time side effect.

`Better:`

### data_utils.py
```python
def clean_data(df):
    return df.dropna()


def main():
    print("Cleaning started")


if __name__ == "__main__":
    main()
```
Now the print only runs when you directly run:

python data_utils.py

This matters in ML because later your files may import functions from each other.

---

##🔥 Day 4: Code Organization

Today I refactored messy data analysis code into reusable functions.

### What I practiced

- separating code into functions
- using clear names
- writing small docstrings
- using a main() function
- validating required columns
- avoiding silent data cleaning

### ✨Failure modes I noticed

- giant functions are hard to debug
- unclear names hide meaning
- Hidden hardcoded values
    - only works on your computer
    - breaks on GitHub
    - breaks on another machine
- `dropna()` can silently remove important rows

  Bad:

  ```python
  df = df.dropna()
  ```

  Problem:

  You do not know how many rows were removed.

  Better:

  ```python
  rows_before = len(df)
  df = df.dropna()
  rows_after = len(df)

  print(f"Rows removed: {rows_before - rows_after}")
  ```

- Top-level code can create import-time side effects

  Better:

  ```python
  if __name__ == "__main__":
      main()
  ```