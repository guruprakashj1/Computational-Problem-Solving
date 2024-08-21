# Find the largest of the given three numbers

This README file provides a step-by-step procedure to determine the largest of three given numbers.

## Problem Statement

Given three numbers, find and report which one is the largest (or if they are equal).

## Step-by-Step Procedure

1. Start with the three given numbers, let's call them a, b, and c.

2. Compare a, b, and c:
   - First, compare a and b:
     - If a is greater than b, remember a as the temporary largest.
     - Otherwise, remember b as the temporary largest.
   - Then, compare the temporary largest with c:
     - If the temporary largest is greater than c, it remains the largest.
     - Otherwise, c is the largest.

3. Report the result:
   - Report "[largest number] is the largest" (replace with the actual number).
   - If all numbers are equal, report "All numbers are equal".

## Explanation

- This method uses a series of comparisons to determine which number is the largest.
- We first find the larger of the first two numbers, then compare that result with the third number.
- This approach minimizes the number of comparisons needed.
- The method accounts for the possibility that two or all three numbers might be equal.

## Examples

1. Let's say the given numbers are 5, 3, and 7:
   - Compare 5 and 3: 5 is larger
   - Compare 5 and 7: 7 is larger
   - Report: "7 is the largest"

2. If the given numbers are -2, 7, and 4:
   - Compare -2 and 7: 7 is larger
   - Compare 7 and 4: 7 is larger
   - Report: "7 is the largest"

3. If the given numbers are 4.5, 4.5, and 4.5:
   - Compare 4.5 and 4.5: They're equal, so either is temporary largest
   - Compare 4.5 and 4.5: They're equal
   - Report: "All numbers are equal"

This procedure works for any three real numbers, including integers and decimal numbers.

## Note

- When implementing this in a programming language, you could use the built-in max() function (if available) to simplify the process: largest = max(a, b, c).
- For very large numbers or very precise decimal numbers, be mindful of the limitations of your programming language or system's number representation to avoid precision errors.
- This method can be extended to find the largest of any number of values by repeatedly comparing the current largest with the next number in the list.
- In some programming contexts, you might want to return the larger number itself rather than a descriptive string. Adjust the reporting step as needed for your specific use case.
