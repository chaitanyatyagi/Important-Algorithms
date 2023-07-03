class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data: return
        if data < self.data:
            if self.left: self.left.add_child(data)
            else: self.left = TreeNode(data)    
        else:
            if self.right: self.right.add_child(data)
            else: self.right = TreeNode(data)

    def search_node(self,value):
        if value == self.data: return True
        if value < self.data:
            if self.left: return self.left.search(value)
            else: return False
        else:
            if self.right: return self.right.search(value)
            else: return False
    
    def find_min(self):
        if self.left: return self.left.find_min()
        else: return self.data

    def find_max(self):
        if self.right: return self.right.find_max()
        else: return self.data

    def delete_node(self,value):
        if value < self.data:
            if self.left: self.left = self.left.delete_node(value)
        elif value > self.data:
            if self.right: self.right = self.right.delete_node(value)
        else:
            if not self.left and not self.right: return None
            if not self.left: return self.right
            if not self.right: return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        return self
    
    def in_order_traversal(self):
        if self.left: self.left.in_order_traversal()
        print(self.data)
        if self.right: self.right.in_order_traversal()
    
    def pre_order_traversal(self):
        print(self.data)
        if self.left: self.left.pre_order_traversal()
        if self.right: self.right.pre_order_traversal()
    
    def post_order_traversal(self):
        if self.left: self.left.post_order_traversal()
        if self.right: self.right.post_order_traversal()
        print(self.data)

def build_tree(elements):
    root = TreeNode(elements[0])
    for index in range(1,len(elements)):
        root.add_child(elements[index])
    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.in_order_traversal()
    numbers_tree.pre_order_traversal()
    numbers_tree.post_order_traversal()
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
