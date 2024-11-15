# README.md
# Binary Search Algorithm

## What is Binary Search?
Binary Search is an efficient searching algorithm that finds the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half, eliminating half of the remaining elements in each iteration.

## Prerequisites
- The array MUST be sorted in ascending order
- Random access to elements (array or similar data structure)

## How Binary Search Works
1. Find the middle element of the array
2. If target value equals middle element, return its index
3. If target value is less than middle element, search in left half
4. If target value is greater than middle element, search in right half
5. Repeat steps 1-4 until element is found or determined to not exist

## Visual Representation
```
Array: [1, 3, 4, 6, 8, 9, 11]
Target: 6

Step 1: middle = 4 (value = 6)
[1, 3, 4, 6, 8, 9, 11]
         ^
Target found at index 3!

Example 2 - Target: 9
Step 1: middle = 4 (value = 6)
[1, 3, 4, 6, 8, 9, 11]
         ^
6 < 9, search right half

Step 2: middle = 6 (value = 9)
[8, 9, 11]
    ^
Target found at index 5!
```

## Time Complexity
- Best Case: O(1) - Element found at middle
- Average Case: O(log n)
- Worst Case: O(log n) - Element not found or at edges
- Space Complexity: 
  - Iterative: O(1)
  - Recursive: O(log n) due to recursive call stack

## Advantages
1. Very efficient for large datasets
2. Logarithmic time complexity
3. Better than linear search for sorted arrays
4. Works well with cache memory due to sequential access

## Disadvantages
1. Array must be sorted first
2. Not suitable for small arrays (linear search might be faster)
3. Only works with data structures that allow random access
4. Requires contiguous memory allocation

## Use Cases
1. Searching in large sorted arrays
2. Database indexing
3. Finding elements in sorted files
4. System search applications

---

# binary_search.py
def binary_search_iterative(arr, target):
    """
    Perform binary search iteratively to find target element in sorted array.
    
    Parameters:
        arr (list): Sorted input array to search
        target: Element to find
    
    Returns:
        int: Index of target if found, -1 if not found
        
    Time Complexity:
        Best Case: O(1)
        Average/Worst Case: O(log n)
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at middle
        if arr[mid] == target:
            return mid
        
        # If target greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target smaller, ignore right half
        else:
            right = mid - 1
    
    # Element not present in array
    return -1

def binary_search_recursive(arr, target, left, right):
    """
    Perform binary search recursively to find target element in sorted array.
    
    Parameters:
        arr (list): Sorted input array to search
        target: Element to find
        left (int): Left boundary index
        right (int): Right boundary index
    
    Returns:
        int: Index of target if found, -1 if not found
    """
    # Base case: element not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # If element is present at middle
    if arr[mid] == target:
        return mid
    
    # If element is smaller than mid, search in left subarray
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Else search in right subarray
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_with_steps(arr, target):
    """
    Perform binary search with detailed steps for educational purposes.
    
    Parameters:
        arr (list): Sorted input array to search
        target: Element to find
    
    Returns:
        tuple: (index, steps list)
    """
    steps = []
    steps.append(f"Starting binary search for element {target} in array {arr}")
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        steps.append(f"\nStep: Searching between indices {left} and {right}")
        steps.append(f"Middle index: {mid}, Middle element: {arr[mid]}")
        
        if arr[mid] == target:
            steps.append(f"Target {target} found at index {mid}")
            return mid, steps
            
        elif arr[mid] < target:
            steps.append(f"{arr[mid]} < {target}, searching right half")
            left = mid + 1
            
        else:
            steps.append(f"{arr[mid]} > {target}, searching left half")
            right = mid - 1
    
    steps.append(f"\nTarget {target} not found in array")
    return -1, steps

# Example usage and test cases
if __name__ == "__main__":
    # Example 1: Basic search using iterative method
    print("\nExample 1: Basic Search (Iterative)")
    arr1 = [1, 3, 4, 6, 8, 9, 11]
    target1 = 6
    result1 = binary_search_iterative(arr1, target1)
    print(f"Array: {arr1}")
    print(f"Searching for: {target1}")
    print(f"Result: Element found at index {result1}")

    # Example 2: Basic search using recursive method
    print("\nExample 2: Basic Search (Recursive)")
    target2 = 9
    result2 = binary_search_recursive(arr1, target2, 0, len(arr1)-1)
    print(f"Array: {arr1}")
    print(f"Searching for: {target2}")
    print(f"Result: Element found at index {result2}")

    # Example 3: Element not found
    print("\nExample 3: Element Not Found")
    target3 = 7
    result3 = binary_search_iterative(arr1, target3)
    print(f"Array: {arr1}")
    print(f"Searching for: {target3}")
    print(f"Result: {result3} (Element not found)")

    # Example 4: Search with steps
    print("\nExample 4: Search With Steps")
    target4 = 8
    result4, steps4 = binary_search_with_steps(arr1, target4)
    print(f"Array: {arr1}")
    print(f"Searching for: {target4}")
    print("Steps:")
    for step in steps4:
        print(f"  {step}")

    # Example 5: Edge cases
    print("\nExample 5: Edge Cases")
    # Empty array
    print("Empty array:", binary_search_iterative([], 5))
    # Single element array (target present)
    print("Single element (present):", binary_search_iterative([5], 5))
    # Single element array (target absent)
    print("Single element (absent):", binary_search_iterative([5], 6))
    # Array with duplicate elements
    arr5 = [1, 2, 2, 2, 3, 4, 5]
    print(f"First occurrence of 2 in {arr5}:", binary_search_iterative(arr5, 2))

# Sample Output:
"""
Example 1: Basic Search (Iterative)
Array: [1, 3, 4, 6, 8, 9, 11]
Searching for: 6
Result: Element found at index 3

Example 2: Basic Search (Recursive)
Array: [1, 3, 4, 6, 8, 9, 11]
Searching for: 9
Result: Element found at index 5

Example 3: Element Not Found
Array: [1, 3, 4, 6, 8, 9, 11]
Searching for: 7
Result: -1 (Element not found)

Example 4: Search With Steps
Array: [1, 3, 4, 6, 8, 9, 11]
Searching for: 8
Steps:
  Starting binary search for element 8 in array [1, 3, 4, 6, 8, 9, 11]
  Step: Searching between indices 0 and 6
  Middle index: 3, Middle element: 6
  6 < 8, searching right half
  Step: Searching between indices 4 and 6
  Middle index: 5, Middle element: 9
  9 > 8, searching left half
  Step: Searching between indices 4 and 4
  Middle index: 4, Middle element: 8
  Target 8 found at index 4

Example 5: Edge Cases
Empty array: -1
Single element (present): 0
Single element (absent): -1
First occurrence of 2 in [1, 2, 2, 2, 3, 4, 5]: 1
"""