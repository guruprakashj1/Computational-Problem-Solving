# map_operations.py

def square(x):
    return x ** 2

def demonstrate_map_operations():
    # Using map with a built-in function
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(square, numbers)
    print(f"Squared numbers: {list(