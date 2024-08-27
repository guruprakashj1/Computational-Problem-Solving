# 3-Ternary-Operator-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Age Classifier
# Write a function that takes an age as input and returns "Minor" if the age is less than 18,
# and "Adult" otherwise. Use the ternary operator to implement this function.
# Hint: The ternary operator structure is: value_if_true if condition else value_if_false

def classify_age(age):
    # TODO: Implement the function using a ternary operator
    pass

# Test your function
print(classify_age(20))  # Should print "Adult"
print(classify_age(15))  # Should print "Minor"


# Question 2: List Element Checker
# Create a function that takes a list and an element as input. The function should return
# "Found" if the element is in the list, and "Not Found" otherwise. Use the ternary operator
# and the 'in' operator to implement this function.
# Hint: You can use the 'in' operator inside the condition of the ternary operator

def check_element(lst, element):
    # TODO: Implement the function using a ternary operator
    pass

# Test your function
print(check_element([1, 2, 3, 4, 5], 3))  # Should print "Found"
print(check_element([1, 2, 3, 4, 5], 6))  # Should print "Not Found"


# Question 3: String Shortener
# Implement a function that takes a string and a maximum length as input. If the string is longer
# than the maximum length, it should return a shortened version with an ellipsis (...) at the end.
# If it's not longer, it should return the original string. Use the ternary operator to implement this.
# Hint: You can use string slicing along with the ternary operator

def shorten_string(string, max_length):
    # TODO: Implement the function using a ternary operator
    pass

# Test your function
print(shorten_string("Hello, World!", 10))  # Should print "Hello, W..."
print(shorten_string("Python", 10))         # Should print "Python"


# Bonus Challenge: Grade Classifier
# Create a function that takes a numerical grade (0-100) and returns the letter grade
# according to the following scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# Use nested ternary operators to implement this function.
# Hint: You can chain multiple ternary operators, but be careful about readability

def classify_grade(grade):
    # TODO: Implement the function using nested ternary operators
    pass

# Test your function
print(classify_grade(95))  # Should print "A"
print(classify_grade(81))  # Should print "B"
print(classify_grade(72))  # Should print "C"
print(classify_grade(65))  # Should print "D"
print(classify_grade(45))  # Should print "F"

