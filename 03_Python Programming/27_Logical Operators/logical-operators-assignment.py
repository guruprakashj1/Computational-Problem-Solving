# 4- Logical Operators - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Loan Eligibility Checker
# Create a function that determines if a person is eligible for a loan based on the following criteria:
# - Credit score is above 700
# - Annual income is at least $50,000
# - Debt-to-income ratio is below 0.3
# The function should return True if the person is eligible, False otherwise.

# Hint: Use the 'and' operator to combine all conditions.

def is_eligible_for_loan(credit_score, annual_income, debt_to_income_ratio):
    # Your code here
    pass

# Test your function
print(is_eligible_for_loan(750, 60000, 0.2))  # Should return True
print(is_eligible_for_loan(680, 55000, 0.25))  # Should return False


# Question 2: Traffic Light Simulator
# Create a function that simulates a traffic light. The function should take two parameters:
# - color: current color of the traffic light ("red", "yellow", or "green")
# - time_elapsed: time elapsed since the light turned to the current color (in seconds)
# The function should return True if it's safe to go, and False if it's not safe to go.
# Assume:
# - Red light lasts for 60 seconds
# - Yellow light lasts for 5 seconds
# - Green light lasts for 45 seconds

# Hint: Use a combination of 'and' and 'or' operators to check different conditions.

def is_safe_to_go(color, time_elapsed):
    # Your code here
    pass

# Test your function
print(is_safe_to_go("green", 30))  # Should return True
print(is_safe_to_go("yellow", 3))  # Should return False
print(is_safe_to_go("red", 65))  # Should return False


# Question 3: Password Validator
# Create a function that checks if a given password is strong enough. A password is considered strong if it meets all of the following criteria:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one digit
# - Does not contain the word "password" (case-insensitive)

# Hint: Use the 'and' operator to combine all conditions. You may find the 'any()' function and list comprehensions useful for checking character types.

def is_strong_password(password):
    # Your code here
    pass

# Test your function
print(is_strong_password("Str0ngP@ss"))  # Should return True
print(is_strong_password("weakpass"))  # Should return False
print(is_strong_password("MyPassword123"))  # Should return False
