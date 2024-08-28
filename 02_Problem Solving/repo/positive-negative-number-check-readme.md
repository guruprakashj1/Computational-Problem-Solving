# Find if a given number is positive or negative

This README file provides a step-by-step procedure to determine whether a given number is positive or negative.

## Problem Statement

Given a number, determine if it is positive or negative and report the result.

## Step-by-Step Procedure

1. Start with the given number.

2. Compare the number to zero:
   - If the number is greater than zero, it is positive.
   - If the number is less than zero, it is negative.
   - If the number is equal to zero, it is neither positive nor negative (it's zero).

3. Report the result:
   - If the number is positive, report "POSITIVE"
   - If the number is negative, report "NEGATIVE"
   - If the number is zero, report "ZERO"

## Explanation

- Positive numbers are greater than zero and are located to the right of zero on a number line.
- Negative numbers are less than zero and are located to the left of zero on a number line.
- Zero is neither positive nor negative; it's the point that separates positive and negative numbers on the number line.

## Examples

1. Let's say the given number is 5:
   - 5 is greater than 0, so it's positive.
   - Report "POSITIVE"

2. If the given number is -3:
   - -3 is less than 0, so it's negative.
   - Report "NEGATIVE"

3. If the given number is 0:
   - 0 is neither greater than nor less than itself.
   - Report "ZERO"

This procedure works for any real number, including integers and decimal numbers.

## Note

In some contexts, zero is considered to be non-negative (i.e., either positive or zero). If this is the case for your specific application, you may want to adjust the procedure to report zero as "NON-NEGATIVE" instead of "ZERO".


# Computational Problem Solving: Positive, Negative, or Zero Number Checker

## 1. Understand the Problem
- Input: A real number (floating-point)
- Output: Determine if the number is positive, negative, or zero
- Positive numbers are greater than 0
- Negative numbers are less than 0
- Zero is neither positive nor negative

## 2. Plan the Solution
- Take a floating-point input from the user
- Use conditional statements to check if the number is greater than, less than, or equal to zero
- Print the appropriate message based on the condition met

## 3. Design the Algorithm
1. Prompt the user to enter a number
2. Convert the input to a floating-point number
3. If the number is greater than 0, it's positive
4. If the number is equal to 0, it's zero
5. If the number is less than 0, it's negative
6. Print the result

## 4. Implement the Solution
Here's the Python code implementing this algorithm:

```python
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

## 5. Test the Solution
- Test with positive numbers: 1.2, 5, 0.001
- Test with negative numbers: -1, -0.5, -100
- Test with zero: 0, 0.0
- Test with edge cases: very large numbers, very small numbers close to zero

## 6. Optimize and Refine
- The current solution is efficient for this simple problem
- We could improve user experience by adding error handling:

```python
try:
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")
except ValueError:
    print("Invalid input. Please enter a valid number.")
```

## 7. Reflect and Explain
- This solution uses a float to handle both integers and decimal numbers
- The if-elif-else structure allows for three distinct outcomes
- The order of conditions matters: we check for positive first, then zero, then negative
- Using `>` and `==` operators for comparison
- Time complexity is O(1) as it performs a constant number of operations

## 8. Potential Extensions
- Extend the program to categorize the number as a whole number or decimal
- Add a feature to round the number to a specified number of decimal places
- Implement a function that returns an enumeration or integer code instead of printing

## 9. Learning Outcomes
- Understanding of floating-point numbers in programming
- Practice with multi-way conditional statements (if-elif-else)
- Introduction to basic input/output operations and type conversion in Python
- Consideration of edge cases and error handling in numeric input

## 10. Common Pitfalls and Considerations
- Floating-point precision: Be aware that very small numbers close to zero might be interpreted as zero due to floating-point arithmetic limitations
- Input validation: The basic version doesn't handle non-numeric input, which is addressed in the optimized version
- Zero comparison: Using `== 0` for floating-point numbers can sometimes be problematic due to precision issues. For more critical applications, you might use a small epsilon value: `abs(num) < 1e-10`
