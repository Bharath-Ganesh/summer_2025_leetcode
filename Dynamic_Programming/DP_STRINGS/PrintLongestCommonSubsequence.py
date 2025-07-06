from typing import List


class Solution:
    def printLongestCommonSubsequence(self, text1: str, text2: str) -> int:

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

        ind1, ind2 = m, n
        res = ""
        while ind1 > 0 or ind2 > 0:
            if text1[ind1 - 1] == text2[ind2 - 1]:
                res = res + text1[ind1 - 1]
                ind1 -= 1
                ind2 -= 1
            elif dp[ind1 - 1][ind2] > dp[ind1][ind2 - 1 ]:
                ind1 -= 1
            else:
                ind2 -= 1
        return res[::-1]

if __name__ == '__main__':
    s = Solution()
    ans = s.printLongestCommonSubsequence("abcde", "ace")
    print(ans)
