from typing import List


class Solution:

    def uniquePathsWithObstaclesTabulation(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    dp[row][col] = 1
                    continue
                elif obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                down, right = 0, 0
                if row - 1 >= 0:
                    down = dp[row - 1][col]
                if col - 1 >= 0:
                    right = dp[row][col - 1]
                dp[row][col] = down + right

        return dp[rows - 1][cols - 1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[-1] * cols for _ in range(rows)]
        if obstacleGrid[rows - 1][cols - 1] == 1:
            return 0
        dp[rows - 1][cols - 1] = 1

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or obstacleGrid[row][col] == 1:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]

            down = dfs(row + 1, col)
            right = dfs(row, col + 1)
            dp[row][col] = (down + right)
            return dp[row][col]

        return dfs(0, 0)


if __name__ == '__main__':
    sol = Solution()
    ans = sol.uniquePathsWithObstaclesTabulation([[0,0,0],[0,1,0],[0,0,0]])
    print(ans)