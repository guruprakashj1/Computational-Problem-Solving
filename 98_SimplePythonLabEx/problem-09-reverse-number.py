# Problem 9: Reverse a number using a while loop

"""
Explanation: This problem uses a while loop to manipulate digits of a number.
Logic: Extract digits from right to left and build the reversed number.
Algorithm:
1. Input a number
2. Initialize reversed_num to 0
3. While number > 0:
   a. Extract the rightmost digit (digit = number % 10)
   b. Add digit to reversed_num (reversed_num = reversed_num * 10 + digit)
   c. Remove the rightmost digit from number (number = number // 10)
4. Print the reversed number
"""

number = int(input("Enter a number to reverse: "))
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = (reversed_num * 10) + digit
    number //= 10

print(f"Reversed number: {reversed_num}")
