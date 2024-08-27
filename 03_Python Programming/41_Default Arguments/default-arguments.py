# 5- Default Arguments
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of default arguments in Python

# 1. Basic function with a default argument
def greet(name, greeting="Hello"):
    """A simple function demonstrating a default argument"""
    return f"{greeting}, {name}!"

print("1. Basic default argument:")
print(greet("Alice"))  # Uses default greeting
print(greet("Bob", "Hi"))  # Overrides default greeting
print()

# 2. Function with multiple default arguments
def create_profile(name, age, city="Unknown", occupation=None):
    """Function demonstrating multiple default arguments"""
    profile = f"Name: {name}, Age: {age}, City: {city}"
    if occupation:
        profile += f", Occupation: {occupation}"
    return profile

print("2. Multiple default arguments:")
print(create_profile("Charlie", 30))
print(create_profile("David", 25, "New York", "Developer"))
print()

# 3. Default arguments with mutable objects (potential pitfall)
def add_item(item, list_arg=[]):
    """
    Function demonstrating the pitfall of using mutable objects as default arguments
    Note: This is generally not recommended
    """
    list_arg.append(item)
    return list_arg

print("3. Mutable default argument (pitfall):")
print(add_item(1))  # Creates a new list [1]
print(add_item(2))  # Adds to the same list: [1, 2]
print(add_item(3, [10, 20]))  # Uses a new list: [10, 20, 3]
print(add_item(4))  # Back to the modified default list: [1, 2, 4]
print()

# 4. Correct way to use mutable objects with default arguments
def add_item_correct(item, list_arg=None):
    """
    Function demonstrating the correct way to use mutable objects with default arguments
    """
    if list_arg is None:
        list_arg = []
    list_arg.append(item)
    return list_arg

print("4. Correct use of mutable objects:")
print(add_item_correct(1))  # Creates a new list [1]
print(add_item_correct(2))  # Creates another new list [2]
print()

# 5. Using default arguments with keyword arguments
def power(base, exponent=2):
    """Function demonstrating default argument with keyword argument"""
    return base ** exponent

print("5. Default argument with keyword argument:")
print(power(3))  # Uses default exponent
print(power(2, exponent=3))  # Overrides default using keyword argument
print()

# 6. Default arguments with type hints
def greet_with_age(name: str, age: int = 30) -> str:
    """Function demonstrating default argument with type hints"""
    return f"Hello, {name}! You are {age} years old."

print("6. Default argument with type hints:")
print(greet_with_age("Eve"))
print(greet_with_age("Frank", 25))
print()

# 7. Dynamic default values
import datetime

def log_message(message, timestamp=None):
    """Function demonstrating dynamic default value"""
    if timestamp is None:
        timestamp = datetime.datetime.now()
    return f"[{timestamp}] {message}"

print("7. Dynamic default value:")
print(log_message("First message"))
import time
time.sleep(2)  # Wait for 2 seconds
print(log_message("Second message"))
print()

# This program covers various aspects of default arguments in Python,
# demonstrating their usage, potential pitfalls, and best practices.
