class Solution:

    def frogJump(self, steps):

        n = len(steps)
        dp = [-1] * n
        dp[n - 1] = 0
        def findMinimumCost(index):

            if dp[index] != -1:
                return dp[index]

            one_jump = float('inf')
            two_jump = float('inf')
            if index + 1 < n:
                one_jump = findMinimumCost(index + 1) + abs(steps[index + 1] - steps[index])
            if index + 2 < n:
                two_jump = findMinimumCost(index + 2) + abs(steps[index + 2] - steps[index])
            dp[index] = min(one_jump, two_jump)
            return dp[index]

        return findMinimumCost(0)


if __name__ == '__main__':
    sol = Solution()
    ans = sol.frogJump([10,60, 0, 100])
    print(ans)