# Problem 18: Print the ASCII value of all characters in a string using a for loop

"""
Explanation: This problem uses a for loop to iterate through characters in a string.
Logic: Use the ord() function to get the ASCII value of each character.
Algorithm:
1. Input a string
2. For each character in the string:
   a. Print the character and its ASCII value
"""

text = input("Enter a string: ")

for char in text:
    print(f"'{char}': {ord(char)}")
