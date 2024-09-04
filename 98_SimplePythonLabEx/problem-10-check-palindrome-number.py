# Problem 10: Check if a number is a palindrome using a while loop and if statement

"""
Explanation: This problem combines a while loop with an if statement to check for palindromes.
Logic: Reverse the number and compare it with the original.
Algorithm:
1. Input a number
2. Store the original number
3. Reverse the number (use the algorithm from Problem 9)
4. If original number equals reversed number, it's a palindrome
"""

number = int(input("Enter a number to check if it's a palindrome: "))
original_number = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = (reversed_num * 10) + digit
    number //= 10

if original_number == reversed_num:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")
