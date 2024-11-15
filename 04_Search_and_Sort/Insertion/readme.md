# README.md
# Insertion Sort Algorithm

## What is Insertion Sort?
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It works by iterating through the array and for each element, placing it in its correct position among the previously sorted elements.

## How Insertion Sort Works
1. Start with the first element (considered sorted)
2. Take next element and compare with sorted portion
3. Insert element in correct position in sorted portion
4. Repeat until all elements are sorted

## Visual Representation
```
Initial Array: [64, 34, 25, 12]

First Pass (element = 34):
[64 | 34, 25, 12] → Compare 34 with 64
[34, 64 | 25, 12] → Insert 34 before 64

Second Pass (element = 25):
[34, 64 | 25, 12] → Compare 25 with 64, then 34
[25, 34, 64 | 12] → Insert 25 before 34

Third Pass (element = 12):
[25, 34, 64 | 12] → Compare 12 with 64, 34, 25
[12, 25, 34, 64] → Insert 12 before 25

Final Array: [12, 25, 34, 64]
```

## Time Complexity
- Best Case: O(n) - Array already sorted
- Average Case: O(n²)
- Worst Case: O(n²) - Array sorted in reverse order
- Space Complexity: O(1)

## Characteristics
1. Stable Sort: Maintains relative order of equal elements
2. In-place Algorithm: Only requires constant amount O(1) of additional memory
3. Adaptive: Performance improves for partially sorted arrays
4. Online: Can sort a list as it receives it

## Advantages
1. Simple implementation
2. Efficient for small data sets
3. Adaptive - efficient for data sets already substantially sorted
4. Stable - maintains relative order of equal elements
5. In-place - only requires constant amount O(1) of additional memory
6. Online - can sort list as it receives it

## Disadvantages
1. Quadratic time complexity O(n²) in average and worst cases
2. Not suitable for large datasets
3. Generally performs worse than advanced algorithms like QuickSort

## Use Cases
1. Small datasets where simplicity is preferred
2. Nearly sorted arrays (very efficient in this case)
3. Online sorting (when receiving data in real-time)
4. When stable sorting is needed
5. When memory is limited

---

# insertion_sort.py

def insertion_sort(arr):
    """
    Sort array using basic insertion sort algorithm.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        list: Sorted array
        
    Time Complexity:
        Best Case: O(n)
        Average/Worst Case: O(n²)
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def insertion_sort_with_steps(arr):
    """
    Perform insertion sort with detailed steps for educational purposes.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        tuple: (sorted array, steps list)
    """
    steps = []
    steps.append(f"Initial array: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        steps.append(f"\nPass {i}:")
        steps.append(f"Current element to insert: {key}")
        steps.append(f"Sorted portion: {arr[:i]}, Unsorted portion: {arr[i:]}")
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            steps.append(f"Compare {key} with {arr[j]}")
            arr[j + 1] = arr[j]
            steps.append(f"Shift {arr[j]} right: {arr}")
            j -= 1
            
        arr[j + 1] = key
        steps.append(f"Insert {key} at position {j+1}: {arr}")
        
    steps.append(f"\nFinal sorted array: {arr}")
    return arr, steps

def insertion_sort_reversed(arr):
    """
    Sort array in descending order using insertion sort.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        list: Sorted array in descending order
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:  # Changed comparison operator
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def insertion_sort_recursive(arr, n):
    """
    Recursive implementation of insertion sort.
    
    Parameters:
        arr (list): Input array to sort
        n (int): Length of array
    
    Returns:
        list: Sorted array
    """
    # Base case
    if n <= 1:
        return arr
    
    # Sort first n-1 elements recursively
    insertion_sort_recursive(arr, n-1)
    
    # Insert last element at correct position in sorted array
    last = arr[n-1]
    j = n - 2
    
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last
    
    return arr

def binary_insertion_sort(arr):
    """
    Modified insertion sort using binary search to find insertion position.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        list: Sorted array
    """
    for i in range(1, len(arr)):
        key = arr[i]
        # Find location to insert using binary search
        j = binary_search(arr, key, 0, i-1)
        
        # Move all elements after location to create space
        arr[j+1:i+1] = arr[j:i]
        arr[j] = key
    
    return arr

