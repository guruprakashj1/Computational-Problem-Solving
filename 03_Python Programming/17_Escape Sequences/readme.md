# 4- Escape Sequences in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
Escape sequences in Python are special characters that are used to represent certain actions within strings. These sequences allow you to include characters in your strings that would otherwise be difficult or impossible to directly include.

## Common Escape Sequences

1. **\n** - Newline
   - Moves the cursor to the beginning of the next line.
   
2. **\t** - Tab
   - Inserts a tab space.
   
3. **\\\** - Backslash
   - Used to insert a literal backslash.
   
4. **\'** - Single Quote
   - Used to insert a single quote in a string enclosed by single quotes.
   
5. **\"** - Double Quote
   - Used to insert a double quote in a string enclosed by double quotes.
   
6. **\r** - Carriage Return
   - Moves the cursor to the beginning of the current line.
   
7. **\b** - Backspace
   - Moves the cursor one character backward.
   
8. **\f** - Form Feed
   - Moves the cursor to the next page.

## Using Escape Sequences

Escape sequences are preceded by a backslash (\) and are interpreted within string literals.

Example:
```python
print("Hello\nWorld")  # Prints on two lines
print("This is a\ttabbed line")  # Inserts a tab
print("She said, \"Hello!\"")  # Includes double quotes in the string
```

## Raw Strings

If you need to use backslashes extensively (e.g., for file paths in Windows), you can use raw strings by prefixing the string with 'r':

```python
print(r"C:\Users\YourName\Documents")  # Backslashes are treated as literal characters
```

## Unicode Escape Sequences

Python also supports Unicode escape sequences, allowing you to represent Unicode characters in strings:

- **\u** followed by four hexadecimal digits for 16-bit Unicode characters
- **\U** followed by eight hexadecimal digits for 32-bit Unicode characters

Example:
```python
print("\u03C0")  # Prints the Greek letter π (pi)
```

## Conclusion
Understanding escape sequences is crucial for string manipulation in Python, especially when dealing with special characters, formatting, or representing non-printable characters. They provide a way to include characters in strings that would otherwise be difficult to represent directly in code.
