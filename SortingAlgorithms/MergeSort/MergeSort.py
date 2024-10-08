import random

# ✦ Divide: Divide the list or array recursively into two halves until it can no more be divided.
# ✦ Conquer: Each subarray is sorted individually using the merge sort algorithm.
# ✦ Merge: The sorted subarrays are merged back together in sorted order. The process continues 
# until all elements from both subarrays have been merged.

def MergeSort(arr):
    """Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works 
    by recursively dividing the input array into smaller subarrays and sorting those subarrays 
    then merging them back together to obtain the sorted array."""
    n = len(arr)
    if n <= 1:
        return arr
    middle = n // 2
    left = arr[:middle]
    right = arr[middle:]

    left = MergeSort(left)
    right = MergeSort(right)
    
    return Merge(left, right)

def Merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

number = int(input("Enter the number of elements: "))
list = random.sample(range(1, 101), number)
print(f"Original list: {list}")
print(f"Sorted list using Merge sort: {MergeSort(list)}")