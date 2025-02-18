class Node:
    def __init__(self, data=None, next=None):
        self.data = data # Assign data
        self.next = next # initialize next (pointer to the next element) as null

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at the beginning
    def insert_at_beginning(self, data):
        node = Node(data, self.head) # next is the current head
        self.head = node  # Big O(1) operation
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
            print(llstr)
    def inserting_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None) # If the linked list is empty, then the new node is the head
            return 
        
        itr = self.head
        while itr.next: # Traverse the linked list until the last node (where next is None)
            itr = itr.next
        itr.next = Node(data, None) # Assign the new node to the next of the last node, hence big O(n) operation; traverse the linked list before inserting the new node
            
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(12)
    ll.inserting_at_end(100)
    ll.inserting_at_end(200)
    ll.print()
    