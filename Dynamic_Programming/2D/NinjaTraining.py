class Solution:

    def ninja_training(self, ninja_score):
        rows = len(ninja_score)
        cols = len(ninja_score[0])
        dp = [[-1] * cols for _ in range(rows)]
        for c2 in range(0, cols):
            dp[rows - 1][c2] = ninja_score[rows - 1][c2]

        def findMaximumScore(row, col):

            if dp[row][col] != -1:
                return dp[row][col]

            points = float('-inf')
            for c1 in range(cols):
                if c1!= col:
                    points = max(points, findMaximumScore(row + 1, c1))

            dp[row][col] =  ninja_score[row][col] + points
            return dp[row][col]

        maximum_points = float('-inf')
        for c in range(cols):
            maximum_points =  max(maximum_points, findMaximumScore(0, c))
        print(dp)
        return maximum_points


if __name__ == '__main__':
    sol = Solution()
    ans = sol.ninja_training([[10, 20, 30],[100, 60, 40],[10, 30, 100]])
    print(ans)