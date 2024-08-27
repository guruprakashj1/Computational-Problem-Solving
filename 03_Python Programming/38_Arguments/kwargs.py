# 7- **args (Keyword Variable-Length Arguments)
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of **kwargs in Python

# 1. Basic function with **kwargs
def print_kwargs(**kwargs):
    """
    Function to print all keyword arguments.
    **kwargs collects all keyword arguments into a dictionary.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("1. Basic **kwargs usage:")
print_kwargs(name="Alice", age=30, city="New York")
print()

# 2. Combining **kwargs with regular arguments
def greet(greeting, **kwargs):
    """
    Function demonstrating **kwargs with a regular argument.
    Regular arguments must come before **kwargs.
    """
    print(f"{greeting}!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("2. Combining **kwargs with regular arguments:")
greet("Hello", name="Bob", age=25)
print()

# 3. Unpacking a dictionary into **kwargs
def create_person(name, age, **kwargs):
    """Function to create a person dictionary with optional additional info."""
    person = {"name": name, "age": age}
    person.update(kwargs)
    return person

person_info = {"occupation": "Engineer", "city": "San Francisco"}
print("3. Unpacking a dictionary into **kwargs:")
print(create_person("Charlie", 35, **person_info))
print()

# 4. Using **kwargs in lambda functions
format_person = lambda **kwargs: ", ".join(f"{k}={v}" for k, v in kwargs.items())

print("4. **kwargs in lambda functions:")
print(format_person(name="David", age=40, country="Canada"))
print()

# 5. Type hinting with **kwargs
def process_data(**kwargs: dict) -> None:
    """
    Function demonstrating type hinting with **kwargs.
    This suggests that kwargs is a dictionary of key-value pairs.
    """
    for key, value in kwargs.items():
        print(f"Processing {key}: {value}")

print("5. Type hinting with **kwargs:")
process_data(id=1, data="sample", category="test")
print()

# 6. Combining *args and **kwargs
def example_function(*args, **kwargs):
    """
    Function demonstrating the combination of *args and **kwargs.
    *args collects positional arguments, **kwargs collects keyword arguments.
    """
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

print("6. Combining *args and **kwargs:")
example_function(1, 2, 3, name="Eve", age=28)
print()

# 7. Using **kwargs to forward arguments
def wrapper_function(**kwargs):
    """
    A wrapper function that forwards all its keyword arguments to another function.
    This is a common use case in decorators and API wrappers.
    """
    print("Before calling the function")
    process_data(**kwargs)  # Forwarding kwargs to process_data
    print("After calling the function")

print("7. Forwarding **kwargs:")
wrapper_function(id=2, status="active", priority="high")
print()

# This program covers various aspects of **kwargs in Python,
# demonstrating its flexibility and common use cases.
