# Check if the given number is palindrome

This README file provides a step-by-step procedure to determine whether a given number is a palindrome or not.

## Problem Statement

Given a positive integer, determine if it reads the same backwards as forwards, i.e., if it is a palindrome.

## Definition

A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome, while 123 is not.

## Step-by-Step Procedure

1. Start with the given number, let's call it n.

2. Convert the number to a string.

3. Initialize two pointers:
   - left pointer at the start of the string (index 0)
   - right pointer at the end of the string (index length - 1)

4. While the left pointer is less than the right pointer:
   a. If the digit at the left pointer doesn't match the digit at the right pointer, the number is NOT a palindrome. End the procedure.
   b. Move the left pointer one step to the right.
   c. Move the right pointer one step to the left.

5. If you've completed the loop without finding any mismatches, the number IS a palindrome.

6. Report the result: either "PALINDROME" or "NOT PALINDROME"

## Explanation

- This method compares digits from both ends of the number, moving towards the center.
- If at any point the digits don't match, we know it's not a palindrome.
- If we make it through all comparisons without finding a mismatch, it must be a palindrome.
- Converting to a string allows for easy comparison and eliminates the need for complex mathematical operations.

## Examples

1. Let's say the given number is 12321:
   - Convert to string: "12321"
   - Compare 1 and 1: match
   - Compare 2 and 2: match
   - Compare 3 and 3: match
   - All comparisons matched, so 12321 is a PALINDROME

2. If the given number is 12345:
   - Convert to string: "12345"
   - Compare 1 and 5: don't match
   - 12345 is NOT a PALINDROME

3. If the given number is 1221:
   - Convert to string: "1221"
   - Compare 1 and 1: match
   - Compare 2 and 2: match
   - All comparisons matched, so 1221 is a PALINDROME

This procedure works for any positive integer.

## Note

- This method treats the number as a string, so it considers the exact representation of the number.
- Leading zeros are typically not considered in integer representations, so numbers like 00100 would not typically be considered as inputs for this problem when working with integers.
- In some programming languages, you might need to handle the conversion from number to string explicitly.
- For very large numbers, be mindful of the limitations of your programming language's string or integer size limits.
