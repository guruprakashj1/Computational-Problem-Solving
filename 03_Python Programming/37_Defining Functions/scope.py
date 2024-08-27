# 8- Scope
# Author: Guruprakash J
# Email: j_guruprakash@cb.amrita.edu
# Course: Computational Problem Solving - ver G

# This program demonstrates various aspects of scope in Python

# Global variable
global_var = "I'm a global variable"

def demonstrate_local_scope():
    """Function demonstrating local scope"""
    local_var = "I'm a local variable"
    print(local_var)  # Accessing local variable
    print(global_var)  # Accessing global variable

print("1. Local and Global Scope:")
demonstrate_local_scope()
# print(local_var)  # This would raise a NameError as local_var is not accessible here
print()

def modify_global_variable():
    """Function demonstrating the use of the global keyword"""
    global global_var
    global_var = "I'm a modified global variable"
    print(global_var)

print("2. Modifying Global Variable:")
print("Before modification:", global_var)
modify_global_variable()
print("After modification:", global_var)
print()

def outer_function():
    """Function demonstrating enclosing scope"""
    outer_var = "I'm in the outer function"
    
    def inner_function():
        print("Inner function:", outer_var)  # Accessing variable from enclosing scope
    
    inner_function()
    print("Outer function:", outer_var)

print("3. Enclosing Scope:")
outer_function()
print()

def demonstrate_nonlocal():
    """Function demonstrating the use of the nonlocal keyword"""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        print("Inside increment:", count)
    
    increment()
    print("After increment:", count)

print("4. Nonlocal Keyword:")
demonstrate_nonlocal()
print()

print("5. Built-in Scope:")
print("Length of 'Python':", len("Python"))  # Using built-in function len()

def len(x):
    """Function shadowing the built-in len() function"""
    return "Custom len function"

print("Custom len function:", len("Python"))  # Using custom len() function
print()

def demonstrate_name_resolution():
    """Function demonstrating name resolution order"""
    x = "local"
    print("x from local scope:", x)
    
    def inner():
        x = "enclosing"
        print("x from enclosing scope:", x)
    
    inner()

x = "global"
print("6. Name Resolution:")
print("x from global scope:", x)
demonstrate_name_resolution()
print()

# This program covers various aspects of scope in Python,
# demonstrating local, global, enclosing, and built-in scopes,
# as well as the use of global and nonlocal keywords.