def binary_search(arr, key, start, end):
    """
    Binary search to find insertion position.
    """
    if start >= end:
        if arr[start] > key:
            return start
        else:
            return start + 1
    
    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid - 1)
    else:
        return mid

# Example usage and test cases
if __name__ == "__main__":
    # Example 1: Basic sorting
    print("\nExample 1: Basic Sorting")
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr1 = insertion_sort(arr1.copy())
    print(f"Original array: {arr1}")
    print(f"Sorted array: {sorted_arr1}")

    # Example 2: Already sorted array
    print("\nExample 2: Already Sorted Array")
    arr2 = [1, 2, 3, 4, 5]
    sorted_arr2 = insertion_sort(arr2.copy())
    print(f"Original array: {arr2}")
    print(f"Sorted array: {sorted_arr2}")

    # Example 3: Reverse sorted array
    print("\nExample 3: Reverse Sorted Array")
    arr3 = [5, 4, 3, 2, 1]
    sorted_arr3 = insertion_sort(arr3.copy())
    print(f"Original array: {arr3}")
    print(f"Sorted array: {sorted_arr3}")

    # Example 4: Array with duplicates
    print("\nExample 4: Array with Duplicates")
    arr4 = [64, 34, 25, 12, 22, 11, 90, 34]
    sorted_arr4 = insertion_sort(arr4.copy())
    print(f"Original array: {arr4}")
    print(f"Sorted array: {sorted_arr4}")

    # Example 5: Sorting with steps
    print("\nExample 5: Sorting with Steps")
    arr5 = [64, 34, 25, 12]
    sorted_arr5, steps5 = insertion_sort_with_steps(arr5.copy())
    print("Insertion Sort Steps:")
    for step in steps5:
        print(step)

    # Example 6: Reverse sorting
    print("\nExample 6: Reverse Sorting")
    arr6 = [64, 34, 25, 12, 22, 11, 90]
    reverse_sorted_arr6 = insertion_sort_reversed(arr6.copy())
    print(f"Original array: {arr6}")
    print(f"Reverse sorted array: {reverse_sorted_arr6}")

    # Example 7: Recursive insertion sort
    print("\nExample 7: Recursive Insertion Sort")
    arr7 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr7 = insertion_sort_recursive(arr7.copy(), len(arr7))
    print(f"Original array: {arr7}")
    print(f"Sorted array: {sorted_arr7}")

    # Example 8: Binary insertion sort
    print("\nExample 8: Binary Insertion Sort")
    arr8 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr8 = binary_insertion_sort(arr8.copy())
    print(f"Original array: {arr8}")
    print(f"Sorted array: {sorted_arr8}")

# Sample Output:
"""
Example 1: Basic Sorting
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]

Example 2: Already Sorted Array
Original array: [1, 2, 3, 4, 5]
Sorted array: [1, 2, 3, 4, 5]

Example 3: Reverse Sorted Array
Original array: [5, 4, 3, 2, 1]
Sorted array: [1, 2, 3, 4, 5]

Example 4: Array with Duplicates
Original array: [64, 34, 25, 12, 22, 11, 90, 34]
Sorted array: [11, 12, 22, 25, 34, 34, 64, 90]

Example 5: Sorting with Steps
Insertion Sort Steps:
Initial array: [64, 34, 25, 12]
Pass 1:
Current element to insert: 34
Sorted portion: [64], Unsorted portion: [34, 25, 12]
Compare 34 with 64
Shift 64 right: [64, 64, 25, 12]
Insert 34 at position 0: [34, 64, 25, 12]
...

Example 6: Reverse Sorting
Original array: [64, 34, 25, 12, 22, 11, 90]
Reverse sorted array: [90, 64, 34, 25, 22, 12, 11]

Example 7: Recursive Insertion Sort
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]

Example 8: Binary Insertion Sort
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
"""