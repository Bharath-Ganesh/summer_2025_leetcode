from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])

        dp = [0] * (n + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for index in range(2, n):
            dp[index] = cost[index] + min(dp[index - 2], dp[index - 1])

        return min(dp[n - 2], dp[n - 1])

if __name__ == '__main__':
    sol = Solution()
    ans = sol.minCostClimbingStairs(cost=[1,100,1,1,1,100,1,1,100,1])
    print(ans)