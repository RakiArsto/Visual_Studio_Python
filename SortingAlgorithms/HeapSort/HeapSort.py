import random

# ★ First convert the array into a max heap using heapify, Please note that this happens in-place. 
# The array elements are re-arranged to follow heap properties. Then one by one delete the root 
# node of the Max-heap and replace it with the last node and heapify. Repeat this process while 
# size of heap is greater than 1.

# ✦ Rearrange array elements so that they form a Max Heap.
# ✦ Repeat the following steps until the heap contains only one element:
    # ✧ Swap the root element of the heap (which is the largest element in current heap) 
    # with the last element of the heap.
    # ✧ Remove the last element of the heap (which is now in the correct position). We 
    # mainly reduce heap size and do not remove element from the actual array.
    # ✧ Heapify the remaining elements of the heap.
# ✦ Finally we get sorted array.

# ⬛ Detailed Working of Heap Sort
# Step ➊: Treat the Array as a Complete Binary Tree
# Step ➋: Build a Max Heap
# Step ➌: Sort the array by placing largest element at end of unsorted array.

def HeapSort(arr):
    """Heap sort is a comparison-based sorting technique based on Binary Heap Data Structure. It can 
    be seen as an optimization over selection sort where we first find the max (or min) element and 
    swap it with the last (or first). We repeat the same process for the remaining elements. In Heap 
    Sort, we use Binary Heap so that we can quickly find and move the max element in O(Log n) instead 
    of O(n) and hence achieve the O(n Log n) time complexity."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        Heapify(arr, n, i)
    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        Heapify(arr, j, 0)

    return arr

def Heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr, n, largest)

number = int(input("Enter the number of elements: "))
list = random.sample(range(1, 101), number)
print(f"Original list: {list}")
print(f"Sorted list using Heap sort: {HeapSort(list)}")