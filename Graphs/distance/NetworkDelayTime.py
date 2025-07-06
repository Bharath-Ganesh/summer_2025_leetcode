import heapq
from collections import defaultdict, deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        """
        BFS Traversal:

        [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        adjList = (v, wt) : u -> v
        [[],
        [(1,1), (3,1)]
        [(4,1)]
        [[]]
        network_time = 0
        [(2, network_time)]
        [(3) (1)] total_time = 1
        [(4)] total_time = 2
        [] total_time = 3 // queue is free = total_time - 1
        """
        adjList = defaultdict(list)
        for u, v, wt in times:
            adjList[u].append((v, wt))

        minheap = []
        heapq.heappush(minheap, (0, k))
        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        while minheap:
            time_required, u = heapq.heappop(minheap)
            for v, wt in adjList[u]:
                if time_required + wt < distance[v]:
                    distance[v] = time_required + wt
                    heapq.heappush(minheap, (distance[v], v))

        max_time = 0
        for i in range(1, n + 1):
            if distance[i] == float('inf'):
                return -1
            max_time = max(max_time, distance[i])
        return max_time


if __name__ == '__main__':
    sol = Solution()
    ans = sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
    print(ans)