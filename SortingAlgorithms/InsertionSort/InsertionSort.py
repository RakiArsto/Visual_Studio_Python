﻿import random

# ✦ We start with second element of the array as first element in the array is assumed to be sorted.
# ✦ Compare second element with the first element and check if the second element is smaller then 
# swap them.
# ✦ Move to the third element and compare it with the second element, then the first element and 
# swap as necessary to put it in the correct position among the first three elements.
# ✦ Continue this process, comparing each element with the ones before it and swapping as needed 
# to place it in the correct position among the sorted elements.
# ✦ Repeat until the entire array is sorted.

def InsertionSort(arr):
    """Insertion sort is a simple sorting algorithm that works by building a sorted array one element 
    at a time. It is considered an ” in-place ” sorting algorithm, meaning it doesn’t require any 
    additional memory space beyond the original array."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

number = int(input("Enter the number of elements: "))
list = random.sample(range(1, 101), number)
print(f"Original list: {list}")
print(f"Sorted list using Insertion sort: {InsertionSort(list)}")