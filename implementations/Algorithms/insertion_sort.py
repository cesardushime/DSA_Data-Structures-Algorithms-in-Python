def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i-1 # last index of the sorted part of the array
        while j >= 0 and anchor < arr[j]: # if the anchor is less than the last element of the sorted part of the array
            # shift the last element of the sorted part of the array to the right
            arr[j+1] = arr[j]
            j -= 1 # move to the next element of the sorted part of the array until the anchor is in the right position
        # insert the anchor in the right position in the sorted part of the array
        arr[j+1] = anchor # 
    return arr

if __name__=='__main__':
    elements = [11, 9, 29, 7, 2,1,23, 15, 28]
    print(insertion_sort(elements)) # [2, 7, 9, 11, 15, 28, 29]
    
    elements = [11, 9, 29, 7, 2,1,23, 15, 28, 1]
    print(insertion_sort(elements)) # [1, 1, 2, 7, 9, 11, 15, 23, 28, 29]
    
    