# 10- Nested Loops - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Pattern Printer
# Create a function called print_pattern that takes an integer n as input and prints the following pattern:
# For n = 4:
# 1
# 2 2
# 3 3 3
# 4 4 4 4

# Hint: Use two nested loops. The outer loop controls the rows, and the inner loop prints the numbers in each row.

def print_pattern(n):
    # Your code here
    pass

# Test your function
print_pattern(4)
# Should print:
# 1
# 2 2
# 3 3 3
# 4 4 4 4


# Question 2: Matrix Transposition
# Create a function called transpose_matrix that takes a matrix (a list of lists) as input
# and returns its transpose. The transpose of a matrix is a new matrix whose rows are
# the columns of the original matrix.

# Hint: Create a new matrix with dimensions swapped, then use nested loops to fill it.

def transpose_matrix(matrix):
    # Your code here
    pass

# Test your function
original_matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = transpose_matrix(original_matrix)
print(transposed)
# Should print:
# [[1, 4],
#  [2, 5],
#  [3, 6]]


# Question 3: Prime Pair Counter
# Create a function called count_prime_pairs that takes a list of integers as input
# and returns the count of pairs where both numbers are prime.
# A pair is defined as two adjacent numbers in the list.

# Hint: First, create a helper function is_prime(n) to check if a number is prime.
# Then use nested loops: one to iterate through the list, and another to check primality.

def is_prime(n):
    # Helper function to check if a number is prime
    # Your code here
    pass

def count_prime_pairs(numbers):
    # Your code here
    pass

# Test your function
test_list = [2, 3, 4, 5, 6, 7, 11, 13]
result = count_prime_pairs(test_list)
print(result)  # Should print 3 (pairs: 2-3, 5-7, 11-13)
