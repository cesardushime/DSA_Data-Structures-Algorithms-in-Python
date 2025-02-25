from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, item):
        self.queue.appendleft(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        return "Queue is empty"
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        if not self.is_empty():
            return len(self.queue)
        return "Queue is empty"
    
    

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")

print(q.dequeue())
