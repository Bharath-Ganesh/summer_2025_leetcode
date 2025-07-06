from typing import List


class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        dp : List[List[int]] = self.longestCommonSubsequence(text1, text2)
        m, n = len(text1), len(text2)
        m, n = m, n
        res = ""
        while m > 0 and n > 0:
            if text1[m - 1] == text2[n - 1]:
                res += text1[m - 1]
                m -= 1
                n -= 1
            # upward
            elif dp[m - 1][n] > dp[m][n - 1]:
                res += text1[m - 1]
                m -= 1

            else:
                res += text2[n - 1]
                n -= 1


        if m > 0:
            res += text1[m - 1]

        if n > 0:
            res += text2[n - 1]

        return res[::-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match → extend the previous diagonal subsequence
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Otherwise, take the max of dropping one character from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp

if __name__ == '__main__':
    sol = Solution()
    ans = sol.shortestCommonSupersequence("cab","abac"  )
    print(ans)