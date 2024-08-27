# 5- Short-circuit Evaluation - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Safe Division
# Create a function called safe_divide that takes two parameters: numerator and denominator.
# The function should return the result of numerator / denominator if the denominator is not zero.
# If the denominator is zero, the function should return None.
# Use short-circuit evaluation to prevent ZeroDivisionError.

# Hint: Use the 'and' operator to check the denominator before performing the division.

def safe_divide(numerator, denominator):
    # Your code here
    pass

# Test your function
print(safe_divide(10, 2))  # Should return 5.0
print(safe_divide(10, 0))  # Should return None


# Question 2: User Authentication
# Create a function called authenticate_user that takes a username and password as parameters.
# The function should return True if both the username and password are valid, False otherwise.
# A username is valid if it's not empty and has at least 3 characters.
# A password is valid if it's not empty and has at least 8 characters.
# Use short-circuit evaluation to check conditions efficiently.

# Hint: Use the 'and' operator to combine conditions. Check for empty strings first.

def authenticate_user(username, password):
    # Your code here
    pass

# Test your function
print(authenticate_user("", "password123"))  # Should return False
print(authenticate_user("user", ""))  # Should return False
print(authenticate_user("user", "pass"))  # Should return False
print(authenticate_user("alice", "securepass"))  # Should return True


# Question 3: Efficient Data Processing
# Create a function called process_data that takes a list of numbers as a parameter.
# The function should return the sum of all positive even numbers in the list.
# If the list is empty or contains no positive even numbers, return 0.
# Use short-circuit evaluation to make your function efficient.

# Hint: Use a list comprehension with short-circuit evaluation to filter numbers before summing.

def process_data(numbers):
    # Your code here
    pass

# Test your function
print(process_data([1, 2, 3, 4, 5, 6]))  # Should return 12 (2 + 4 + 6)
print(process_data([-1, -2, 0, 1, 3, 5]))  # Should return 0
print(process_data([]))  # Should return 0
