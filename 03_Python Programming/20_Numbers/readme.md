# 7- Numbers in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
Numbers are fundamental data types in Python used to store numeric values. Python supports several types of numbers, each with its own characteristics and use cases.

## Types of Numbers in Python

### 1. Integers (int)
- Whole numbers, positive or negative, without decimals
- Examples: -5, 0, 42
- Unlimited precision in Python 3

### 2. Floating-Point Numbers (float)
- Numbers with decimal points or in scientific notation
- Examples: 3.14, -0.001, 2.5e-4
- Limited precision (typically 15-17 significant digits)

### 3. Complex Numbers (complex)
- Numbers with a real and imaginary part
- Written as x + yj, where x is the real part and y is the imaginary part
- Example: 3 + 4j

## Numeric Operations

### Basic Arithmetic
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/` (always returns a float)
- Floor Division: `//` (rounds down to nearest integer)
- Modulus: `%` (remainder of division)
- Exponentiation: `**`

### Built-in Functions for Numbers
- `abs(x)`: Absolute value of x
- `round(x, n)`: Round x to n decimal places
- `max(x1, x2, ...)`: Maximum of given numbers
- `min(x1, x2, ...)`: Minimum of given numbers
- `pow(x, y)`: x raised to the power y

### Type Conversion
- `int()`: Convert to integer
- `float()`: Convert to float
- `complex()`: Convert to complex number

## The math Module
Python's `math` module provides additional mathematical functions:
- Trigonometric functions: `sin()`, `cos()`, `tan()`
- Logarithmic functions: `log()`, `log10()`
- Constants: `pi`, `e`
- And many more

## The random Module
For generating random numbers:
- `random.random()`: Random float between 0 and 1
- `random.randint(a, b)`: Random integer between a and b (inclusive)
- `random.choice(seq)`: Random element from a sequence

## Best Practices
1. Use integers when working with whole numbers
2. Be aware of floating-point precision limitations
3. Use the `decimal` module for precise decimal calculations (e.g., financial calculations)
4. Utilize the `math` module for advanced mathematical operations

## Conclusion
Understanding how to work with numbers in Python is crucial for many programming tasks, from basic calculations to complex scientific computing. Mastering these concepts will greatly enhance your ability to manipulate numeric data in Python.
