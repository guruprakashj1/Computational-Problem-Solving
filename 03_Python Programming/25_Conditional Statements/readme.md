# 2- Conditional Statements in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
Conditional statements in Python allow you to execute different blocks of code based on whether certain conditions are true or false. They are fundamental to creating decision-making processes in your programs.

## Types of Conditional Statements

### 1. if Statement
The `if` statement is used to execute a block of code only if a specified condition is true.

Syntax:
```python
if condition:
    # code to execute if condition is true
```

### 2. if-else Statement
The `if-else` statement allows you to execute one block of code if the condition is true and another if it's false.

Syntax:
```python
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

### 3. if-elif-else Statement
The `if-elif-else` chain allows you to check multiple conditions.

Syntax:
```python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if all conditions are false
```

### 4. Nested Conditional Statements
You can nest conditional statements inside other conditional statements.

### 5. Conditional Expressions (Ternary Operator)
A shorthand way to write simple if-else statements.

Syntax:
```python
value_if_true if condition else value_if_false
```

## Best Practices
1. Keep conditions simple and readable
2. Use compound conditions with logical operators (and, or, not) when appropriate
3. Consider using elif for multiple related conditions instead of nested if statements
4. Use the ternary operator for simple conditional assignments

## Common Pitfalls
1. Forgetting to use proper indentation
2. Using assignment (=) instead of comparison (==) in conditions
3. Overcomplicating conditions, making them hard to understand
4. Not considering all possible cases, leading to unexpected behavior

## Conclusion
Mastering conditional statements is crucial for creating dynamic and responsive Python programs. They allow your code to make decisions and adapt to different scenarios, forming the backbone of program logic and flow control.
