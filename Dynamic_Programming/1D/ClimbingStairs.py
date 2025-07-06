class Solution:

    def climbStairs(self, n: int) -> int:
        """
            n - 4
            1 -> 1
            2 -> 2
            3 -> 3
            4 -> 5
            5 -> 8
        """

        if n <= 2:
            return n

        prev_2 = 1
        prev = 2
        possible_ways = 0
        for ways in range(3, n + 1):
            possible_ways = prev + prev_2
            prev_2 = prev
            prev = possible_ways

        return possible_ways

    def climbStairsTabulation(self, n: int) -> int:

        dp = [0 for _ in range(n + 1)]
        if n == 0 or n == 1 or n == 2:
            return n
        dp[1] = 1
        dp[2] = 2

        for step in range(3, n + 1):
            dp[step] = dp[step - 1] + dp[step - 2]

        return dp[n]

    def climbStairsRecursion(self, n: int) -> int:
        dp = [-1 for _ in range(n + 1)]
        def dfs():
            if n <= 2:
                return n

            if dp[n] != -1:
                return dp[n]

            one_step = self.climbStairs(n - 1)
            two_step = 0
            if n >= 2:
                two_step = self.climbStairs(n - 2)
            dp[n] = one_step + two_step
            return dp[n]
        return dfs()


if __name__ == '__main__':
    sol = Solution()
    ans = sol.climbStairs(5)
    print(ans)