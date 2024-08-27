# 2- Arguments - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Shopping Cart
# Create a function called calculate_total that calculates the total price of items in a shopping cart.
# The function should accept any number of keyword arguments where the key is the item name and the value is the price.
# Apply a discount if the total is over a certain threshold.
# 
# Function signature: calculate_total(discount_threshold=100, discount_percent=10, **items)
#
# Hint: Use **kwargs to accept the items and their prices. Sum up the prices and apply the discount if necessary.

def calculate_total(discount_threshold=100, discount_percent=10, **items):
    # Your code here
    pass

# Test your function
print(calculate_total(apple=0.5, banana=0.3, orange=0.6))
print(calculate_total(discount_threshold=50, discount_percent=5, shirt=20, pants=40, shoes=60))


# Question 2: Flexible Greeting
# Create a function called flexible_greeting that can accept various pieces of information about a person and create a greeting.
# The function should have parameters for name, age, city, and hobby, but should be flexible enough to work with any combination of these.
# If a piece of information is not provided, it should not be included in the greeting.
#
# Hint: Use default values of None for all parameters and check which ones are provided to construct the greeting.

def flexible_greeting(name=None, age=None, city=None, hobby=None):
    # Your code here
    pass

# Test your function
print(flexible_greeting(name="Alice", age=30))
print(flexible_greeting(name="Bob", city="New York", hobby="painting"))
print(flexible_greeting(name="Charlie", age=25, city="London", hobby="guitar"))


# Question 3: Math Operations
# Create a function called math_operation that performs a specified mathematical operation on a variable number of arguments.
# The function should accept an operation parameter (e.g., "add", "multiply") and any number of numeric arguments.
# If no numbers are provided, the function should return None.
#
# Function signature: math_operation(operation, *args)
#
# Hint: Use *args to accept any number of arguments. Use if/elif statements to perform different operations based on the operation parameter.

def math_operation(operation, *args):
    # Your code here
    pass

# Test your function
print(math_operation("add", 1, 2, 3, 4, 5))
print(math_operation("multiply", 2, 4, 6))
print(math_operation("subtract", 10, 4, 2))
print(math_operation("add"))  # Should return None
