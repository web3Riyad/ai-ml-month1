def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


scores = [80, 90, 70, 100]
# scores = []
average_score = calculate_average(scores)

print(f"Average score: {average_score}")

""" 
Do not just say “this calculates average.”

Read it like a debugger:

calculate_average accepts one argument: numbers.
It assumes numbers is a non-empty list of numeric values.
sum(numbers) adds all values.
len(numbers) counts how many values exist.
total / count returns the mean.
If numbers is empty, count becomes 0 and the code crashes with ZeroDivisionError.
If numbers contains strings, sum(numbers) may fail.

That is Python reasoning.


🧠 Assumption:
1. The list is not empty
2. All values are numbers
3. The input is list : sum(None) -> causes type error

"""

def safe_version(numbers):
    if numbers is None:
        raise ValueError("Numbers cannot be None")
    if len(numbers) == 0 :
        raise ValueError("Numbers cannot be empty")
    if not all(isinstance(number,(int,float)) for number in numbers):
        raise TypeError("All items in numbers must be numeric")
    
    total = sum(numbers)
    count = len(numbers)
    
    return total/count       


def calculate_total(prices):
    return sum(prices)
""" 
def calculate_total(prices):
    # Input: prices should be a list of integers or floats.
    # Output: returns the sum of all numbers in prices.
    # sum(prices) adds all values inside the list.
    # Assumption: prices is not None.
    # Assumption: every item inside prices is numeric.
    # Failure: if prices is None, sum(prices) causes TypeError.
    # Failure: if prices contains strings like ["10", "20"], result may fail or behave incorrectly.
    # Failure: if prices contains mixed values like [10, "20"], it causes TypeError.
    return sum(prices)
    """

def is_adult(age):
    return age >= 18
""" def is_adult(age):
    # Input: age should be an integer or float.
    # Output: returns True if age is 18 or greater, otherwise returns False.
    # age >= 18 compares age with 18.
    # Assumption: age is not None.
    # Assumption: age is a number, not a string.
    # Failure: if age is None, comparison causes TypeError.
    # Failure: if age is a string like "20", comparison causes TypeError.
    return age >= 18

"""

def get_first_item(items):
    return items[0]

""" 
def get_first_item(items):
    # Input: items should be a list or list-like object.
    # Output: returns the first item from items.
    # items[0] accesses the first element.
    # Assumption: items is not None.
    # Assumption: items is not empty.
    # Failure: if items is empty, items[0] causes IndexError.
    # Failure: if items is None, items[0] causes TypeError.
    return items[0]
"""