# Print the Asterisk Triangle Pattern

This README file provides a step-by-step procedure to print the triangle pattern of asterisks as shown in the image.

## Problem Statement

Print a pattern of asterisks (*) that forms a right-angled triangle, where each row has one more asterisk than the previous row, starting from one asterisk in the first row.

## Pattern Description

The pattern looks like this:
```
*
* *
* * *
* * * *
* * * * *
```

## Step-by-Step Procedure

1. Determine the number of rows for the pattern (in this case, it's 5).

2. Create an outer loop that iterates from 1 to the number of rows (inclusive).

3. For each iteration of the outer loop:
   a. Create an inner loop that iterates from 1 to the current row number.
   b. In each iteration of the inner loop, print an asterisk (*) followed by a space.
   c. After the inner loop completes, print a newline character to move to the next line.

4. Repeat steps 3a-3c until all rows are printed.

## Explanation

- The outer loop controls the number of rows.
- The inner loop prints the asterisks for each row.
- We print a space after each asterisk to separate them horizontally.
- The newline character after each row of asterisks ensures each row starts on a new line.

## Pseudocode

```
n = 5  // Number of rows

for i from 1 to n:
    for j from 1 to i:
        print "*" followed by a space
    print newline
```

## Note

- This pattern is often used as a basic exercise in learning nested loops.
- The number of rows can be easily modified by changing the value of n.
- Make sure to handle any language-specific syntax for loops and print statements when implementing this in a specific programming language.
- In some languages, you might need to use string concatenation or formatting to achieve the same result.
- The image shows clear spacing between asterisks, which is accounted for in our procedure by adding a space after each asterisk.

## Variations

You can create variations of this pattern by:
1. Aligning the triangle to the right side.
2. Using different characters instead of asterisks.
3. Creating an inverted triangle by starting with the maximum number of asterisks and decreasing.

These variations can be achieved by modifying the loop conditions and adding additional print statements for spacing if necessary.
