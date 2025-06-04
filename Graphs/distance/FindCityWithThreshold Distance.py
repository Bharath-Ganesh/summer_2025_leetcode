from collections import defaultdict
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = 10**8
        x= defaultdict(list)
        # Step 1: Initialize distance matrix
        distance = [[INF] * n for _ in range(n)]
        for i in range(n):
            distance[i][i] = 0  # Distance from a node to itself is 0

        # Step 2: Fill in initial edge weights (undirected)
        for u, v, wt in edges:
            distance[u][v] = wt
            distance[v][u] = wt

        # Step 3: Floyd-Warshall all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        # Step 4: Find the city with the smallest number of reachable cities within threshold
        city = 0
        min_count = n + 1
        for i in range(n):
            count = 0
            for j in range(n):
                if i!=j and distance[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_count:  # break ties by larger city number
                min_count = count
                city = i

        return city


if __name__ == '__main__':
    s = Solution()
    n = 5
    edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    distanceThreshold = 2
    ans = s.findTheCity(n, edges, distanceThreshold)
    print(ans)