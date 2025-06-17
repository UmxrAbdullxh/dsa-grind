class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        result = []

        for node1, node2 in edges:
           res = uf.union(node1, node2)
           if len(res) > 0:
            result.append(res)
        return result[len(result)-1]
        

class UnionFind:
    def __init__(self, n):
        # Initialize parent and size arrays
        self.parent = [i for i in range(n + 1)]  # 1-indexed
        self.size = [1] * (n + 1)

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by size
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return [x, y]

        # Always attach smaller tree to larger tree
        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX  # Swap

        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        return []

