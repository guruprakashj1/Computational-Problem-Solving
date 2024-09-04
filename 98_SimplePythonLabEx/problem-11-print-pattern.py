# Problem 11: Print a pattern using nested loops

"""
Explanation: This problem uses nested loops to create a pattern.
Logic: Use one loop for rows and another for columns, print stars based on row number.
Algorithm:
1. Input number of rows
2. For each row from 1 to number of rows:
   a. For each column from 1 to row number:
      i. Print a star
   b. Move to next line
"""

rows = int(input("Enter the number of rows for the pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
