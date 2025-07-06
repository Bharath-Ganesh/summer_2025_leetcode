from typing import List


class Solution:
    def coin_permutation(self, coins: List[int], amount: int) -> int:
     
        dp = [0] * (amount + 1)
        dp[0] = 1
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] += dp[amt - coin]

        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    ans = s.coin_permutation([2, 3, 5], 10)
    print(ans)