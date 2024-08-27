# 1-Variables-Example.py

# Basic variable assignment
age = 25  # Assigning an integer value to the variable 'age'
print(f"Age: {age}")

name = "Alice"  # Assigning a string value to the variable 'name'
print(f"Name: {name}")

# Variable reassignment
age = 26  # Changing the value of 'age'
print(f"Updated age: {age}")

# Multiple assignment
x, y, z = 1, 2, 3  # Assigning values to multiple variables in one line
print(f"x: {x}, y: {y}, z: {z}")

# Dynamic typing
var = 10  # 'var' is an integer
print(f"var as integer: {var}")
var = "ten"  # 'var' is now a string
print(f"var as string: {var}")

# Using variables in expressions
a = 5
b = 3
sum_result = a + b  # Using variables in a mathematical operation
print(f"Sum of {a} and {b} is: {sum_result}")

# String formatting with variables
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)

# Constants (by convention)
PI = 3.14159  # Constants are typically written in all caps
radius = 5
area = PI * (radius ** 2)
print(f"Area of a circle with radius {radius}: {area}")

# Variable type
print(f"Type of 'name': {type(name)}")
print(f"Type of 'age': {type(age)}")
print(f"Type of 'PI': {type(PI)}")

# Variable naming conventions
snake_case_variable = "This is a snake case variable"
camelCaseVariable = "This is a camel case variable (not typical in Python)"
_private_var = "This is a convention for private variables"

print(snake_case_variable)
print(camelCaseVariable)
print(_private_var)
