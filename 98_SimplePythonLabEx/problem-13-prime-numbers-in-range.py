# Problem 13: Print all prime numbers in a given range using nested loops

"""
Explanation: This problem uses nested loops to check primality for a range of numbers.
Logic: For each number in the range, check if it's prime using the method from Problem 7.
Algorithm:
1. Input start and end of range
2. For each number n in the range:
   a. Assume n is prime
   b. For each potential divisor i from 2 to sqrt(n):
      i. If n is divisible by i, it's not prime
   c. If n is prime, print it
"""

import math

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for n in range(start, end + 1):
    if n > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, end=" ")
print()
