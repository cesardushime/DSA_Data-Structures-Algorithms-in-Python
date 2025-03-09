
# Bubble sort Function

def bubble_sort(elements, key=None):
    size = len(elements)
    for i in range(size-1): # goes from 0 to n-1, as the last element will be sorted by the time we reach the n-1th element
        swapped = False
        for j in range(size-1-i): # minus i because the last i elements are already sorted
            if elements[j][key] > elements[j+1][key]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped:
            break
    return elements

if __name__ == '__main__':
    elements = [
            { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
            { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
            { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
            { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]

    print(bubble_sort(elements, key='transaction_amount'))
    print(bubble_sort(elements, key='name'))
    print(bubble_sort(elements, key='device'))  
