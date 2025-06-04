import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        pq = []
        distance = [float('inf')] * n
        distance[src] = 0
        stops, dist, u = 0, 0, src
        heapq.heappush(pq, (stops, dist, u))
        adj_list = self.construct_adj_list(flights)

        while pq:
            stops, dist, u = heapq.heappop(pq)
            if stops > k:
                continue
            for v, wt in adj_list[u]:
                if distance[u] + wt < distance[v]:
                    if stops == k and v != dst:
                        continue
                    distance[v] = distance[u] + wt
                    heapq.heappush(pq, (stops + 1, distance[v], v))

        if distance[dst] == float('inf'):
            return -1

        return distance[dst]

    # Helper function to build adjacency list
    def construct_adj_list(self, edges: List[List[int]]) -> defaultdict:
        adj_list = defaultdict(list)

        # Each edge is [u, v, time], add both directions since it's undirected
        for u, v, wt in edges:
            adj_list[u].append((v, wt))
        return adj_list

if __name__ == '__main__':
    s = Solution()
    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    ans = s.findCheapestPrice(n, flights, src, dst, k)
    print(ans)