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

    def SoThanhPhan(self):
        visited = [False] * self.V
        count = 0
        for v in range(self.V):
            if not visited[v]:
                self.DFS(v, visited)
                count += 1
        return count

# Test
g = Graph(5)
g.themCanh(0, 1)
g.themCanh(0, 2)
g.themCanh(3, 4)

print("Số thành phần liên thông của đồ thị:", g.SoThanhPhan())  # Kết quả: 2
