import heapq
# Time Complexity: O(nlogn)
# heapq creates a min heap by default
# heapq.heapify(arr) converts the list into a heap in O(n) time
# heapq.heappop(arr) pops the smallest element from the heap in O(logn) time

def heapsort(arr):
    heapq.heapify(arr) 
    new_list = []
    for i in range(len(arr)):
        new_list.append(heapq.heappop(arr))

    return new_list


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 9, 1, 2, 3]
    print(heapsort(arr))