# Problem 23: Generate a random password using loops and conditional statements

"""
Explanation: This problem uses loops and conditional statements to generate a random password.
Logic: Create a password with a mix of uppercase, lowercase, digits, and special characters.
Algorithm:
1. Import necessary modules (random, string)
2. Define character sets for each type (uppercase, lowercase, digits, special)
3. Input desired password length
4. Initialize an empty password string
5. While password length is less than desired length:
   a. Randomly choose a character type
   b. Add a random character of that type to the password
6. Print the generated password
"""

import random
import string

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    password = ""
    while len(password) < length:
        char_type = random.choice([uppercase, lowercase, digits, special])
        password += random.choice(char_type)

    return password

length = int(input("Enter the desired password length: "))
password = generate_password(length)
print(f"Generated password: {password}")
