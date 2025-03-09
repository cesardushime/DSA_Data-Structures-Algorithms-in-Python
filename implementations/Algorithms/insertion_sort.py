def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i-1
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = anchor # 
    return arr


if __name__=='__main__':
    elements = [11, 9, 29, 7, 2,1,23, 15, 28]
    print(insertion_sort(elements)) # [2, 7, 9, 11, 15, 28, 29]