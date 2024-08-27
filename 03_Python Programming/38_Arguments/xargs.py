# 6- xargs (Variable-Length Arguments)
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of *args in Python

# 1. Basic function with *args
def sum_all(*args):
    """
    Function to sum all given numbers.
    *args collects all positional arguments into a tuple.
    """
    return sum(args)

print("1. Basic *args usage:")
print(sum_all(1, 2, 3))  # Passing multiple arguments
print(sum_all(10, 20, 30, 40))  # Can handle any number of arguments
print()

# 2. Combining *args with regular arguments
def greet(greeting, *names):
    """
    Function demonstrating *args with a regular argument.
    Regular arguments must come before *args.
    """
    for name in names:
        print(f"{greeting}, {name}!")

print("2. Combining *args with regular arguments:")
greet("Hello", "Alice", "Bob", "Charlie")
print()

# 3. Unpacking a list into *args
def multiply(*args):
    """Function to multiply all given numbers."""
    result = 1
    for num in args:
        result *= num
    return result

numbers = [2, 3, 4, 5]
print("3. Unpacking a list into *args:")
print(multiply(*numbers))  # Unpacking the list into individual arguments
print()

# 4. Using *args in lambda functions
power = lambda x, *args: x ** (args[0] if args else 1)

print("4. *args in lambda functions:")
print(power(2))  # No extra argument, uses default exponent 1
print(power(2, 3))  # Uses 3 as the exponent
print()

# 5. Type hinting with *args
def print_args(*args: int) -> None:
    """
    Function demonstrating type hinting with *args.
    This suggests that all arguments should be integers.
    """
    for arg in args:
        print(arg)

print("5. Type hinting with *args:")
print_args(1, 2, 3)
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
example_function(1, 2, 3, name="Alice", age=30)
print()

# 7. Using *args to forward arguments
def wrapper_function(*args):
    """
    A wrapper function that forwards all its arguments to another function.
    This is a common use case in decorators.
    """
    print("Before calling the function")
    print_args(*args)  # Forwarding args to print_args
    print("After calling the function")

print("7. Forwarding *args:")
wrapper_function(10, 20, 30)
print()

# This program covers various aspects of *args in Python,
# demonstrating its flexibility and common use cases.
