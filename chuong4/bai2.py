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

    def hienthi(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def DaoNguoc(self):
        if self.head is None or self.head.next is None:
            return

        stack = []
        current = self.head
        while current is not None:
            stack.append(current)
            current = current.next

        self.head = stack.pop()
        current = self.head
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None

# Kiểm tra kết quả
dslk = LinkedList()
dslk.them(1)
dslk.them(2)
dslk.them(3)
dslk.them(4)

print("Danh sách liên kết ban đầu:")
dslk.hienthi()

print("Danh sách liên kết sau khi đảo ngược:")
dslk.DaoNguoc()
dslk.hienthi()
