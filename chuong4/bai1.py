class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def them(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def in_nguoc_recursive(self, node):
        if node is None:
            return
        self.in_nguoc_recursive(node.next)
        print(node.data, end=" ")

    def in_nguoc_iterative(self):
        stack = []
        current = self.head
        while current is not None:
            stack.append(current.data)
            current = current.next
        while stack:
            print(stack.pop(), end=" ")

# Kiểm tra kết quả
dslk = LinkedList()
dslk.them(1)
dslk.them(2)
dslk.them(3)
dslk.them(4)

print("Danh sách liên kết ban đầu:")
current = dslk.head
while current is not None:
    print(current.data, end=" ")
    current = current.next
print()

print("In ngược danh sách liên kết (dùng đệ qui):")
dslk.in_nguoc_recursive(dslk.head)
print()

print("In ngược danh sách liên kết (dùng không đệ qui):")
dslk.in_nguoc_iterative()
print()
