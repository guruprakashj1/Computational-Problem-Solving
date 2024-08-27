# 6- xargs - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Flexible Arithmetic Function
# Create a function called flexible_arithmetic that takes an operation name as the first argument,
# followed by any number of numeric arguments. The function should perform the specified operation
# on all the numbers provided. Support the following operations: 'add', 'multiply', 'max', 'min'.
# If no numbers are provided, return None.

# Hint: Use a dictionary to map operation names to corresponding functions (sum, max, min).
# For multiplication, you can use the math.prod function from the math module.

import math

def flexible_arithmetic(operation, *args):
    # Your code here
    pass

# Test your function
print(flexible_arithmetic('add', 1, 2, 3, 4))  # Should return 10
print(flexible_arithmetic('multiply', 2, 3, 4))  # Should return 24
print(flexible_arithmetic('max', 5, 3, 9, 1))  # Should return 9
print(flexible_arithmetic('min', 5, 3, 9, 1))  # Should return 1
print(flexible_arithmetic('add'))  # Should return None


# Question 2: Tag Wrapper
# Create a function called wrap_with_tag that takes a tag name as the first argument,
# followed by any number of strings. The function should wrap each string with the specified HTML tag.
# If no strings are provided, it should return an empty list.

# Hint: Use list comprehension to apply the tag to each string in *args.

def wrap_with_tag(tag, *args):
    # Your code here
    pass

# Test your function
print(wrap_with_tag('p', 'Hello', 'World'))  # Should return ['<p>Hello</p>', '<p>World</p>']
print(wrap_with_tag('div', 'Content'))  # Should return ['<div>Content</div>']
print(wrap_with_tag('span'))  # Should return []


# Question 3: Flexible Data Processing
# Create a function called process_data that takes any number of lists as arguments.
# The function should perform the following operations:
# 1. Find the longest list among the inputs
# 2. Pad shorter lists with None values to match the length of the longest list
# 3. Create and return a new list of tuples, where each tuple contains the elements
#    from each input list at the same index.

# Hint: Use the max() function with a key to find the longest list.
# Use list comprehension with zip_longest from itertools to create the result.

from itertools import zip_longest

def process_data(*args):
    # Your code here
    pass

# Test your function
result = process_data([1, 2, 3], ['a', 'b'], [True, False, True, False])
print(result)
# Should return [(1, 'a', True), (2, 'b', False), (3, None, True), (None, None, False)]

