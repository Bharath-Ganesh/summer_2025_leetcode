class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)
        dp = {}

        def backtracking(ind1, ind2):

            if ind1 == m or ind2 == n:
                return 0
            key = (ind1, ind2)
            if key in dp:
                return dp[key]

            pick, not_pick = 0, 0
            if text1[ind1] == text2[ind2]:
                pick = 1 + backtracking(ind1 + 1, ind2 + 1)
            else:
                not_pick = max(backtracking(ind1 + 1, ind2), backtracking(ind1, ind2 + 1))

            dp[key] = max(not_pick, pick)
            return dp[key]

        return backtracking(0, 0)

if __name__ == '__main__':
    s = Solution()
    ans = s.longestCommonSubsequence("abcde", "ace")
    print(ans)
