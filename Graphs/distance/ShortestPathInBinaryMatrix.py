from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        """
        [1,0,0],
        [1,1,0],
        [1,1,0]
        """
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        queue = deque()
        queue.append((0, 0))
        distance = [[float("inf")] * cols for _ in range(rows)]
        distance[0][0] = 1
        while queue:
            r, c = queue.popleft()
            # TDL U TDR
            dirR = [-1, -1, -1, 0, 0, 0, 1,  1,1]
            dirC = [-1,  0, 1, -1, 0, 1, -1, 0,1]
            for i in range(9):
                row = r + dirR[i]
                col = c + dirC[i]

                if row == r and col == c:
                    continue
                if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 1:
                    continue

                if distance[r][c] + 1 < distance[row][col]:
                    distance[row][col] = distance[r][c] + 1
                    queue.append((row, col))

        return distance[rows - 1][cols - 1]

if __name__ == '__main__':
    sol = Solution()
    ans = sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
    print(ans)