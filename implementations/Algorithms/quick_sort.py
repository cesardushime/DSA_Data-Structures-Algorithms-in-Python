# Implementation of quick sort algorithm
def quick_sort(arr, left, right): # big O(nlogn) because we are dividing the array into halves in log(n) time and partitioning it O(n) time.
    if left < right: 
        partition_index = partition(arr, left, right)  # Get partition index
        quick_sort(arr, left, partition_index - 1) # Recursively sort the left part until the left index is less than the partition index
        quick_sort(arr, partition_index + 1, right)  # Recursively sort the right part until the partition index is less than the right index

def partition(arr, left, right): # Big O(n) because we are iterating through the array once to partition it
    pivot = arr[right]   
    i = left  # i starts at the leftmost element
    j = right - 1  # j starts at the element before the pivot
    
    while i <= j:  # The loop continues until i surpasses j
        while i <= j and arr[i] < pivot:  # i moves to the right to find elements >= pivot
            i += 1
        while i <= j and arr[j] > pivot:  # j moves to the left to find elements <= pivot
            j -= 1
        
        if i <= j:  # Swap arr[i] and arr[j] if i has not surpassed j
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    # Place the pivot in its correct position as i has surpassed j, the position of the pivot is at i
    arr[i], arr[right] = arr[right], arr[i]
    return i  # Return the partition index


if __name__ == '__main__':
    # 5 List variety of test cases
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 5, 2, 4],
        [5, 3, 1, 4, 2],
        [5, 3, 1, 2, 4]
    ]

    for arr in test_cases:
        print(f"Before: {arr}")
        quick_sort(arr, 0, len(arr) - 1)
        print(f"After: {arr}\n")