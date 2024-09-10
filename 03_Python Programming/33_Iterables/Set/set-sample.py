# set_operations.py

def demonstrate_set_operations():
    # Creating sets
    fruits = {"apple", "banana", "cherry"}
    citrus = {"orange", "lemon", "lime"}
    
    # Adding an element
    fruits.add("dragonfruit")
    print(f"Fruits after adding dragonfruit: {fruits}")
    
    # Removing an element
    fruits.remove("banana")
    print(f"Fruits after removing banana: {fruits}")
    
    # Union of two sets
    all_fruits = fruits.union(citrus)
    print(f"All fruits (union): {all_fruits}")
    
    # Intersection of two sets
    common_fruits = fruits.intersection(citrus)
    print(f"Common fruits (intersection): {common_fruits}")
    
    # Difference between sets
    unique_fruits = fruits.difference(citrus)
    print(f"Fruits unique to the fruits set (difference): {unique_fruits}")
    
    # Symmetric difference
    exclusive_fruits = fruits.symmetric_difference(citrus)
    print(f"Fruits in either set but not both (symmetric difference): {exclusive_fruits}")

if __name__ == "__main__":
    demonstrate_set_operations()

# Assignment:
# 1. Create a set of your favorite colors
# 2. Create another set of primary colors (red, blue, yellow)
# 3. Add a new color to your favorite colors set
# 4. Remove a color from your favorite colors set
# 5. Find the union of your favorite colors and primary colors
# 6. Find the difference between your favorite colors and primary colors
# 7. Check if a specific color is in your favorite colors set
