# Implementing selection sort algorithm

def selection_sort(arr):
    for i in range(len(arr)-1): # because the last element will be at its correct position after n-1 iterations
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index: # If the minimum element is not at the current index, swap the elements
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__=='__main__':
    elements = [11, 9, 29, 7, 2,1,23, 15, 28]
    print(selection_sort(elements)) # [1, 2, 7, 9, 11, 15, 23, 28, 29]
    