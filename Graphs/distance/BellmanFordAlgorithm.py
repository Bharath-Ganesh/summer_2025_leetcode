import heapq
from collections import defaultdict, deque


# User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        # distance, node = 0, 0
        distance = [100000000] * V
        distance[src] = 0
        for _ in range(V - 1):
            for u, v, wt in edges:
                if distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt

        for u, v, wt in edges:
            if distance[u] + wt < distance[v]:
                return -1

        return distance



if __name__ == '__main__':
    s = Solution()
    V = 3
    edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
    src = 0
    ans = s.bellmanFord(V, edges, src)
    print(ans)
