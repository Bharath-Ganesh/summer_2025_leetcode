# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()

        def dfs(root):
            # 1
            res = []
            if root and root.val not in visited:
                # root.val = 1
                visited.add(root.val)
                # neighbors of 1 : 2 and 4
                for adjNode in root.neighbors:
                    neighborNodes = dfs(adjNode)
                    res.append(neighborNodes)
                    return res
            return Node(root.val)

        return dfs(node)

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Helper to build the graph from adjacency list
def build_graph(adjList: List[List[int]]) -> List[Node]:
    # Create all nodes
    nodes = [Node(i + 1) for i in range(len(adjList))]
    # Attach neighbors
    for i, neigh_indices in enumerate(adjList):
        nodes[i].neighbors = [nodes[j - 1] for j in neigh_indices]
    return nodes

# Example input



if __name__ == '__main__':
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    nodes = build_graph(adjList)
    # Display each node and its neighbors
    for node in nodes:
        neighbor_vals = [n.val for n in node.neighbors]
        print(f"Node {node.val} neighbors -> {neighbor_vals}")
    s = Solution()
    s.cloneGraph(nodes[0])