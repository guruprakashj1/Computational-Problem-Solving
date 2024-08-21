# Print the Consecutive Alphabet Triangle Pattern

This README file provides a step-by-step procedure to print the triangle pattern of consecutive alphabet letters as shown in the image.

## Problem Statement

Print a pattern of uppercase letters that forms a right-angled triangle, where each row starts with the next consecutive letter of the alphabet and contains as many letters as the row number, continuing the sequence from the previous row.

## Pattern Description

The pattern looks like this:
```
A
B C
D E F
G H I J
K L M N O
```

## Step-by-Step Procedure

1. Determine the number of rows for the pattern (in this case, it's 5).

2. Initialize a variable `current_letter` to 'A'.

3. Create an outer loop that iterates from 1 to the number of rows (inclusive).

4. For each iteration of the outer loop:
   a. Create an inner loop that iterates from 1 to the current row number.
   b. In each iteration of the inner loop:
      - Print the `current_letter` followed by a space.
      - Increment `current_letter` to the next alphabet letter.
   c. After the inner loop completes, print a newline character to move to the next line.

5. Repeat steps 4a-4c until all rows are printed.

## Explanation

- The outer loop controls the number of rows.
- The inner loop prints the letters for each row, starting from the current letter and printing as many letters as the row number.
- We use a `current_letter` variable to keep track of the next letter to be printed, which continues incrementing across rows.
- We print a space after each letter to separate them horizontally.
- The newline character after each row ensures each row starts on a new line.

## Pseudocode

```
n = 5  // Number of rows
current_letter = 'A'

for i from 1 to n:
    for j from 1 to i:
        print current_letter followed by a space
        increment current_letter to next alphabet letter
    print newline
```

## Note

- This pattern requires keeping track of a running alphabet sequence across rows.
- The number of rows can be modified by changing the value of n, which will automatically adjust the final letter in the pattern.
- Make sure to handle the case when `current_letter` goes beyond 'Z'. You may choose to wrap around to 'A' or stop the pattern.
- In most programming languages, you can increment a character by converting it to its ASCII value, incrementing that, and then converting back to a character.
- Ensure proper spacing between letters to maintain readability.

## Variations

You can create variations of this pattern by:
1. Starting with a different initial letter.
2. Using lowercase letters instead of uppercase.
3. Reversing the order of letters in each row.
4. Aligning the triangle to the right side (which would require calculating the maximum width and padding with spaces).

These variations can be achieved by modifying the initial value, the increment logic, or adding additional formatting steps.
