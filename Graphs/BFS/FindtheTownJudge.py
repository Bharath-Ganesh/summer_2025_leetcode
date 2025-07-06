from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        [[1,3],[1,4],[2,3],[2,4],[4,3]]
        1 -> 3
        1 -> 4
        """
        indegree = [0] * (n + 1)
        for u, v in trust:
            indegree[v] += 1

        town_judge = -1
        for idx in range(1, n + 1):
            if indegree[idx] == (n - 1):
                town_judge = idx
                break
        for u, v in trust:
            if u == town_judge:
                return -1
        return town_judge

if __name__ == '__main__':
    s = Solution()
    ans = s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
    print(ans)