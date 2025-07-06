import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        intervals =
        [[1,6],[1,9],[4,5],[5,8],[8,10]]
        queries = [3,3,7,9,9] <= [7,9,3,9,3]
        [[6,6],[9,6]]

                        4.4
                3...............6
            2...........4
        1...............4

        [[4,4],[3,4]]
        [3,3,1,4]
        """
        intervals.sort(key=lambda x: (x[0], x[1]))
        minheap = []
        idx = 0
        n = len(intervals)
        query_lookup = defaultdict(int)
        for query in sorted(queries):
            while idx < n and intervals[idx][0] <= query:
                interval = (intervals[idx][1] - intervals[idx][0]) + 1
                heapq.heappush(minheap, (interval, intervals[idx][1]))
                idx += 1

            while minheap and minheap[0][1] < query:
                heapq.heappop(minheap)

            query_lookup[query] = minheap[0][0] if minheap else -1

        return [query_lookup[query] for query in queries]

if __name__ == '__main__':
    sol = Solution()
    ans = sol.minInterval(intervals = [[4,5],[5,8],[1,9],[8,10],[1,6]], queries = [7,9,3,9,3])
    print(ans)