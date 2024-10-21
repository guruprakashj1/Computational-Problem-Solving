""" Dictionary:

Create a dictionary of student grades and calculate the average.
Count the frequency of words in a sentence.
Merge two dictionaries.

Files:

Write to a file and read its contents.
Append to a file and read line by line.
Count words in a file.

List:

Create a list of squares of even numbers from 1 to 10.
Remove duplicates from a list while preserving order.
Flatten a nested list.

Map:

Use map to convert a list of temperatures from Celsius to Fahrenheit.
Use map with lambda to square each number in a list.
Use map with multiple iterables to add corresponding elements of two lists.

Set:

Find unique elements in two lists using sets.
Remove duplicates from a list using a set.
Find common elements in multiple lists using sets.

String:

Reverse words in a sentence.
Count vowels and consonants in a string.
Check if a string is a palindrome.

Tuple:

Create a list of tuples containing student names and their grades.
Unpack a tuple into variables.
Use a tuple as a dictionary key. """

# Exercise 1: Create a dictionary of student grades and calculate the average
def calculate_average_grade():
    # Initialize an empty dictionary to store student grades
    grades = {}
    
    # Input grades for 3 students
    for i in range(3):
        name = input(f"Enter student {i+1} name: ")
        grade = float(input(f"Enter {name}'s grade: "))
        grades[name] = grade  # Add the name-grade pair to the dictionary
    
    # Calculate the average grade
    average = sum(grades.values()) / len(grades)
    
    print("Grades:", grades)
    print(f"Average grade: {average:.2f}")

# Exercise 2: Count the frequency of words in a sentence
def word_frequency():
    sentence = input("Enter a sentence: ")
    words = sentence.lower().split()  # Convert to lowercase and split into words
    
    # Create a dictionary to store word frequencies
    freq_dict = {}
    
    # Count the frequency of each word
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1  # Increment count, default to 0 if not found
    
    print("Word frequencies:", freq_dict)

# Exercise 3: Merge two dictionaries
def merge_dictionaries():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    
    # Merge dict2 into dict1, updating existing keys
    merged = dict1.copy()  # Create a copy of dict1
    merged.update(dict2)   # Update with values from dict2
    
    print("Dict1:", dict1)
    print("Dict2:", dict2)
    print("Merged dictionary:", merged)

# Run the exercises
calculate_average_grade()
word_frequency()
merge_dictionaries()


