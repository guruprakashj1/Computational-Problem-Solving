# 3-Control-Flow-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# 1. Conditional Statements

# if statement
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

# 2. Loops

# for loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()  # New line

# while loop
print("\nCounting down from 5 to 1:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print()  # New line

# 3. Control Statements

# break statement
print("\nBreak example:")
for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ")
print("\nLoop ended early")

# continue statement
print("\nContinue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print("\nSkipped 3")

# pass statement
class EmptyClass:
    pass

# 4. Exception Handling

# try-except
print("\nException handling:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# try-except-else-finally
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"You entered {num}")
finally:
    print("Thank you for using this program.")

# 5. Context Managers

# with statement
print("\nContext manager example:")
with open("example.txt", "w") as file:
    file.write("Hello, World!")
print("File has been written and closed automatically.")

# 6. Nested Control Structures

print("\nNested control structures:")
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()  # New line after each row

# 7. Ternary Operator

age = 20
status = "adult" if age >= 18 else "minor"
print(f"\nStatus: {status}")

# 8. Short-circuit Evaluation

print("\nShort-circuit evaluation:")
x = 5
y = 10
if x > 0 and y/x > 1:  # y/x is not evaluated if x <= 0
    print("Condition is true")

# 9. Loop with else clause
print("\nLoop with else clause:")
for i in range(5):
    if i == 10:  # This condition is never true
        break
    print(i, end=" ")
else:
    print("\nLoop completed normally")

