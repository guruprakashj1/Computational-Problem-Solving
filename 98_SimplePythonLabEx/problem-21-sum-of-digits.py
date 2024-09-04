# Problem 21: Calculate the sum of digits of a number using a while loop

"""
Explanation: This problem uses a while loop to extract and sum digits of a number.
Logic: Extract each digit using modulo and integer division, then sum them.
Algorithm:
1. Input a number
2. Initialize sum to 0
3. While number > 0:
   a. Extract the rightmost digit (digit = number % 10)
   b. Add digit to sum
   c. Remove the rightmost digit from number (number = number // 10)
4. Print the sum of digits
"""

number = int(input("Enter a number: "))
original_number = number
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print(f"The sum of digits of {original_number} is: {sum_of_digits}")
