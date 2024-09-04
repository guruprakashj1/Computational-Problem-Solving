# Problem 16: Convert decimal to binary using a while loop

"""
Explanation: This problem uses a while loop to perform base conversion.
Logic: Repeatedly divide by 2 and keep track of remainders.
Algorithm:
1. Input a decimal number
2. Initialize an empty string for binary
3. While number > 0:
   a. Prepend (number % 2) to binary string
   b. number = number // 2
4. Print the binary string
"""

decimal = int(input("Enter a decimal number: "))
binary = ""
original_decimal = decimal

while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2

print(f"The binary representation of {original_decimal} is: {binary}")
