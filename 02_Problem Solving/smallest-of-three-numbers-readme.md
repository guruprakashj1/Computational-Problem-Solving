# Find the smallest of the given three numbers

This README file provides a step-by-step procedure to determine the smallest of three given numbers.

## Problem Statement

Given three numbers, find and report which one is the smallest (or if they are equal).

## Step-by-Step Procedure

1. Start with the three given numbers, let's call them a, b, and c.

2. Compare a, b, and c:
   - First, compare a and b:
     - If a is less than b, remember a as the temporary smallest.
     - Otherwise, remember b as the temporary smallest.
   - Then, compare the temporary smallest with c:
     - If the temporary smallest is less than c, it remains the smallest.
     - Otherwise, c is the smallest.

3. Report the result:
   - Report "[smallest number] is the smallest" (replace with the actual number).
   - If all numbers are equal, report "All numbers are equal".

## Explanation

- This method uses a series of comparisons to determine which number is the smallest.
- We first find the smaller of the first two numbers, then compare that result with the third number.
- This approach minimizes the number of comparisons needed.
- The method accounts for the possibility that two or all three numbers might be equal.

## Examples

1. Let's say the given numbers are 5, 3, and 7:
   - Compare 5 and 3: 3 is smaller
   - Compare 3 and 7: 3 is smaller
   - Report: "3 is the smallest"

2. If the given numbers are -2, 7, and 4:
   - Compare -2 and 7: -2 is smaller
   - Compare -2 and 4: -2 is smaller
   - Report: "-2 is the smallest"

3. If the given numbers are 4.5, 4.5, and 4.5:
   - Compare 4.5 and 4.5: They're equal, so either is temporary smallest
   - Compare 4.5 and 4.5: They're equal
   - Report: "All numbers are equal"

This procedure works for any three real numbers, including integers and decimal numbers.

## Note

- When implementing this in a programming language, you could use the built-in min() function (if available) to simplify the process: smallest = min(a, b, c).
- For very large numbers or very precise decimal numbers, be mindful of the limitations of your programming language or system's number representation to avoid precision errors.
- This method can be extended to find the smallest of any number of values by repeatedly comparing the current smallest with the next number in the list.
- In some programming contexts, you might want to return the smaller number itself rather than a descriptive string. Adjust the reporting step as needed for your specific use case.
- This operation is the inverse of finding the largest number. In many programming languages, you can use the same comparison operator and just switch the logic (e.g., change > to <).
