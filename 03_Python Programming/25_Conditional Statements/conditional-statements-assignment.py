# 2-Conditional-Statements-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Grade Calculator
# Write a function that takes a student's score as input and returns their grade according to the following criteria:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# The function should also handle invalid inputs (scores below 0 or above 100).
# Hint: Use if-elif-else statements and consider the order of conditions.

def calculate_grade(score):
    # TODO: Implement the function
    pass

# Test your function
print(calculate_grade(85))  # Should print "B"
print(calculate_grade(92))  # Should print "A"
print(calculate_grade(50))  # Should print "F"
print(calculate_grade(110))  # Should handle invalid input


# Question 2: Leap Year Checker
# Create a function that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Hint: Use nested if statements or logical operators to check the conditions.

def is_leap_year(year):
    # TODO: Implement the function
    pass

# Test your function
print(is_leap_year(2000))  # Should print True
print(is_leap_year(1900))  # Should print False
print(is_leap_year(2024))  # Should print True
print(is_leap_year(2023))  # Should print False


# Question 3: Simple Calculator
# Implement a function that takes two numbers and an operator (+, -, *, /) as input,
# and returns the result of the operation. The function should handle division by zero
# and invalid operators.
# Hint: Use if-elif statements for different operators and consider edge cases.

def simple_calculator(num1, num2, operator):
    # TODO: Implement the function
    pass

# Test your function
print(simple_calculator(10, 5, '+'))  # Should print 15
print(simple_calculator(10, 5, '-'))  # Should print 5
print(simple_calculator(10, 5, '*'))  # Should print 50
print(simple_calculator(10, 5, '/'))  # Should print 2.0
print(simple_calculator(10, 0, '/'))  # Should handle division by zero
print(simple_calculator(10, 5, '%'))  # Should handle invalid operator


# Bonus Challenge: Rock Paper Scissors Game
# Create a function that simulates a game of Rock Paper Scissors between the user and the computer.
# The function should take the user's choice as input, randomly generate the computer's choice,
# determine the winner, and return the result.
# Hint: Use the random module to generate the computer's choice, and use nested if statements
# or a combination of if-elif statements to determine the winner.

import random

def rock_paper_scissors(user_choice):
    # TODO: Implement the function
    pass

# Test your function
print(rock_paper_scissors("rock"))
print(rock_paper_scissors("paper"))
print(rock_paper_scissors("scissors"))
print(rock_paper_scissors("invalid"))  # Should handle invalid input

