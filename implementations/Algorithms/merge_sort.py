def mergeSort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr) // 2 # floor division round down to the nearest whole number
    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left) # recursively divide the left half of the array until we have single elements
    mergeSort(right) # recursively divide the right half of the array until we have single elements

    merge2_sortedArrays(left, right, arr) # merge the two sorted arrays into a single sorted array

def merge2_sortedArrays(a,b, arr): # and b are the two sorted arrays and arr is the merged array
    
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0 # i for a (left array), j for b (right array), k for arr (merged array)
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    # handle the remaining elements when one of the arrays is exhausted
    while i < len_a: # if there are remaining elements in a
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b: # if there are remaining elements in b
        arr[k] = b[j]
        j += 1   
        k += 1
    

if __name__ == '__main__':
    # Testing with mixed and nested lists
    testCases = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [1, 3, 5, 7, 2, 4, 6, 8],
        [],
    ]
    
    for arr in testCases:
        mergeSort(arr)
        print(arr) # [1, 2, 3, 4, 5, 6, 7, 8] [1, 2, 3, 4, 5, 6, 7, 8] [1, 2, 3, 4, 5, 6, 7, 8] []