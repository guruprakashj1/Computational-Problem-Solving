# 2-Variable-Names-Assignment.py

# Question 1: Improving Variable Names
# The following code uses poor variable names. Rewrite it using better variable names.
# Hint: Think about what each variable represents and use descriptive names.

x = 5
y = 10
z = x + y
a = ["John", "Jane", "Alice"]
b = len(a)

# TODO: Rewrite the above code with better variable names


# Question 2: Naming Conventions
# Create variables or functions that follow these Python naming conventions:
# a) A constant
# b) A function that calculates the average of a list of numbers
# c) A variable for a list of student grades
# d) A boolean variable indicating if a task is completed
# e) A class representing a book
# Hint: Remember to use appropriate capitalization and underscores where needed.

# TODO: Write your code here


# Question 3: Identifying Bad Variable Names
# The following code contains some variables with bad names. Identify these variables
# and explain why they are poorly named. Then, suggest better names for them.

def func(l):
    t = 0
    for i in l:
        t += i
    return t / len(l)

data = [1, 2, 3, 4, 5]
result = func(data)
print(f"The a is: {result}")

# TODO: Comment on each bad variable name and suggest improvements


# Bonus: Rewrite the entire function and its usage with good variable names

