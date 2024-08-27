# 3-Strings-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: String Manipulation
# Create a function that takes a full name (e.g., "John Doe") and returns the initials.
# For example, "John Doe" should return "J.D."
# Hint: Use string splitting and indexing.

def get_initials(full_name):
    # TODO: Implement the function
    pass

# Test your function
print(get_initials("John Doe"))  # Should print "J.D."


# Question 2: Palindrome Checker
# Write a function that checks if a given string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
# Hint: Use string methods to remove spaces and change case, then compare the string with its reverse.

def is_palindrome(text):
    # TODO: Implement the function
    pass

# Test your function
print(is_palindrome("A man a plan a canal Panama"))  # Should print True
print(is_palindrome("race a car"))  # Should print False


# Question 3: String Formatting
# Create a function that takes a person's name and age, and returns a formatted string.
# The function should return: "Hello, [Name]! You will be [age+1] years old next year."
# Use f-strings for formatting.
# Hint: Remember to convert the age to an integer for calculation.

def birthday_greeting(name, age):
    # TODO: Implement the function
    pass

# Test your function
print(birthday_greeting("Alice", "30"))  # Should print "Hello, Alice! You will be 31 years old next year."


# Bonus Challenge:
# Modify the palindrome checker to ignore punctuation as well.
# For example, "A man, a plan, a canal: Panama" should be considered a palindrome.
# Hint: You might want to use the string module and a list comprehension or filter() function.

import string

def advanced_palindrome_checker(text):
    # TODO: Implement the function
    pass

# Test your advanced function
print(advanced_palindrome_checker("A man, a plan, a canal: Panama"))  # Should print True

