# 9-Type-Conversion-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: String to Number Converter
# Create a function that takes a string input and returns a tuple containing:
# 1. The input converted to an integer (or None if not possible)
# 2. The input converted to a float (or None if not possible)
# 3. A boolean indicating if the original input is numeric
# Hint: Use try-except blocks for conversions and the str.isnumeric() method.

def string_to_number(input_string):
    # TODO: Implement the function
    pass

# Test your function
print(string_to_number("123"))
print(string_to_number("3.14"))
print(string_to_number("hello"))


# Question 2: List Type Converter
# Write a function that takes a list of strings as input and returns a new list
# where each element is converted to int, float, or remains a string based on its content.
# If a string can be converted to both int and float, prefer int.
# Hint: You can use the string_to_number function from Question 1 to help with this.

def convert_list_items(string_list):
    # TODO: Implement the function
    pass

# Test your function
print(convert_list_items(["1", "2.5", "3", "4.0", "hello", "5.5"]))


# Question 3: Dictionary Value Converter
# Create a function that takes a dictionary as input where all values are strings.
# The function should return a new dictionary with the same keys, but values converted
# to appropriate types (int, float, or bool) where possible. If conversion is not possible,
# the value should remain a string.
# Hint: Remember that any non-empty string is considered True when converting to bool,
# except for "False" which should be converted to False.

def convert_dict_values(input_dict):
    # TODO: Implement the function
    pass

# Test your function
test_dict = {
    "a": "123",
    "b": "3.14",
    "c": "True",
    "d": "False",
    "e": "hello"
}
print(convert_dict_values(test_dict))


# Bonus Challenge: Custom Number Base Converter
# Implement a function that converts a number from any base (2-36) to any other base (2-36).
# The function should take three parameters:
# 1. The number as a string
# 2. The base of the input number
# 3. The base to convert to
# The function should return the converted number as a string.
# Hint: You can use int(string, base) to convert from a given base to decimal,
# and then implement your own logic to convert from decimal to the target base.

def convert_base(number, from_base, to_base):
    # TODO: Implement the function
    pass

# Test your function
print(convert_base("1010", 2, 10))  # Should print "10"
print(convert_base("FF", 16, 2))   # Should print "11111111"
