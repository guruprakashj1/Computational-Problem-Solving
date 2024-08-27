# 8-Working-with-Numbers-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

import math
import random
from decimal import Decimal
from fractions import Fraction

# Basic arithmetic operations
a, b = 10, 3
print(f"Basic arithmetic:")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")  # Floor division
print(f"a % b = {a % b}")    # Modulus
print(f"a ** b = {a ** b}")  # Exponentiation

# Augmented assignment
c = 5
c += 2  # Equivalent to c = c + 2
print(f"\nAfter c += 2, c = {c}")

# Order of operations
result = 2 + 3 * 4
print(f"\nOrder of operations: 2 + 3 * 4 = {result}")

# Using the math module
print(f"\nMath module functions:")
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Sine of 30 degrees: {math.sin(math.radians(30))}")
print(f"Ceiling of 3.7: {math.ceil(3.7)}")

# Using the random module
print(f"\nRandom module functions:")
print(f"Random float between 0 and 1: {random.random()}")
print(f"Random integer between 1 and 10: {random.randint(1, 10)}")
print(f"Random choice from list: {random.choice([1, 2, 3, 4, 5])}")

# Number formatting
pi = math.pi
print(f"\nNumber formatting:")
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Pi in scientific notation: {pi:e}")
print(f"Pi as percentage: {pi:.2%}")

# Type conversion
print(f"\nType conversion:")
print(f"Integer 5 to float: {float(5)}")
print(f"Float 3.14 to integer: {int(3.14)}")
print(f"String '100' to integer: {int('100')}")

# Working with large numbers (Decimal)
print(f"\nWorking with Decimal:")
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(f"0.1 + 0.2 as floats: {0.1 + 0.2}")
print(f"0.1 + 0.2 as Decimals: {d1 + d2}")

# Fractions
print(f"\nWorking with Fraction:")
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print(f"1/3 + 1/6 = {f1 + f2}")

# Bitwise operations
x, y = 10, 6  # In binary: 1010 and 0110
print(f"\nBitwise operations:")
print(f"x & y = {x & y}")  # AND
print(f"x | y = {x | y}")  # OR
print(f"x ^ y = {x ^ y}")  # XOR
print(f"~x = {~x}")        # NOT
print(f"x << 1 = {x << 1}")  # Left shift
print(f"x >> 1 = {x >> 1}")  # Right shift

# Number systems
num = 42
print(f"\nNumber systems:")
print(f"Decimal 42 in binary: {bin(num)}")
print(f"Decimal 42 in octal: {oct(num)}")
print(f"Decimal 42 in hexadecimal: {hex(num)}")

# Complex numbers
c1 = 3 + 4j
c2 = 1 - 2j
print(f"\nComplex numbers:")
print(f"c1 + c2 = {c1 + c2}")
print(f"Magnitude of c1: {abs(c1)}")

# Error handling in numeric operations
try:
    result = 10 / 0
except ZeroDivisionError:
    print("\nError: Division by zero!")

# Using underscores for readability in large numbers
large_num = 1_000_000_000
print(f"\nLarge number with underscores: {large_num}")

