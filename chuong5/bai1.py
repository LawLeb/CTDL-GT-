class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoNut(self, node):
        if node is None:
            return 0
        else:
            return self.SoNut(node.left) + self.SoNut(node.right) + 1

# Test
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Số nút của cây:", tree.SoNut(tree.root)) 
