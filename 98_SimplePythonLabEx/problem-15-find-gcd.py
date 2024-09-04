# Problem 15: Find the GCD of two numbers using a while loop and if statement

"""
Explanation: This problem uses a while loop and if statement to implement the Euclidean algorithm.
Logic: Repeatedly replace the larger number with the remainder of the larger divided by the smaller.
Algorithm:
1. Input two numbers a and b
2. While b != 0:
   a. Set temp = b
   b. Set b = a % b
   c. Set a = temp
3. Print a as the GCD
"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print(f"The GCD is: {a}")
