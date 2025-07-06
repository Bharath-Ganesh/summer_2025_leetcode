from typing import List

class TrieNode:
    __slots__ = ("children", "is_word")
    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.is_word = False   # True if path to here spells a dict word

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for w in words:
            node = self.root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True



class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        dp = {n: 0}
        trie = Trie(dictionary).root

        def dfs(idx: int) -> int:
            # return cached if seen
            if idx in dp:
                return dp[idx]

            # 1) Try all dictionary matches first
            best = 1 + dfs(idx + 1)
            curr = trie
            for j in range(idx, n):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.is_word:
                    best = min(best, dfs(j + 1))
                # no extra chars for this span
            # 2) Then consider skipping the current char

            dp[idx] = best
            return best

        return dfs(0)


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.minExtraChar("leetscode", ["leet","code","leetcode"]))  # → 1
