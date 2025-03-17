# Each node has at most 2 children in a binary search tree.
# The left child is always less than the parent node.
# The right child is always greater than the parent node.
# Elements are always unique (set property).

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return 
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
            
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def in_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        # visit base node
        elements.append(self.data)
        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def build_tree(elements):
        root = BinaryTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i]) # adds elements to the tree by making them children of the root node, while maintaining the binary search tree property
        
        return root
    
    def post_order_traversal(self): 
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()
        # visit base node
        elements.append(self.data)

        return elements
    def search(self, val):
        found_at_level = 0
        if self.data == val:
            return True
        if val < self.data: # search in left subtree
            if self.left:
                return self.left.search(val)
                found_at_level += 1
            else:
                return False
            
        if val > self.data: # search in right subtree
            if self.right:
                return self.right.search(val)
                found_at_level += 1
            else:
                return False
    

if __name__ == '__main__':
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    elements_tree = BinaryTreeNode.build_tree(elements)

    print(elements_tree.in_order_traversal()) # outputs [1, 4, 9, 17, 18, 20, 23, 34]
    print(elements_tree.pre_order_traversal())  # outputs [17, 4, 1, 9, 20, 18, 23, 34]
    print(elements_tree.post_order_traversal()) # outputs [1, 9, 4, 18, 34, 23, 20, 17]


    print(elements_tree.search(20)) 
    print(elements_tree.search(100)) # outputs False
    print(elements_tree.search(17)) 
    
 

    
