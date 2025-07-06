# User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_length = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[j - 1] == s2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0
                max_length = max(max_length, dp[i][j])
        return max_length

if __name__ == '__main__':
    sol = Solution()
    s1 = "ABCDGH"
    s2 = "ACDGHR"
    ans = sol.longestCommonSubstr(s1, s2)
    print(ans)
