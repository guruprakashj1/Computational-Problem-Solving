# Iterable Files in Python

In Python, file objects are iterable, allowing you to process files line by line efficiently. This is particularly useful when working with large files.

## Key Features:
- Files can be opened in various modes (read, write, append, etc.).
- File objects can be iterated over to read lines.
- The `with` statement ensures proper file handling and closure.
- Files support methods like `read()`, `readline()`, and `write()`.

## Common Operations:
- Opening a file: `open(filename, mode)`
- Reading entire file: `file.read()`
- Reading line by line: `for line in file:`
- Writing to file: `file.write(string)`
- Closing file: `file.close()` (or use `with` statement)

## Use Cases:
- Reading and processing log files
- Parsing CSV or other structured text files
- Writing output or logs
- Data import/export operations

For more details and examples, refer to the sample program in this package.
