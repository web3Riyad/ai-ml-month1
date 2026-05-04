"""
Day 3: Python Debugging

Goal:
Debug 5 intentionally broken snippets.

Debugging process:
1. Predict expected behavior
2. Run the broken code
3. Read the error
4. Find the exact failing line
5. Explain the cause
6. Fix the code
"""


# ============================================================
# Snippet 1: Empty List Bug
# ============================================================

# Broken code:
def average(values):
    return sum(values) / len(values)

print(average([]))

# Expected:
# I expected the function to calculate an average.

# Actual:
# ZeroDivisionError: division by zero

# Cause:
# The list is empty, so len(values) is 0.
# The function tries to divide by 0.

# Fixed code:
def average(values):
    if len(values) == 0:
        raise ValueError("values cannot be empty")

    return sum(values) / len(values)


print("Average:", average([10, 20, 30]))


# ============================================================
# Snippet 2: Wrong Type Bug
# ============================================================

# Broken code:
age = "20"
print(age + 5)

# Expected:
# 25

# Actual:
# TypeError because Python cannot add a string and an integer.

# Cause:
# "20" looks like a number, but it is a string.

# Fixed code:
age = "20"
age = int(age)

print("Age after 5 years:", age + 5)


# ============================================================
# Snippet 3: Missing Dictionary Key
# ============================================================

# Broken code:
student = {"name": "Riyad"}
print(student["grade"])

# Expected:
# Print the student's grade.

# Actual:
# KeyError: 'grade'

# Cause:
# The dictionary does not contain the key "grade".

# Fixed code:
student = {"name": "Riyad"}

print("Grade:", student.get("grade", "No grade found"))


# ============================================================
# Snippet 4: Off-by-One Error
# ============================================================

# Broken code:
items = ["a", "b", "c"]

for i in range(len(items) + 1):
    print(items[i])

# Expected:
# Print a, b, c.

# Actual:
# IndexError: list index out of range

# Cause:
# The loop tries to access index 3, but valid indexes are 0, 1, and 2.

# Fixed code:
items = ["a", "b", "c"]

for item in items:
    print("Item:", item)


# ============================================================
# Snippet 5: Bad Import Bug
# ============================================================

# Broken code:
# import helper
# helper.clean_data()

# Possible error 1:
# ModuleNotFoundError: No module named 'helper'
#
# Cause:
# Python cannot find helper.py.

# Possible error 2:
# AttributeError: module 'helper' has no attribute 'clean_data'
#
# Cause:
# helper.py exists, but there is no function named clean_data inside it.

# Possible error 3:
# Import-time side effect
#
# Cause:
# helper.py runs unwanted code immediately when imported.

# Fixed helper.py example:
#
def clean_data(data):
    return data

# Fixed main.py example:

# import helper

data = [1, 2, 3]
# cleaned_data = helper.clean_data(data)
# print(cleaned_data)