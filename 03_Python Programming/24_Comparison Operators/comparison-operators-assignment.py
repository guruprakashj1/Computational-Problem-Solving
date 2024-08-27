# 1-Comparison-Operators-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Age Group Classifier
# Write a function that takes an age as input and returns a string indicating the age group:
# "Child" for ages 0-12, "Teenager" for ages 13-19, "Adult" for ages 20-59, and "Senior" for ages 60 and above.
# Hint: Use comparison operators and if-elif-else statements.

def classify_age(age):
    # TODO: Implement the function
    pass

# Test your function
print(classify_age(8))   # Should print "Child"
print(classify_age(15))  # Should print "Teenager"
print(classify_age(30))  # Should print "Adult"
print(classify_age(70))  # Should print "Senior"


# Question 2: Number Range Checker
# Create a function that takes a number and two range limits. The function should return True if the number
# is within the range (inclusive), and False otherwise. The range limits can be provided in any order.
# Hint: Use comparison operators and the min() and max() functions.

def is_in_range(number, limit1, limit2):
    # TODO: Implement the function
    pass

# Test your function
print(is_in_range(5, 1, 10))  # Should print True
print(is_in_range(5, 10, 1))  # Should print True (note the reversed limits)
print(is_in_range(11, 1, 10)) # Should print False


# Question 3: String Comparison Tool
# Implement a function that compares two strings and returns a dictionary with the following information:
# - 'equal': Boolean indicating if the strings are exactly equal
# - 'same_length': Boolean indicating if the strings have the same length
# - 'first_longer': Boolean indicating if the first string is longer than the second
# - 'common_start': The longest common substring starting from the beginning of both strings
# Hint: Use comparison operators, string slicing, and a loop for finding the common start.

def compare_strings(str1, str2):
    # TODO: Implement the function
    pass

# Test your function
result = compare_strings("Python", "Pytorch")
print(result)  # Should print something like: {'equal': False, 'same_length': False, 'first_longer': False, 'common_start': 'Py'}


# Bonus Challenge: Version Number Comparator
# Create a function that compares two version numbers. Version numbers have the format 'MAJOR.MINOR.PATCH'
# (e.g., '2.5.1'). The function should return -1 if the first version is lower, 1 if it's higher, and 0 if they're equal.
# Assume all version numbers have three components.
# Hint: Split the version strings, convert to integers, and compare component by component.

def compare_versions(version1, version2):
    # TODO: Implement the function
    pass

# Test your function
print(compare_versions("1.2.3", "1.2.4"))   # Should return -1
print(compare_versions("2.0.0", "1.9.9"))   # Should return 1
print(compare_versions("1.0.0", "1.0.0"))   # Should return 0
print(compare_versions("1.0.1", "1.0.0"))   # Should return 1

