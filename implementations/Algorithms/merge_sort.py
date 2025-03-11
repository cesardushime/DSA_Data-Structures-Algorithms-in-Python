def mergeSort(a,b):
    sort_list = []
    
    len_a = len(a)
    len_b = len(b)
    i=j=0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sort_list.append(a[i])
            i += 1
        else:
            sort_list.append(b[j])
            j += 1
            
    while i < len_a:
        sort_list.append(a[i])
        i += 1
    while j < len_b:
        sort_list.append(b[j])
        j += 1
    return sort_list
    

if __name__ == '__main__':
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10, 15]
    
    print(mergeSort(a,b)) # [1, 2, 3, 4, 5, 6, 7, 8]