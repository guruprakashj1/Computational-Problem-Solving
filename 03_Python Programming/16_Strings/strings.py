# 3-Strings-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# String creation
single_quoted = 'Hello, World!'  # Using single quotes
double_quoted = "Python Programming"  # Using double quotes
multi_line = '''This is a
multi-line string'''  # Using triple quotes for multi-line

print("Different ways to create strings:")
print(single_quoted)
print(double_quoted)
print(multi_line)

# String concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("\nConcatenation:", result)

# String repetition
repeated = "Python" * 3
print("Repetition:", repeated)

# String indexing
text = "Python"
print("\nIndexing:")
print("First character:", text[0])
print("Last character:", text[-1])

# String slicing
text = "Python Programming"
print("\nSlicing:")
print("Substring:", text[7:18])
print("Every other character:", text[::2])
print("Reverse string:", text[::-1])

# String methods
print("\nString methods:")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

# Splitting and joining
words = text.split()
print("\nSplit:", words)
joined = "-".join(words)
print("Joined:", joined)

# Finding and replacing
print("\nFind and replace:")
print("Index of 'gram':", text.find("gram"))
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# String formatting
name = "Alice"
age = 30
print("\nString formatting:")
print(f"1. f-string: My name is {name} and I am {age} years old.")
print("2. format() method: My name is {} and I am {} years old.".format(name, age))
print("3. %-formatting: My name is %s and I am %d years old." % (name, age))

# String checking methods
print("\nString checking:")
print("Is 'Python' alphanumeric?", "Python".isalnum())
print("Is '12345' numeric?", "12345".isnumeric())
print("Is 'Hello' in uppercase?", "Hello".isupper())
print("Does 'Programming' start with 'Pro'?", "Programming".startswith("Pro"))

# Raw strings
print("\nRaw string:")
print(r"This is a raw string: \n will not create a new line")

# Comparing strings
str_a = "apple"
str_b = "banana"
print("\nString comparison:")
print(f"Is '{str_a}' equal to '{str_b}'?", str_a == str_b)
print(f"Is '{str_a}' less than '{str_b}'?", str_a < str_b)

