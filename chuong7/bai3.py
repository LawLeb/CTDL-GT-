class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def themCanh(self, u, v):
        self.adj[u].append(v)

    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                if self.isCyclicUtil(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def ChuTrinh(self):
        visited = [False] * self.V
        for v in range(self.V):
            if not visited[v]:
                if self.isCyclicUtil(v, visited, -1):
                    return True
        return False

# Test
g = Graph(5)
g.themCanh(0, 1)
g.themCanh(0, 2)
g.themCanh(1, 2)
g.themCanh(2, 0)
g.themCanh(2, 3)
g.themCanh(3, 4)

print("Đồ thị có chứa chu trình:", g.ChuTrinh())  # Kết quả: True
