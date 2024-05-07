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

    def Cong(self, dathuc):
        result = LinkedList()

        current1 = self.head
        while current1 is not None:
            result.them(current1.heso, current1.somu)
            current1 = current1.ketiep

        current2 = dathuc.head
        while current2 is not None:
            result.them(current2.heso, current2.somu)
            current2 = current2.ketiep

        result.rut_gon()

        return result

# Kiểm tra kết quả
dathuc1 = LinkedList()
dathuc1.them(3, 2)  # Thêm số hạng 3x^2
dathuc1.them(-4, 1) # Thêm số hạng -4x^1
dathuc1.them(5, 0)  # Thêm số hạng 5x^0

dathuc2 = LinkedList()
dathuc2.them(2, 3)  # Thêm số hạng 2x^3
dathuc2.them(1, 1)  # Thêm số hạng x^1

print("Đa thức 1:")
dathuc1.hienthi()   # Hiển thị đa thức 1
print("Đa thức 2:")
dathuc2.hienthi()   # Hiển thị đa thức 2

dathuc_tong = dathuc1.Cong(dathuc2)
print("Đa thức tổng:")
dathuc_tong.hienthi() # Hiển thị đa thức tổng
