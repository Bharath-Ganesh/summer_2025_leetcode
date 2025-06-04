from collections import defaultdict, deque
from typing import List

class Solution:


    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        all_chars = set(''.join(words))

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            # Fix: Detect invalid prefix case
            if len(first) > len(second) and first.startswith(second):
                return ""

            index = self.buildAdjList(first, second)
            if index != -1:
                u = first[index]
                v = second[index]
                if v not in adj_list[u]:
                    adj_list[u].append(v)
                    indegree[v] += 1

        for ch in all_chars:
            if ch not in indegree:
                indegree[ch] = 0

        queue = deque([ch for ch in indegree if indegree[ch] == 0])
        result = []

        while queue:
            ch = queue.popleft()
            result.append(ch)
            for neighbor in adj_list[ch]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(all_chars):
            return ""  # cycle detected

        return ''.join(result)

    def buildAdjList(self, first_word, second_word):
        length = min(len(first_word), len(second_word))
        for i in range(length):
            if first_word[i] != second_word[i]:
                return i
        return -1

if __name__ == '__main__':
    s = Solution()
    ans = s.foreignDictionary(["hrn","hrf","er","enn","rfnn"])
    print(ans)