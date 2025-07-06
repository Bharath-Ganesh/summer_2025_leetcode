import heapq
from typing import List


class DisjoinSet:

    def __init__(self, total_nodes):
        self.parent = [parentNode for parentNode in range(total_nodes)]
        self.size = [1] * total_nodes

    def findUltimateParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):

        parentU = self.findUltimateParent(u)
        parentV = self.findUltimateParent(v)
        if parentU == parentV:
            return
        if self.size[parentU] >= self.size[parentV]:
            self.parent[parentV] = parentU
            self.size[parentU] += self.size[parentV]
        else:
            self.parent[parentU] = parentV
            self.size[parentV] += self.size[parentU]

    def areConnected(self, u, v):
        parentU = self.findUltimateParent(u)
        parentV = self.findUltimateParent(v)
        return parentU == parentV


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        # code here
        disjoinSet = DisjoinSet(V)
        spanningTreeSum = 0
        minheap = []

        for u, v, wt in adj:
            heapq.heappush(minheap, (wt, u, v))

        while minheap:
            wt, u, v = heapq.heappop(minheap)
            if not disjoinSet.areConnected(u, v):
                disjoinSet.unionBySize(u, v)
                spanningTreeSum += wt
        return spanningTreeSum


# --------------------------
# Test Case
# --------------------------

if __name__ == "__main__":
    V = 3  # Number of vertices
    edges = [
        [0, 1, 5],
        [1, 2, 3],
        [0, 2, 1]
    ]

    sol = Solution()
    result = sol.spanningTree(V, edges)
    print("Minimum Spanning Tree Total Weight:", result)