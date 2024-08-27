# 3- Types of Functions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various types of functions in Python

import functools

# 1. Built-in Functions
print("1. Built-in Functions:")
numbers = [1, 2, 3, 4, 5]
print(f"Sum of numbers: {sum(numbers)}")
print(f"Maximum number: {max(numbers)}")
print(f"Length of list: {len(numbers)}")
print()

# 2. User-Defined Functions
def greet(name):
    """A simple user-defined function"""
    return f"Hello, {name}!"

print("2. User-Defined Functions:")
print(greet("Alice"))
print()

# 3. Anonymous (Lambda) Functions
square = lambda x: x**2

print("3. Anonymous (Lambda) Functions:")
print(f"Square of 5: {square(5)}")
print()

# 4. Higher-Order Functions
def apply_operation(func, x, y):
    """A higher-order function that applies a given function to two arguments"""
    return func(x, y)

add = lambda x, y: x + y
multiply = lambda x, y: x * y

print("4. Higher-Order Functions:")
print(f"Result of add: {apply_operation(add, 3, 4)}")
print(f"Result of multiply: {apply_operation(multiply, 3, 4)}")
print()

# 5. Recursive Functions
def factorial(n):
    """A recursive function to calculate factorial"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("5. Recursive Functions:")
print(f"Factorial of 5: {factorial(5)}")
print()

# 6. Generator Functions
def fibonacci_generator(n):
    """A generator function for Fibonacci sequence"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("6. Generator Functions:")
print("First 5 Fibonacci numbers:", end=" ")
for num in fibonacci_generator(5):
    print(num, end=" ")
print("\n")

# 7. Coroutines (Python 3.5+)
import asyncio

async def greet_async(name):
    """A simple coroutine"""
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    return f"Hello, {name}!"

print("7. Coroutines:")
async def main():
    result = await greet_async("Bob")
    print(result)

asyncio.run(main())
print()

# 8. Method Functions
class Calculator:
    """A class demonstrating different types of method functions"""
    
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def add(self, x):
        """Instance method"""
        self.value += x
    
    @classmethod
    def create_empty(cls):
        """Class method"""
        return cls()
    
    @staticmethod
    def is_even(x):
        """Static method"""
        return x % 2 == 0

print("8. Method Functions:")
calc = Calculator(5)
calc.add(3)
print(f"Calculator value: {calc.value}")
print(f"Is 4 even? {Calculator.is_even(4)}")
print()

# 9. Closure Functions
def outer_function(x):
    """A function that returns a closure"""
    def inner_function(y):
        return x + y
    return inner_function

print("9. Closure Functions:")
add_five = outer_function(5)
print(f"Result of add_five(3): {add_five(3)}")
print()

# 10. Decorator Functions
def uppercase_decorator(func):
    """A decorator that converts the result to uppercase"""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"

print("10. Decorator Functions:")
print(say_hello())
print()

# This program demonstrates various types of functions in Python,
# showcasing their different use cases and capabilities.
