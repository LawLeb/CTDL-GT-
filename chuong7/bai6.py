class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def themCanh(self, u, v):
        self.adj[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for u in range(self.V):
            if v in self.adj[u]:
                count += 1
        return count

# Test
g = Graph(5)
g.themCanh(0, 1)
g.themCanh(1, 2)
g.themCanh(2, 0)
g.themCanh(2, 3)
g.themCanh(3, 4)
g.themCanh(4, 0)

print("Số cung vào đỉnh 0:", g.SoCungVao(0))  # Kết quả: 2
print("Số cung vào đỉnh 3:", g.SoCungVao(3))  # Kết quả: 1
