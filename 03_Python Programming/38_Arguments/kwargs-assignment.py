# 7- **args - Assignment Questions
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Question 1: Flexible Object Creator
# Create a function called create_object that takes a class name as the first argument,
# followed by any number of keyword arguments. The function should create and return
# an instance of the specified class with the given keyword arguments as attributes.

# Hint: Use the type() function to create a new class dynamically, and then instantiate it.
# You can use setattr() to set the attributes of the instance.

def create_object(class_name, **kwargs):
    # Your code here
    pass

# Test your function
person = create_object("Person", name="Alice", age=30, city="New York")
print(person.name, person.age, person.city)

car = create_object("Car", make="Toyota", model="Corolla", year=2022)
print(car.make, car.model, car.year)


# Question 2: Command-Line Argument Parser
# Create a function called parse_cli_args that simulates parsing command-line arguments.
# The function should take any number of keyword arguments where the key is the argument name
# and the value is a dictionary containing the argument's properties (type, default, help text).
# The function should return a dictionary of parsed arguments.

# Hint: Use input() to simulate command-line input. Use the type specified in the properties
# to convert the input to the correct data type. If no input is provided, use the default value.

def parse_cli_args(**kwargs):
    # Your code here
    pass

# Test your function
args = parse_cli_args(
    name={"type": str, "default": "User", "help": "Your name"},
    age={"type": int, "default": 0, "help": "Your age"},
    is_student={"type": bool, "default": False, "help": "Are you a student?"}
)
print(args)


# Question 3: Flexible Data Validator
# Create a function called validate_data that takes a data dictionary as input and
# validates it against a set of rules provided as keyword arguments. Each rule should
# be a function that returns True if the data is valid, and False otherwise.
# The validate_data function should return a dictionary of validation results.

# Hint: Use a dictionary comprehension to apply each validation rule to the corresponding
# data field. Handle cases where a field might be missing from the data dictionary.

def validate_data(data, **validation_rules):
    # Your code here
    pass

# Test your function
data = {"name": "Alice", "age": 25, "email": "alice@example.com"}

def is_non_empty_string(value):
    return isinstance(value, str) and len(value) > 0

def is_positive_integer(value):
    return isinstance(value, int) and value > 0

def is_valid_email(value):
    return isinstance(value, str) and "@" in value and "." in value.split("@")[1]

results = validate_data(data,
    name=is_non_empty_string,
    age=is_positive_integer,
    email=is_valid_email,
    phone=is_non_empty_string  # This field is missing in the data
)
print(results)

