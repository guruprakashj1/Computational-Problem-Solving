# 9- IF..Else - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Leap Year Checker
# Create a function called is_leap_year that takes a year as input and returns
# True if it's a leap year, and False otherwise.
# A leap year is divisible by 4, but if it's divisible by 100, it must also be divisible by 400.

# Hint: Use nested if statements or logical operators to check the conditions.

def is_leap_year(year):
    # Your code here
    pass

# Test your function
print(is_leap_year(2000))  # Should print True
print(is_leap_year(1900))  # Should print False
print(is_leap_year(2024))  # Should print True
print(is_leap_year(2023))  # Should print False


# Question 2: Triangle Type Classifier
# Create a function called classify_triangle that takes three side lengths of a triangle
# as input and returns the type of triangle:
# "Equilateral" if all sides are equal
# "Isosceles" if exactly two sides are equal
# "Scalene" if no sides are equal
# "Not a triangle" if the sides cannot form a triangle

# Hint: First check if the sides can form a triangle (sum of any two sides must be greater than the third).
# Then use if-elif-else to classify the triangle type.

def classify_triangle(side1, side2, side3):
    # Your code here
    pass

# Test your function
print(classify_triangle(5, 5, 5))       # Should print "Equilateral"
print(classify_triangle(5, 5, 7))       # Should print "Isosceles"
print(classify_triangle(3, 4, 5))       # Should print "Scalene"
print(classify_triangle(1, 1, 10))      # Should print "Not a triangle"


# Question 3: Simple Calculator
# Create a function called calculator that takes two numbers and an operator (+, -, *, /) as input
# and returns the result of the operation. If the operator is invalid or if there's an attempt to
# divide by zero, return an appropriate error message.

# Hint: Use if-elif-else to handle different operators. Be sure to handle the division by zero case separately.

def calculator(num1, num2, operator):
    # Your code here
    pass

# Test your function
print(calculator(10, 5, '+'))  # Should print 15
print(calculator(10, 5, '-'))  # Should print 5
print(calculator(10, 5, '*'))  # Should print 50
print(calculator(10, 5, '/'))  # Should print 2.0
print(calculator(10, 0, '/'))  # Should print an error message
print(calculator(10, 5, '%'))  # Should print an error message
