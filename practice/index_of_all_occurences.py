def binary_search(arr, target, left_index, right_index):
    
    
    if left_index > right_index:
        return []
    
    mid_index = (left_index + right_index)// 2
    mid_number = arr[mid_index]
    
    if mid_number == target:
        indices = [mid_index]
        left_index = mid_index - 1
        while left_index >= 0 and arr[left_index] == target:
            indices.append(left_index)
            left_index -= 1
        right_index = mid_index + 1
        while right_index < len(arr) and arr[right_index] == target:
            indices.append(right_index)
            right_index += 1
        return sorted(indices)
    if mid_number < target:
        return binary_search(arr, target, mid_index + 1, right_index)
    else:
        return binary_search(arr, target, left_index, mid_index - 1)
    
    
    
if __name__ == '__main__':
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    target = 15
    print(binary_search(numbers, target, 0, len(numbers) - 1))  # [5, 6, 7]