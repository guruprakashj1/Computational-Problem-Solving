# 4-Escape-Sequences-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Newline (\n)
print("Hello\nWorld")
# Output:
# Hello
# World

# Tab (\t)
print("Name:\tJohn Doe")
# Output: Name:	John Doe

# Backslash (\\)
print("This is a backslash: \\")
# Output: This is a backslash: \

# Single quote (\')
print('It\'s a beautiful day')
# Output: It's a beautiful day

# Double quote (\")
print("She said, \"Hello!\"")
# Output: She said, "Hello!"

# Carriage Return (\r)
print("Hello\rWorld")
# Output: World (overwrites "Hello")

# Backspace (\b)
print("Hello\bWorld")
# Output: HellWorld (removes the 'o')

# Form Feed (\f)
print("Page 1\fPage 2")
# Output: Page 1Page 2 (may not be visible in all consoles)

# Combining multiple escape sequences
print("Line 1\nLine 2\n\tIndented Line 3")
# Output:
# Line 1
# Line 2
#     Indented Line 3

# Using raw strings
windows_path = r"C:\Users\YourName\Documents"
print(windows_path)
# Output: C:\Users\YourName\Documents

# Unicode escape sequences
print("\u03C0")  # Greek letter pi
print("\U0001F600")  # Smiling face emoji

# Multiline string with escape sequences
multiline = "This is a long string that spans \
multiple lines in the code, but will be \
printed as a single line."
print(multiline)

# Comparing raw string with regular string
print("Regular string: \\t")
print(r"Raw string: \t")

# Escape sequences in formatted strings
name = "Alice"
age = 30
print(f"Name:\t{name}\nAge:\t{age}")

# Using escape sequences for alignment
print("Column 1\tColumn 2\tColumn 3")
print("Value 1\tValue 2\tValue 3")

# Demonstrating octal and hexadecimal escape sequences
print("\110\145\154\154\157")  # Octal for "Hello"
print("\x48\x65\x6C\x6C\x6F")  # Hexadecimal for "Hello"

