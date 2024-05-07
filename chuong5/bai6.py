class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def isAVLUtil(self, node):
        if node is None:
            return True
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return (self.isAVLUtil(node.left) and self.isAVLUtil(node.right))

    def KiemTraAVL(self):
        return self.isAVLUtil(self.root)

# Test
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Cây là một cây AVL:", tree.KiemTraAVL())  # Kết quả: True

# Cây không phải là AVL
tree.root.right.right.right = Node(8)
print("Cây là một cây AVL:", tree.KiemTraAVL())  # Kết quả: False
