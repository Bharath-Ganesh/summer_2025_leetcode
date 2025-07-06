import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        minheap = [(cap, profit) for profit, cap in zip(profits, capital)]
        heapq.heapify(minheap)
        maxheap = []
        initial_capital = w
        while maxheap or minheap:

            while minheap and minheap[0][0] <= initial_capital:
                _, profit = heapq.heappop(minheap)
                heapq.heappush(maxheap, (-profit))

            if maxheap:
                curr_profit = heapq.heappop(maxheap)
                initial_capital += (-curr_profit)
                k -= 1
            else:
                break

        return initial_capital

if __name__ == '__main__':
    s = Solution()
    ans = s.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,9,10])
    print(ans)