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
                self.left.add_child(data) # big O(log n) time complexity because we are only traversing the left subtree of the tree
            else:
                self.left = BinaryTreeNode(data)
            
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data) # big O(log n) time complexity because we are only traversing the right subtree of the tree
            else:
                self.right = BinaryTreeNode(data)
    
    def build_tree(elements):
        root = BinaryTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i]) # big O(log n) time complexity because we are only traversing the left or right subtree of the tree, depending on the value of the element
        
        return root
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max() # big O(log n) time complexity because we are only traversing the right subtree of the tree

if __name__ == '__main__':
    elements = [100, 17, 4, 1, 20, 9, 23, 18, 34, 90]
    elements_tree = BinaryTreeNode.build_tree(elements)

    print('The maximum is', elements_tree.find_max())
 

    
