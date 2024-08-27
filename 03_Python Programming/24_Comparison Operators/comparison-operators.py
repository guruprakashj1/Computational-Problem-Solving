# 1-Comparison-Operators-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Equal to (==)
print("Equal to (==):")
print(5 == 5)   # True
print(5 == 6)   # False
print("hello" == "hello")  # True
print("hello" == "Hello")  # False (case-sensitive)

# Not equal to (!=)
print("\nNot equal to (!=):")
print(5 != 6)   # True
print(5 != 5)   # False
print("hello" != "world")  # True

# Greater than (>)
print("\nGreater than (>):")
print(10 > 5)   # True
print(5 > 10)   # False
print(10 > 10)  # False

# Less than (<)
print("\nLess than (<):")
print(5 < 10)   # True
print(10 < 5)   # False
print(10 < 10)  # False

# Greater than or equal to (>=)
print("\nGreater than or equal to (>=):")
print(10 >= 5)  # True
print(10 >= 10) # True
print(5 >= 10)  # False

# Less than or equal to (<=)
print("\nLess than or equal to (<=):")
print(5 <= 10)  # True
print(10 <= 10) # True
print(10 <= 5)  # False

# Chaining comparison operators
print("\nChaining comparison operators:")
x = 5
print(1 < x < 10)  # True (equivalent to 1 < x and x < 10)
print(10 < x < 20) # False

# Comparing different types
print("\nComparing different types:")
print(5 == "5")  # False (int vs string)
print(5 == 5.0)  # True (int vs float, Python converts int to float)

# Identity comparison (is, is not)
print("\nIdentity comparison (is, is not):")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True (same value)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)

# Membership comparison (in, not in)
print("\nMembership comparison (in, not in):")
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)     # True
print("grape" not in fruits) # True

# Comparing strings
print("\nComparing strings:")
print("apple" < "banana")  # True (lexicographical comparison)
print("Z" < "a")           # True (ASCII value of 'Z' is less than 'a')

# Floating-point comparison (be cautious!)
print("\nFloating-point comparison:")
print(0.1 + 0.2 == 0.3)  # False (due to floating-point precision)
print(abs((0.1 + 0.2) - 0.3) < 1e-9)  # True (a better way to compare floats)

# Boolean comparison
print("\nBoolean comparison:")
print(True == 1)   # True
print(False == 0)  # True
print(True > False) # True

# None comparison
print("\nNone comparison:")
print(None == None)  # True
print(None is None)  # True (preferred way to compare with None)

