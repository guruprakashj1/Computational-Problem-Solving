# 3-Ternary-Operator-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Basic ternary operator usage
x = 10
result = "Positive" if x > 0 else "Non-positive"
print(f"x is {result}")  # Output: x is Positive

# Ternary operator with zero as a condition
y = 0
state = "Zero" if y == 0 else "Non-zero"
print(f"y is {state}")  # Output: y is Zero

# Using ternary operator with strings
name = "Alice"
greeting = "Hello, " + ("Alice" if name == "Alice" else "stranger")
print(greeting)  # Output: Hello, Alice

# Ternary operator in a function
def is_even(num):
    return "Even" if num % 2 == 0 else "Odd"

print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd

# Ternary operator with function calls
def is_morning():
    return True  # Assume it's morning for this example

time_greeting = "Good morning" if is_morning() else "Good evening"
print(time_greeting)  # Output: Good morning

# Using ternary operator in a list comprehension
numbers = [1, 2, 3, 4, 5]
parity = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(parity)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Nested ternary operator (use with caution)
a = 5
result = "Positive" if a > 0 else "Zero" if a == 0 else "Negative"
print(f"a is {result}")  # Output: a is Positive

# Ternary operator with comparison operations
x, y = 10, 20
larger = x if x > y else y
print(f"The larger number is {larger}")  # Output: The larger number is 20

# Using ternary operator with logical operators
a, b = True, False
result = "Both True" if a and b else "At least one False"
print(result)  # Output: At least one False

# Ternary operator in dictionary comprehension
numbers = [1, 2, 3, 4, 5]
num_dict = {num: "Even" if num % 2 == 0 else "Odd" for num in numbers}
print(num_dict)  # Output: {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}

# Using ternary operator with 'in' operator
fruits = ["apple", "banana", "cherry"]
has_apple = "Yes" if "apple" in fruits else "No"
print(f"Has apple? {has_apple}")  # Output: Has apple? Yes

# Ternary operator with None checking
value = None
result = "Not None" if value is not None else "None"
print(result)  # Output: None

# Using ternary operator in a lambda function
is_adult = lambda age: "Adult" if age >= 18 else "Minor"
print(is_adult(20))  # Output: Adult
print(is_adult(15))  # Output: Minor

