# README.md
# Linear Search Algorithm

## What is Linear Search?
Linear Search (also known as Sequential Search) is the simplest searching algorithm that finds the position of a target value within a list or array. It sequentially checks each element in the list until a match is found or the whole list has been searched.

## How Linear Search Works
1. Start from the leftmost element of the array
2. Compare each element with the target value
3. If the element matches the target value, return its index
4. If the element doesn't match, move to the next element
5. If no match is found after checking all elements, return -1

## Characteristics
- Simple and easy to implement
- No pre-requisites (works with sorted and unsorted arrays)
- Good for small arrays
- Memory usage is constant

## Time Complexity
- Best Case: O(1) - Element found at first position
- Average Case: O(n/2) - Element found at middle position
- Worst Case: O(n) - Element found at last position or not found
- Space Complexity: O(1) - No extra space needed

## Advantages
1. Simple to understand and implement
2. No preprocessing required (works with unsorted data)
3. Works with any data type that supports equality comparison
4. Doesn't require the array to be sorted
5. Good for small datasets

## Disadvantages
1. Slow for large datasets
2. Not suitable for large arrays
3. Less efficient compared to other search algorithms like Binary Search

## Use Cases
1. Searching in small arrays
2. When array is unsorted and searching needs to be done only once
3. When simplicity is preferred over efficiency
4. When array elements are being modified frequently

---

# linear_search.py
def linear_search(arr, target):
    """
    Perform linear search to find the target element in an array.
    
    Parameters:
        arr (list): The input array to search through
        target: The element to find
    
    Returns:
        int: Index of target if found, -1 if not found
        
    Time Complexity:
        Best Case: O(1)
        Average Case: O(n/2)
        Worst Case: O(n)
    """
    # Iterate through array indices
    for i in range(len(arr)):
        # If element is found, return its index
        if arr[i] == target:
            return i
    
    # If element is not found, return -1
    return -1

def linear_search_with_steps(arr, target):
    """
    Perform linear search with detailed steps for educational purposes.
    
    Parameters:
        arr (list): The input array to search through
        target: The element to find
    
    Returns:
        tuple: (index, steps list)
    """
    steps = []
    steps.append(f"Starting search for element {target} in array {arr}")
    
    for i in range(len(arr)):
        steps.append(f"Step {i+1}: Checking index {i}, value {arr[i]}")
        
        if arr[i] == target:
            steps.append(f"Element {target} found at index {i}")
            return i, steps
            
        steps.append(f"Element at index {i} doesn't match, moving to next element")
    
    steps.append(f"Element {target} not found in array")
    return -1, steps

def find_all_occurrences(arr, target):
    """
    Find all occurrences of target element in array.
    
    Parameters:
        arr (list): The input array to search through
        target: The element to find
    
    Returns:
        list: List of indices where target was found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

# Example usage and test cases
if __name__ == "__main__":
    # Example 1: Basic search
    print("\nExample 1: Basic Search")
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    target1 = 12
    result1 = linear_search(arr1, target1)
    print(f"Array: {arr1}")
    print(f"Searching for: {target1}")
    print(f"Result: Element found at index {result1}")

    # Example 2: Element not found
    print("\nExample 2: Element Not Found")
    target2 = 50
    result2 = linear_search(arr1, target2)
    print(f"Array: {arr1}")
    print(f"Searching for: {target2}")
    print(f"Result: {result2} (Element not found)")

    # Example 3: Search with steps
    print("\nExample 3: Search With Steps")
    arr3 = [10, 20, 30, 40, 50]
    target3 = 30
    result3, steps3 = linear_search_with_steps(arr3, target3)
    print(f"Array: {arr3}")
    print(f"Searching for: {target3}")
    print("Steps:")
    for step in steps3:
        print(f"  {step}")

    # Example 4: Multiple occurrences
    print("\nExample 4: Multiple Occurrences")
    arr4 = [10, 20, 10, 30, 40, 10, 50]
    target4 = 10
    result4 = find_all_occurrences(arr4, target4)
    print(f"Array: {arr4}")
    print(f"Searching for: {target4}")
    print(f"Found at indices: {result4}")

    # Example 5: Different data types
    print("\nExample 5: Different Data Types")
    arr5 = ["apple", "banana", "orange", "grape"]
    target5 = "orange"
    result5 = linear_search(arr5, target5)
    print(f"Array: {arr5}")
    print(f"Searching for: {target5}")
    print(f"Result: Element found at index {result5}")

# Sample Output:
"""
Example 1: Basic Search
Array: [64, 34, 25, 12, 22, 11, 90]
Searching for: 12
Result: Element found at index 3

Example 2: Element Not Found
Array: [64, 34, 25, 12, 22, 11, 90]
Searching for: 50
Result: -1 (Element not found)

Example 3: Search With Steps
Array: [10, 20, 30, 40, 50]
Searching for: 30
Steps:
  Starting search for element 30 in array [10, 20, 30, 40, 50]
  Step 1: Checking index 0, value 10
  Element at index 0 doesn't match, moving to next element
  Step 2: Checking index 1, value 20
  Element at index 1 doesn't match, moving to next element
  Step 3: Checking index 2, value 30
  Element 30 found at index 2

Example 4: Multiple Occurrences
Array: [10, 20, 10, 30, 40, 10, 50]
Searching for: 10
Found at indices: [0, 2, 5]

Example 5: Different Data Types
Array: ['apple', 'banana', 'orange', 'grape']
Searching for: orange
Result: Element found at index 2
"""