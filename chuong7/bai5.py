class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Thêm cả cạnh ngược lại

    def BacDinh(self, v):
        return len(self.adj[v])

# Test
g = Graph(5)
g.themCanh(0, 1)
g.themCanh(0, 2)
g.themCanh(1, 2)
g.themCanh(2, 3)
g.themCanh(3, 4)

print("Bậc của đỉnh 2:", g.BacDinh(2))  # Kết quả: 3
