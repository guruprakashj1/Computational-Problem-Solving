Author: Guruprakash J  
Email: j_guruprakash@cb.amrita.edu  
Course: Computational Problem Solving - ver G

# What is a Keyword ? 
Keywords are the reserved words in Python. We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language. In Python, keywords are case sensitive.

# Python has total of 33 keywords.

1. False - This keyword is used to represent a false value.
2. None - This is a special constant used to denote a null value or a void.
3. True - This keyword is used to represent a true value.
4. and - This is a logical operator in python. It is used to combine two conditional statements.
5. as - This keyword is used to create an alias.
6. assert - This keyword is used for debugging purposes.
7. break - This keyword is used to terminate the loop or statement.
8. class - This keyword is used to declare a new class.
9. continue - This keyword is used to skip the current block, and return to the "for" or "while" statement.
10. def - This keyword is used to declare a new function.
11. del - This keyword is used to delete an object.
12. elif - This keyword is used in conditional statements.
13. else - This keyword is used in conditional statements.
14. except - This keyword is used with exceptions.
15. finally - This keyword is used to execute code, regardless of the result of the try and except blocks.
16. for - This keyword is used to create a for loop.
17. from - This keyword is used to import specific attributes or functions into the current namespace.
18. global - This keyword is used to declare that a variable inside the function is global.
19. if - This keyword is used to test a condition.
20. import - This keyword is used to import modules into the current namespace.
21. in - This keyword is used to check if a value is present in a sequence.
22. is - This keyword is used to test if two variables are equal.
23. lambda - This keyword is used to create an anonymous function.
24. nonlocal - This keyword works similar to the global keyword but rather than global, this keyword declares a variable to point to variables in the nearest enclosing scope.
25. not - This keyword is a logical operator.
26. or - This keyword is a logical operator.
27. pass - This keyword is used as a placeholder.
28. raise - This keyword is used to raise an exception.
29. return - This keyword is used to return a value from a function.
30. try - This keyword is used to start a try...except block.
31. while - This keyword is used to create a while loop.
32. with - This keyword is used to simplify exception handling.
33. yield - This keyword is used to end a function, returning a generator.

#Lets use a python code to list all the keywords in python

```python  
import keyword
print(keyword.kwlist)
```
