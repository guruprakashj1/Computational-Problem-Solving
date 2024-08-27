# 14- Functions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of functions in Python

# 1. Basic function definition and calling
def greet(name):
    """This function greets the person passed in as a parameter"""
    return f"Hello, {name}!"

print("1. Basic function:")
print(greet("Alice"))
print()

# 2. Function with default parameter
def power(base, exponent=2):
    """
    This function calculates the power of a number.
    If no exponent is provided, it calculates the square.
    """
    return base ** exponent

print("2. Function with default parameter:")
print(power(3))      # Using default exponent
print(power(3, 3))   # Providing custom exponent
print()

# 3. Function with multiple return values
def min_max(numbers):
    """This function returns both the minimum and maximum of a list of numbers"""
    return min(numbers), max(numbers)

print("3. Function with multiple return values:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
minimum, maximum = min_max(numbers)
print(f"Min: {minimum}, Max: {maximum}")
print()

# 4. Lambda function
square = lambda x: x**2

print("4. Lambda function:")
print(square(5))
print()

# 5. Function as an argument (Higher-order function)
def apply_operation(func, x, y):
    """This function applies a given operation to two numbers"""
    return func(x, y)

add = lambda x, y: x + y
multiply = lambda x, y: x * y

print("5. Higher-order function:")
print(apply_operation(add, 3, 4))
print(apply_operation(multiply, 3, 4))
print()

# 6. Recursive function
def factorial(n):
    """This function calculates the factorial of a number recursively"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("6. Recursive function:")
print(factorial(5))
print()

# 7. Function with *args and **kwargs
def print_args(*args, **kwargs):
    """This function demonstrates the use of *args and **kwargs"""
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("7. Function with *args and **kwargs:")
print_args(1, 2, 3, name="Alice", age=30)
print()

# 8. Function with type hints
def greet_with_age(name: str, age: int) -> str:
    """This function demonstrates the use of type hints"""
    return f"Hello, {name}! You are {age} years old."

print("8. Function with type hints:")
print(greet_with_age("Bob", 25))
print()

# 9. Decorator function
def uppercase_decorator(func):
    """This decorator converts the result of the function to uppercase"""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"

print("9. Decorator function:")
print(say_hello())
print()

# This program covers various aspects of functions in Python,
# demonstrating their versatility and common use cases.
