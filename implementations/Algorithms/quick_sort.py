# Implementation of quick sort algorithm

def quick_sort(arr, left, right):
    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)
    
    

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i <= j:
        while i < j and arr[i] < pivot:
            i += 1
        while i < j and arr[j] >= pivot:
            j -= 1 
        
        # swap the elements at i and j if elements at i is greater than pivot and elements at j is less than pivot
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    # swap the pivot with the element at i
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i # return the partition index


if __name__ == '__main__':
    # Testing with mixed and nested lists
    testCases = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [1, 3, 5, 7, 2, 4, 6, 8],
        [],
    ]
    
    for arr in testCases:
        quick_sort(arr, 0, len(arr) - 1)
        print(arr) # [1, 2, 3, 4, 5, 6, 7, 8] [1, 2, 3, 4, 5, 6, 7, 8] [1, 2, 3, 4, 5, 6, 7, 8] []