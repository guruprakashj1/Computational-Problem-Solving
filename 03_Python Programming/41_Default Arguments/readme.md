# 5- Default Arguments

## Author Details
- **Name:** Guruprakash J
- **Email:** j_guruprakash@cb.amrita.edu
- **Course:** Computational Problem Solving - ver G

## Overview
Default arguments in Python allow you to specify default values for function parameters. This feature enhances function flexibility, making it easier to use functions with fewer arguments while still providing the option to customize behavior when needed.

## Key Concepts

1. **Basic Syntax:**
   ```python
   def function_name(param1, param2=default_value):
       # function body
   ```

2. **Purpose:**
   - Provide default values for parameters
   - Make functions more flexible and easier to use
   - Allow optional parameters

3. **Order of Parameters:**
   - Parameters with default values must come after parameters without default values

4. **Overriding Default Values:**
   - Default values can be overridden by providing a value when calling the function

5. **Mutable Default Arguments:**
   - Be cautious when using mutable objects (like lists or dictionaries) as default arguments
   - Mutable default arguments are created only once, at function definition time

6. **Dynamic Default Values:**
   - Use `None` as a sentinel value for default arguments that should be computed dynamically

7. **Default Arguments and Keyword Arguments:**
   - Often used together to create flexible function interfaces

8. **Documentation:**
   - Always document default argument values in function docstrings

## Best Practices

1. Use immutable objects for default argument values when possible
2. Use `None` as a default value for arguments that should be mutable or dynamically created
3. Be aware of the "mutable default argument" pitfall
4. Keep default arguments simple and intuitive
5. Use default arguments to make the most common use case the easiest

## Common Pitfalls

1. **Mutable Default Arguments:**
   ```python
   def add_item(item, list=[]):  # Problematic
       list.append(item)
       return list
   ```
   This can lead to unexpected behavior as the list is created only once.

2. **Late Binding:**
   Be aware that default argument values are evaluated at function definition time, not at call time.

## Conclusion

Default arguments are a powerful feature in Python that, when used correctly, can greatly enhance the usability and flexibility of your functions. Understanding how to use them effectively, along with their potential pitfalls, is crucial for writing robust and user-friendly Python code.
