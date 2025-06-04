import heapq
from collections import defaultdict


class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here

        adj_list = self.construct_adjlist(edges)
        pq = []
        # distance, node = 0, 0
        heapq.heappush(pq, (0, src))
        distance = [float('inf')] * V
        distance[src] = 0

        while pq:

            dist, u = heapq.heappop(pq)
            for v, wt in adj_list[u]:
                if distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt
                    heapq.heappush(pq, (distance[v], v))

        return distance

    def construct_adjlist(self, edges):

        adj_list = defaultdict(list)
        for u, v, wt in edges:
            adj_list[u].append((v, wt))
            adj_list[v].append((u, wt))
        return adj_list


if __name__ == '__main__':
    s = Solution()
    V = 3
    edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
    src = 2
    ans = s.dijkstra(V, edges, src)
    print(ans)
