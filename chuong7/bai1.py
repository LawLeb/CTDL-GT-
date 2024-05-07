class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.DFS(i, visited)

    def LienThong(self):
        visited = [False] * self.V
        self.DFS(0, visited)

        # Kiểm tra xem tất cả các đỉnh đã được duyệt qua hay chưa
        for i in range(self.V):
            if not visited[i]:
                return False
        return True

# Test
g = Graph(5)
g.themCanh(0, 1)
g.themCanh(0, 2)
g.themCanh(1, 2)
g.themCanh(3, 4)

print("Đồ thị là đồ thị liên thông:", g.LienThong())  # Kết quả: False

g2 = Graph(4)
g2.themCanh(0, 1)
g2.themCanh(0, 2)
g2.themCanh(1, 2)
g2.themCanh(2, 3)

print("Đồ thị là đồ thị liên thông:", g2.LienThong())  # Kết quả: True
