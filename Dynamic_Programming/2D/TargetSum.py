from typing import List


class Solution:

    def findTargetSumTabulation(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for row in range(n + 1):
            dp[row][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                val = nums[i - 1]
                not_pick = dp[i - 1][j]
                pick = False
                if j >= val:
                    pick = dp[i - 1][j - val]
                dp[i][j] = not_pick or pick

        print(dp)
        return dp[n][target]


    def findTargetSum(self, nums: List[int], target: int) -> int:

        def dfs(index, sum):
            if sum < 0:
                return False
            if index == len(nums) - 1:
                if sum == nums[index]:
                    return True
                return False

            pick = dfs(index + 1, sum - nums[index])
            not_pick = dfs(index + 1, sum)
            return pick or not_pick

        return dfs(0, target)


if __name__ == '__main__':
    sol = Solution()
    ans = sol.findTargetSumTabulation([4,2,7,1,3], 10)
    print(ans)