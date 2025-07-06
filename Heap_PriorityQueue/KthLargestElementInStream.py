import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.capacity = k
        for num in nums:
            self.addElements(num)

    def addElements(self, num):
        if not self.minHeap or len(self.minHeap) < self.capacity:
            heapq.heappush(self.minHeap, num)
        elif self.minHeap and self.minHeap[0] < num:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, num)

    def add(self, val: int) -> int:
        self.addElements(val)
        return self.minHeap[0]

if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))