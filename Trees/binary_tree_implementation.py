class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        pat1 = " "*self.get_level()*3
        pat2 = pat1 + "|__" if self.parent else ""
        print(pat2+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    A = TreeNode("A_0")

    B = TreeNode("B_1")
    B.add_child(TreeNode("C_2"))
    B.add_child(TreeNode("D_2"))
    B.add_child(TreeNode("E_2"))

    F = TreeNode("F_1")
    F.add_child(TreeNode("G_2"))
    F.add_child(TreeNode("H_2"))
    F.add_child(TreeNode("I_2"))

    A.add_child(B)
    A.add_child(F)
    
    return A.print_tree()


if __name__ == '__main__':
    build_tree()
