# 5- Formatted Strings in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
Formatted strings in Python provide a powerful and flexible way to embed expressions inside string literals. They allow you to create complex strings with variables, expressions, and even function calls embedded directly within them.

## Types of String Formatting in Python

### 1. f-Strings (Formatted String Literals)
Introduced in Python 3.6, f-strings are the most modern and recommended way to format strings.

Syntax: `f"...{expression}..."`

Example:
```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

Features:
- Can include expressions and function calls inside curly braces
- Support format specifiers for alignment, padding, and precision

### 2. str.format() Method
This method has been available since Python 2.6 and is still widely used.

Syntax: `"...{}...".format(value)`

Example:
```python
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```

Features:
- Allows positional and keyword arguments
- Supports indexing for reuse of arguments

### 3. %-formatting (String Interpolation)
This is the oldest method, inherited from C programming. While still supported, it's generally less preferred in modern Python.

Syntax: `"... %s ..." % value`

Example:
```python
name = "Charlie"
age = 35
print("My name is %s and I am %d years old." % (name, age))
```

Features:
- Uses format specifiers like %s for strings, %d for integers
- Limited compared to newer methods

## Format Specifiers
Format specifiers allow you to control how values are presented:

- Alignment and padding: `{:>10}` (right-align, width 10)
- Number formatting: `{:.2f}` (2 decimal places for floats)
- Date formatting: `{:%Y-%m-%d}` (for datetime objects)

Example:
```python
import datetime
price = 19.99
date = datetime.date(2023, 5, 15)
print(f"Price: ${price:.2f}, Date: {date:%B %d, %Y}")
```

## Best Practices
1. Use f-strings for simplicity and readability when possible
2. Use str.format() for compatibility with older Python versions
3. Avoid %-formatting in new code unless necessary for legacy reasons
4. Use meaningful names in placeholder expressions for clarity

## Conclusion
Formatted strings are an essential tool in Python for creating dynamic, readable text output. Understanding and effectively using these formatting methods can greatly enhance your ability to work with strings in Python.
