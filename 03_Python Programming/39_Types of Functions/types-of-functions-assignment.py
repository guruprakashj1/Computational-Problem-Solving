# 3- Types of Functions - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Recursive Function
# Create a recursive function called sum_digits that takes a positive integer as input
# and returns the sum of its digits. For example, sum_digits(123) should return 6 (1 + 2 + 3).

# Hint: You can use integer division (//) and modulo (%) operations to separate the digits.
# The base case should be when the number is less than 10.

def sum_digits(n):
    # Your code here
    pass

# Test your function
print(sum_digits(123))  # Should print 6
print(sum_digits(9876))  # Should print 30


# Question 2: Generator Function
# Create a generator function called prime_generator that yields prime numbers indefinitely.
# The function should yield the next prime number each time it's called.

# Hint: You can create a helper function is_prime(n) to check if a number is prime.
# Use a while True loop in the generator to continuously find and yield the next prime number.

def is_prime(n):
    # Helper function to check if a number is prime
    # Your code here
    pass

def prime_generator():
    # Your code here
    pass

# Test your function
gen = prime_generator()
for _ in range(10):
    print(next(gen), end=" ")  # Should print the first 10 prime numbers


# Question 3: Decorator Function
# Create a decorator function called time_it that measures and prints the execution time
# of the decorated function. The decorator should not modify the return value of the original function.

# Hint: You'll need to import the time module to measure execution time.
# Use time.time() before and after calling the original function to calculate the elapsed time.

import time

def time_it(func):
    # Your code here
    pass

# Test your decorator
@time_it
def slow_function():
    time.sleep(2)  # Simulate a slow operation
    return "Function completed"

print(slow_function())  # Should print the execution time and return "Function completed"

