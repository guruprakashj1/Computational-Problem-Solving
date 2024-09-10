# list_operations.py

def demonstrate_list_operations():
    # Creating a list
    fruits = ["apple", "banana", "cherry"]
    print(f"Original list: {fruits}")
    
    # Appending an element
    fruits.append("dragonfruit")
    print(f"After appending dragonfruit: {fruits}")
    
    # Inserting an element at a specific position
    fruits.insert(1, "blueberry")
    print(f"After inserting blueberry at index 1: {fruits}")
    
    # Removing an element
    fruits.remove("cherry")
    print(f"After removing cherry: {fruits}")
    
    # Accessing elements
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    
    # Slicing
    print(f"First two fruits: {fruits[:2]}")
    
    # List comprehension
    uppercase_fruits = [fruit.upper() for fruit in fruits]
    print(f"Uppercase fruits: {uppercase_fruits}")
    
    # Sorting
    fruits.sort()
    print(f"Sorted fruits: {fruits}")
    
    # Reversing
    fruits.reverse()
    print(f"Reversed fruits: {fruits}")

if __name__ == "__main__":
    demonstrate_list_operations()

# Assignment:
# 1. Create a list of your favorite movies
# 2. Add a new movie to the end of the list
# 3. Insert a movie at the beginning of the list
# 4. Remove a movie from the list
# 5. Print the movie at index 2
# 6. Create a new list with the first three movies
# 7. Create a list of the lengths of each movie title using list comprehension
# 8. Sort the list of movies alphabetically
# 9. Reverse the order of the list
