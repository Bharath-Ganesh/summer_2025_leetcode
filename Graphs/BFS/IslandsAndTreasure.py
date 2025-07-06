from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]

            [3,-1,0,1],
            [2,2,1,-1],
            [1,-1,2,-1],
            [0,-1,3,4]
        """

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            rIndex, cIndex = queue.popleft()
            curr_value = board[rIndex][cIndex]
            dirR = [-1, 0, 0, 1]
            dirC = [0, -1, 1, 0]
            for r, c in zip(dirR, dirC):
                row = rIndex + r
                col = cIndex + c
                if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == -1:
                    continue
                if board[row][col] > curr_value + 1:
                    board[row][col] = curr_value + 1
                    queue.append((row, col))

if __name__ == '__main__':
    board = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],[2147483647, -1, 2147483647, -1],[0, -1, 2147483647, 2147483647]]
    solution = Solution()
    solution.islandsAndTreasure(board)
    print(board)
