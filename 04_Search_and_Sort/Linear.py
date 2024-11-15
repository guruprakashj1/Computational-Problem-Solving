def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
array = [3, 1, 4, 7, 5]
target = 7
result = linear_search(array, target)
print(f"Element found at index {result}" if result != -1 else "Element not found")
