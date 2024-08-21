# Find the GCD of the given two numbers

This README file provides a step-by-step procedure to calculate the Greatest Common Divisor (GCD) of two given numbers.

## Problem Statement

Given two integers a and b, find their Greatest Common Divisor (GCD).

## Definition

The Greatest Common Divisor (GCD) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers.

## Step-by-Step Procedure (Euclidean Algorithm)

1. Start with the two given numbers, let's call them a and b.

2. Take the absolute value of a and b.

3. While b is not 0:
   a. Compute the remainder of a divided by b.
   b. Set a to b.
   c. Set b to the remainder.

4. When b becomes 0, a is the GCD.

5. Return or display a as the GCD.

## Explanation

- This method uses the Euclidean algorithm, which is based on the principle that the greatest common divisor of two numbers does not change if the smaller number is subtracted from the larger number.
- The algorithm efficiently reduces the problem of computing the GCD to computing the GCD of smaller numbers.
- We use absolute values because GCD is defined only for positive integers, but we often want to compute the GCD of negative integers as well.

## Examples

1. Let's find the GCD of 48 and 18:
   - Start with a = 48, b = 18
   - 48 ÷ 18 = 2 remainder 12, so a = 18, b = 12
   - 18 ÷ 12 = 1 remainder 6, so a = 12, b = 6
   - 12 ÷ 6 = 2 remainder 0, so a = 6, b = 0
   - b is 0, so we stop. The GCD is 6.

2. Let's find the GCD of 17 and 23:
   - Start with a = 17, b = 23
   - 23 ÷ 17 = 1 remainder 6, so a = 17, b = 6
   - 17 ÷ 6 = 2 remainder 5, so a = 6, b = 5
   - 6 ÷ 5 = 1 remainder 1, so a = 5, b = 1
   - 5 ÷ 1 = 5 remainder 0, so a = 1, b = 0
   - b is 0, so we stop. The GCD is 1.

3. Let's find the GCD of 0 and 5:
   - Start with a = 0, b = 5
   - 5 ÷ 0 is undefined, but in the algorithm, we simply set a = 5, b = 0
   - b is 0, so we stop. The GCD is 5.

## Note

- The GCD is always positive, even if the input numbers are negative.
- The GCD of 0 and 0 is not defined, as 0 is divisible by every integer.
- In most programming languages, you can use the modulo operator (%) to compute the remainder.
- This algorithm is very efficient and works well even for very large numbers.
- The GCD has many applications in mathematics, including simplifying fractions and solving Diophantine equations.
- A related concept is the Least Common Multiple (LCM), which can be computed using the GCD: LCM(a,b) = |a*b| / GCD(a,b).

## Recursive Implementation

The Euclidean algorithm can also be implemented recursively:

```
function gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)
```

This recursive implementation directly reflects the mathematical definition of the Euclidean algorithm.
