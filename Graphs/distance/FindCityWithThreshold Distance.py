from collections import defaultdict
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        adjList:

        STEP - 1
            0    1   2   3
        0   0   inf inf inf
        1   inf inf inf inf
        2   inf inf inf inf
        3   inf inf inf inf

        STEP - 2
            0    1   2   3
        0   0    3  inf inf
        1   inf  0  inf inf
        2   inf inf inf inf
        3   inf inf inf inf
        """
        distance = [[float('inf')] * n for _ in range(n)]
        for u, v, wt in edges:
            distance[u][v] = wt
            distance[v][u] = wt
            distance[u][u] = 0
            distance[v][v] = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if distance[i][k] == float('inf') or distance[k][j] == float('inf'):
                        continue
                    distance_via_k = distance[i][k] + distance[k][j]
                    if distance_via_k <= distanceThreshold and distance_via_k < distance[i][j]:
                        distance[i][j] = distance_via_k

        minimum_path_reachable = n
        city = 0
        for i in range(n):
            path_count = 0
            for j in range(n):
                if i != j and distance[i][j] != float('inf'):
                    path_count += 1

            if path_count <= minimum_path_reachable:
                minimum_path_reachable = path_count
                city = i

        return city


if __name__ == '__main__':
    s = Solution()
    n = 5
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    distanceThreshold = 2
    ans = s.findTheCity(n, edges, distanceThreshold)
    print(ans)