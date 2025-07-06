from collections import deque, defaultdict
from typing import List


class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        word_set.discard(beginWord)

        # track parents explicitly
        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()
            # remove all current-level words from set to prevent revisits
            word_set -= level
            for word in level:
                for idx in range(len(word)):
                    arr = list(word)
                    for j in range(26):
                        arr[idx] = chr(ord('a') + j)
                        nxt = "".join(arr)
                        if nxt in word_set:
                            parents[nxt].append(word)  # record parent link
                            if nxt == endWord:
                                found = True
                            next_level.add(nxt)
            level = next_level

        # backtrack from endWord via parents map
        res = []

        def dfs(path, w):
            if w == beginWord:
                res.append(path[::-1])
                return
            for p in parents[w]:
                dfs(path + [p], p)

        dfs([endWord], endWord)
        return res


if __name__ == '__main__':
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution.findLadders(beginWord=beginWord, endWord=endWord, wordList=wordList))
