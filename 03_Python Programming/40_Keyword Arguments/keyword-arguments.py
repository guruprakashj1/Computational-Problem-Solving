# 4- Keyword Arguments
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of keyword arguments in Python

# 1. Basic function with keyword arguments
def greet(name, greeting="Hello"):
    """A simple function demonstrating keyword arguments with a default value"""
    return f"{greeting}, {name}!"

print("1. Basic keyword arguments:")
print(greet("Alice"))  # Uses default greeting
print(greet("Bob", greeting="Hi"))  # Overrides default greeting
print()

# 2. Function with multiple keyword arguments
def create_profile(name, age, city="Unknown", occupation=None):
    """Function demonstrating multiple keyword arguments, some with default values"""
    profile = f"Name: {name}, Age: {age}, City: {city}"
    if occupation:
        profile += f", Occupation: {occupation}"
    return profile

print("2. Multiple keyword arguments:")
print(create_profile("Charlie", 30))
print(create_profile("David", 25, city="New York", occupation="Developer"))
print()

# 3. Mixing positional and keyword arguments
def power(base, exponent=2):
    """Function demonstrating mixing of positional and keyword arguments"""
    return base ** exponent

print("3. Mixing positional and keyword arguments:")
print(power(3))  # Uses positional argument and default exponent
print(power(2, exponent=3))  # Uses positional and keyword argument
print()

# 4. Variable-length keyword arguments (**kwargs)
def print_key_values(**kwargs):
    """Function accepting variable number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("4. Variable-length keyword arguments:")
print_key_values(name="Eve", age=28, country="Canada")
print()

# 5. Keyword-only arguments
def greet_formally(*, first_name, last_name):
    """Function demonstrating keyword-only arguments"""
    return f"Hello, {first_name} {last_name}!"

print("5. Keyword-only arguments:")
print(greet_formally(first_name="John", last_name="Doe"))
# print(greet_formally("John", "Doe"))  # This would raise a TypeError
print()

# 6. Unpacking dictionaries into keyword arguments
def calculate_rectangle_area(length, width):
    """Function to calculate rectangle area"""
    return length * width

rectangle_dims = {"length": 5, "width": 3}

print("6. Unpacking dictionaries:")
print(f"Rectangle area: {calculate_rectangle_area(**rectangle_dims)}")
print()

# 7. Combining various argument types
def complex_function(a, b, *args, c, d=10, **kwargs):
    """Function combining positional, variable-length, keyword-only, and variable-length keyword arguments"""
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"c: {c}, d: {d}")
    print(f"kwargs: {kwargs}")

print("7. Combining various argument types:")
complex_function(1, 2, 3, 4, c=5, e=6, f=7)
print()

# This program covers various aspects of keyword arguments in Python,
# demonstrating their flexibility and use cases.
