# 1- Defining Functions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of defining functions in Python

# 1. Basic function definition
def greet(name):
    """
    This function greets the person passed in as a parameter.
    
    Args:
    name (str): The name of the person to greet
    
    Returns:
    str: A greeting message
    """
    return f"Hello, {name}!"

# Calling the greet function
print("1. Basic function:")
print(greet("Alice"))
print()

# 2. Function with default parameter
def power(base, exponent=2):
    """
    This function calculates the power of a number.
    If no exponent is provided, it calculates the square.
    
    Args:
    base (int or float): The base number
    exponent (int, optional): The exponent (default is 2)
    
    Returns:
    int or float: The result of base raised to the exponent
    """
    return base ** exponent

# Calling the power function
print("2. Function with default parameter:")
print(power(3))      # Using default exponent
print(power(3, 3))   # Providing custom exponent
print()

# 3. Function with multiple parameters and return values
def calculate_rectangle(length, width):
    """
    This function calculates the area and perimeter of a rectangle.
    
    Args:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    tuple: A tuple containing the area and perimeter
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Calling the calculate_rectangle function
print("3. Function with multiple parameters and return values:")
rect_area, rect_perimeter = calculate_rectangle(5, 3)
print(f"Area: {rect_area}, Perimeter: {rect_perimeter}")
print()

# 4. Function with type hints
def add_numbers(a: int, b: int) -> int:
    """
    This function adds two numbers.
    
    Args:
    a (int): The first number
    b (int): The second number
    
    Returns:
    int: The sum of a and b
    """
    return a + b

# Calling the add_numbers function
print("4. Function with type hints:")
print(add_numbers(5, 7))
print()

# 5. Function with variable number of arguments
def sum_all(*args):
    """
    This function sums up all the arguments passed to it.
    
    Args:
    *args: Variable number of arguments
    
    Returns:
    int or float: The sum of all arguments
    """
    return sum(args)

# Calling the sum_all function
print("5. Function with variable number of arguments:")
print(sum_all(1, 2, 3, 4, 5))
print()

# This program covers various aspects of defining functions in Python,
# demonstrating their versatility and common use cases.
