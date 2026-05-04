def clean_name(name):
    return name.strip().title()


student_name = "  riyad khandaker  "
# student_name = None
cleaned_name = clean_name(student_name)

print(cleaned_name)

""" 
    # Input: name should be a string.
    # Output: returns a cleaned version of the name.
    # .strip() removes spaces from the beginning and end.
    # .title() capitalizes the first letter of each word.
    # Assumption: name is not None.
    # Assumption: name is a string.
    # Failure: if name is None, .strip() will cause an AttributeError.
    # Failure: if name is an integer, .strip() will cause an AttributeError.
    return name.strip().title()

"""