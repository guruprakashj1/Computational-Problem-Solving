# 7-Numbers-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Importing necessary modules
import math
import random

# Integer examples
int_num1 = 42
int_num2 = -17
print(f"Integers: {int_num1}, {int_num2}")

# Floating-point examples
float_num1 = 3.14
float_num2 = -0.001
float_num3 = 2.5e-4  # Scientific notation
print(f"Floats: {float_num1}, {float_num2}, {float_num3}")

# Complex number example
complex_num = 3 + 4j
print(f"Complex number: {complex_num}")

# Basic arithmetic operations
a, b = 10, 3
print(f"\nArithmetic operations with {a} and {b}:")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")  # Always returns a float
print(f"Floor Division: {a // b}")  # Rounds down to nearest integer
print(f"Modulus: {a % b}")  # Remainder of division
print(f"Exponentiation: {a ** b}")

# Built-in functions for numbers
numbers = [1, -5, 3.14, -2.5, 10]
print(f"\nBuilt-in functions:")
print(f"Absolute value of -5: {abs(-5)}")
print(f"Rounded value of 3.14159 to 2 decimal places: {round(3.14159, 2)}")
print(f"Maximum of {numbers}: {max(numbers)}")
print(f"Minimum of {numbers}: {min(numbers)}")
print(f"2 raised to the power of 3: {pow(2, 3)}")

# Type conversion
print(f"\nType conversion:")
print(f"Integer conversion of 3.14: {int(3.14)}")
print(f"Float conversion of 42: {float(42)}")
print(f"Complex conversion of 5: {complex(5)}")

# Using the math module
print(f"\nMath module functions:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Sine of 30 degrees: {math.sin(math.radians(30))}")
print(f"Value of pi: {math.pi}")
print(f"Value of e: {math.e}")

# Using the random module
print(f"\nRandom module functions:")
print(f"Random float between 0 and 1: {random.random()}")
print(f"Random integer between 1 and 10: {random.randint(1, 10)}")
print(f"Random choice from a list: {random.choice(['apple', 'banana', 'cherry'])}")

# Demonstration of floating-point precision
print(f"\nFloating-point precision:")
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # Note: This might not be exactly 0.3
print(f"Is 0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")

# Large integer demonstration
large_int = 123456789012345678901234567890
print(f"\nLarge integer: {large_int}")
print(f"Type of large integer: {type(large_int)}")

# Complex number operations
c1 = 3 + 4j
c2 = 1 - 2j
print(f"\nComplex number operations:")
print(f"Addition: {c1} + {c2} = {c1 + c2}")
print(f"Multiplication: {c1} * {c2} = {c1 * c2}")
print(f"Absolute value of {c1}: {abs(c1)}")

# Number system conversions
decimal_num = 42
print(f"\nNumber system conversions for {decimal_num}:")
print(f"Binary: {bin(decimal_num)}")
print(f"Octal: {oct(decimal_num)}")
print(f"Hexadecimal: {hex(decimal_num)}")

