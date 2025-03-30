# Sort three different colors in an array
# Time complexity: O(n)


def sortColors(arr):
    
    colorCount = {}

    # Count the number of each color in the array
    for color in arr:
        if color in colorCount:
            colorCount[color] += 1
        else:
            colorCount[color] = 1
    
    # array to store the sorted colors
    sortedColors = []

    # Append the colors in the order of Red, White, and Blue
    if 'Red' in colorCount:
        sortedColors.extend(['Red'] * colorCount['Red'])
    
    if 'White' in colorCount:
        sortedColors.extend(['White'] * colorCount['White'])

    if 'Blue' in colorCount:
        sortedColors.extend(['Blue'] * colorCount['Blue'])

    return sortedColors

# Sorting using the merge sort approach to sort the colors
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    arr = ['Red', 'White', 'Blue', 'Red', 'White', 'Blue', 'Red', 'White', 'Blue']
    print(sortColors(arr)) # Output: ['Red', 'Red', 'Red', 'White', 'White', 'White', 'Blue', 'Blue', 'Blue']
    print(mergeSort(arr)) # Output: ['Blue', 'Blue', 'Blue', 'Red', 'Red', 'Red', 'White', 'White', 'White']