from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_dict_lookUp = set(wordDict)

        def backtrack(idx):
            if idx == len(s):
                return True

            for word in word_dict_lookUp:
                length = len(word)
                if idx + length <= len(s) and s[idx: idx + length] in word_dict_lookUp:
                    if backtrack(idx + length):
                        return True

            return False

        return backtrack(0)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.wordBreak(s = "leetcode", wordDict = ["leet","code"])
    print(ans)