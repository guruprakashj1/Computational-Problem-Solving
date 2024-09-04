# Problem 1: Check if a number is positive, negative, or zero

"""
Explanation: This problem introduces simple if-elif-else statements.
Logic: Compare the number to 0 and categorize it accordingly.
Algorithm:
1. Input a number
2. If number > 0, print "Positive"
3. Else if number < 0, print "Negative"
4. Else, print "Zero"
"""

number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
