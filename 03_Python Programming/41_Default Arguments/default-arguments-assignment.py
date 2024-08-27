# 5- Default Arguments - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Email Formatter
# Create a function called format_email that takes the following parameters:
# - recipient (required): the email recipient's name
# - sender (required): the sender's name
# - subject (optional): the email subject (default to "No Subject")
# - body (optional): the email body (default to an empty string)
# The function should return a formatted email string.

# Hint: Use default arguments for optional parameters and use string formatting to create the email.

def format_email(recipient, sender, subject="No Subject", body=""):
    # Your code here
    pass

# Test your function
print(format_email("Alice", "Bob"))
print(format_email("Charlie", "David", subject="Meeting", body="Let's meet at 2 PM."))


# Question 2: Shopping Cart
# Create a function called add_to_cart that simulates adding items to a shopping cart.
# The function should take the following parameters:
# - item (required): the name of the item to add
# - quantity (optional): the quantity of the item (default to 1)
# - cart (optional): the current shopping cart (default to an empty list)
# The function should return the updated cart.

# Hint: Be careful with the mutable default argument pitfall. Use None as the default value for the cart parameter.

def add_to_cart(item, quantity=1, cart=None):
    # Your code here
    pass

# Test your function
print(add_to_cart("apple"))
print(add_to_cart("banana", 2))
cart = add_to_cart("orange", 3)
print(add_to_cart("grape", 2, cart))


# Question 3: Data Processor
# Create a function called process_data that takes the following parameters:
# - data (required): a list of numbers
# - operation (optional): a string indicating the operation to perform (default to "sum")
# - round_result (optional): a boolean indicating whether to round the result (default to False)
# - decimal_places (optional): the number of decimal places to round to (default to 2)
# The function should perform the specified operation on the data and return the result.
# Supported operations: "sum", "average", "max", "min"

# Hint: Use a dictionary to map operation strings to corresponding functions (sum, max, min).
# For the average operation, you can use sum(data) / len(data).

def process_data(data, operation="sum", round_result=False, decimal_places=2):
    # Your code here
    pass

# Test your function
data = [1.1, 2.2, 3.3, 4.4, 5.5]
print(process_data(data))
print(process_data(data, operation="average", round_result=True))
print(process_data(data, operation="max", round_result=True, decimal_places=1))

