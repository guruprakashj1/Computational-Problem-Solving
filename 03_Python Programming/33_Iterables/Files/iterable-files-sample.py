# iterable_files.py

def demonstrate_iterable_files():
    # 1. Writing to a file
    print("1. Writing to a file:")
    with open("sample.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("Python is awesome.\n")
        file.write("File handling is easy.\n")
    print("File 'sample.txt' created and written to.")

    # 2. Reading entire file
    print("\n2. Reading entire file:")
    with open("sample.txt", "r") as file:
        content = file.read()
        print(f"File contents:\n{content}")

    # 3. Reading file line by line
    print("\n3. Reading file line by line:")
    with open("sample.txt", "r") as file:
        for line in file:
            print(f"Line: {line.strip()}")

    # 4. Reading lines into a list
    print("\n4. Reading lines into a list:")
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print(f"Lines as list: {lines}")

    # 5. Writing multiple lines at once
    print("\n5. Writing multiple lines at once:")
    lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
    with open("sample.txt", "a") as file:
        file.writelines(lines_to_write)
    print("Additional lines appended to 'sample.txt'")

    # 6. Reading with context
    print("\n6. Reading with context:")
    with open("sample.txt", "r") as file:
        print(f"First line: {next(file).strip()}")
        print(f"Second line: {next(file).strip()}")

if __name__ == "__main__":
    demonstrate_iterable_files()

# Assignment:
# 1. Write a function that reads a text file and returns the number of words in it.
# 2. Create a program that reads a CSV file and calculates the average of a specific column.
# 3. Implement a function that takes two file names as input and merges their contents into a third file.
# 4. Write a program that reads a log file and extracts all lines containing a specific keyword.
# 5. Create a function that reads a text file, reverses each line, and writes the result to a new file.
