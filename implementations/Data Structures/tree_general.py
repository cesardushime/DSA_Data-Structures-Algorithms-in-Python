class TreeNode: 
    def __init__(self, data):
        self.data = data
        self.children = [] # holds the children of each node in the tree, big O(1) time complexity
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child) # adding child to the children list of the parent node, big O(1) time complexity it's just appending to the list
    
    def print_tree(self):
        spaces = ' ' * self.get_level()
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children: # accessing children of the node which is also a TreeNode object
                child.print_tree() # The recursion works in big O(n) time complexity because we are traversing all the nodes in the tree

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent # moves up the tree to the parent node until it reaches the root node
        return level # big O(n) time complexity because we are traversing the tree from the current node to the root node

def build_product_tree():
    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("HP")) # big O(1) time complexity because we are just adding the child to the children list of the parent node

    cellphone = TreeNode("Cell Phones")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Samsung"))

    tv = TreeNode("Televisions")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Vizio"))
    tv.add_child(TreeNode("Panasonic"))

    root = TreeNode("Electronics")
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root # has value "Electronics" and children as laptop, cellphone, tv
if __name__== '__main__':
    root = build_product_tree()
    root.print_tree()
    