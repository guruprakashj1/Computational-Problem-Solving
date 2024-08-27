# 7-Numbers-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

import math
import random

# Question 1: Prime Number Checker
# Write a function that takes a number as input and returns True if it's prime, False otherwise.
# A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
# Hint: You can optimize by checking up to the square root of the number.

def is_prime(n):
    # TODO: Implement the function
    pass

# Test your function
print(is_prime(17))  # Should return True
print(is_prime(4))   # Should return False


# Question 2: Temperature Converter
# Create a function that converts temperature from Celsius to Fahrenheit and vice versa.
# The function should take two parameters: the temperature and a unit identifier ('C' or 'F').
# It should return the converted temperature rounded to one decimal place.
# Formulas: 
# - Celsius to Fahrenheit: (C * 9/5) + 32
# - Fahrenheit to Celsius: (F - 32) * 5/9
# Hint: Use the round() function to round the result.

def convert_temperature(temp, unit):
    # TODO: Implement the function
    pass

# Test your function
print(convert_temperature(100, 'C'))  # Should return approximately 212.0
print(convert_temperature(32, 'F'))   # Should return 0.0


# Question 3: Random Password Generator
# Write a function that generates a random password of a specified length.
# The password should include a mix of uppercase letters, lowercase letters, numbers, and special characters.
# Hint: You can use string.ascii_letters, string.digits, and string.punctuation from the string module,
# along with random.choice() to select characters.

import string

def generate_password(length):
    # TODO: Implement the function
    pass

# Test your function
print(generate_password(12))  # Should print a random 12-character password


# Bonus Challenge: Fibonacci Sequence
# Implement a function that returns the nth number in the Fibonacci sequence.
# The Fibonacci sequence is defined as: F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.
# Your function should work efficiently for large values of n.
# Hint: Consider using memoization or an iterative approach for better performance.

def fibonacci(n):
    # TODO: Implement the function
    pass

# Test your function
print(fibonacci(10))  # Should return 55
print(fibonacci(50))  # Should return 12586269025

