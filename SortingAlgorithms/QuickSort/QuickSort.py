import random

# ✦ Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary 
# (e.g., first element, last element, random element, or median).
# ✦ Partition the Array: Rearrange the array around the pivot. After partitioning, all elements 
# smaller than the pivot will be on its left, and all elements greater than the pivot will be on 
# its right. The pivot is then in its correct position, and we obtain the index of the pivot.
# ✦ Recursively Call: Recursively apply the same process to the two partitioned sub-arrays 
# (left and right of the pivot).
# ✦ Base Case: The recursion stops when there is only one element left in the sub-array, as 
# a single element is already sorted.

def QuickSort(arr):
    """QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element 
    as a pivot and partitions the given array around the picked pivot by placing the pivot in 
    its correct position in the sorted array."""
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return QuickSort(less) + [pivot] + QuickSort(greater)

number = int(input("Enter the number of elements: "))
list = random.sample(range(1, 101), number)
print(f"Original list: {list}")
print(f"Sorted list using Quick sort: {QuickSort(list)}")