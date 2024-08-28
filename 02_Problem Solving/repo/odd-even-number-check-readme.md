# Print if a given number is ODD or EVEN

This README file provides a step-by-step procedure to determine whether a given number is odd or even.

## Problem Statement

Given a number, determine if it is odd or even and print the result.

## Step-by-Step Procedure

1. Start with the given number.

2. Divide the number by 2.

3. Check if there is a remainder after the division:
   - If there is no remainder (the result is a whole number), the original number is even.
   - If there is a remainder, the original number is odd.

4. Print the result:
   - If the number is even, print "EVEN"
   - If the number is odd, print "ODD"

## Explanation

- Even numbers are integers that can be divided by 2 without leaving a remainder.
- Odd numbers are integers that, when divided by 2, always have a remainder of 1.
- The division by 2 and checking for a remainder is the fundamental method to distinguish between odd and even numbers.

## Example

Let's say the given number is 7:

1. Start with 7.
2. Divide 7 by 2: 7 ÷ 2 = 3 remainder 1
3. There is a remainder (1), so 7 is odd.
4. Print "ODD"

This procedure works for any integer, positive or negative.

# Computational Problem Solving: Prime Number Checker

## 1. Understand the Problem
- Input: An integer number
- Output: Determine if the number is prime or not
- A prime number is only divisible by 1 and itself

## 2. Plan the Solution
- We need to check if the number is divisible by any number from 2 to the square root of the input
- If it's divisible by any of these numbers, it's not prime
- Special cases: numbers less than or equal to 1 are not prime

## 3. Design the Algorithm
1. Input a number
2. If the number is less than or equal to 1, it's not prime
3. For numbers from 2 to the square root of the input:
   - If the input is divisible by any of these numbers, it's not prime
4. If we've checked all numbers and found no divisors, the number is prime

## 4. Implement the Solution
Here's the Python code implementing this algorithm:

```python
num = int(input("enter a number: "))
flag = False
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
```

## 5. Test the Solution
- Test with prime numbers: 2, 3, 5, 7, 11, 23
- Test with non-prime numbers: 4, 6, 8, 9, 15
- Test edge cases: 0, 1, negative numbers

## 6. Optimize and Refine
- The current solution is efficient as it only checks up to the square root of the number
- We could further optimize by checking only odd numbers after 2, as even numbers (except 2) are never prime

## 7. Reflect and Explain
- This solution uses a flag variable to keep track of whether a divisor was found
- The range in the for loop goes up to int(num**0.5) + 1 to include the square root in the check
- The algorithm has a time complexity of O(√n), which is efficient for most practical purposes
