class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoNutLa(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self.SoNutLa(node.left) + self.SoNutLa(node.right)

# Test
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print("Số nút lá của cây:", tree.SoNutLa(tree.root))  # Kết quả: 4
