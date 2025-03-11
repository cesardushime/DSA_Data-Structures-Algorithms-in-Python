def mergeSort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr) // 2 # floor division round down to the nearest whole number
    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left) # recursively divide the left half of the array until we have single elements
    mergeSort(right) # recursively divide the right half of the array until we have single elements

    merge2_sortedArrays(left, right, arr) # repeatedly merge the sorted arrays until we have a single sorted array

def merge2_sortedArrays(a,b, arr):
    
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    # handle the remaining elements when one of the arrays is exhausted
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1   
        k += 1
    

if __name__ == '__main__':
    # Unsorted array
    arr = [3, 7, 1, 8, 2, 4, 5, 6, 10, 0]
    mergeSort(arr)
    print(arr) # [1, 2, 3, 4, 5, 6, 7, 8]