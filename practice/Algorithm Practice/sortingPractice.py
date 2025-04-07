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

def mergeSort(arr):
    # Works by recursively dividing the colors into halves and merging them back together in sorted order by color priority.
    # Time complexity: O(nlogn) because we are dividing the array into halves in log(n) time and merging them O(n) time.
    # Space complexity: O(n) because we are using additional space to store the left and right halves of the array.
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L) 
        mergeSort(R) # big O(nlogn) because the merge sort recursively divides the array into halves in log(n) time and merges them O(n) time.

        i = j = k = 0

        # Mapping colors to priority: 'Red' < 'White' < 'Blue'
        color_priority = {'Red': 0, 'White': 1, 'Blue': 2}

        # Merge the two sorted halves based on color priority
        while i < len(L) and j < len(R): 
            if color_priority[L[i]] < color_priority[R[j]]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # If there are remaining elements in L or R, add them to arr
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

if __name__ == '__main__':
    arr = ['White', 'Blue', 'Blue', 'White', 'Blue', 'Blue', 'Red', 'White', 'White', 'Blue']

    print(mergeSort(arr))  # Output: ['Red', 'Red', 'Red', 'White', 'White', 'White', 'Blue', 'Blue', 'Blue']
