class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n  # Start each component with size 1

    def findUParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, node1, node2):
        pu = self.findUParent(node1)
        pv = self.findUParent(node2)
        if pu == pv:
            return
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

    def areConnected(self, u: int, v: int) -> bool:
        return self.findUParent(u) == self.findUParent(v)


if __name__ == '__main__':
    s = DisjointSet(9)

    edges = [
        (1, 2), (1, 3), (2, 4), (3, 4),
        (2, 5), (5, 6), (6, 8), (8, 7), (5, 7)
    ]


    print("Are 1 and 6 connected?", s.areConnected(1, 6))  # True
    print("Are 1 and 8 connected?", s.areConnected(1, 8))  # True
    print("Are 4 and 6 connected?", s.areConnected(4, 6))  # True
    print("Are 5 and 7 connected?", s.areConnected(5, 7))  # True

    for u, v in edges:
        s.unionBySize(u, v)

    print("Are 1 and 7 connected?", s.areConnected(1, 7))  # True
    print("Are 1 and 6 connected?", s.areConnected(1, 6))  # True
    print("Are 1 and 8 connected?", s.areConnected(1, 8))  # True
    print("Are 4 and 6 connected?", s.areConnected(4, 6))  # True
    print("Are 5 and 7 connected?", s.areConnected(5, 7))  # True