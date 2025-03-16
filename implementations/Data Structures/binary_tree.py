# Each node has at most 2 children in a binary tree.
# The left child is always less than the parent node.
# The right child is always greater than the parent node.
# Elements are always unique.

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None