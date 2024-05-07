class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def themCanh(self, u, v):
        self.adj[u].append(v)

    def SoCungRa(self, v):
        return len(self.adj[v])

# Test
g = Graph(5)
g.themCanh(0, 1)
g.themCanh(1, 2)
g.themCanh(2, 0)
g.themCanh(2, 3)
g.themCanh(3, 4)
g.themCanh(4, 0)

print("Số cung ra khỏi đỉnh 0:", g.SoCungRa(0))  # Kết quả: 1
print("Số cung ra khỏi đỉnh 3:", g.SoCungRa(3))  # Kết quả: 1
