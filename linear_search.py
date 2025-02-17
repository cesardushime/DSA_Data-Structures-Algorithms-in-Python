def linear_search(list, target):
    '''Returns the index position of the target if found, else returns None
    '''
    for i in range(0, len(list)):
        if list[i] == target:
            return i
        else:
            return None