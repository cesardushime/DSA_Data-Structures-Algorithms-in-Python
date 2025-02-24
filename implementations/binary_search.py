import time

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    
    left_index = 0
    right_index = len(arr) - 1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index)// 2
        mid_number = arr[mid_index]
        
        if mid_number == target:
            return mid_index
        if mid_number < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1
    


if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    print(binary_search(mylist, 100))  # 9