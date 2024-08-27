# 6-String-Methods-Example.py

# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# Sample string
text = "  Hello, World!  "
print("Original string:", text)

# 1. Case Modification
print("\n1. Case Modification:")
print("Upper:", text.upper())  # Converts all characters to uppercase
print("Lower:", text.lower())  # Converts all characters to lowercase
print("Capitalize:", text.capitalize())  # Capitalizes the first character
print("Title:", text.title())  # Capitalizes the first character of each word

# 2. Searching and Replacing
print("\n2. Searching and Replacing:")
print("Find 'o':", text.find('o'))  # Returns the lowest index of 'o'
print("Count 'l':", text.count('l'))  # Counts occurrences of 'l'
print("Replace:", text.replace("World", "Python"))  # Replaces "World" with "Python"

# 3. Stripping Whitespace
print("\n3. Stripping Whitespace:")
print("Strip:", text.strip())  # Removes leading and trailing whitespace
print("Left Strip:", text.lstrip())  # Removes leading whitespace
print("Right Strip:", text.rstrip())  # Removes trailing whitespace

# 4. Splitting and Joining
print("\n4. Splitting and Joining:")
words = text.split(',')  # Splits the string at ',' into a list
print("Split:", words)
print("Join:", "-".join(words))  # Joins the list elements with '-'

# 5. Checking String Content
print("\n5. Checking String Content:")
print("Starts with 'Hello':", text.strip().startswith("Hello"))  # Checks if the string starts with "Hello"
print("Ends with '!':", text.strip().endswith("!"))  # Checks if the string ends with "!"
print("Is alphanumeric:", "Hello123".isalnum())  # Checks if all characters are alphanumeric
print("Is alphabetic:", "Hello".isalpha())  # Checks if all characters are alphabetic
print("Is digit:", "123".isdigit())  # Checks if all characters are digits

# 6. Formatting
print("\n6. Formatting:")
print("Center:", "Python".center(20, '-'))  # Centers "Python" in a 20-character string
print("Left Justify:", "Python".ljust(20, '*'))  # Left-justifies "Python" in a 20-character string
print("Right Justify:", "Python".rjust(20, '*'))  # Right-justifies "Python" in a 20-character string
print("Zero Fill:", "42".zfill(5))  # Pads "42" with zeros on the left to make it 5 characters long

# 7. Miscellaneous
print("\n7. Miscellaneous:")
print("Length:", len(text))  # Returns the length of the string

# 8. Chaining Methods
print("\n8. Chaining Methods:")
result = text.strip().lower().replace("world", "python")
print("Chained result:", result)

# 9. String Slicing (not a method, but important for string manipulation)
print("\n9. String Slicing:")
print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])
print("Every second character:", text[::2])

# 10. Advanced Methods
print("\n10. Advanced Methods:")
print("Partition:", "Hello-World".partition('-'))  # Splits the string at the first occurrence of '-'
print("Translate:", "Hello".translate(str.maketrans('o', '0')))  # Replaces 'o' with '0'

# Remember: String methods return new strings; they don't modify the original string
print("\nOriginal string is still:", text)
