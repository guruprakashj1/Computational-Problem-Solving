# 8- For Loops
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of for loops in Python

# Basic for loop with a list
print("1. Basic for loop with a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
print()

# Using range() function
print("2. Using range() function:")
for i in range(5):
    print(f"Count: {i}")
print()

# Using range() with start, stop, and step
print("3. Using range() with start, stop, and step:")
for i in range(2, 10, 2):
    print(f"Even number: {i}")
print()

# Iterating over a string
print("4. Iterating over a string:")
for char in "Python":
    print(char)
print()

# Using enumerate() to get index and value
print("5. Using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
print()

# Nested for loops
print("6. Nested for loops:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each inner loop
print()

# Using break statement
print("7. Using break statement:")
for number in range(1, 10):
    if number == 5:
        break
    print(number, end=" ")
print("\n")

# Using continue statement
print("8. Using continue statement:")
for number in range(1, 6):
    if number == 3:
        continue
    print(number, end=" ")
print("\n")

# Using else clause with for loop
print("9. Using else clause with for loop:")
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed normally")
print()

# List comprehension
print("10. List comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# This program covers various aspects of for loops in Python,
# demonstrating their versatility and common use cases.