# Exercise 1: Write to a file and read its contents
def write_and_read_file():
    # Write to a file
    with open("sample.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
    
    # Read from the file
    with open("sample.txt", "r") as file:
        contents = file.read()
    
    print("File contents:")
    print(contents)

# Exercise 2: Append to a file and read line by line
def append_and_read_lines():
    # Append to the file
    with open("sample.txt", "a") as file:
        file.write("This line is appended.\n")
    
    # Read the file line by line
    print("Reading line by line:")
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes leading/trailing whitespace

# Exercise 3: Count words in a file
def count_words_in_file():
    word_count = 0
    
    with open("sample.txt", "r") as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    
    print(f"Total number of words in the file: {word_count}")

# Run the exercises
write_and_read_file()
append_and_read_lines()
count_words_in_file()


# Exercise 1: Create a list of squares of even numbers from 1 to 10
def even_squares():
    squares = [x**2 for x in range(2, 11, 2)]  # List comprehension to create squares of even numbers
    print("Squares of even numbers from 1 to 10:", squares)

# Exercise 2: Remove duplicates from a list while preserving order
def remove_duplicates():
    original = [1, 2, 2, 3, 4, 3, 5, 6, 5, 7, 8, 8]
    
    unique = []
    seen = set()  # Use a set to keep track of seen elements
    
    for item in original:
        if item not in seen:
            seen.add(item)     # Add to set of seen elements
            unique.append(item)  # Append to unique list
    
    print("Original list:", original)
    print("List with duplicates removed:", unique)

# Exercise 3: Flatten a nested list
def flatten_list():
    nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    
    flattened = [item for sublist in nested for item in sublist]  # Nested list comprehension
    
    print("Nested list:", nested)
    print("Flattened list:", flattened)

# Run the exercises
even_squares()
remove_duplicates()
flatten_list()



# Exercise 1: Use map to convert a list of temperatures from Celsius to Fahrenheit
def celsius_to_fahrenheit():
    celsius = [0, 10, 20, 30, 40]
    
    # Define the conversion function
    def to_fahrenheit(c):
        return (c * 9/5) + 32
    
    # Use map to apply the conversion function to each temperature
    fahrenheit = list(map(to_fahrenheit, celsius))
    
    print("Celsius temperatures:", celsius)
    print("Fahrenheit temperatures:", fahrenheit)

# Exercise 2: Use map with lambda to square each number in a list
def square_numbers():
    numbers = [1, 2, 3, 4, 5]
    
    # Use map with a lambda function to square each number
    squared = list(map(lambda x: x**2, numbers))
    
    print("Original numbers:", numbers)
    print("Squared numbers:", squared)

# Exercise 3: Use map with multiple iterables to add corresponding elements of two lists
def add_lists():
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    
    # Use map to add corresponding elements
    sums = list(map(lambda x, y: x + y, list1, list2))
    
    print("List 1:", list1)
    print("List 2:", list2)
    print("Sums of corresponding elements:", sums)

# Run the exercises
celsius_to_fahrenheit()
square_numbers()
add_lists()



# Exercise 1: Find unique elements in two lists using sets
def unique_elements():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [5, 6, 7, 8, 9, 10]
    
    set1 = set(list1)
    set2 = set(list2)
    
    unique_to_list1 = set1 - set2  # Elements in set1 but not in set2
    unique_to_list2 = set2 - set1  # Elements in set2 but not in set1
    all_unique = unique_to_list1.union(unique_to_list2)  # All unique elements
    
    print("Unique to list1:", unique_to_list1)
    print("Unique to list2:", unique_to_list2)
    print("All unique elements:", all_unique)

# Exercise 2: Remove duplicates from a list using a set
def remove_duplicates():
    original = [1, 2, 2, 3, 4, 3, 5, 6, 5, 7, 8, 8]
    
    # Convert to set to remove duplicates, then back to list
    unique = list(set(original))
    
    print("Original list:", original)
    print("List with duplicates removed:", unique)

# Exercise 3: Find common elements in multiple lists using sets
def common_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    list3 = [5, 6, 7, 8, 9]
    
    # Convert lists to sets and find intersection
    common = set(list1).intersection(set(list2), set(list3))
    
    print("List 1:", list1)
    print("List 2:", list2)
    print("List 3:", list3)
    print("Common elements:", common)

# Run the exercises
unique_elements()
remove_duplicates()
common_elements()



# Exercise 1: Reverse words in a sentence
def reverse_words():
    sentence = "Python is an amazing programming language"
    
    # Split the sentence into words, reverse the list, and join back
    reversed_sentence = " ".join(sentence.split()[::-1])
    
    print("Original sentence:", sentence)
    print("Sentence with reversed words:", reversed_sentence)

# Exercise 2: Count vowels and consonants in a string
def count_vowels_consonants():
    text = "Hello, World!"
    vowels = "aeiouAEIOU"
    
    # Count vowels and consonants
    vowel_count = sum(1 for char in text if char.isalpha() and char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    
    print("Text:", text)
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)

# Exercise 3: Check if a string is a palindrome
def is_palindrome():
    def check_palindrome(s):
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]  # Compare with its reverse
    
    test_strings = ["A man, a plan, a canal: Panama", "race a car", "hello"]
    
    for string in test_strings:
        result = "is" if check_palindrome(string) else "is not"
        print(f"'{string}' {result} a palindrome")

# Run the exercises
reverse_words()
count_vowels_consonants()
is_palindrome()



# Exercise 1: Create a list of tuples containing student names and their grades
def student_grades():
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
    
    # Sort the list of tuples based on grades (descending order)
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    
    print("Original list of students and grades:", students)
    print("Sorted list (by grades, descending):", sorted_students)

# Exercise 2: Unpack a tuple into variables
def unpack_tuple():
    # Create a tuple with personal information
    person = ("John Doe", 30, "Software Developer", "New York")
    
    # Unpack the tuple into variables
    name, age, occupation, city = person
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Occupation: {occupation}")
    print(f"City: {city}")

# Exercise 3: Use a tuple as a dictionary key
def tuple_as_dict_key():
    # Create a dictionary with tuples as keys
    stock_prices = {
        ("AAPL", "2023-10-20"): 175.50,
        ("GOOGL", "2023-10-20"): 130.25,
        ("MSFT", "2023-10-20"): 330.75
    }
    
    # Access and print the stock prices
    for (symbol, date), price in stock_prices.items():
        print(f"Stock: {symbol}, Date: {date}, Price: ${price}")

    # Add a new entry
    stock_prices[("AMZN", "2023-10-20")] = 128.90
    
    print("\nUpdated stock prices:")
    for (symbol, date), price in stock_prices.items():
        print(f"Stock: {symbol}, Date: {date}, Price: ${price}")

# Run the exercises
student_grades()
unpack_tuple()
tuple_as_dict_key()