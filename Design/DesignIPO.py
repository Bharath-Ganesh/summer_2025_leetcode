import heapq
from collections import deque
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 1. Build a min-heap of (required_capital, profit)
        min_cap_heap = [(cap, prof) for prof, cap in zip(profits, capital)]
        heapq.heapify(min_cap_heap)

        # 2. Max-heap for profits (negated)
        max_profit_heap: List[int] = []

        current_capital = w
        for _ in range(k):
            # 3. Unlock all affordable projects
            while min_cap_heap and min_cap_heap[0][0] <= current_capital:
                cap_req, prof = heapq.heappop(min_cap_heap)
                heapq.heappush(max_profit_heap, -prof)

            # 4. If none affordable, break early
            if not max_profit_heap:
                break

            # 5. Invest in the most profitable project
            current_capital += -heapq.heappop(max_profit_heap)

        return current_capital

if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))