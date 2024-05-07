class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Nếu là đồ thị vô hướng, phải thêm cả cạnh ngược lại

    def ChuaDinh(self, v):
        if v >= 0 and v < self.V:
            return True
        return False

# Test
g = Graph(5)
g.themCanh(0, 1)
g.themCanh(0, 2)
g.themCanh(1, 2)
g.themCanh(2, 3)
g.themCanh(3, 4)

print("Đỉnh 3 có tồn tại trong đồ thị:", g.ChuaDinh(3))  # Kết quả: True
print("Đỉnh 6 có tồn tại trong đồ thị:", g.ChuaDinh(6))  # Kết quả: False
