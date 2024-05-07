class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def Chep(self, node):
        if node is None:
            return None
        else:
            new_node = Node(node.info)
            new_node.left = self.Chep(node.left)
            new_node.right = self.Chep(node.right)
            return new_node

# Test
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

new_tree = BinaryTree()
new_tree.root = tree.Chep(tree.root)

# In cây gốc
print("Cây gốc:")
def print_tree(node):
    if node:
        print(node.info)
        print_tree(node.left)
        print_tree(node.right)

print_tree(tree.root)

# In cây sao chép
print("\nCây sau khi sao chép:")
print_tree(new_tree.root)
