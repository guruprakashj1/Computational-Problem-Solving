# 11- Iterables
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of iterables in Python

# 1. Basic iteration over built-in iterables
print("1. Basic iteration:")
# List iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")
print("\n")

# String iteration
for char in "Python":
    print(char, end=" ")
print("\n")

# 2. Using iter() and next()
print("\n2. Using iter() and next():")
numbers = [1, 2, 3, 4, 5]
iter_numbers = iter(numbers)
print(next(iter_numbers))  # 1
print(next(iter_numbers))  # 2
print(next(iter_numbers))  # 3

# 3. Creating a custom iterable class
print("\n3. Custom iterable class:")
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration

evens = EvenNumbers(8)
for num in evens:
    print(num, end=" ")
print()

# 4. Generator function
print("\n4. Generator function:")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(8):
    print(num, end=" ")
print()

# 5. List comprehension
print("\n5. List comprehension:")
squares = [x**2 for x in range(1, 6)]
print(squares)

# 6. Dictionary iteration
print("\n6. Dictionary iteration:")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# 7. Using enumerate()
print("\n7. Using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 8. Using zip()
print("\n8. Using zip():")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 9. File iteration
print("\n9. File iteration:")
with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3")

with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# This program covers various aspects of iterables in Python,
# demonstrating their versatility and common use cases.
