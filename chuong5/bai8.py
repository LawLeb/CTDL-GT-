class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        
        return (node1.info == node2.info and
                self.SoSanh(node1.left, node2.left) and
                self.SoSanh(node1.right, node2.right))

# Test
tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)

tree2 = BinaryTree()
tree2.root = Node(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)
tree2.root.left.left = Node(4)
tree2.root.left.right = Node(5)

tree3 = BinaryTree()
tree3.root = Node(1)
tree3.root.left = Node(2)
tree3.root.right = Node(3)
tree3.root.left.left = Node(4)
tree3.root.left.right = Node(6)

print("Cây 1 và cây 2 giống hệt hoàn toàn:", tree1.SoSanh(tree1.root, tree2.root))  # Kết quả: True
print("Cây 1 và cây 3 giống hệt hoàn toàn:", tree1.SoSanh(tree1.root, tree3.root))  # Kết quả: False
