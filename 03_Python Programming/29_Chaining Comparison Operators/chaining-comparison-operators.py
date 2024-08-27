# 6- Chaining Comparison Operators
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates chaining comparison operators in Python

def explain_comparison(a, b, c):
    """
    This function demonstrates and explains chained comparisons.
    It checks if 'b' is between 'a' and 'c' (inclusive).
    """
    # Chained comparison
    result = a <= b <= c
    
    # Equivalent to:
    # result = (a <= b) and (b <= c)
    
    print(f"Is {b} between {a} and {c} (inclusive)? {result}")
    return result

# Demonstrate basic chaining
print("Basic chaining demonstration:")
explain_comparison(1, 5, 10)
explain_comparison(1, 0, 10)
print()

# Demonstrate chaining with different operators
def is_valid_score(score):
    """Check if a score is valid (between 0 and 100, inclusive)"""
    return 0 <= score <= 100

print("Chaining different operators:")
print(f"Is 75 a valid score? {is_valid_score(75)}")
print(f"Is -5 a valid score? {is_valid_score(-5)}")
print(f"Is 100 a valid score? {is_valid_score(100)}")
print()

# Demonstrate chaining multiple comparisons
def categorize_number(num):
    """Categorize a number based on its value"""
    if num < 0:
        return "Negative"
    elif 0 <= num < 10:
        return "Single digit positive"
    elif 10 <= num < 100:
        return "Double digit positive"
    else:
        return "Large positive"

print("Chaining multiple comparisons:")
print(f"Category of -5: {categorize_number(-5)}")
print(f"Category of 7: {categorize_number(7)}")
print(f"Category of 42: {categorize_number(42)}")
print(f"Category of 100: {categorize_number(100)}")
print()

# Demonstrate short-circuit evaluation in chained comparisons
def expensive_check(x):
    """A function that simulates an expensive check"""
    print(f"Performing expensive check on {x}")
    return x < 100

print("Demonstrating short-circuit evaluation:")
# The expensive_check(200) is not called because 150 < 100 is already False
result = 0 < 50 < 150 < 100 < expensive_check(200)
print(f"Result of chained comparison: {result}")
