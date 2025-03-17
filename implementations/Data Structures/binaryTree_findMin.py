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

    
    def build_tree(elements): # builds a binary search tree from a list of elements
        root = BinaryTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i]) # adds elements to the tree by making them children of the root node, while maintaining the binary search tree property
        
        return root
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    

if __name__ == '__main__':
    elements = [17, 4, 10, 20, 9, 23, 18, 34]
    elements_tree = BinaryTreeNode.build_tree(elements)

    print(elements_tree.find_min()) 
 

    
