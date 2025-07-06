import heapq
from collections import defaultdict
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        adjList = defaultdict(list)
        for u, v, wt in roads:
            adjList[u].append((v, wt))
            adjList[v].append((u, wt))

        distance = [float('inf')] * n
        num_ways = [0] * n
        minheap = []
        heapq.heappush(minheap, (0, 0))

        while minheap:
            dist, u = heapq.heappop(minheap)
            for v, wt in adjList[u]:
                if dist + wt < distance[v]:
                    distance[v] = dist + wt
                    num_ways[v] = 1
                elif dist + wt == distance[v]:
                    num_ways[v] = (num_ways[v] + num_ways[u]) % MOD

        return -1 if distance[n - 1] == float('inf') else num_ways[n - 1]

if __name__ == '__main__':
    sol = Solution()
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
                    [4, 6, 2]]
    ans = sol.countPaths(n, roads)
    print(ans)