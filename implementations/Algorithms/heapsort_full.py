
# Time Complexity: O(nlogn)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def heapify(lst, i, upper): 
    # upper is the length of the list, which is the upper bound of the list and i is the index of the element to be heapified
    # This function is used to heapify the list from the index i to the end of the list
    # This is a max heap
    # Time Complexity: O(logn) because we are moving the element down the tree to its correct position, and the height of the tree is logn
    
    while True: # continue until the element is in the correct position
        left, right = 2 * i + 1, 2 * i + 2

        if max(left, right) < upper: # if left and right are within the bounds of the list, then we can compare them
            if lst[i] >= max(lst[left], lst[right]): # if the parent is greater than both children, then we are done
                break
            if lst[left] > lst[right]: 
                swap(lst, i, left) 
                i = left
            else: 
                swap(lst, i, right)
                i = right
        elif left < upper: # if only the left child is within the bounds of the list, then we can compare the current element with the left child
            if lst[left] > lst[i]:
                swap(lst, i, left)
                i = left
            else:
                break
        elif right < upper: # if only the right child is within the bounds of the list, then we can compare the current element with the right child
            if lst[right] > lst[i]:
                swap(lst, i, right)
                i = right
            else:
                break
        else: # if both left and right children are out of bounds, then we are done
            break

def heapsort(lst):
    # Time Complexity: O(nlogn) because we are heapifying the list in O(n) time and swapping in O(logn) time

    for j in range((len(lst)-2)//2, -1, -1): # starting from the last parent to the root, we heapify the list
        # The last parent is at index (len(lst)-2)//2 because the last element is a leaf node and does not need to be heapified
        heapify(lst, j, len(lst))  

    for end in range(len(lst)-1, 0, -1): # starting from the end of the list, we swap the first element with the last element and heapify the list
        swap(lst, 0, end)
        heapify(lst, 0, end) # heapify the list from the first element to the end-1 element, because the last element makes the sorted list with each iteration

    return lst

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 9, 1, 2, 3]
    print(heapsort(arr)) # [1, 2, 3, 5, 6, 7, 9, 11, 12, 13]