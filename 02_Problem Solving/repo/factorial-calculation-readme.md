# Find the factorial of the given number

This README file provides a step-by-step procedure to calculate the factorial of a given number.

## Problem Statement

Given a non-negative integer n, calculate its factorial (denoted as n!).

## Definition

The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.

By definition:
- 0! = 1
- For n > 0, n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1

## Step-by-Step Procedure

1. Start with the given number, let's call it n.

2. If n is less than 0, return an error message as factorial is not defined for negative numbers.

3. If n is 0 or 1, return 1 (as 0! = 1! = 1).

4. Initialize a variable result to 1.

5. For each integer i from 2 to n (inclusive):
   - Multiply result by i and update result with this new value.

6. After the loop completes, result contains the factorial of n.

7. Return or display the result.

## Explanation

- This method calculates the factorial by multiplying all integers from 1 to n.
- We start the multiplication from 2 because multiplying by 1 doesn't change the result.
- The special cases of 0! and 1! are handled separately as they're defined to be 1.

## Examples

1. Let's calculate 5!:
   - Start with result = 1
   - Multiply by 2: result = 1 × 2 = 2
   - Multiply by 3: result = 2 × 3 = 6
   - Multiply by 4: result = 6 × 4 = 24
   - Multiply by 5: result = 24 × 5 = 120
   - Therefore, 5! = 120

2. Let's calculate 0!:
   - By definition, 0! = 1

3. Let's calculate 3!:
   - Start with result = 1
   - Multiply by 2: result = 1 × 2 = 2
   - Multiply by 3: result = 2 × 3 = 6
   - Therefore, 3! = 6

## Note

- Factorial grows very quickly. 20! is already larger than can be stored in a 64-bit integer.
- For large n, consider using a big integer library or numerical approximations like Stirling's formula.
- Factorial is only defined for non-negative integers.
- Factorial has many applications in combinatorics, probability theory, and algebra.
- In some programming languages, you might implement this recursively, though the iterative approach is generally more efficient.
- Be aware of potential overflow errors when implementing this in a programming language.

## Recursive Definition

For those interested in recursion, factorial can be defined recursively as:
- 0! = 1
- For n > 0, n! = n × (n-1)!

This definition directly translates to a recursive implementation in many programming languages.
