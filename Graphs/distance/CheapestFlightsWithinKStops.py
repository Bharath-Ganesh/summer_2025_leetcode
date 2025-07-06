import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        n = 4, flights =
        [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
        src = 0, dst = 3, k = 1

             0
        100/   \  100
          /     \
         1 -----> 2
          \ 100 /
           \   / 200
         600\ /


        STEP 0:
        (distance, node, k)
        [0, 0, 0]
        STEP 1
        k = 1: (distance, node, k)
        [(100, 1, 1),]
         0   1  2   3
        [0 100 inf inf]

        STEP 2
        k = 2:
        (100, 1, 1) => [(200, 2, 2), (700, 3, 2)]
         0   1  2   3
        [0 100 200 700]

        STEP 3
        k = :
        (100, 1, 1) => [(200, 2, 2), (700, 3, 2)]
         0   1  2   3
        [0 100 200 700]
        """

        minheap = []
        heapq.heappush(minheap, (0, src, 0))
        adjList = defaultdict(list)
        for u, v, w in flights:
            adjList[u].append((v, w))

        distance = [float('inf')] * n
        distance[src] = 0
        while minheap:
            stops, u, dist = heapq.heappop(minheap)

            if stops > k:
                continue

            for v, wt in adjList[u]:
                if dist + wt < distance[v]:
                    if stops == k and v != dst:
                        continue
                    distance[v] = dist + wt
                    heapq.heappush(minheap, (stops + 1, v, distance[v]))

        if distance[dst] == float('inf'):
            return -1

        return distance[dst]


if __name__ == '__main__':
    s = Solution()
    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    ans = s.findCheapestPrice(n, flights, src, dst, k)
    print(ans)