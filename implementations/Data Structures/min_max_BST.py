# Implementing a binary search tree and finding the minimum element in the tree
# Each node has at most 2 children in a binary search tree.
# The left most is always the minimum element in the tree.
# The right most element is always the maximum element in the tree.

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

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    

if __name__ == '__main__':
    elements = [100, 4, 10, 20, 9, 23, 18, 2,34, 1]
    elements_tree = BinaryTreeNode.build_tree(elements)

    print("Minimum element in the tree is:", elements_tree.find_min())
    print("Maximum element in the tree is:", elements_tree.find_max())


 

    
