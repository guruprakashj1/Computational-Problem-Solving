# Problem 17: Check if a string is a palindrome using a for loop

"""
Explanation: This problem uses a for loop to compare characters in a string.
Logic: Compare characters from both ends moving towards the center.
Algorithm:
1. Input a string
2. Convert string to lowercase and remove non-alphanumeric characters
3. For i from 0 to half the length of the string:
   a. If character at i doesn't match character at (length - 1 - i), it's not a palindrome
4. If all characters match, it's a palindrome
"""

import re

text = input("Enter a string to check if it's a palindrome: ")
text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
is_palindrome = True

for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
