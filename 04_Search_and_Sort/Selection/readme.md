# README.md
# Selection Sort Algorithm

## What is Selection Sort?
Selection Sort is a simple sorting algorithm that divides the input list into two parts: a sorted portion at the left end and an unsorted portion at the right end. The algorithm repeatedly selects the smallest element from the unsorted portion and adds it to the sorted portion.

## How Selection Sort Works
1. Find the minimum element in unsorted array
2. Swap it with the first element of unsorted part
3. Move the boundary between sorted and unsorted parts one element to the right
4. Repeat until array is sorted

## Visual Representation
```
Initial Array: [64, 25, 12, 22, 11]

First Pass:
[64, 25, 12, 22, 11] → Find minimum (11)
[11, 25, 12, 22, 64] → Swap with first element

Second Pass:
[11 | 25, 12, 22, 64] → Find minimum in unsorted part (12)
[11, 12, 25, 22, 64] → Swap with first unsorted element

Third Pass:
[11, 12 | 25, 22, 64] → Find minimum (22)
[11, 12, 22, 25, 64] → Swap

Fourth Pass:
[11, 12, 22 | 25, 64] → Find minimum (25)
[11, 12, 22, 25, 64] → Swap

Final Array: [11, 12, 22, 25, 64]
```

## Time Complexity
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)
- Space Complexity: O(1)

## Characteristics
1. In-place Algorithm: Only requires a constant amount O(1) of additional memory space
2. Simple Implementation: Easy to understand and implement
3. Unstable Sort: Does not preserve the relative order of equal elements
4. Number of Swaps: O(n) swaps - performs less swaps compared to Bubble Sort

## Advantages
1. Simple and easy to understand
2. Performs well on small arrays
3. Minimal memory usage (in-place sorting)
4. Performs minimum number of swaps (O(n) swaps)

## Disadvantages
1. Poor time complexity O(n²) for all cases
2. Not suitable for large datasets
3. Not stable - doesn't preserve relative order of equal elements
4. Performance doesn't improve for partially sorted arrays

## Use Cases
1. Small arrays where simplicity is preferred
2. When memory space is limited
3. When number of swaps needs to be minimized
4. Educational purposes
5. When stability is not required

---

# selection_sort.py

def selection_sort(arr):
    """
    Sort array using basic selection sort algorithm.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        list: Sorted array
        
    Time Complexity:
        Best/Average/Worst Case: O(n²)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def selection_sort_with_steps(arr):
    """
    Perform selection sort with detailed steps for educational purposes.
    
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
        steps.append(f"Current array: {arr}")
        
        # Find the minimum element in remaining unsorted array
        min_idx = i
        steps.append(f"Finding minimum element in unsorted portion {arr[i:]}")
        
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                steps.append(f"New minimum found: {arr[j]} at index {j}")
        
        # Swap the found minimum element with the first element
        if min_idx != i:
            steps.append(f"Swapping {arr[i]} with {arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append(f"Array after swap: {arr}")
        else:
            steps.append("No swap needed - minimum element already in position")
            
    steps.append(f"\nFinal sorted array: {arr}")
    return arr, steps

def selection_sort_reversed(arr):
    """
    Sort array in descending order using selection sort.
    
    Parameters:
        arr (list): Input array to sort
    
    Returns:
        list: Sorted array in descending order
    """
    n = len(arr)
    
    for i in range(n):
        # Find the maximum element in remaining unsorted array
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        # Swap the found maximum element with the first element
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    
    return arr

def find_k_smallest(arr, k):
    """
    Find the k smallest elements in the array using selection sort concept.
    
    Parameters:
        arr (list): Input array
        k (int): Number of smallest elements to find
    
    Returns:
        list: k smallest elements in sorted order
    """
    if k > len(arr):
        return sorted(arr)
        
    # Create a copy to avoid modifying original array
    temp_arr = arr.copy()
    result = []
    
    for i in range(k):
        min_idx = i
        for j in range(i+1, len(temp_arr)):
            if temp_arr[j] < temp_arr[min_idx]:
                min_idx = j
        temp_arr[i], temp_arr[min_idx] = temp_arr[min_idx], temp_arr[i]
        result.append(temp_arr[i])
    
    return result

# Example usage and test cases
if __name__ == "__main__":
    # Example 1: Basic sorting
    print("\nExample 1: Basic Sorting")
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr1 = selection_sort(arr1.copy())
    print(f"Original array: {arr1}")
    print(f"Sorted array: {sorted_arr1}")

    # Example 2: Already sorted array
    print("\nExample 2: Already Sorted Array")
    arr2 = [1, 2, 3, 4, 5]
    sorted_arr2 = selection_sort(arr2.copy())
    print(f"Original array: {arr2}")
    print(f"Sorted array: {sorted_arr2}")

    # Example 3: Reverse sorted array
    print("\nExample 3: Reverse Sorted Array")
    arr3 = [5, 4, 3, 2, 1]
    sorted_arr3 = selection_sort(arr3.copy())
    print(f"Original array: {arr3}")
    print(f"Sorted array: {sorted_arr3}")

    # Example 4: Array with duplicates
    print("\nExample 4: Array with Duplicates")
    arr4 = [64, 34, 25, 12, 22, 11, 90, 34]
    sorted_arr4 = selection_sort(arr4.copy())
    print(f"Original array: {arr4}")
    print(f"Sorted array: {sorted_arr4}")

    # Example 5: Sorting with steps
    print("\nExample 5: Sorting with Steps")
    arr5 = [64, 34, 25, 12]
    sorted_arr5, steps5 = selection_sort_with_steps(arr5.copy())
    print("Selection Sort Steps:")
    for step in steps5:
        print(step)

    # Example 6: Reverse sorting
    print("\nExample 6: Reverse Sorting")
    arr6 = [64, 34, 25, 12, 22, 11, 90]
    reverse_sorted_arr6 = selection_sort_reversed(arr6.copy())
    print(f"Original array: {arr6}")
    print(f"Reverse sorted array: {reverse_sorted_arr6}")

    # Example 7: Finding k smallest elements
    print("\nExample 7: Finding k Smallest Elements")
    arr7 = [64, 34, 25, 12, 22, 11, 90]
    k = 3
    k_smallest = find_k_smallest(arr7.copy(), k)
    print(f"Original array: {arr7}")
    print(f"{k} smallest elements: {k_smallest}")

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
Selection Sort Steps:
Initial array: [64, 34, 25, 12]
Pass 1:
Current array: [64, 34, 25, 12]
Finding minimum element in unsorted portion [64, 34, 25, 12]
New minimum found: 34 at index 1
New minimum found: 25 at index 2
New minimum found: 12 at index 3
Swapping 64 with 12
Array after swap: [12, 34, 25, 64]
...

Example 6: Reverse Sorting
Original array: [64, 34, 25, 12, 22, 11, 90]
Reverse sorted array: [90, 64, 34, 25, 22, 12, 11]

Example 7: Finding k Smallest Elements
Original array: [64, 34, 25, 12, 22, 11, 90]
3 smallest elements: [11, 12, 22]
"""