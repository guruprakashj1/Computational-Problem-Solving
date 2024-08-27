# 10- Nested Loops
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of nested loops in Python

# 1. Basic nested for loops
print("1. Basic nested for loops:")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"({i}, {j})", end=" ")
    print()  # New line after each inner loop completes
print()

# 2. Nested loops with lists
print("2. Nested loops with lists:")
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "pink"]
for fruit in fruits:
    for color in colors:
        print(f"{color} {fruit}", end=", ")
    print()
print()

# 3. Creating a multiplication table
print("3. Multiplication table:")
for i in range(1, 6):  # Outer loop for rows
    for j in range(1, 6):  # Inner loop for columns
        print(f"{i*j:2d}", end=" ")
    print()
print()

# 4. Working with 2D lists (matrices)
print("4. Working with 2D lists:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
print()

# 5. Nested while loops
print("5. Nested while loops:")
i = 1
while i <= 3:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
print()

# 6. Breaking out of nested loops
print("6. Breaking out of nested loops:")
for x in range(3):
    for y in range(3):
        if x == y == 1:
            print("Breaking inner loop")
            break
        print(f"({x}, {y})", end=" ")
    print()
print()

# 7. Using enumerate with nested loops
print("7. Using enumerate with nested loops:")
characters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
for i, row in enumerate(characters):
    for j, char in enumerate(row):
        print(f"characters[{i}][{j}] = {char}")
    print()

# This program covers various aspects of nested loops in Python,
# demonstrating their versatility and common use cases.
