# Problem 24: Implement a Caesar cipher using loops and if statements

"""
Explanation: This problem uses loops and if statements to implement a simple encryption technique.
Logic: Shift each letter in the plaintext by a fixed number of positions in the alphabet.
Algorithm:
1. Input a plaintext message and shift value
2. Initialize an empty ciphertext string
3. For each character in the plaintext:
   a. If it's a letter, shift it by the given value (wrapping around if necessary)
   b. If it's not a letter, keep it unchanged
4. Add the resulting character to the ciphertext
5. Print the ciphertext
"""

def caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

plaintext = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value (1-25): "))
encrypted_message = caesar_cipher(plaintext, shift)
print(f"Encrypted message: {encrypted_message}")
