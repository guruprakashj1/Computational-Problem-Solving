# Python Dictionaries

A dictionary in Python is an unordered collection of key-value pairs. It is also known as an associative array, hash table, or hash map in other programming languages.

## Key Features:
- Key-Value Pairs: Each item in a dictionary consists of a key and its corresponding value.
- Unordered: As of Python 3.7+, dictionaries maintain insertion order, but they are still considered unordered.
- Mutable: Dictionaries can be modified after creation (add, remove, or change key-value pairs).
- Keys must be unique and immutable: Typically strings, numbers, or tuples.
- Values can be of any type: Including other dictionaries or complex objects.

## Common Operations:
- Creation: `{}` or `dict()`
- Adding/Updating key-value pair: `dict[key] = value`
- Accessing value: `dict[key]` or `dict.get(key)`
- Removing key-value pair: `del dict[key]` or `dict.pop(key)`
- Getting all keys: `dict.keys()`
- Getting all values: `dict.values()`
- Getting all key-value pairs: `dict.items()`

## Use Cases:
- Storing related information
- Fast lookup of values based on unique keys
- Representing structured data (e.g., JSON-like data)

For more details and examples, refer to the sample program in this package.
