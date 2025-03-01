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
    
    def insert_values(self, data_list):
        self.head = None # Clear the linked list
        for data in data_list:
            self.inserting_at_end(data)
    
    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count +=1 
            itr = itr.next
        return count # big O(n) operation as we need to traverse the linked list to get the length
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next  # Remove head
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next  # Works for all cases (middle & last node), big O(n) operation because we need to traverse the linked list to the node before the node to be removed
                break

            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next) 
                itr.next = node # big O(n) operation because we need to traverse the linked list to the node before the node to be inserted
                break
            itr = itr.next
            count += 1

    
    
if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_beginning(12)
    # ll.inserting_at_end(100)
    # ll.inserting_at_end(200)
    
    ll.insert_values([45, 7, 12, 567, 99])
    ll.print()
    # ll.remove_at(4)
    # ll.insert_at_beginning(67)
    ll.insert_at(0, 10)
    ll.insert_at(2, 20)

    ll.print()
    