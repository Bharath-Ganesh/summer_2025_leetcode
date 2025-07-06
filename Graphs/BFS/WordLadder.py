from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        word_set = ["hot","dot","dog","lot","log","cog"]
        STEP - 1
        (hit, 0)

        (hot, 1)

        word_set = ["dot", "dog","lot","log","cog"]
        STEP - 2
        (hot, 1)

        (dot, 2)  (lot, 2)

        word_set = ["dog","log","cog"]
        STEP - 3
        (dot, 2)  (lot, 2)

        (dot, 2)  (lot, 2)
        """
        word_set = set(wordList)
        queue = deque()
        if endWord not in wordList:
            return 0
        word_set.discard(beginWord)
        queue.append((beginWord, 1))
        while queue:

            word, operations = queue.popleft()
            if word == endWord:
                return operations

            for idx in range(len(word)):
                arr = list(word)
                for j in range(26):
                    arr[idx] = chr(ord('a') + j)
                    new_word = "".join(arr)
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, operations + 1))

        return 0


if __name__ == '__main__':
    s = Solution()
    ans = s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
    print(ans)
