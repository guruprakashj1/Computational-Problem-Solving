# 8- For Loops - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Factorial Calculator
# Create a function called calculate_factorial that takes a positive integer n as input
# and returns its factorial (n!). Use a for loop to calculate the factorial.
# Remember, 0! is defined as 1.

# Hint: Initialize the result to 1 and use a for loop to multiply numbers from 1 to n.

def calculate_factorial(n):
    # Your code here
    pass

# Test your function
print(calculate_factorial(5))  # Should print 120
print(calculate_factorial(0))  # Should print 1
print(calculate_factorial(10))  # Should print 3628800


# Question 2: Prime Number Checker
# Create a function called is_prime that takes a positive integer as input and
# returns True if the number is prime, and False otherwise.
# A prime number is only divisible by 1 and itself.

# Hint: Use a for loop to check divisibility from 2 to the square root of the number.
# You can import math and use math.isqrt() to get the integer square root.

import math

def is_prime(n):
    # Your code here
    pass

# Test your function
print(is_prime(17))  # Should print True
print(is_prime(4))   # Should print False
print(is_prime(97))  # Should print True
print(is_prime(100)) # Should print False


# Question 3: Pattern Printer
# Create a function called print_pattern that takes a positive integer n as input
# and prints the following pattern:
# For n = 5:
# 1
# 22
# 333
# 4444
# 55555

# Hint: Use nested for loops. The outer loop controls the rows,
# and the inner loop prints the numbers in each row.

def print_pattern(n):
    # Your code here
    pass

# Test your function
print_pattern(5)
# Should print:
# 1
# 22
# 333
# 4444
# 55555

print()  # Add a blank line

print_pattern(3)
# Should print:
# 1
# 22
# 333
