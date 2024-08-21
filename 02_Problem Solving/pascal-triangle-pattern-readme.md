# Print the Pattern for Pascal's Triangle

This README file provides a step-by-step procedure to print Pascal's triangle pattern.

## Problem Statement

Print Pascal's triangle up to n rows, where each number is the sum of the two numbers directly above it.

## Pattern Description

Pascal's triangle looks like this (for the first 5 rows):
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

## Step-by-Step Procedure

1. Determine the number of rows for the pattern (n).

2. Create an outer loop that iterates from 0 to n-1 (inclusive).

3. For each iteration of the outer loop (let's call the iterator 'row'):
   a. Print spaces for alignment: n - row - 1 spaces.
   b. Initialize 'number' as 1 and print it.
   c. Create an inner loop that iterates from 1 to 'row' (inclusive):
      - Calculate the next number: number = number * (row - i + 1) / i
      - Print the calculated number followed by a space.
   d. After the inner loop completes, print a newline character.

4. Repeat steps 3a-3d until all rows are printed.

## Explanation

- Each number in Pascal's triangle is the sum of the two numbers directly above it.
- The formula used (number = number * (row - i + 1) / i) is a clever way to calculate binomial coefficients without needing to store previous rows.
- Proper spacing is crucial for maintaining the triangular shape.

## Pseudocode

```
function printPascalTriangle(n):
    for row from 0 to n-1:
        // Print spaces for alignment
        print n - row - 1 spaces
        
        number = 1
        print number followed by a space
        
        for i from 1 to row:
            number = number * (row - i + 1) / i
            print number followed by a space
        
        print newline
```

## Mathematical Background

- The numbers in Pascal's triangle are the coefficients of the binomial expansion.
- Each number is a combination (nCr), where n is the row number and r is the position in the row (both 0-indexed).
- The formula used is an efficient way to calculate these combinations.

## Note

- This pattern combines mathematical calculations with pattern printing, making it more complex than simple shape patterns.
- The numbers can grow very large for higher rows, which might cause overflow in some programming languages. Consider using appropriate data types.
- For a large number of rows, you might need to adjust the spacing to accommodate larger numbers.
- Pascal's triangle has many interesting properties and applications in mathematics and computer science.

## Variations

You can create variations of this pattern by:
1. Printing only the numbers, without spacing for the triangle shape.
2. Using a different base number instead of 1 (which would change the mathematical properties).
3. Highlighting specific numbers (e.g., prime numbers or Fibonacci numbers) within the triangle.
4. Printing the triangle rotated 90 degrees.

These variations can provide different insights into the properties of Pascal's triangle.
