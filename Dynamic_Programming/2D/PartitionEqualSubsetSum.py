from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for row in range(n + 1):
            for col in range(target + 1):

                if row == 0 and col == 0:
                    dp[row][col] = True
                elif row == 0:
                    dp[row][col] = False
                elif col == 0:
                    dp[row][col] = True
                else:
                    not_pick = dp[row - 1][col]
                    pick = False
                    if col >= nums[row - 1]:
                        pick = dp[row - 1][col - nums[row - 1]]
                    dp[row][col] = pick or not_pick

        return dp[n][target]

if __name__ == "__main__":
    s = Solution()
    ans = s.canPartition([1,5,11,5])
    print(ans)