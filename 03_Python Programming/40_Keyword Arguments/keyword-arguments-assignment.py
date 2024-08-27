# 4- Keyword Arguments - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Recipe Creator
# Create a function called create_recipe that takes the following parameters:
# - name (required): the name of the recipe
# - ingredients (required): a list of ingredients
# - prep_time (optional): preparation time in minutes (default to 0)
# - cook_time (optional): cooking time in minutes (default to 0)
# - instructions (optional): a list of cooking instructions (default to an empty list)
# The function should return a dictionary containing all the recipe information.

# Hint: Use default values for optional parameters and create a dictionary to store the recipe information.

def create_recipe(name, ingredients, prep_time=0, cook_time=0, instructions=None):
    # Your code here
    pass

# Test your function
print(create_recipe("Pasta", ["Spaghetti", "Tomato Sauce", "Cheese"], prep_time=10, cook_time=15))
print(create_recipe("Toast", ["Bread", "Butter"], instructions=["Toast bread", "Spread butter"]))


# Question 2: Flexible Formatter
# Create a function called format_string that takes a string as the first argument
# and can accept any number of keyword arguments. The function should replace any
# occurrences of {key} in the string with the corresponding value from the keyword arguments.

# Hint: Use **kwargs to accept any number of keyword arguments and the str.format() method with **kwargs.

def format_string(template, **kwargs):
    # Your code here
    pass

# Test your function
print(format_string("Hello, {name}! You are {age} years old.", name="Alice", age=30))
print(format_string("The {animal} jumped over the {obstacle}.", animal="cat", obstacle="moon", color="brown"))


# Question 3: Advanced Calculator
# Create a function called calculate that performs different mathematical operations
# based on the provided keyword arguments. The function should accept the following:
# - operation (required): a string specifying the operation ('add', 'subtract', 'multiply', 'divide')
# - numbers (required): a list of numbers to perform the operation on
# - round_result (optional): a boolean indicating whether to round the result (default to False)
# - round_to (optional): number of decimal places to round to (default to 2, only used if round_result is True)

# Hint: Use a dictionary to map operation strings to lambda functions. Use the round() function conditionally.

def calculate(operation, numbers, round_result=False, round_to=2):
    # Your code here
    pass

# Test your function
print(calculate(operation="add", numbers=[1, 2, 3, 4, 5]))
print(calculate(operation="multiply", numbers=[2, 3, 4], round_result=True))
print(calculate(operation="divide", numbers=[10, 3], round_result=True, round_to=3))

