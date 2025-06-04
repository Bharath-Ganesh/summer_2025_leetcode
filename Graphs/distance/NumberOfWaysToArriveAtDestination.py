import heapq
from collections import defaultdict
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        pq = []
        distance = [float('inf')] * n
        distance[0] = 0
        paths = [0] * n
        paths[0] = 1
        dist, u = 0, 0
        heapq.heappush(pq, (dist, u))
        adj_list = self.construct_adj_list(roads)

        while pq:

            dist, u = heapq.heappop(pq)
            for v, wt in adj_list[u]:
                if dist + wt < distance[v]:
                    paths[v] = paths[u]
                    distance[v] = dist + wt
                    heapq.heappush(pq, (distance[v], v))
                elif dist + wt == distance[v]:
                    paths[v] += paths[u]


        if distance[n - 1] == float('inf'):
            return -1

        return paths[n - 1]

        # Helper function to build adjacency list

    def construct_adj_list(self, roads: List[List[int]]) -> defaultdict:
        adj_list = defaultdict(list)

        # Each edge is [u, v, time], add both directions since it's undirected
        for u, v, wt in roads:
            adj_list[u].append((v, wt))
            adj_list[v].append((u, wt))
        return adj_list

if __name__ == '__main__':
    sol = Solution()
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
                    [4, 6, 2]]
    ans = sol.countPaths(n, roads)
    print(ans)