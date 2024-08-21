# Print the Consecutive Numeric Triangle Pattern

This README file provides a step-by-step procedure to print the triangle pattern of consecutive numbers as shown in the image.

## Problem Statement

Print a pattern of numbers that forms a right-angled triangle, where each row starts with the next consecutive number and contains as many numbers as the row number, continuing the sequence from the previous row.

## Pattern Description

The pattern looks like this:
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

## Step-by-Step Procedure

1. Determine the number of rows for the pattern (in this case, it's 5).

2. Initialize a variable `current_number` to 1.

3. Create an outer loop that iterates from 1 to the number of rows (inclusive).

4. For each iteration of the outer loop:
   a. Create an inner loop that iterates from 1 to the current row number.
   b. In each iteration of the inner loop:
      - Print the `current_number` followed by a space.
      - Increment `current_number` by 1.
   c. After the inner loop completes, print a newline character to move to the next line.

5. Repeat steps 4a-4c until all rows are printed.

## Explanation

- The outer loop controls the number of rows.
- The inner loop prints the numbers for each row, starting from the current number and printing as many numbers as the row number.
- We use a `current_number` variable to keep track of the next number to be printed, which continues incrementing across rows.
- We print a space after each number to separate them horizontally.
- The newline character after each row ensures each row starts on a new line.

## Pseudocode

```
n = 5  // Number of rows
current_number = 1

for i from 1 to n:
    for j from 1 to i:
        print current_number followed by a space
        increment current_number by 1
    print newline
```

## Note

- This pattern requires keeping track of a running count across rows, unlike simpler patterns that reset each row.
- The number of rows can be modified by changing the value of n, which will automatically adjust the final number in the pattern.
- Make sure to handle any language-specific syntax for loops and print statements when implementing this in a specific programming language.
- For numbers with two digits, ensure proper spacing to maintain alignment.
- The pattern continues the numeric sequence across rows, which creates a unique triangular arrangement of consecutive numbers.

## Variations

You can create variations of this pattern by:
1. Starting with a different initial number.
2. Using a different increment value between numbers.
3. Aligning the triangle to the right side (which would require calculating the maximum width and padding with spaces).

These variations can be achieved by modifying the initial value, the increment step, or adding logic for right alignment.
