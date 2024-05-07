class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.ketiep = None

class LinkedList:
    def __init__(self):
        self.head = None

    def them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ketiep is not None:
                current = current.ketiep
            current.ketiep = new_node

    def hienthi(self):
        current = self.head
        while current is not None:
            print(current.heso, "x^", current.somu, end="")
            current = current.ketiep
            if current is not None:
                print(" + ", end="")
        print()

    def DoiDau(self):
        current = self.head
        while current is not None:
            current.heso = -current.heso
            current = current.ketiep

# Kiểm tra kết quả
dathuc = LinkedList()
dathuc.them(3, 2)  # Thêm số hạng 3x^2
dathuc.them(-4, 1) # Thêm số hạng -4x^1
dathuc.them(5, 0)  # Thêm số hạng 5x^0

print("Đa thức ban đầu:")
dathuc.hienthi()   # Hiển thị đa thức ban đầu

dathuc.DoiDau()
print("Đa thức sau khi đổi dấu:")
dathuc.hienthi()   # Hiển thị đa thức sau khi đổi dấu
