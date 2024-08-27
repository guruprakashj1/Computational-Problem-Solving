# 14- Functions - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Palindrome Checker
# Create a function called is_palindrome that takes a string as input and returns True if the string is a palindrome, and False otherwise.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

# Hint: You can use string methods like lower() and replace() to preprocess the string, and slicing to reverse it.

def is_palindrome(s: str) -> bool:
    # Your code here
    pass

# Test your function
print(is_palindrome("A man a plan a canal Panama"))  # Should return True
print(is_palindrome("race a car"))  # Should return False
print(is_palindrome("Was it a car or a cat I saw?"))  # Should return True


# Question 2: Prime Factorization
# Create a function called prime_factors that takes a positive integer as input and returns a list of its prime factors in ascending order.
# If the input number is less than 2, the function should return an empty list.

# Hint: You can use a while loop to continuously divide the number by its smallest prime factor.

def prime_factors(n: int) -> list:
    # Your code here
    pass

# Test your function
print(prime_factors(84))  # Should return [2, 2, 3, 7]
print(prime_factors(17))  # Should return [17]
print(prime_factors(1))   # Should return []


# Question 3: Fibonacci Sequence Generator
# Create a generator function called fibonacci_generator that yields numbers in the Fibonacci sequence.
# The function should take an optional parameter max_value that specifies the maximum value to generate.
# If max_value is not provided, the generator should continue indefinitely.

# Hint: Use a while loop inside the generator function. Remember to use the yield keyword instead of return.

def fibonacci_generator(max_value=None):
    # Your code here
    pass

# Test your function
fib = fibonacci_generator(100)
print(list(fib))  # Should print Fibonacci numbers up to 100

# Bonus: Use the generator to print the first 10 Fibonacci numbers
fib_infinite = fibonacci_generator()
for _, num in zip(range(10), fib_infinite):
    print(num, end=" ")
print()  # New line at the end

