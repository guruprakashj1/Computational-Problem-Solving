# 4-Escape-Sequences-Assignment.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Formatting a Receipt
# Create a function that takes item name, quantity, and price as parameters
# and returns a formatted receipt string using escape sequences.
# The receipt should have aligned columns for Item, Quantity, and Price.
# Hint: Use \t for alignment and \n for new lines.

def format_receipt(item, quantity, price):
    # TODO: Implement the function
    pass

# Test your function
print(format_receipt("Apple", 5, 0.5))
# Expected output:
# Item    Quantity    Price
# Apple   5           $0.50


# Question 2: Creating a Directory Tree
# Write a function that takes a list of file and directory names
# and returns a string representation of a simple directory tree.
# Use appropriate escape sequences for indentation and newlines.
# Hint: You can use \t for indentation and \n for new lines.

def create_directory_tree(items):
    # TODO: Implement the function
    pass

# Test your function
files = ["Documents", "file1.txt", "file2.txt", "Images", "img1.jpg", "img2.jpg"]
print(create_directory_tree(files))
# Expected output:
# Documents
#     file1.txt
#     file2.txt
# Images
#     img1.jpg
#     img2.jpg


# Question 3: Escape Sequence Decoder
# Create a function that takes a string containing escape sequences
# and returns two strings: one with the escape sequences interpreted,
# and another showing the raw string (with visible escape sequences).
# Hint: Use the repr() function to get the raw string representation.

def escape_sequence_decoder(text):
    # TODO: Implement the function
    pass

# Test your function
test_string = "Hello\tWorld\nThis is a \"quote\""
interpreted, raw = escape_sequence_decoder(test_string)
print("Interpreted:", interpreted)
print("Raw:", raw)
# Expected output:
# Interpreted: Hello    World
# This is a "quote"
# Raw: Hello\tWorld\nThis is a "quote"


# Bonus Challenge:
# Implement a function that converts a given text to "leet speak".
# Replace certain letters with numbers or symbols:
# A/a -> 4, E/e -> 3, I/i -> 1, O/o -> 0, S/s -> 5, T/t -> 7
# Hint: You can use the replace() method or create a translation table.

def to_leet_speak(text):
    # TODO: Implement the function
    pass

# Test your function
print(to_leet_speak("This is an Elite Message"))
# Expected output: 7h15 15 4n 3l173 M3554g3

