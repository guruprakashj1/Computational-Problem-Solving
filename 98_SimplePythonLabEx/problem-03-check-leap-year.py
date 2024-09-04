# Problem 3: Check if a year is a leap year

"""
Explanation: This problem introduces complex conditions in if-elif-else statements.
Logic: A year is a leap year if it's divisible by 4, except for century years, which must be divisible by 400.
Algorithm:
1. Input a year
2. If year is divisible by 4 and not divisible by 100, or if it's divisible by 400, it's a leap year
3. Otherwise, it's not a leap year
"""

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
