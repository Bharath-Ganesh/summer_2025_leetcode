from collections import deque
from typing import List


class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        """
            [[1,2,2],      [[0, ,inf,inf]
             [3,8,2],       [inf,inf,inf],
             [5,3,5]]       [inf,inf,inf]

            [[1,2,2],      [[0, ,1, 1]
             [3,8,2],       [2,  5, 1],
             [5,3,5]]       [2, 2 , 2]
        """

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        queue.append((0, 0))

        minimumEffortPath = [[float("inf")] * cols for _ in range(rows)]
        minimumEffortPath[0][0] = 0
        while queue:
            r, c = queue.popleft()
            # U L D
            dirR = [-1, 0, 1, 0]
            dirC = [0, -1, 0, 1]
            for i in range(4):
                row = r + dirR[i]
                col = c + dirC[i]
                if row < 0 or col < 0 or row >= rows or col >= cols:
                    continue
                height_diff = abs(grid[row][col] - grid[r][c])
                present_diff = max(minimumEffortPath[r][c], height_diff)
                if present_diff < minimumEffortPath[row][col]:
                    minimumEffortPath[row][col] = present_diff
                    queue.append((row, col))

        return minimumEffortPath[rows - 1][cols - 1]

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])
    print(ans)