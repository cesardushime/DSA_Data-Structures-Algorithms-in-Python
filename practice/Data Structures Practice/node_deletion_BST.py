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

    def build_tree(elements):
        root = BinaryTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i]) # adds elements to the tree by making them children of the root node, while maintaining the binary search tree property
        
        return root

    def in_order_traversal(self): # left -> base -> right, also known as depth-first search (DFS)
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
    
    def pre_order_traversal(self): # base -> left -> right, also known as depth-first search (DFS)
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
    
    def post_order_traversal(self): # left -> right -> base, also known as depth-first search (DFS)
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
        
        if self.data == val:
            return True
        if val < self.data: # search in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data: # search in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self, val): # big O(log n) time complexity because we are traversing only one path to find the element to be deleted
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else: # when the value to be deleted is found
            # if the node to be deleted has no children, simply delete the node
            if self.left is None and self.right is None:
                return None
            # if the node to be deleted has only one child, 
            # return the child node to replace the node to be deleted
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
           # find maximum element in the left subtree to replace the node to be deleted, then delete the maximum element
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val) # big O(log n) time complexity because we are traversing the tree to find the maximum element in the left subtreeree

        return self
            


if __name__ == '__main__':
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    elements_tree = BinaryTreeNode.build_tree(elements)

    print("In order traversal gives this sorted list:", elements_tree.in_order_traversal())

    # Testing delete method
    elements_tree.delete(9)
    elements_tree.delete(20)
    print("In order traversal after deleting 9 and 20:", elements_tree.in_order_traversal())
    
 

    
