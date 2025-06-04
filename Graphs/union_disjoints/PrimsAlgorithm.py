import heapq
from typing import List
from collections import defaultdict


class Solution:
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        visited = [False] * V
        min_heap = []
        min_sum = 0

        adj_list = self.build_adjlist(adj)

        # Start Prim's algorithm from node 0
        heapq.heappush(min_heap, (0, 0))  # (weight, node)

        while min_heap:
            wt, u = heapq.heappop(min_heap)

            if visited[u]:
                continue  # Skip already visited nodes

            visited[u] = True
            min_sum += wt  # Include edge in MST

            for v, edge_wt in adj_list[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (edge_wt, v))

        return min_sum

    def build_adjlist(self, edges: List[List[int]]):
        adj_list = defaultdict(list)
        for u, v, wt in edges:
            adj_list[u].append((v, wt))
            adj_list[v].append((u, wt))  # Because it's undirected
        return adj_list


# Example Usage
if __name__ == '__main__':
    s = Solution()
    V = 3
    edges = [[0, 1, 5], [0, 2, 1], [1, 2, 3]]
    ans = s.spanningTree(V, edges)
    print(ans)  # Expected output: 4 (edges: 0-2 (1) and 2-1 (3))
