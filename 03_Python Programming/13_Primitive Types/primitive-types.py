# 2-Primitive-Types-Example.py

# Integer
age = 25
print(f"Age: {age}")
print(f"Type of age: {type(age)}")

# Float
height = 5.9
print(f"\nHeight: {height}")
print(f"Type of height: {type(height)}")

# String
name = "Alice"
print(f"\nName: {name}")
print(f"Type of name: {type(name)}")

# Boolean
is_student = True
print(f"\nIs student: {is_student}")
print(f"Type of is_student: {type(is_student)}")

# NoneType
empty_value = None
print(f"\nEmpty value: {empty_value}")
print(f"Type of empty_value: {type(empty_value)}")

# Type conversion
string_number = "42"
converted_number = int(string_number)
print(f"\nConverted number: {converted_number}")
print(f"Type of converted_number: {type(converted_number)}")

# Boolean conversion
print(f"\nBoolean conversion of 0: {bool(0)}")
print(f"Boolean conversion of 1: {bool(1)}")
print(f"Boolean conversion of empty string: {bool('')}")
print(f"Boolean conversion of non-empty string: {bool('Hello')}")

# String formatting with different types
formatted_string = f"My name is {name}, I'm {age} years old, and my height is {height} feet."
print(f"\n{formatted_string}")
