# 4- Logical Operators
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates the usage of logical operators in Python

# Define some boolean variables
is_sunny = True
is_warm = True
has_umbrella = False
is_raining = True

# Demonstrate the 'and' operator
# The 'and' operator returns True if both operands are True
print("Example of 'and' operator:")
go_to_beach = is_sunny and is_warm
print(f"Is it sunny and warm? {go_to_beach}")  # True

# Demonstrate the 'or' operator
# The 'or' operator returns True if at least one operand is True
print("\nExample of 'or' operator:")
stay_dry = has_umbrella or not is_raining
print(f"Will you stay dry? {stay_dry}")  # False

# Demonstrate the 'not' operator
# The 'not' operator returns the opposite boolean value
print("\nExample of 'not' operator:")
stay_inside = not is_sunny
print(f"Should you stay inside? {stay_inside}")  # False

# Combine multiple logical operators
print("\nCombining multiple logical operators:")
go_out = (is_sunny or has_umbrella) and not is_raining
print(f"Should you go out? {go_out}")  # False

# Demonstrate short-circuit evaluation
print("\nDemonstrating short-circuit evaluation:")
x = 5
y = 0
# In the following line, (y != 0) is evaluated first, and since it's False,
# Python doesn't evaluate (x / y) to avoid a division by zero error
result = (y != 0) and (x / y > 2)
print(f"Result of short-circuit evaluation: {result}")  # False

# Using logical operators in if statements
print("\nUsing logical operators in if statements:")
temperature = 28

if temperature > 30 and is_sunny:
    print("It's a hot and sunny day!")
elif temperature > 20 or is_sunny:
    print("It's a nice day for outdoor activities.")
else:
    print("Consider indoor activities today.")
