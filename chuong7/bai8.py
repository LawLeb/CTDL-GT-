class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Nếu là đồ thị vô hướng, thêm cả cạnh ngược lại

    def DFS(self, v, visited, dest):
        visited[v] = True
        if v == dest:
            return True
        for i in self.adj[v]:
            if not visited[i]:
                if self.DFS(i, visited, dest):
                    return True
        return False

    def DuongDi(self, v1, v2):
        visited = [False] * self.V
        return self.DFS(v1, visited, v2)

# Test
g = Graph(5)
g.themCanh(0, 1)
g.themCanh(0, 2)
g.themCanh(1, 2)
g.themCanh(2, 3)
g.themCanh(3, 4)

print("Có đường đi từ đỉnh 0 đến đỉnh 4:", g.DuongDi(0, 4))  # Kết quả: True
print("Có đường đi từ đỉnh 3 đến đỉnh 0:", g.DuongDi(3, 0))  # Kết quả: False
