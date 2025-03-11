def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2 # floor division round down to the nearest whole number
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSort(left) # recursively divide the left half of the array until we have single elements
    right = mergeSort(right) # recursively divide the right half of the array until we have single elements

    return merge2_sortedArrays(left, right) # repeatedly merge the sorted arrays until we have a single sorted array

def merge2_sortedArrays(a,b):
    sorted_list = []
    
    len_a = len(a)
    len_b = len(b)
    i=j=0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    # handle the remaining elements when one of the arrays is exhausted
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1      
    return sorted_list
    

if __name__ == '__main__':
    # Unsorted array
    arr = [3, 7, 1, 8, 2, 4, 5, 6, 10, 0]
    
    print(mergeSort(arr)) # [1, 2, 3, 4, 5, 6, 7, 8]