# Check if the given number is Armstrong or NOT

This README file provides a step-by-step procedure to determine whether a given number is an Armstrong number or not.

## Problem Statement

Given a positive integer, determine if it is an Armstrong number.

## Definition

An Armstrong number (also known as a narcissistic number, pluperfect digital invariant, or pluperfect number) is a number that is the sum of its own digits each raised to the power of the number of digits.

## Step-by-Step Procedure

1. Start with the given number, let's call it n.

2. Count the number of digits in n. Let's call this count d.

3. Initialize a variable sum to 0.

4. For each digit in n:
   a. Raise the digit to the power of d.
   b. Add the result to sum.

5. If sum equals the original number n, then n is an Armstrong number.

6. Report the result: either "ARMSTRONG" or "NOT ARMSTRONG"

## Explanation

- This method calculates the sum of each digit raised to the power of the total number of digits.
- If this sum equals the original number, it satisfies the definition of an Armstrong number.
- The process involves both identifying individual digits and performing exponentiation.

## Examples

1. Let's say the given number is 153:
   - Number of digits (d) is 3
   - Calculate: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
   - 153 equals the original number, so 153 is an ARMSTRONG number

2. If the given number is 1634:
   - Number of digits (d) is 4
   - Calculate: 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
   - 1634 equals the original number, so 1634 is an ARMSTRONG number

3. If the given number is 123:
   - Number of digits (d) is 3
   - Calculate: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
   - 36 does not equal the original number, so 123 is NOT an ARMSTRONG number

This procedure works for any positive integer.

## Note

- Armstrong numbers are rare. In the decimal system, there are only 89 Armstrong numbers, the largest of which is 115,132,219,018,763,992,565,095,597,973,971,522,401.
- The concept of Armstrong numbers can be extended to other bases, but this procedure assumes base 10.
- When implementing this in a programming language, be careful of integer overflow when dealing with large numbers or high powers.
- Efficient algorithms for identifying Armstrong numbers can be crucial when searching for them in large ranges.
