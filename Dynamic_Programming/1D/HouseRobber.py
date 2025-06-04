from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(cost: List[int]) -> int:
            n = len(cost)
            if n == 1:
                return cost[0]
            elif n == 2:
                return max(cost[0], cost[1])

            dp = [0] * (n + 1)
            dp[0] = cost[0]
            dp[1] = max(cost[0], cost[1])

            for index in range(2, n):
                dp[index] = max(dp[index - 2] + cost[index], dp[index - 1])

            return dp[n - 1]

        length = len(nums)
        if length == 1:
            return nums[0]
        return max(dfs(nums[:length - 1]), dfs(nums[1:]))


if __name__ == '__main__':
    sol = Solution()
    ans = sol.rob([2,3,2])
    print(ans)