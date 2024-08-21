# Find if the given number is PRIME or NOT

This README file provides a step-by-step procedure to determine whether a given number is prime or not.

## Problem Statement

Given a positive integer, determine if it is a prime number or not.

## Definition

A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

## Step-by-Step Procedure

1. Start with the given number, let's call it n.

2. If n is less than or equal to 1, it is NOT prime. End the procedure.

3. If n is 2 or 3, it IS prime. End the procedure.

4. If n is divisible by 2 or 3, it is NOT prime. End the procedure.

5. Let i = 5 (start checking from 5)

6. While i * i <= n, do the following:
   a. If n is divisible by i, it is NOT prime. End the procedure.
   b. If n is divisible by (i + 2), it is NOT prime. End the procedure.
   c. Increase i by 6 (i = i + 6)

7. If you've completed the loop without finding any divisors, the number IS prime.

8. Report the result: either "PRIME" or "NOT PRIME"

## Explanation

- This method is based on the fact that all primes greater than 3 can be written in the form 6k ± 1.
- We first check for the simplest cases: numbers less than or equal to 3, and even numbers.
- Then we check for divisibility by numbers of the form 6k ± 1 up to the square root of n.
- This method is more efficient than checking all numbers up to n-1.

## Examples

1. Let's say the given number is 17:
   - 17 > 1, continue
   - 17 is not 2 or 3, continue
   - 17 is not divisible by 2 or 3, continue
   - 5 * 5 = 25, which is > 17, so we don't enter the loop
   - No divisors found, so 17 is PRIME

2. If the given number is 24:
   - 24 > 1, continue
   - 24 is not 2 or 3, continue
   - 24 is divisible by 2, so it is NOT PRIME

3. If the given number is 1:
   - 1 <= 1, so it is NOT PRIME

This procedure works for any positive integer.

## Note

- This method is efficient for reasonably sized numbers, but for very large numbers, more advanced primality tests are used in practice.
- In programming implementations, be mindful of integer overflow when dealing with very large numbers.
