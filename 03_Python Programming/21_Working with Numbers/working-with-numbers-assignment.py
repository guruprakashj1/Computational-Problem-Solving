# 8-Working-with-Numbers-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

import math
import random

# Question 1: Statistical Calculator
# Create a function that takes a list of numbers and returns a dictionary containing:
# - mean (average)
# - median (middle value)
# - mode (most frequent value)
# - standard deviation
# Hint: Use the statistics module for some of these calculations.

import statistics

def calculate_statistics(numbers):
    # TODO: Implement the function
    pass

# Test your function
data = [2, 3, 3, 4, 5, 5, 5, 6, 6, 7]
print(calculate_statistics(data))


# Question 2: Interest Calculator
# Write a function that calculates compound interest.
# The function should take principal amount, annual interest rate (in percentage),
# time period (in years), and number of times interest is compounded per year.
# Return the final amount rounded to two decimal places.
# Formula: A = P(1 + r/n)^(nt)
# Where: A = final amount, P = principal, r = annual rate, n = compound frequency, t = time in years
# Hint: Use the math.pow() function for exponentiation.

def compound_interest(principal, rate, time, compound_freq):
    # TODO: Implement the function
    pass

# Test your function
print(compound_interest(1000, 5, 5, 12))  # 5% interest, compounded monthly for 5 years


# Question 3: Binary to Decimal Converter
# Implement a function that converts a binary number (given as a string) to its decimal equivalent.
# Do not use the built-in int() function with base 2.
# Hint: You can iterate through the binary string, using powers of 2.

def binary_to_decimal(binary_string):
    # TODO: Implement the function
    pass

# Test your function
print(binary_to_decimal("1010"))  # Should print 10
print(binary_to_decimal("11110000"))  # Should print 240


# Bonus Challenge: Monte Carlo Pi Estimation
# Use the Monte Carlo method to estimate the value of Pi.
# The idea is to randomly generate points in a 1x1 square and determine the ratio of points
# that fall within a quarter circle of radius 1 to the total number of points.
# This ratio approximates Pi/4.
# Hint: Use random.random() to generate points and math.hypot() to calculate distance from origin.

def estimate_pi(num_points):
    # TODO: Implement the function
    pass

# Test your function
print(estimate_pi(1000000))  # Should be close to math.pi

