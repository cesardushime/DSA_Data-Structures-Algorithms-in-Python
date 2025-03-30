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


    if 'Red' in colorCount:
        sortedColors.extend(['Red'] * colorCount['Red'])
    
    if 'White' in colorCount:
        sortedColors.extend(['White'] * colorCount['White'])

    if 'Blue' in colorCount:
        sortedColors.extend(['Blue'] * colorCount['Blue'])

    return sortedColors

if __name__ == '__main__':
    arr = ['Red', 'White', 'Blue', 'Red', 'White', 'Blue', 'Red', 'White', 'Blue']
    print(sortColors(arr)) # Output: ['Red', 'Red', 'Red', 'White', 'White', 'White', 'Blue', 'Blue', 'Blue']