# Problem 14: Calculate the power of a number using a while loop

"""
Explanation: This problem uses a while loop to perform exponentiation.
Logic: Multiply the base by itself 'exponent' number of times.
Algorithm:
1. Input base and exponent
2. Initialize result to 1
3. While exponent > 0:
   a. Multiply result by base
   b. Decrement exponent
4. Print the result
"""

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
original_exponent = exponent

while exponent > 0:
    result *= base
    exponent -= 1

print(f"{base} raised to the power of {original_exponent} is: {result}")
