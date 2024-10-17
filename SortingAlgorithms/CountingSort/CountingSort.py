import random

# ✦ Declare an auxiliary array countArray[] of size max(inputArray[])+1 and initialize it with 0.
# ✦ Traverse array inputArray[] and map each element of inputArray[] as an index of countArray[] array, 
# i.e., execute countArray[inputArray[i]]++ for 0 <= i < N.
# ✦ Calculate the prefix sum at every index of array inputArray[].
# ✦ Create an array outputArray[] of size N.
# ✦ Traverse array inputArray[] from end and update outputArray[countArray[inputArray[i]] – 1] = inputArray[i]. 
# Also, update countArray[ inputArray[i] ] = countArray[inputArray[i]]-–.

def CountingSort(arr):
    """Counting Sort is a non-comparison-based sorting algorithm. It is particularly efficient when the 
    range of input values is small compared to the number of elements to be sorted. The basic idea 
    behind Counting Sort is to count the frequency of each distinct element in the input array and use 
    that information to place the elements in their correct sorted positions."""
    n = len(arr)
    maxValue = max(arr)
    count = [0] * (maxValue + 1)
    for num in arr:
        count[num] += 1

    for i in range(1, maxValue + 1):
        count[i] += count[i - 1]

    outputArray = [0] * n
    for i in range(n - 1, -1, -1):
        outputArray[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return outputArray

number = int(input("Enter the number of elements: "))
list = random.sample(range(1, 101), number)
print(f"Original list: {list}")
print(f"Sorted list using Counting sort: {CountingSort(list)}")