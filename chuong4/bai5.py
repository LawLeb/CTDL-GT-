class HanoiTower:
    def __init__(self, n):
        self.n = n
        self.tower1 = list(range(n, 0, -1))
        self.tower2 = []
        self.tower3 = []

    def move(self, n, source, target, auxiliary):
        if n > 0:
            # Di chuyển n-1 tầng từ nguồn đến trung gian
            self.move(n - 1, source, auxiliary, target)
            # Di chuyển tầng cuối cùng từ nguồn đến đích
            target.append(source.pop())
            # In ra trạng thái hiện tại của các tháp
            print("Move disk", n, "from", source, "to", target)
            print("Tower 1:", self.tower1)
            print("Tower 2:", self.tower2)
            print("Tower 3:", self.tower3)
            # Di chuyển n-1 tầng từ trung gian đến đích
            self.move(n - 1, auxiliary, target, source)

    def solve(self):
        print("Initial Tower State:")
        print("Tower 1:", self.tower1)
        print("Tower 2:", self.tower2)
        print("Tower 3:", self.tower3)
        self.move(self.n, self.tower1, self.tower3, self.tower2)

# Test
n = 3  # Số tầng của tháp
hanoi = HanoiTower(n)
hanoi.solve()
