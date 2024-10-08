import random

def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def BubbleSort(arr2):
    m = len(arr2)   
    for i in range(m):
        for j in range(0, m - i - 1):
            if arr2[j] > arr2[j + 1]:
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
    return arr2

number = int(input("Enter the number of elements: "))
# list = []
# for e in range(number):
#     element = int(input(f"Enter element {e + 1}: "))
#     list.append(element)

# list = [random.randint(1, 100) for _ in range(number)]

list = random.sample(range(1, 101), number)
print(f"Original list: {list}")
print(f"Sorted list using Selection sort: {SelectionSort(list)}")
print(f"Sorted list using Bubble sort: {BubbleSort(list)}")