# 12- While Loops - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Guessing Game
# Create a function called guessing_game that generates a random number between 1 and 100,
# and then prompts the user to guess the number. The game should continue until the user
# guesses correctly. After each guess, the function should tell the user if their guess
# was too high or too low. Keep track of the number of guesses and display it at the end.

# Hint: Use the random module to generate a random number. Use a while loop to continue
# prompting the user until they guess correctly.

import random

def guessing_game():
    # Your code here
    pass

# Test your function
# guessing_game()


# Question 2: Collatz Conjecture
# The Collatz Conjecture states that for any positive integer n, the sequence defined by:
# - If n is even, the next term is n / 2
# - If n is odd, the next term is 3n + 1
# will eventually reach 1, regardless of the starting value.

# Create a function called collatz_sequence that takes a positive integer as input and
# returns a list of numbers in the Collatz sequence starting from that number and ending at 1.

# Hint: Use a while loop to generate the sequence. Be sure to handle both even and odd cases.

def collatz_sequence(n):
    # Your code here
    pass

# Test your function
print(collatz_sequence(13))  # Should print [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


# Question 3: Password Validator
# Create a function called validate_password that prompts the user to enter a password
# and validates it against the following criteria:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one digit
# The function should continue prompting the user until a valid password is entered.

# Hint: Use a while loop to keep prompting the user. Use separate functions to check
# each criterion, and combine them in the main validation loop.

def validate_password():
    # Your code here
    pass

# Test your function
# validate_password()

