# 9- Type Conversion in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
Type conversion, also known as type casting, is the process of changing an object's data type in Python. This is a crucial concept in programming as it allows for flexibility in data manipulation and ensures that data is in the appropriate format for specific operations.

## Types of Type Conversion

### 1. Implicit Type Conversion (Coercion)
Python automatically converts one data type to another without user intervention.

Example:
```python
integer_num = 10
float_num = 3.14
result = integer_num + float_num  # result will be a float
```

### 2. Explicit Type Conversion (Casting)
The programmer explicitly converts the data type of an object to the required data type.

## Common Type Conversion Functions

1. **int()**: Converts to integer
   - From float: truncates decimal part
   - From string: must contain a valid integer

2. **float()**: Converts to float
   - From integer: adds decimal point
   - From string: must contain a valid float or integer

3. **str()**: Converts to string
   - Works with most types

4. **bool()**: Converts to boolean
   - False: 0, None, False, empty sequences or collections
   - True: non-zero numbers, True, non-empty sequences or collections

5. **list()**: Converts to list
   - Works with any iterable (e.g., tuples, strings, sets)

6. **tuple()**: Converts to tuple
   - Works with any iterable

7. **set()**: Converts to set
   - Works with any iterable, removes duplicates

8. **dict()**: Converts to dictionary
   - From sequences of key-value pairs

## Best Practices

1. Always check if type conversion is necessary
2. Handle potential exceptions when converting (e.g., ValueError)
3. Be aware of data loss in certain conversions (e.g., float to int)
4. Use appropriate conversion for the task at hand

## Common Pitfalls

1. Losing precision when converting float to int
2. Unexpected results when converting to boolean
3. TypeError when trying to convert incompatible types

## Conclusion
Understanding type conversion is essential for effective Python programming. It allows for more flexible and robust code, enabling you to work with different data types seamlessly. Always be mindful of the implications of type conversion, especially regarding potential data loss or unexpected behavior.
