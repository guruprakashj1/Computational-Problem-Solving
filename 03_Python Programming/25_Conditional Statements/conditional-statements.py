# 2-Conditional-Statements-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Simple if statement
x = 10
if x > 0:
    print("x is positive")

# if-else statement
y = -5
if y > 0:
    print("y is positive")
else:
    print("y is non-positive")

# if-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")

# Nested conditional statements
num = 15
if num > 0:
    if num % 2 == 0:
        print("num is positive and even")
    else:
        print("num is positive and odd")
else:
    print("num is non-positive")

# Using logical operators in conditions
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")

# Conditional expression (ternary operator)
is_adult = "Yes" if age >= 18 else "No"
print(f"Is adult? {is_adult}")

# Using 'in' operator for membership test
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is in the fruits list")

# Checking for multiple conditions
grade = 75
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Using 'pass' as a placeholder
if True:
    pass  # TODO: Implement this later

# Comparing strings
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")
elif name == "Bob":
    print("Hello, Bob!")
else:
    print("Hello, stranger!")

# Short-circuit evaluation
a = 5
b = 0
if b != 0 and a/b > 2:
    print("This won't cause a divide-by-zero error")

# Checking if a value is None
value = None
if value is None:
    print("Value is None")

# Using not operator
is_busy = False
if not is_busy:
    print("You are free")

# Chaining comparisons
number = 50
if 0 <= number <= 100:
    print("Number is between 0 and 100")

