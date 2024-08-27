# 6-String-Methods-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Password Validator
# Create a function that takes a password as input and returns True if it's valid, False otherwise.
# A valid password should:
# - Be at least 8 characters long
# - Contain at least one uppercase letter, one lowercase letter, and one digit
# - Not contain spaces
# Hint: Use string methods like isdigit(), isupper(), islower(), and isspace()

def is_valid_password(password):
    # TODO: Implement the function
    pass

# Test your function
print(is_valid_password("Abc123!@"))  # Should return True
print(is_valid_password("abc123"))    # Should return False
print(is_valid_password("ABC123!"))   # Should return False
print(is_valid_password("Abc 123!"))  # Should return False


# Question 2: String Cleaner
# Write a function that takes a string and returns a cleaned version of it:
# - Remove leading and trailing whitespace
# - Convert to lowercase
# - Replace all occurrences of '&' with 'and'
# - Remove any duplicate spaces (i.e., multiple spaces should become a single space)
# Hint: Use methods like strip(), lower(), replace(), and split()

def clean_string(text):
    # TODO: Implement the function
    pass

# Test your function
print(clean_string("  Hello   World & Python  "))  # Should return "hello world and python"


# Question 3: Acronym Generator
# Create a function that takes a phrase and returns its acronym.
# An acronym is formed by taking the first letter of each word, capitalized.
# Ignore any word that starts with a lowercase letter.
# Hint: Use split(), isupper(), and join() methods

def generate_acronym(phrase):
    # TODO: Implement the function
    pass

# Test your function
print(generate_acronym("Portable Network Graphics"))  # Should return "PNG"
print(generate_acronym("As Soon As Possible"))        # Should return "ASAP"
print(generate_acronym("First In, First Out"))        # Should return "FIFO"
print(generate_acronym("For Your Information"))       # Should return "FYI"


# Bonus Challenge: String Analyzer
# Implement a function that takes a string and returns a dictionary with the following information:
# - 'length': The length of the string
# - 'words': The number of words in the string
# - 'uppercase': The number of uppercase letters
# - 'lowercase': The number of lowercase letters
# - 'digits': The number of digits
# - 'special': The number of special characters (not alphanumeric)
# Hint: Use various string methods and possibly list comprehensions or generator expressions

def analyze_string(text):
    # TODO: Implement the function
    pass

# Test your function
result = analyze_string("Hello World! 123 #Python")
print(result)
# Expected output: {'length': 24, 'words': 3, 'uppercase': 2, 'lowercase': 8, 'digits': 3, 'special': 3}

