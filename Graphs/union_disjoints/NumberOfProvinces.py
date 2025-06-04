from typing import List


class DisjointSet:

    def __init__(self, n):
        self.size = [0] * n
        self.parent = [i for i in range(n)]

    def unionBySize(self, node1, node2):
        pu = self.findUltimateParent(node1)
        pv = self.findUltimateParent(node2)
        if pu == pv:
            return
        if self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv

    def findUltimateParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUltimateParent(self.parent[node])  # path compression
        return self.parent[node]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ds = DisjointSet(n)

        # adj_list = self.build_adjlist(isConnected)

        for u in range(n):
            for v in range(n):
                if u != v and isConnected[u][v] == 1:
                    ds.unionBySize(u, v)

        dis_connected = 0
        for node, parent_node in enumerate(ds.parent):
            if parent_node == node:
                dis_connected += 1

        return dis_connected


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(Solution().findCircleNum(isConnected))
