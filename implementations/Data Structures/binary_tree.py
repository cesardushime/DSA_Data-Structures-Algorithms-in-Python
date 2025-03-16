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
    
