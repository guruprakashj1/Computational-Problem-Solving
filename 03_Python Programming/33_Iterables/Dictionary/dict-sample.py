# dictionary_operations.py

def demonstrate_dictionary_operations():
    # Creating a dictionary
    person = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    print(f"Original dictionary: {person}")
    
    # Adding a new key-value pair
    person["occupation"] = "Engineer"
    print(f"After adding occupation: {person}")
    
    # Updating a value
    person["age"] = 31
    print(f"After updating age: {person}")
    
    # Accessing a value
    print(f"Name: {person['name']}")
    
    # Accessing with get() (provides a default value if key doesn't exist)
    print(f"Country: {person.get('country', 'Unknown')}")
    
    # Removing a key-value pair
    removed_city = person.pop("city")
    print(f"Removed city: {removed_city}")
    print(f"After removing city: {person}")
    
    # Getting all keys
    print(f"Keys: {list(person.keys())}")
    
    # Getting all values
    print(f"Values: {list(person.values())}")
    
    # Getting all key-value pairs
    print(f"Items: {list(person.items())}")
    
    # Dictionary comprehension
    squared_numbers = {x: x**2 for x in range(5)}
    print(f"Squared numbers: {squared_numbers}")

if __name__ == "__main__":
    demonstrate_dictionary_operations()

# Assignment:
# 1. Create a dictionary representing a book (title, author, year, etc.)
# 2. Add a new key-value pair for the book's genre
# 3. Update the year of publication
# 4. Print the author of the book
# 5. Try to access a key that doesn't exist using the get() method with a default value
# 6. Remove the year from the dictionary and print the removed value
# 7. Create a list of all the keys in the dictionary
# 8. Create a dictionary comprehension that takes the original book dictionary and creates a new one with all values capitalized (if they're strings)
