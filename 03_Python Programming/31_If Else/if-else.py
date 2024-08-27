# 9- IF..Else
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of IF..ELSE statements in Python

# Basic IF statement
print("1. Basic IF statement:")
x = 10
if x > 5:
    print("x is greater than 5")
print()

# IF..ELSE statement
print("2. IF..ELSE statement:")
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")
print()

# IF..ELIF..ELSE statement
print("3. IF..ELIF..ELSE statement:")
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")
print()

# Nested IF statements
print("4. Nested IF statements:")
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")
print()

# Using logical operators
print("5. Using logical operators:")
age = 25
has_license = True
if age >= 18 and has_license:
    print("Can drive")
else:
    print("Cannot drive")
print()

# Ternary operator (conditional expression)
print("6. Ternary operator:")
a = 7
b = 10
max_value = a if a > b else b
print(f"Max value: {max_value}")
print()

# Truthy and Falsy values
print("7. Truthy and Falsy values:")
empty_list = []
if empty_list:
    print("List is not empty")
else:
    print("List is empty")
print()

# Short-circuit evaluation
print("8. Short-circuit evaluation:")
def check_positive(num):
    print("Checking if positive")
    return num > 0

if check_positive(5) or check_positive(-3):
    print("At least one number is positive")
print()

# This program covers various aspects of IF..ELSE statements in Python,
# demonstrating their versatility and common use cases.
