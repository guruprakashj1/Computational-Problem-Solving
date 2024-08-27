# 3- Control Flow in Python

Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

## Introduction
Control flow is the order in which individual statements, instructions, or function calls are executed in a program. Python provides various control flow statements that allow you to control the flow of your program, making decisions and repeating actions based on certain conditions.

## Key Control Flow Statements

### 1. Conditional Statements
- **if statement**: Executes a block of code if a specified condition is true.
- **if-else statement**: Executes one block if the condition is true, another if it's false.
- **if-elif-else statement**: Allows checking multiple conditions.

### 2. Loops
- **for loop**: Iterates over a sequence (list, tuple, string, etc.) or other iterable objects.
- **while loop**: Repeats a block of code as long as a condition is true.

### 3. Control Statements
- **break**: Exits the current loop prematurely.
- **continue**: Skips the rest of the current iteration and moves to the next one.
- **pass**: A null operation; does nothing. Used as a placeholder.

### 4. Exception Handling
- **try-except**: Catches and handles exceptions (errors) that occur during execution.
- **try-except-else-finally**: A more comprehensive form of exception handling.

### 5. Context Managers
- **with statement**: Simplifies exception handling by encapsulating common preparation and cleanup tasks.

## Best Practices
1. Use clear and descriptive condition names in if statements.
2. Avoid deep nesting of control structures; consider refactoring into functions.
3. Use for loops when the number of iterations is known, while loops when it's not.
4. Always provide a base case in recursive functions to prevent infinite recursion.
5. Use exception handling to make your code more robust and user-friendly.

## Common Pitfalls
1. Infinite loops due to improper condition updates in while loops.
2. Off-by-one errors in for loops when working with indices.
3. Forgetting to handle potential exceptions, leading to program crashes.
4. Overusing break and continue, which can make code harder to read.

## Conclusion
Mastering control flow is essential for writing efficient and effective Python programs. It allows you to create dynamic and responsive code that can make decisions, repeat actions, and handle errors gracefully. Practice using these control structures to become proficient in directing the flow of your Python programs.
