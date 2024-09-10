# iterable_strings.py

def demonstrate_iterable_strings():
    # Sample string
    text = "Python"

    # 1. Accessing individual characters
    print("1. Accessing individual characters:")
    print(f"First character: {text[0]}")
    print(f"Last character: {text[-1]}")

    # 2. Slicing
    print("\n2. Slicing:")
    print(f"First three characters: {text[:3]}")
    print(f"Last three characters: {text[-3:]}")
    print(f"Reverse string: {text[::-1]}")

    # 3. Iteration
    print("\n3. Iteration:")
    for char in text:
        print(f"Character: {char}")

    # 4. String methods
    print("\n4. String methods:")
    print(f"Uppercase: {text.upper()}")
    print(f"Character count: {text.count('n')}")

    # 5. String manipulation
    print("\n5. String manipulation:")
    words = "  Hello,  World!  "
    print(f"Original: '{words}'")
    print(f"Stripped: '{words.strip()}'")
    print(f"Split: {words.split()}")

    # 6. Character check
    print("\n6. Character check:")
    print(f"Is 'Python' alphanumeric? {'Python'.isalnum()}")
    print(f"Is '123' numeric? {'123'.isnumeric()}")

if __name__ == "__main__":
    demonstrate_iterable_strings()

# Assignment:
# 1. Write a function that counts the number of vowels in a given string.
# 2. Create a function that reverses words in a sentence without reversing the characters in each word.
# 3. Implement a function that checks if a string is a palindrome (reads the same forwards and backwards).
# 4. Write a program that removes all duplicate characters from a string while preserving the order.
# 5. Create a function that converts snake_case strings to camelCase.
