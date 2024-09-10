# Python Tuples

A tuple in Python is an ordered, immutable sequence of elements. Tuples are similar to lists, but they cannot be changed once created.

## Key Features:
- Ordered: Elements in a tuple have a defined order, and that order will not change.
- Immutable: Once a tuple is created, you cannot add, remove, or modify its elements.
- Allow Duplicates: You can have multiple identical elements in a tuple.
- Indexed: Elements can be accessed by their position in the tuple.

## Common Operations:
- Creation: `()` or `tuple()`
- Accessing elements: Using index `tuple[index]`
- Slicing: `tuple[start:end]`
- Concatenation: `tuple1 + tuple2`
- Repetition: `tuple * n`
- Unpacking: `a, b, c = tuple`

## Use Cases:
- Representing fixed collections of items
- Returning multiple values from a function
- Dictionary keys (when you need an immutable sequence)
- Data that shouldn't be modified

For more details and examples, refer to the sample program in this package.
