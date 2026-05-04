**Day:3 - Python debugging**

`Main skill`

Debugging means finding the difference between:

What I expected the code to do

and

What the code actually did

Your roadmap wants you to debug 5 intentionally broken snippets.

- Debugging tool 1: print debugging
- Debugging tool 2: assert (Assertions check assumptions.)
- Debugging tool 3: stack traces (A stack trace tells you where the code failed.)
- Five debugging snippets to practice
    - Snippet 1: Empty list
    - Snippet 2: Wrong type
    - Snippet 3: Missing key
    - Snippet 4: Off-by-one error
    - Snippet 5: Bad import


### 🔨 The Day 3 Debugging Formula

For every bug, use this 6-step process:

1. Predict the expected output.
2. Run the code.
3. Read the error or wrong output.
4. Find the exact failing line.
5. Explain the cause in plain English.
6. Fix the code and test again.

Use this template in your file:

-  Expected:
-  Actual:
-  Error:
-  Cause:
-  Fix:

This turns debugging into reasoning, not guessing.



## 🔥Tool 4: Break the code intentionally

This is the most important debugging practice.

Do not only test normal input.

For every function, test:

empty input
None
wrong type
missing key
zero
negative value
duplicate value
unexpected shape/list length

For example:

def calculate_average(numbers):

    return sum(numbers) / len(numbers)

Test:

print(calculate_average([10, 20, 30]))   # normal
print(calculate_average([]))             # empty
print(calculate_average(None))           # None
print(calculate_average([10, "20"]))     # wrong type

This is how you discover failure modes.