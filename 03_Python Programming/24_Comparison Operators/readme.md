# 1- Comparison Operators in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
Comparison operators in Python are used to compare values. They return either `True` or `False` depending on whether the comparison is valid. These operators are fundamental in creating conditional statements and loops in Python programs.

## Types of Comparison Operators

1. **Equal to (==)**
   - Checks if two values are equal
   - Example: `5 == 5` returns `True`

2. **Not equal to (!=)**
   - Checks if two values are not equal
   - Example: `5 != 3` returns `True`

3. **Greater than (>)**
   - Checks if the left value is greater than the right value
   - Example: `7 > 3` returns `True`

4. **Less than (<)**
   - Checks if the left value is less than the right value
   - Example: `2 < 8` returns `True`

5. **Greater than or equal to (>=)**
   - Checks if the left value is greater than or equal to the right value
   - Example: `5 >= 5` returns `True`

6. **Less than or equal to (<=)**
   - Checks if the left value is less than or equal to the right value
   - Example: `4 <= 4` returns `True`

## Special Comparisons

1. **Identity comparison (is, is not)**
   - Checks if two objects have the same identity (same memory location)
   - Example: `x is y` checks if `x` and `y` are the same object

2. **Membership comparison (in, not in)**
   - Checks if a value is a member of a sequence (like a list, tuple, or string)
   - Example: `'a' in 'abc'` returns `True`

## Best Practices

1. Use `==` for value comparison and `is` for identity comparison
2. Be cautious when comparing floating-point numbers due to precision issues
3. Use parentheses to group comparisons for clarity in complex conditions

## Common Pitfalls

1. Confusing `=` (assignment) with `==` (comparison)
2. Using `is` when `==` is intended (especially with numbers and strings)
3. Overlooking type differences in comparisons

## Conclusion
Mastering comparison operators is crucial for writing effective conditional statements and creating logical flows in Python programs. They form the basis of decision-making in code and are essential for tasks ranging from simple data validation to complex algorithmic operations.
