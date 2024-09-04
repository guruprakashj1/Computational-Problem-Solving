# Problem 7: Check if a number is prime using a for loop and if statement

"""
Explanation: This problem combines a for loop with an if statement to check primality.
Logic: A number is prime if it's only divisible by 1 and itself.
Algorithm:
1. Input a number n
2. If n is less than 2, it's not prime
3. For each number i from 2 to sqrt(n):
   a. If n is divisible by i, it's not prime
4. If no divisors found, it's prime
"""

import math

n = int(input("Enter a number to check if it's prime: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
