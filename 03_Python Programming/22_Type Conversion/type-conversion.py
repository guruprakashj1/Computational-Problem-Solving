# 9-Type-Conversion-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Implicit Type Conversion
print("Implicit Type Conversion:")
integer_num = 10
float_num = 3.14
result = integer_num + float_num
print(f"{integer_num} + {float_num} = {result}")
print(f"Type of result: {type(result)}")

# Explicit Type Conversion

# int() conversion
print("\nint() conversion:")
print(f"int(3.14) = {int(3.14)}")
print(f"int('100') = {int('100')}")
try:
    print(int('3.14'))  # This will raise a ValueError
except ValueError as e:
    print(f"Error: {e}")

# float() conversion
print("\nfloat() conversion:")
print(f"float(10) = {float(10)}")
print(f"float('3.14') = {float('3.14')}")
print(f"float('10') = {float('10')}")

# str() conversion
print("\nstr() conversion:")
print(f"str(10) = '{str(10)}'")
print(f"str(3.14) = '{str(3.14)}'")
print(f"str(True) = '{str(True)}'")

# bool() conversion
print("\nbool() conversion:")
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"bool('') = {bool('')}")
print(f"bool('False') = {bool('False')}")  # Note: This is True because it's a non-empty string

# list() conversion
print("\nlist() conversion:")
print(f"list('Python') = {list('Python')}")
print(f"list((1, 2, 3)) = {list((1, 2, 3))}")

# tuple() conversion
print("\ntuple() conversion:")
print(f"tuple([1, 2, 3]) = {tuple([1, 2, 3])}")
print(f"tuple('Python') = {tuple('Python')}")

# set() conversion
print("\nset() conversion:")
print(f"set([1, 2, 2, 3, 3, 3]) = {set([1, 2, 2, 3, 3, 3])}")
print(f"set('Mississippi') = {set('Mississippi')}")

# dict() conversion
print("\ndict() conversion:")
pairs = [('a', 1), ('b', 2), ('c', 3)]
print(f"dict({pairs}) = {dict(pairs)}")

# Complex conversions and error handling
print("\nComplex conversions and error handling:")

# Converting string to int, then to float
num_str = "42"
num_int = int(num_str)
num_float = float(num_int)
print(f"'{num_str}' -> int -> float: {num_float}")

# Handling potential errors
def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to int")
        return None

print(f"safe_int_convert('10'): {safe_int_convert('10')}")
print(f"safe_int_convert('3.14'): {safe_int_convert('3.14')}")

# Demonstrating data loss
large_float = 1234567890.123456
int_from_float = int(large_float)
float_from_int = float(int_from_float)
print(f"\nData loss demonstration:")
print(f"Original float: {large_float}")
print(f"Converted to int and back to float: {float_from_int}")
print(f"Data lost in conversion: {large_float - float_from_int}")

