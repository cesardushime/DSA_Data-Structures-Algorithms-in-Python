from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    def is_empty(self):
        return self.stack == 0
    def size(self):
        if not self.is_empty():
            return len(self.stack)
        return "stack is empty"
    


s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")

print(s.size())