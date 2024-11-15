def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
array = [1, 3, 4, 5, 7, 8, 9]
target = 5
result = binary_search(array, target)
print(f"Element found at index {result}" if result != -1 else "Element not found")
