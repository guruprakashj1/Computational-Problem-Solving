# Problem 5: Calculate the sum of numbers from 1 to n using a for loop

"""
Explanation: This problem introduces a for loop with the range function.
Logic: Iterate through numbers from 1 to n and add them to a sum variable.
Algorithm:
1. Input n
2. Initialize sum to 0
3. For each number i from 1 to n:
   a. Add i to sum
4. Print the sum
"""

n = int(input("Enter a positive integer n: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"The sum of numbers from 1 to {n} is: {sum}")
