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


