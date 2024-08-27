# 3- Strings in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
Strings are one of the most commonly used data types in Python. They represent sequences of characters and are used to store and manipulate text data. Understanding strings is crucial for text processing, data analysis, and many other programming tasks.

## String Basics

### Creating Strings
Strings in Python can be created using single quotes (''), double quotes (""), or triple quotes (''' ''' or """ """) for multi-line strings.

```python
single_quoted = 'Hello, World!'
double_quoted = "Python Programming"
multi_line = '''This is a
multi-line string'''
```

### String Operations

1. **Concatenation**: Joining two or more strings
   ```python
   str1 = "Hello"
   str2 = "World"
   result = str1 + " " + str2  # "Hello World"
   ```

2. **Repetition**: Repeating a string
   ```python
   repeated = "Python" * 3  # "PythonPythonPython"
   ```

3. **Indexing**: Accessing individual characters
   ```python
   text = "Python"
   first_char = text[0]  # 'P'
   last_char = text[-1]  # 'n'
   ```

4. **Slicing**: Extracting a portion of a string
   ```python
   text = "Python Programming"
   substring = text[7:18]  # "Programming"
   ```

### String Methods

Python provides numerous built-in methods for string manipulation:

1. `len()`: Returns the length of the string
2. `lower()`, `upper()`: Convert to lowercase or uppercase
3. `strip()`: Removes whitespace from the beginning and end
4. `split()`: Splits the string into a list
5. `join()`: Joins elements of an iterable into a string
6. `find()`, `index()`: Search for a substring
7. `replace()`: Replace occurrences of a substring

### String Formatting

1. **f-strings** (Python 3.6+):
   ```python
   name = "Alice"
   age = 30
   print(f"My name is {name} and I am {age} years old.")
   ```

2. **format() method**:
   ```python
   print("My name is {} and I am {} years old.".format(name, age))
   ```

3. **%-formatting**:
   ```python
   print("My name is %s and I am %d years old." % (name, age))
   ```

## Conclusion
Strings are versatile and powerful in Python. Mastering string manipulation is essential for effective Python programming, especially in text processing and data analysis tasks.

