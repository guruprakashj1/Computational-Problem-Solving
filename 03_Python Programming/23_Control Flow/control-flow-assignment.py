# 3-Control-Flow-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: FizzBuzz
# Write a function that prints the numbers from 1 to n. But for multiples of 3, print "Fizz"
# instead of the number, and for the multiples of 5, print "Buzz". For numbers which are
# multiples of both 3 and 5, print "FizzBuzz".
# Hint: Use the modulo operator (%) and conditional statements.

def fizzbuzz(n):
    # TODO: Implement the function
    pass

# Test your function
fizzbuzz(15)


# Question 2: Prime Number Checker
# Write a function that takes a number as input and returns True if it's prime, False otherwise.
# A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
# Hint: You can optimize by checking up to the square root of the number.

def is_prime(number):
    # TODO: Implement the function
    pass

# Test your function
print(is_prime(17))  # Should return True
print(is_prime(4))   # Should return False


# Question 3: Password Validator
# Create a function that takes a password as input and returns True if it's valid, False otherwise.
# A valid password should:
# - Be at least 8 characters long
# - Contain at least one uppercase letter, one lowercase letter, and one digit
# - Not contain spaces
# Hint: You can use string methods like isupper(), islower(), isdigit(), and loops.

def is_valid_password(password):
    # TODO: Implement the function
    pass

# Test your function
print(is_valid_password("Abc123!@"))  # Should return True
print(is_valid_password("abc123"))    # Should return False
print(is_valid_password("ABC123!"))   # Should return False
print(is_valid_password("Abc 123!"))  # Should return False


# Bonus Challenge: Balanced Parentheses Checker
# Write a function that takes a string containing just the characters '(', ')', '{', '}', '[' and ']',
# and determines if the input string is valid. An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# Hint: You can use a stack (list) to keep track of opening brackets.

def is_balanced(s):
    # TODO: Implement the function
    pass

# Test your function
print(is_balanced("()"))        # Should return True
print(is_balanced("()[]{}"))    # Should return True
print(is_balanced("(]"))        # Should return False
print(is_balanced("([)]"))      # Should return False
print(is_balanced("{[]}"))      # Should return True

