import heapq
from collections import defaultdict


class Solution:
    def dijkstra(self, V, edges, src, dest):
        """
        Find shortest path from src to dest using distance's algorithm.
        Returns the shortest path as a list of nodes.
        """

        # Build adjacency list from edges
        adj_list = self.construct_adjlist(edges)

        # Priority Queue: (distance, node)
        pq = [(0, src)]

        # Distance and Parent arrays
        distance = [float('inf')] * V
        parentNode = [-1] * V
        distance[src] = 0

        while pq:
            dist, u = heapq.heappop(pq)

            # Early exit if destination is reached
            if u == dest:
                break

            for v, wt in adj_list[u]:
                if distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt
                    parentNode[v] = u
                    heapq.heappush(pq, (distance[v], v))

        # Reconstruct the shortest path from dest to src
        if distance[dest] == float('inf'):
            return []  # No path exists

        path = []
        node = dest
        while node != -1:
            path.append(node)
            node = parentNode[node]

        path.reverse()  # Reverse to get src → dest order
        return path

    def construct_adjlist(self, edges):
        adj_list = defaultdict(list)
        for u, v, wt in edges:
            adj_list[u].append((v, wt))
            adj_list[v].append((u, wt))  # Undirected graph
        return adj_list


# Sample Test
if __name__ == '__main__':
    s = Solution()
    V = 3
    edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
    src = 2
    dest = 0
    ans = s.dijkstra(V, edges, src, dest)
    print(ans)  # Output: [2, 1, 0]
