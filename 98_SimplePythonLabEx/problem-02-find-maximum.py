# Problem 2: Find the maximum of three numbers

"""
Explanation: This problem uses nested if-else statements to compare three numbers.
Logic: Compare pairs of numbers to find the largest.
Algorithm:
1. Input three numbers
2. Compare first two numbers
3. Compare the larger of the first two with the third number
4. Print the largest number
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b:
    if a > c:
        max_num = a
    else:
        max_num = c
else:
    if b > c:
        max_num = b
    else:
        max_num = c

print(f"The maximum number is: {max_num}")
