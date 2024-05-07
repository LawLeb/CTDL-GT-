class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def isBSTUtil(self, node, min_value, max_value):
        if node is None:
            return True
        
        if node.info < min_value or node.info > max_value:
            return False
        
        return (self.isBSTUtil(node.left, min_value, node.info - 1) and
                self.isBSTUtil(node.right, node.info + 1, max_value))

    def KiemTraBST(self):
        return self.isBSTUtil(self.root, float('-inf'), float('inf'))

# Test
tree = BinaryTree()
tree.root = Node(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

print("Cây là một cây BST:", tree.KiemTraBST())  # Kết quả: True

# Cây không phải là BST
tree.root.right.right.left = Node(8)
print("Cây là một cây BST:", tree.KiemTraBST())  # Kết quả: False
