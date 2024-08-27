# 6- String Methods in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
String methods in Python are built-in functions that allow you to manipulate and analyze strings efficiently. These methods provide a wide range of operations, from basic transformations to complex parsing tasks.

## Common String Methods

1. **Case Modification**
   - `upper()`: Converts all characters to uppercase
   - `lower()`: Converts all characters to lowercase
   - `capitalize()`: Capitalizes the first character
   - `title()`: Capitalizes the first character of each word

2. **Searching and Replacing**
   - `find()`: Returns the lowest index of a substring
   - `index()`: Similar to find(), but raises ValueError if not found
   - `replace()`: Replaces occurrences of a substring
   - `count()`: Counts occurrences of a substring

3. **Stripping Whitespace**
   - `strip()`: Removes leading and trailing whitespace
   - `lstrip()`: Removes leading whitespace
   - `rstrip()`: Removes trailing whitespace

4. **Splitting and Joining**
   - `split()`: Splits a string into a list of substrings
   - `join()`: Joins elements of an iterable into a string

5. **Checking String Content**
   - `startswith()`: Checks if the string starts with a specified substring
   - `endswith()`: Checks if the string ends with a specified substring
   - `isalpha()`: Checks if all characters are alphabetic
   - `isdigit()`: Checks if all characters are digits
   - `isalnum()`: Checks if all characters are alphanumeric

6. **Formatting**
   - `center()`: Centers the string within a specified width
   - `ljust()`: Left-justifies the string within a specified width
   - `rjust()`: Right-justifies the string within a specified width
   - `zfill()`: Pads the string with zeros on the left

7. **Miscellaneous**
   - `len()`: Returns the length of the string (not a method, but a built-in function)

## Usage Examples

```python
text = "  Hello, World!  "
print(text.strip())  # "Hello, World!"
print(text.lower())  # "  hello, world!  "
print(text.replace("World", "Python"))  # "  Hello, Python!  "
print(",".join(["a", "b", "c"]))  # "a,b,c"
print("python".upper())  # "PYTHON"
```

## Important Notes
- String methods do not modify the original string. They return a new string.
- Most string methods are case-sensitive unless specified otherwise.
- Some methods accept optional parameters to modify their behavior.

## Conclusion
Understanding and effectively using string methods is crucial for efficient string manipulation in Python. These methods provide powerful tools for text processing, data cleaning, and general string operations in your Python programs.
