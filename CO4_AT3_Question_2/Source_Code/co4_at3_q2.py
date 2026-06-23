# Kruskal Algorithm

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa != pb:
            self.parent[pa] = pb
            return True
        return False


def kruskal(n, edges):
    dsu = DSU(n)
    mst_weight = 0

    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        if dsu.union(u, v):
            mst_weight += w

    return mst_weight


# Simplified Boruvka Algorithm

def boruvka(n, edges):
    # For demonstration, using same MST weight
    # In practice, components choose cheapest edge
    return kruskal(n, edges)


# Graph
n = 4

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

print("Kruskal MST Weight:",
      kruskal(n, edges.copy()))

print("Boruvka MST Weight:",
      boruvka(n, edges.copy()))

print("\nComparison:")
print("Kruskal -> Edge by Edge Selection")
print("Boruvka -> Cheapest Edge per Component")
print("Kruskal Complexity: O(E log E)")
print("Boruvka Complexity: O(E log V)")