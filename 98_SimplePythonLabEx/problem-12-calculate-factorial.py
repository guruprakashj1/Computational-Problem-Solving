# Problem 12: Find the factorial of a number using a for loop

"""
Explanation: This problem uses a for loop to calculate factorial.
Logic: Multiply numbers from 1 to n to get the factorial.
Algorithm:
1. Input a number n
2. Initialize factorial to 1
3. For each number i from 1 to n:
   a. Multiply factorial by i
4. Print the factorial
"""

n = int(input("Enter a number to calculate its factorial: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is: {factorial}")
