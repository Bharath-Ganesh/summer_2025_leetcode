from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = 0

        for j in range(1, amount + 1):
            dp[0][j] = float('inf')

        dp[0][0] = 0
        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(1, amount + 1):
                no_take = dp[i - 1][j]
                take = float('inf')
                if j >= coin:
                    take = 1 + dp[i][j - coin]

                dp[i][j] = min(no_take, take)

        return dp[n][amount]

if __name__ == '__main__':
    s = Solution()
    ans = s.coinChange(coins=[1, 2, 5], amount=11)
    print(ans)
