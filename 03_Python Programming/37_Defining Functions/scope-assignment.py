# 8- Scope - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Counter Factory
# Create a function called create_counter that returns a new function.
# The returned function should act as a counter, incrementing by 1 each time it's called
# and returning the current count. Each counter should have its own independent count.

# Hint: Use a closure to maintain the count in the enclosing scope.
# You'll need to use the nonlocal keyword to modify the count variable.

def create_counter():
    # Your code here
    pass

# Test your function
counter1 = create_counter()
counter2 = create_counter()
print(counter1())  # Should print 1
print(counter1())  # Should print 2
print(counter2())  # Should print 1
print(counter1())  # Should print 3
print(counter2())  # Should print 2


# Question 2: Global Inventory Manager
# Create a program that manages a global inventory. Implement the following functions:
# - add_item(item, quantity): Adds an item to the inventory or updates its quantity if it already exists.
# - remove_item(item, quantity): Removes a certain quantity of an item from the inventory.
# - get_inventory(): Returns the current inventory.

# Hint: Use a global dictionary to store the inventory.
# Remember to use the global keyword when modifying the inventory inside functions.

# Initialize your global inventory here

def add_item(item, quantity):
    # Your code here
    pass

def remove_item(item, quantity):
    # Your code here
    pass

def get_inventory():
    # Your code here
    pass

# Test your functions
add_item("apple", 5)
add_item("banana", 3)
print(get_inventory())  # Should print {"apple": 5, "banana": 3}
remove_item("apple", 2)
add_item("orange", 4)
print(get_inventory())  # Should print {"apple": 3, "banana": 3, "orange": 4}


# Question 3: Nested Function Calculator
# Create a function called create_calculator that returns a dictionary of mathematical operations.
# Each operation should be a nested function. The calculator should support:
# - add(x, y): returns x + y
# - subtract(x, y): returns x - y
# - multiply(x, y): returns x * y
# - divide(x, y): returns x / y (handle division by zero)
# The operations should have access to a global variable called 'operations_count'
# that keeps track of how many operations have been performed.

# Hint: Use nested functions for each operation and the nonlocal keyword
# to modify the operations_count. Use a global variable for operations_count.

operations_count = 0

def create_calculator():
    # Your code here
    pass

# Test your function
calc = create_calculator()
print(calc['add'](5, 3))  # Should print 8
print(calc['multiply'](2, 4))  # Should print 8
print(calc['divide'](10, 2))  # Should print 5.0
print(calc['subtract'](9, 3))  # Should print 6
print(f"Total operations performed: {operations_count}")  # Should print the total number of operations

