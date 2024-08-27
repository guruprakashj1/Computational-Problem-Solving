# 5- Short-circuit Evaluation
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates short-circuit evaluation in Python

def risky_operation(x):
    """A function that simulates a risky operation"""
    print(f"Performing risky operation with {x}")
    return 10 / x  # This will raise a ZeroDivisionError if x is 0

def safe_check(x):
    """A function that safely checks a condition"""
    print(f"Performing safe check on {x}")
    return x > 0

# Demonstrate short-circuit evaluation with 'and'
print("Demonstration of 'and' short-circuit:")
x = 0
# The second part (risky_operation(x)) is not evaluated because safe_check(x) is False
result = safe_check(x) and risky_operation(x)
print(f"Result: {result}\n")  # False

# Demonstrate short-circuit evaluation with 'or'
print("Demonstration of 'or' short-circuit:")
x = 5
# The second part (risky_operation(x)) is not evaluated because safe_check(x) is True
result = safe_check(x) or risky_operation(x)
print(f"Result: {result}\n")  # True

# Demonstrate a case where short-circuit doesn't occur
print("Demonstration without short-circuit:")
x = 2
# Both parts are evaluated because safe_check(x) is True
result = safe_check(x) and risky_operation(x)
print(f"Result: {result}\n")  # 5.0

# Practical example: Null check before accessing an attribute
print("Practical example: Null check")

class User:
    def __init__(self, name):
        self.name = name

def get_user():
    """Simulates getting a user that might be None"""
    return None  # Simulating no user found

# Short-circuit evaluation prevents AttributeError when user is None
user = get_user()
name = user and user.name
print(f"User name: {name}")  # None

# Without short-circuit, this would raise an AttributeError:
# print(user.name)  # This would crash if uncommented

print("\nDemonstration of short-circuit in a loop:")
numbers = [1, 2, 3, 0, 4, 5]
for num in numbers:
    # Short-circuit prevents ZeroDivisionError
    if num != 0 and 10 / num > 2:
        print(f"{num} passes the test")
    else:
        print(f"{num} does not pass the test")
