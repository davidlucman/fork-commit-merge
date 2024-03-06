def bubble_sort(arr):
    # TODO: Implement the bubble sort algorithm
    n = len(arr)

    for i in range(n):
        for j in range(i,n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

#! Test cases (Don't edit):
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)
