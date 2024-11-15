# README.md
# Bubble Sort Algorithm

## What is Bubble Sort?
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no more swaps are needed (list is sorted).

## How Bubble Sort Works
1. Start with first element
2. Compare adjacent elements
3. Swap if they are in wrong order
4. Move to next pair
5. Repeat steps 2-4 until end of list
6. Repeat steps 1-5 until no swaps needed

## Visual Representation
```
Initial Array: [64, 34, 25, 12]

First Pass:
[64, 34, 25, 12] → Compare 64, 34
[34, 64, 25, 12] → Swap, Compare 64, 25
[34, 25, 64, 12] → Swap, Compare 64, 12
[34, 25, 12, 64] → Swap

Second Pass:
[34, 25, 12, 64] → Compare 34, 25
[25, 34, 12, 64] → Swap, Compare 34, 12
[25, 12, 34, 64] → Swap

Third Pass:
[25, 12, 34, 64] → Compare 25, 12
[12, 25, 34, 64] → Swap

Fourth Pass:
[12, 25, 34, 64] → No swaps needed (Sorted!)
```

## Time Complexity
- Best Case: O(n) - Array already sorted
- Average Case: O(n²)
- Worst Case: O(n²) - Array sorted in reverse order
- Space Complexity: O(1) - Only uses a constant amount of extra space

## Characteristics
1. Stable Sorting: Maintains relative order of equal elements
2. In-place Algorithm: Only requires constant amount of extra memory
3. Adaptive: Performance improves for partially sorted arrays
4. Simple Implementation: Easy to understand and code

## Advantages
1. Simple to understand and implement
2. No extra memory needed (in-place sorting)
3. Stable sorting algorithm
4. Adaptive - efficient for data that is already substantially sorted

## Disadvantages
1. Poor time complexity of O(n²)
2. Not suitable for large datasets
3. More swaps compared to other algorithms

## Use Cases
1. Educational purposes (teaching sorting concepts)
2. Small datasets where simplicity is preferred
3. Detecting whether a list is sorted or not
4. When stable sorting is needed
5. When memory usage is a concern

---

# bubble_sort.py

def bubble_sort(arr):
    """
    Sort array using basic bubble sort algorithm.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        list: Sorted array
        
    Time Complexity:
        Best Case: O(n)
        Average/Worst Case: O(n²)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize if no swapping occurs
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

def bubble_sort_with_steps(arr):
    """
    Perform bubble sort with detailed steps for educational purposes.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        tuple: (sorted array, steps list)
    """
    steps = []
    steps.append(f"Initial array: {arr}")
    
    n = len(arr)
    
    for i in range(n):
        steps.append(f"\nPass {i+1}:")
        swapped = False
        
        for j in range(0, n-i-1):
            steps.append(f"  Compare {arr[j]} and {arr[j+1]}")
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                steps.append(f"  Swap: {arr}")
            else:
                steps.append(f"  No swap needed: {arr}")
        
        if not swapped:
            steps.append("  Array is sorted!")
            break
            
    return arr, steps

def bubble_sort_reversed(arr):
    """
    Sort array in descending order using bubble sort.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        list: Sorted array in descending order
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:  # Changed comparison operator
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

# Example usage and test cases
if __name__ == "__main__":
    # Example 1: Basic sorting
    print("\nExample 1: Basic Sorting")
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr1 = bubble_sort(arr1.copy())
    print(f"Original array: {arr1}")
    print(f"Sorted array: {sorted_arr1}")

    # Example 2: Already sorted array
    print("\nExample 2: Already Sorted Array")
    arr2 = [1, 2, 3, 4, 5]
    sorted_arr2 = bubble_sort(arr2.copy())
    print(f"Original array: {arr2}")
    print(f"Sorted array: {sorted_arr2}")

    # Example 3: Reverse sorted array
    print("\nExample 3: Reverse Sorted Array")
    arr3 = [5, 4, 3, 2, 1]
    sorted_arr3 = bubble_sort(arr3.copy())
    print(f"Original array: {arr3}")
    print(f"Sorted array: {sorted_arr3}")

    # Example 4: Array with duplicates
    print("\nExample 4: Array with Duplicates")
    arr4 = [64, 34, 25, 12, 22, 11, 90, 34]
    sorted_arr4 = bubble_sort(arr4.copy())
    print(f"Original array: {arr4}")
    print(f"Sorted array: {sorted_arr4}")

    # Example 5: Sorting with steps
    print("\nExample 5: Sorting with Steps")
    arr5 = [64, 34, 25, 12]
    sorted_arr5, steps5 = bubble_sort_with_steps(arr5.copy())
    print("Bubble Sort Steps:")
    for step in steps5:
        print(step)

    # Example 6: Reverse sorting
    print("\nExample 6: Reverse Sorting")
    arr6 = [64, 34, 25, 12, 22, 11, 90]
    reverse_sorted_arr6 = bubble_sort_reversed(arr6.copy())
    print(f"Original array: {arr6}")
    print(f"Reverse sorted array: {reverse_sorted_arr6}")

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
Bubble Sort Steps:
Initial array: [64, 34, 25, 12]
Pass 1:
  Compare 64 and 34
  Swap: [34, 64, 25, 12]
  Compare 64 and 25
  Swap: [34, 25, 64, 12]
  Compare 64 and 12
  Swap: [34, 25, 12, 64]
...

Example 6: Reverse Sorting
Original array: [64, 34, 25, 12, 22, 11, 90]
Reverse sorted array: [90, 64, 34, 25, 22, 12, 11]
"""