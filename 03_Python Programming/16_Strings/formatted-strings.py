# 5-Formatted-Strings-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# 1. f-Strings (Formatted String Literals)

name = "Alice"
age = 30

# Basic f-string
print(f"My name is {name} and I am {age} years old.")

# f-string with expressions
print(f"Next year, I will be {age + 1} years old.")

# f-string with method calls
print(f"My name in uppercase: {name.upper()}")

# f-string with format specifiers
pi = 3.14159
print(f"Pi to 2 decimal places: {pi:.2f}")

# Alignment with f-strings
for i in range(1, 4):
    print(f"Number {i:2d}: {i*i:3d}")

# 2. str.format() Method

# Basic usage
print("My name is {} and I am {} years old.".format(name, age))

# Using positional arguments
print("The {0} is {1} years old. {0} likes to code.".format(name, age))

# Using keyword arguments
print("My name is {name} and I am {age} years old.".format(name="Bob", age=25))

# Alignment and padding
for i in range(1, 4):
    print("Number {:2d}: {:3d}".format(i, i*i))

# 3. %-formatting (String Interpolation)

# Basic usage
print("My name is %s and I am %d years old." % (name, age))

# With format specifiers
price = 19.99
print("The price is $%.2f" % price)

# Comparison of methods

item = "apple"
count = 3
price = 0.99

# Using f-string
print(f"I have {count} {item}s, each costing ${price:.2f}")

# Using str.format()
print("I have {0} {1}s, each costing ${2:.2f}".format(count, item, price))

# Using %-formatting
print("I have %d %ss, each costing $%.2f" % (count, item, price))

# Advanced formatting

import datetime

# Date formatting
today = datetime.date.today()
print(f"Today's date is {today:%B %d, %Y}")

# Number formatting
large_number = 1234567890
print(f"Large number with commas: {large_number:,}")

# Percentage formatting
percentage = 0.75
print(f"Percentage: {percentage:.1%}")

# Hexadecimal formatting
hex_number = 255
print(f"Hexadecimal: {hex_number:#x}")

# Nested formatting
nested = {"name": "Alice", "age": 30}
print(f"Nested dict: {nested['name']} is {nested['age']}")

# Multiline f-string
multiline = f"""
Name: {name}
Age: {age}
Next Year: {age + 1}
"""
print(multiline)

# Using f-strings with conditional expressions
status = "adult" if age >= 18 else "minor"
print(f"{name} is a {status}")

