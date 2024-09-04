# Problem 22: Check if a number is an Armstrong number using a while loop

"""
Explanation: This problem uses a while loop to check if a number is an Armstrong number.
Logic: An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
Algorithm:
1. Input a number
2. Count the number of digits
3. Initialize sum to 0
4. While number > 0:
   a. Extract the rightmost digit
   b. Add digit raised to the power of number of digits to sum
   c. Remove the rightmost digit from number
5. If sum equals the original number, it's an Armstrong number
"""

def count_digits(n):
    return len(str(n))

number = int(input("Enter a number: "))
original_number = number
num_digits = count_digits(number)
sum_of_powers = 0

while number > 0:
    digit = number % 10
    sum_of_powers += digit ** num_digits
    number //= 10

if sum_of_powers == original_number:
    print(f"{original_number} is an Armstrong number")
else:
    print(f"{original_number} is not an Armstrong number")
