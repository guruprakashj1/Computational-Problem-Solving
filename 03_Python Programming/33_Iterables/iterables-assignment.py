# 11- Iterables - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Custom Range Iterator
# Create a class called CustomRange that behaves similarly to the built-in range() function.
# It should be iterable and support the following:
# - Initialization with start, stop, and step values
# - Iteration to yield values
# - Raising StopIteration when the iteration is complete

# Hint: Implement __iter__() and __next__() methods. Keep track of the current value and increment it by step in each iteration.

class CustomRange:
    # Your code here
    pass

# Test your class
for num in CustomRange(1, 10, 2):
    print(num, end=" ")  # Should print: 1 3 5 7 9
print()


# Question 2: Flatten Nested List
# Write a function called flatten_list that takes a nested list as input and returns a flattened version of the list.
# The function should work for lists with any level of nesting.

# Hint: Use recursion. Check if each element is a list, and if so, recursively flatten it.

def flatten_list(nested_list):
    # Your code here
    pass

# Test your function
nested = [1, [2, 3, [4, 5]], 6, [7, 8]]
flattened = flatten_list(nested)
print(flattened)  # Should print: [1, 2, 3, 4, 5, 6, 7, 8]


# Question 3: Circular Buffer
# Implement a class called CircularBuffer that represents a circular buffer of a fixed size.
# The class should be iterable and support the following operations:
# - Initialization with a fixed size
# - Adding elements (if the buffer is full, overwrite the oldest element)
# - Iteration through the elements in the order they were added

# Hint: Use a list to store elements and keep track of the current position. Implement __iter__() to make it iterable.

class CircularBuffer:
    # Your code here
    pass

# Test your class
buffer = CircularBuffer(5)
for i in range(7):
    buffer.add(i)

for item in buffer:
    print(item, end=" ")  # Should print: 2 3 4 5 6
print()
