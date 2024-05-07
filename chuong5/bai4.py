class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self, node):
        if node is None:
            return 0
        elif node.left is not None or node.right is not None:
            return 1 + self.SoNutTrungGian(node.left) + self.SoNutTrungGian(node.right)
        else:
            return 0

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

print("Số nút trung gian của cây:", tree.SoNutTrungGian(tree.root))  # Kết quả: 6
