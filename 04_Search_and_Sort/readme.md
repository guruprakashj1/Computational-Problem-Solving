# README - Sorting and Searching Algorithms

This repository contains Python implementations of some basic searching and sorting algorithms: Linear Search, Binary Search, Bubble Sort, Selection Sort, and Insertion Sort. These are fundamental algorithms often used for educational purposes to understand the basics of data structures and algorithms.

## Algorithms Included

### 1. Linear Search
**Definition**: Linear Search is a simple search algorithm that checks every element in the array sequentially until the target element is found or the list ends.

**Key Features**:
- **Simplest searching algorithm**: Searches sequentially through the array.
- **Unsorted data**: Works well with small arrays or unsorted data.
- **Time Complexity**: O(n) in the worst case.

### 2. Binary Search
**Definition**: Binary Search is an efficient algorithm for finding an item from a sorted list of elements by repeatedly dividing the search interval in half.

**Key Features**:
- **Efficient for sorted arrays**: Requires the input array to be sorted.
- **Divide and conquer**: Divides the search interval in half each time.
- **Time Complexity**: O(log n) in the worst case.

### 3. Bubble Sort
**Definition**: Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

**Key Features**:
- **Simple sorting algorithm**: Repeatedly swaps adjacent elements if they are in the wrong order.
- **Educational value**: Good for educational purposes and small datasets.
- **Time Complexity**: O(n^2) in the worst case.

### 4. Selection Sort
**Definition**: Selection Sort is a sorting algorithm that divides the array into a sorted and an unsorted region, repeatedly selecting the smallest (or largest) element from the unsorted region and moving it to the sorted region.

**Key Features**:
- **Divides array into sorted/unsorted regions**: Finds the minimum element in the unsorted region and moves it to the sorted region.
- **Stable sorting**: It preserves the order of equal elements.
- **Time Complexity**: O(n^2) in the worst case.

### 5. Insertion Sort
**Definition**: Insertion Sort is a sorting algorithm that builds the final sorted array one item at a time, with the ability to place each item in its proper location.

**Key Features**:
- **Builds sorted array incrementally**: Builds the final sorted array one item at a time.
- **Adaptive**: Works well with small datasets and nearly sorted arrays.
- **Time Complexity**: O(n^2) in the worst case.

## Usage
Each algorithm is implemented as a standalone Python function. You can run any of the algorithms by simply importing the relevant function and passing an array as the input. Below is an example of using the Bubble Sort algorithm:

```python
from sorting_algorithms import bubble_sort

array = [5, 1, 4, 2, 8]
bubble_sort(array)
print("Sorted array:", array)
```

## Requirements
- Python 3.x

## Running the Code
To run the code, make sure you have Python 3 installed. Simply run the Python file containing the algorithm of interest.

```bash
python linear_search.py
```

## License
This project is licensed under the MIT License.

