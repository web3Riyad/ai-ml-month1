# Python Failure Modes

Day 7 is about compressing Week 1.

The goal is not only to write Python code. The goal is to read, debug, organize, and judge Python code.

A failure mode is a common way code breaks or gives the wrong result.

---
A beginner thinks:
> My code has an error. How do I fix it?

A stronger programmer thinks:
> What assumption did my code make that reality violated?

---
## 🚩Python Failure Modes

### 1. Runtime Type Errors
  Python does not always catch type problems before running code.

  Example:

  ```python
  age = "20"
  print(age + 5)
  ```
  **🔨How to detect runtime type errors:**

  Use these questions:

  - What type do I expect?
  - What type did I actually receive?
  - Can this value be None?
  - Can this list contain strings?
  - Can this value come from user input or CSV?

### 2. Bad Imports
  Common import failures:
  - Failure 1: Module not found
  - Failure 2: Function not found
  - Failure 3: Import-time side effect
  
  ✨Detection:

  - Check file location
  - Check filename spelling
  - Check function names
  - Avoid heavy logic at the top level
  - Put execution inside main()
  - Use if __name__ == "__main__"
## 3. Hidden State
  - Hidden state means code behaves differently because of data changed earlier or outside the function

  ✨Detection:

  - Look for global variables
  - Look for list/dict/DataFrame mutation
  - Watch out for inplace=True
  - Avoid mutable default arguments like items=[]
  - Prefer explicit inputs and outputs

## 4. Unreadable Code

 ✨Detection:

  - Bad variable names
  - Long functions
  - No clear input/output
  - Too many responsibilities in one function
  - Magic numbers
  - No docstrings
  - Copy-pasted logic

  🔨Better habits:

  - Use descriptive names
  - Keep functions small
  - One function should do one job
  - Use constants for important values
  - Add docstrings for reusable functions

## 5. Weak Error Handling
Weak error handling means code crashes with unclear errors or fails too late.

✅ Better habits:

- Validate inputs early
- Raise clear exceptions
- Use assertions for assumptions during development
- Test edge cases
- Make error messages explain the real problem

## 6. Silent Logic Bugs
Silent logic bugs happen when code runs without crashing but gives the wrong result.
### 7. File and Path Errors
### 8. Data Validation Failures

## Week 1 Reflection
