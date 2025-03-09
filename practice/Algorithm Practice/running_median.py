# Computing the running median of a sequence of numbers

def running_median(sequence):
    sorted_sequence = []
    medians = []
    
    for index, element in enumerate(sequence):
        sorted_sequence.append(element)
        sorted_sequence.sort()
        size = len(sorted_sequence)
        
        if size  % 2 == 1:
            median_index = size // 2
            median = sorted_sequence[median_index]
        else:
            right_index = size // 2
            left_index = right_index -1 
            
            median = (sorted_sequence[left_index] + sorted_sequence[right_index]) / 2
        
        medians.append(median)
    return medians
        
if __name__ == '__main__':
    sequence = [2, 1, 5, 7, 2, 0, 5]
    print(running_median(sequence)) # [2, 1.5, 2, 3.5, 2, 2, 2]
    

