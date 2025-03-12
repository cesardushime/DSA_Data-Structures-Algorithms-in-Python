def mergeSort(elements, key=None, descending=False):
    if len(elements) <= 1:
        return 
    mid = len(elements) // 2 # floor division round down to the nearest whole number
    left = elements[:mid]
    right = elements[mid:]
    
    # Sorting by time_hours
    mergeSort(left, key)
    mergeSort(right, key)

    merge2_sortedArrays(left, right, key, descending,elements) # repeatedly merge the sorted arrays until we have a single sorted array

def merge2_sortedArrays(a,b, key, descending, elements):
    
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0 # i for a (left array), j for b (right array), k for arr (merged array)
    
    while i < len_a and j < len_b:
        
        if descending:
            if a[i][key] >= b[j][key]:
                elements[k] = a[i]
                i += 1
            else:
                elements[k] = b[j]
                j += 1
            k += 1
            
        if not descending:
            if a[i][key] <= b[j][key]:
                elements[k] = a[i]
                i += 1
            else:
                elements[k] = b[j]
                j += 1
            k += 1
            
    # handle the remaining elements when one of the arrays is exhausted
    while i < len_a:
        elements[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        elements[k] = b[j]
        j += 1   
        k += 1
    

if __name__ == '__main__':
    elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
    
    mergeSort(elements, key='age')
    for element in elements:
        print(element)