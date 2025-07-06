import heapq
from collections import defaultdict, deque


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

    # Returns shortest distances from src to all other vertices
    def dijkstra2(self, V, edges, src):
        # code here

        """
         V = 3,
         edges[][] = [
         [0, 1, 1], [1, 2, 3], [0, 2, 6]],
         src = 2
        """

        adjList = {}
        for u, v, wt in edges:
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []

            adjList[u].append((v, wt))
            adjList[v].append((u, wt))

        dist = [float('inf')] * V
        dist[src] = 0
        queue = deque()
        queue.append((src, 0))

        while queue:
            u, distance = queue.popleft()
            for v, wt in adjList[u]:
                if dist[u] == float('inf'):
                    continue
                elif dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    queue.append((v, dist[v]))

        return dist


if __name__ == '__main__':
    s = Solution()
    V = 3
    edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
    src = 2
    ans = s.dijkstra(V, edges, src)
    print(ans)
