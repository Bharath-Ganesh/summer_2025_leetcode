from typing import List

class Solution:
    INF = 100000000  # Representing unreachable paths
    def floydWarshall(self, distance: List[List[int]]) -> List[List[int]]:

        V = len(distance)

        for i in range(V):
            for j in range(V):
                for k in range(V):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        for i in range(V):
            for j in range(V):
                if distance[i][j] == self.INF:
                    distance[i][j] = -1 # negative cycle

        return distance


if __name__ == '__main__':
    s = Solution()
    INF = 100000000  # Representing unreachable paths
    dist = [
        [0, 4, INF, 5, INF],
        [INF, 0, 1, INF, 6],
        [2, INF, 0, 3, INF],
        [INF, INF, 1, 0, 2],
        [1, INF, INF, 4, 0]
    ]
    ans = s.floydWarshall(dist)
    for row in ans:
        print(row)
