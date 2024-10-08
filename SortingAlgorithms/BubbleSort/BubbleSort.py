import random

# ✦ We sort the array using multiple passes. After the first pass, the maximum element goes to end 
# (its correct position). Same way, after second pass, the second largest element goes to second 
# last position and so on.
# ✦ In every pass, we compare all not-yest-sorted adjacent elements and if we find out of order, 
# we swap.

def BubbleSort(arr):
    """Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the 
    adjacent elements if they are in the wrong order. This algorithm is not suitable for 
    large data sets as its average and worst-case time complexity are quite high."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

number = int(input("Enter the number of elements: "))
list = random.sample(range(1, 101), number)
print(f"Original list: {list}")
print(f"Sorted list using Bubble sort: {BubbleSort(list)}")
