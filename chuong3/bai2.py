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

    def rut_gon(self):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            runner = current.ketiep
            while runner is not None:
                if runner.somu == current.somu:
                    current.heso += runner.heso
                    runner.heso = 0
                runner = runner.ketiep
            current = current.ketiep

        # Loại bỏ các số hạng có hệ số bằng 0
        previous = None
        current = self.head
        while current is not None:
            if current.heso == 0:
                if previous is None:
                    self.head = current.ketiep
                else:
                    previous.ketiep = current.ketiep
            else:
                previous = current
            current = current.ketiep

# Kiểm tra kết quả
dathuc = LinkedList()
dathuc.them(3, 2)  # Thêm số hạng 3x^2
dathuc.them(-4, 1) # Thêm số hạng -4x^1
dathuc.them(5, 0)  # Thêm số hạng 5x^0
print("Đa thức trước khi rút gọn:")
dathuc.hienthi()   # Hiển thị đa thức trước khi rút gọn
dathuc.rut_gon()   # Rút gọn đa thức
print("Đa thức sau khi rút gọn:")
dathuc.hienthi()   # Hiển thị đa thức sau khi rút gọn
