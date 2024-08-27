# 1- Defining Functions - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Temperature Converter
# Create a function called celsius_to_fahrenheit that takes a temperature in Celsius as input
# and returns the equivalent temperature in Fahrenheit.
# The formula is: F = (C * 9/5) + 32

# Hint: Use the given formula to convert the temperature. Remember to use meaningful parameter names and add a docstring.

def celsius_to_fahrenheit(celsius):
    # Your code here
    pass

# Test your function
print(celsius_to_fahrenheit(0))   # Should print 32.0
print(celsius_to_fahrenheit(100)) # Should print 212.0
print(celsius_to_fahrenheit(-40)) # Should print -40.0


# Question 2: Password Strength Checker
# Create a function called check_password_strength that takes a password as input and returns
# a string indicating the password strength: "Weak", "Medium", or "Strong".
# The criteria for password strength are:
# - Weak: Less than 8 characters
# - Medium: 8 or more characters, with at least one number and one uppercase letter
# - Strong: 8 or more characters, with at least one number, one uppercase letter, and one special character (!@#$%^&*)

# Hint: Use string methods like isdigit(), isupper(), and any() to check for specific character types.

def check_password_strength(password):
    # Your code here
    pass

# Test your function
print(check_password_strength("password"))    # Should print "Weak"
print(check_password_strength("Password1"))   # Should print "Medium"
print(check_password_strength("P@ssw0rd!"))   # Should print "Strong"


# Question 3: List Manipulator
# Create a function called manipulate_list that takes a list and three optional parameters:
# - reverse (bool): If True, reverse the list (default: False)
# - sort (bool): If True, sort the list in ascending order (default: False)
# - duplicate_last (int): Duplicate the last element of the list this many times (default: 0)
# The function should return the manipulated list.

# Hint: Use list methods like reverse() and sort(). Use list slicing to duplicate the last element.

def manipulate_list(numbers, reverse=False, sort=False, duplicate_last=0):
    # Your code here
    pass

# Test your function
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(manipulate_list(original_list))                     # Should print [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(manipulate_list(original_list, reverse=True))       # Should print [5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3]
print(manipulate_list(original_list, sort=True))          # Should print [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(manipulate_list(original_list, duplicate_last=3))   # Should print [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 5, 5, 5]
