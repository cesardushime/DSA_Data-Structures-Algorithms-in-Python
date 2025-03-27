# Sort three different colors in an array
# Time complexity: O(n)


def sortColors(arr):
    # Create a dictionary to store the count of each color
    colorCount = {}

    # Count the number of each color in the array
    for color in arr:
        if color in colorCount:
            colorCount[color] += 1
        else:
            colorCount[color] = 1
    
    # Create a new array to store the sorted colors
    sortedColors = []
    # Add the colors to the new array in the correct order

    # Add red to the new array
    if 'Red' in colorCount:
        sortedColors.extend(['Red'] * colorCount['Red'])
    # Add white to the new array
    if 'White' in colorCount:
        sortedColors.extend(['White'] * colorCount['White'])
    # Add blue to the new array
    if 'Blue' in colorCount:
        sortedColors.extend(['Blue'] * colorCount['Blue'])

    return sortedColors

if __name__ == '__main__':
    arr = ['Red', 'White', 'Blue', 'Red', 'White', 'Blue', 'Red', 'White', 'Blue']
    print(sortColors(arr)) # Output: ['Red', 'Red', 'Red', 'White', 'White', 'White', 'Blue', 'Blue', 'Blue']