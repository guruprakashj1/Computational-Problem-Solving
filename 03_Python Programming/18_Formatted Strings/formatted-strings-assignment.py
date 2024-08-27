# 5-Formatted-Strings-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Receipt Generator
# Create a function that takes item name, quantity, and price as parameters
# and returns a formatted receipt string using f-strings.
# The receipt should have aligned columns for Item, Quantity, and Price.
# Hint: Use format specifiers for alignment and decimal places.

def generate_receipt(item, quantity, price):
    # TODO: Implement the function
    pass

# Test your function
print(generate_receipt("Apple", 5, 0.99))
# Expected output:
# Item      Quantity    Price
# Apple     5           $4.95


# Question 2: Progress Bar
# Write a function that takes a percentage (0-100) and returns a string
# representing a progress bar. Use str.format() method for this task.
# The progress bar should be 20 characters wide, using '=' for completed
# parts and '-' for incomplete parts.
# Hint: You can use string multiplication and format specifiers for padding.

def create_progress_bar(percentage):
    # TODO: Implement the function
    pass

# Test your function
print(create_progress_bar(75))
# Expected output: [===============-----] 75%


# Question 3: Date Formatter
# Create a function that takes a date in the format YYYY-MM-DD and returns
# it formatted in three different styles using f-strings:
# 1. Month Day, Year (e.g., January 1, 2023)
# 2. DD/MM/YY (e.g., 01/01/23)
# 3. Day of Week, Month Day (e.g., Sunday, January 1)
# Hint: Use the datetime module to parse the input string and then use
# strftime() method with f-strings for formatting.

import datetime

def format_date(date_string):
    # TODO: Implement the function
    pass

# Test your function
print(format_date("2023-01-01"))
# Expected output:
# January 1, 2023
# 01/01/23
# Sunday, January 1


# Bonus Challenge:
# Implement a function that takes a dictionary of student names and their scores,
# and returns a formatted string representing a leaderboard.
# The leaderboard should be sorted by score (highest to lowest) and include rank.
# Use f-strings for formatting and include appropriate alignment.
# Hint: You might want to use the sorted() function with a key parameter,
# and enumerate() to generate ranks.

def create_leaderboard(students):
    # TODO: Implement the function
    pass

# Test your function
students = {"Alice": 95, "Bob": 82, "Charlie": 90, "David": 88}
print(create_leaderboard(students))
# Expected output:
# Rank  Name      Score
# 1     Alice     95
# 2     Charlie   90
# 3     David     88
# 4     Bob       82

