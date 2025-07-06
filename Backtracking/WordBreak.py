from typing import List


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_set = set(wordDict)           # O(1) lookups
        failed = set()                     # memo of start indices that fail

        def dfs(start: int) -> bool:
            if start == len(s):            # base case: consumed all chars
                return True
            if start in failed:           # already known to fail
                return False

            for end in range(start, len(s)):
                segment = s[start:end + 1]
                if segment in dict_set:
                    if dfs(end + 1):
                        return True
            failed.add(start)             # mark this start as unsolvable
            return False

        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    ans = sol.wordBreak(s, ["leet", "codes"])
    print(ans)