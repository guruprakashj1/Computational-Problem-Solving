# 6- Chaining Comparison Operators - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Age Group Classifier
# Create a function called classify_age that takes an age as a parameter and returns a string 
# describing the age group. Use chained comparisons to classify the age into the following groups:
# - "Child" if age is between 0 and 12 (inclusive)
# - "Teenager" if age is between 13 and 19 (inclusive)
# - "Adult" if age is between 20 and 59 (inclusive)
# - "Senior" if age is 60 or above
# - "Invalid" if age is negative

# Hint: Use chained comparisons to check the age ranges.

def classify_age(age):
    # Your code here
    pass

# Test your function
print(classify_age(8))    # Should print "Child"
print(classify_age(15))   # Should print "Teenager"
print(classify_age(30))   # Should print "Adult"
print(classify_age(70))   # Should print "Senior"
print(classify_age(-5))   # Should print "Invalid"


# Question 2: Grade Calculator
# Create a function called calculate_grade that takes a numerical score (0-100) as input
# and returns the corresponding letter grade based on the following scale:
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: 0-59
# The function should return "Invalid" for scores outside the 0-100 range.

# Hint: Use chained comparisons to check score ranges.

def calculate_grade(score):
    # Your code here
    pass

# Test your function
print(calculate_grade(95))   # Should print "A"
print(calculate_grade(82))   # Should print "B"
print(calculate_grade(75))   # Should print "C"
print(calculate_grade(65))   # Should print "D"
print(calculate_grade(45))   # Should print "F"
print(calculate_grade(101))  # Should print "Invalid"
print(calculate_grade(-5))   # Should print "Invalid"


# Question 3: Season Determiner
# Create a function called determine_season that takes two parameters: 
# month (1-12) and day (1-31). The function should return the season based on the following rules:
# - Spring: March 20 - June 20
# - Summer: June 21 - September 21
# - Autumn: September 22 - December 20
# - Winter: December 21 - March 19
# Return "Invalid" for any invalid month or day combinations.

# Hint: Use nested if statements with chained comparisons to check month and day ranges.

def determine_season(month, day):
    # Your code here
    pass

# Test your function
print(determine_season(2, 14))   # Should print "Winter"
print(determine_season(4, 22))   # Should print "Spring"
print(determine_season(8, 18))   # Should print "Summer"
print(determine_season(11, 5))   # Should print "Autumn"
print(determine_season(13, 1))   # Should print "Invalid"
print(determine_season(6, 32))   # Should print "Invalid"
