# Bubble sort algorithm implementation

def bubble_sort(arr):
    n = len(arr)
    
    swapped = False
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap the elements
                swapped = True
        if not swapped: # if no two elements were swapped in the inner loop, then the array is already sorted
            break
    return arr

if __name__ == '__main__':
    numbers = [5, 3, 8, 6, 7, 2]
    print(bubble_sort(numbers)) # [2, 3, 5, 6, 7, 8]