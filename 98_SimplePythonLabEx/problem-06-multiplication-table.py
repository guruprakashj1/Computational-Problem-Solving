# Problem 6: Print a multiplication table using nested loops

"""
Explanation: This problem introduces nested for loops.
Logic: Use one loop for rows and another for columns to create a table.
Algorithm:
1. For each number i from 1 to 10:
   a. For each number j from 1 to 10:
      i. Print i * j
   b. Print a new line
"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
