# 2- Arguments
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various types of arguments in Python functions

# 1. Positional Arguments
def greet(name, greeting):
    """Basic function with positional arguments"""
    return f"{greeting}, {name}!"

print("1. Positional Arguments:")
print(greet("Alice", "Hello"))
print()

# 2. Keyword Arguments
def describe_person(name, age, city):
    """Function demonstrating keyword arguments"""
    return f"{name} is {age} years old and lives in {city}."

print("2. Keyword Arguments:")
print(describe_person(age=30, city="New York", name="Bob"))
print()

# 3. Default Arguments
def power(base, exponent=2):
    """Function with a default argument"""
    return base ** exponent

print("3. Default Arguments:")
print(power(3))      # Uses default exponent
print(power(3, 3))   # Overrides default exponent
print()

# 4. Variable-Length Arguments (*args)
def sum_all(*args):
    """Function accepting variable number of arguments"""
    return sum(args)

print("4. Variable-Length Arguments:")
print(sum_all(1, 2, 3, 4, 5))
print()

# 5. Keyword Variable-Length Arguments (**kwargs)
def print_info(**kwargs):
    """Function accepting variable number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("5. Keyword Variable-Length Arguments:")
print_info(name="Charlie", age=35, job="Developer")
print()

# 6. Positional-Only Arguments (Python 3.8+)
def multiply(a, b, /):
    """Function with positional-only arguments"""
    return a * b

print("6. Positional-Only Arguments:")
print(multiply(4, 5))
# print(multiply(a=4, b=5))  # This would raise a TypeError
print()

# 7. Keyword-Only Arguments
def greet_formally(*, first_name, last_name):
    """Function with keyword-only arguments"""
    return f"Hello, {first_name} {last_name}!"

print("7. Keyword-Only Arguments:")
print(greet_formally(first_name="John", last_name="Doe"))
# print(greet_formally("John", "Doe"))  # This would raise a TypeError
print()

# 8. Combining Different Types of Arguments
def complex_function(a, b, /, c, d, *args, e, f, **kwargs):
    """Function combining various types of arguments"""
    print(f"a, b (positional-only): {a}, {b}")
    print(f"c, d: {c}, {d}")
    print(f"args: {args}")
    print(f"e, f (keyword-only): {e}, {f}")
    print(f"kwargs: {kwargs}")

print("8. Combining Different Types of Arguments:")
complex_function(1, 2, 3, 4, 5, 6, e=7, f=8, g=9, h=10)
print()

# This program covers various types of arguments in Python functions,
# demonstrating their usage and flexibility.
