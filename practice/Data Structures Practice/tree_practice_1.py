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
        if self.children:
            for child in self.children:
                child.print_tree() # big O(n) time complexity because we are traversing the tree from the current node to the leaf node
        

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent # moves up the tree to the parent node until it reaches the root node
        return level # big O(n) time complexity because we are traversing the tree from the current node to the root node

def build_product_tree():
    ceo = TreeNode("Nilupul (CEO)") # big O(1) time complexity because we are just creating a new node

    cto = TreeNode("Chinmay (CTO)") # big O(1) time complexity because we are just creating a new node
    cto.add_child(TreeNode("Dhaval (Infrastructure Head)"))
    cto.add_child(TreeNode("Abhijit (Application Head)"))
    cto.add_child(TreeNode("Amit (Cloud Head)"))

    hr_head = TreeNode("Gelsy (HR Head)")
    hr_head.add_child(TreeNode("Peter (Recruitment Manager)"))
    hr_head.add_child(TreeNode("Waqas (Policy Manager)"))

    ceo.add_child(cto)
    ceo.add_child(hr_head)
   
    return ceo
if __name__== '__main__':
    root = build_product_tree()
    root.print_tree()
    