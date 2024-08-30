# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# 2-Primitive-Types-Assignment.py

# Question 1: Type Identification and Conversion
# Identify the type of each variable and convert it to a different type as specified in the comments.
# Hint: Use the type() function to check the type, and int(), float(), or str() for conversion.

var1 = "42"
# TODO: Convert var1 to an integer
var1 = int(var1)

var2 = 7.5
# TODO: Convert var2 to an integer
var2 = int(var2)

var3 = 10
# TODO: Convert var3 to a float
var3 = float(var3)

# Print the original and converted values along with their types


# Question 2: String Manipulation
# Create a string that includes variables of different types using f-strings.
# Hint: Use f-strings to incorporate variables into a string.

name = "Alex"
age = 30
height = 5.9

# TODO: Create an f-string that includes all these variables
# The output should be: "My name is Alex, I'm 30 years old, and I'm 5.9 feet tall."
output = f"My name is {name}, I'm {age} years old, and I'm {height} feet tall."


# Question 3: Boolean Logic
# Determine the boolean value of different expressions and explain why they evaluate to True or False.
# Hint: Think about how Python evaluates different values as boolean.

# Expression 1: bool(0)
# Explanation: The expression bool(0) evaluates to False because in Python, any numeric value that is equal to 0 is considered as False.

# Expression 2: bool(42)
# Explanation: The expression bool(42) evaluates to True because in Python, any non-zero numeric value is considered as True.

# Expression 3: bool("")
# Explanation: The expression bool("") evaluates to False because in Python, an empty string is considered as False.

# Expression 4: bool("False")
# Explanation: The expression bool("False") evaluates to True because in Python, any non-empty string is considered as True.

# Expression 5: bool(3.14)
# Explanation: The expression bool(3.14) evaluates to True because in Python, any non-zero numeric value is considered as True.

# TODO: Evaluate and explain the boolean value of each expression
expr1 = bool(0)
expr2 = bool(42)
expr3 = bool("")
expr4 = bool("False")
expr5 = bool(3.14)

# Print each expression and its boolean value
# Explain in comments why each expression evaluates to True or False

