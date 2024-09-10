# tuple_operations.py

def demonstrate_tuple_operations():
    # Creating a tuple
    coordinates = (3, 4)
    print(f"Original tuple: {coordinates}")
    
    # Accessing elements
    x, y = coordinates
    print(f"X: {x}, Y: {y}")
    
    # Attempting to modify a tuple (will raise an error)
    try:
        coordinates[0] = 5
    except TypeError as e:
        print(f"Error when trying to modify tuple: {e}")
    
    # Creating a tuple with different data types
    mixed_tuple = (1, "hello", 3.14, [1, 2, 3])
    print(f"Mixed tuple: {mixed_tuple}")
    
    # Accessing elements using index
    print(f"Second element: {mixed_tuple[1]}")
    
    # Slicing
    print(f"First two elements: {mixed_tuple[:2]}")
    
    # Tuple concatenation
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    concatenated = tuple1 + tuple2
    print(f"Concatenated tuple: {concatenated}")
    
    # Tuple repetition
    repeated = tuple1 * 3
    print(f"Repeated tuple: {repeated}")
    
    # Tuple unpacking
    a, b, c = tuple1
    print(f"Unpacked values: a={a}, b={b}, c={c}")
    
    # Using tuples as dictionary keys
    tuple_dict = {(0, 0): "Origin", (1, 0): "Right", (0, 1): "Up"}
    print(f"Dictionary with tuple keys: {tuple_dict}")

if __name__ == "__main__":
    demonstrate_tuple_operations()

# Assignment:
# 1. Create a tuple of your favorite colors
# 2. Access and print the second color in the tuple
# 3. Try to modify one of the colors in the tuple (this will raise an error)
# 4. Create a new tuple by concatenating your color tuple with another tuple containing some new colors
# 5. Create a tuple of tuples representing points on a 2D plane: ((0, 0), (1, 2), (3, 4))
# 6. Unpack the second point from your tuple of tuples and print its x and y coordinates
# 7. Create a dictionary where the keys are tuples representing dates (year, month, day) and the values are events happening on those dates
# 8. Use tuple slicing to get the first two points from your tuple of points
