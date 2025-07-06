from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_dict_lookUp = set(wordDict)
        res = []
        def backtrack(idx, visited, temp):
            if idx == len(s):
                res.append(" ".join(temp.copy()))
                return

            for word in word_dict_lookUp:
                length = len(word)
                if idx + length <= len(s) and s[idx: idx + length] == word:
                    temp.append(word)
                    backtrack(idx + length, visited, temp)
                    temp.pop()

        backtrack(0, set(), [])
        return res

if __name__ == "__main__":
    sol = Solution()
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(sol.wordBreak(s, wordDict))