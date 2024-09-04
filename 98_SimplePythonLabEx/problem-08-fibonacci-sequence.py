# Problem 8: Print Fibonacci sequence up to n terms using a while loop

"""
Explanation: This problem uses a while loop to generate a sequence.
Logic: Each number in the Fibonacci sequence is the sum of the two preceding ones.
Algorithm:
1. Input n (number of terms)
2. Initialize first two terms (a = 0, b = 1)
3. While count < n:
   a. Print current term
   b. Calculate next term (c = a + b)
   c. Update a and b (a = b, b = c)
   d. Increment count
"""

n = int(input("Enter the number of Fibonacci terms to generate: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a, b = b, c
    count += 1
print()
