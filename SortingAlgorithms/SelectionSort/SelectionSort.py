import random

# ✦ First we find the smallest element and swap it with the first element. This way we get 
# the smallest element at its correct position.
# ✦ Then we find the smallest among remaining elements (or second smallest) and move it to 
# its correct position by swapping.
# ✦ We keep doing this until we get all elements moved to correct position.

def SelectionSort(arr):
    """Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly 
    selecting the smallest (or largest) element from the unsorted portion and swapping it with 
    the first unsorted element. This process continues until the entire array is sorted."""
    n = len(arr)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

number = int(input("Enter the number of elements: "))
list = random.sample(range(1, 101), number)
print(f"Original list: {list}")
print(f"Sorted list using Selection sort: {SelectionSort(list)}")
