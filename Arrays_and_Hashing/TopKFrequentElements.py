import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,1,1,2,2,3], k = 2
        1-3, 2-2, 3-1
        # Create minheap with size 2
        """
        if k == 0:
            return nums

        freq_map = Counter(nums)
        minheap = []

        for num, freq in freq_map.items():
            if len(minheap) < k:
                heapq.heappush(minheap, (num, freq))
            else:
                if minheap[0][1] < freq:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, (num, freq))

        return [ minheap[index][0] for index in range(len(minheap))]

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([4,1,-1,2,-1,2,3], 2))