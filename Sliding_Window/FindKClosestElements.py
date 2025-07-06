import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        """
            x = 7
             0,1,2, 3, 4, 5
            [4,6,8,10,11,14]

            k = 2
            [4,6,100,101,102,103]
        """

        def binary_search(low, high):
            while low < high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    return mid
                if arr[mid] > x:
                    high = mid
                else:
                    low = mid + 1
            return low

        pos_of_x = binary_search(0, len(arr) - 1)
        left_extreme = max(0, pos_of_x - k)
        right_extreme = min(len(arr) - 1, pos_of_x + k)
        maxheap = []
        for i in range(left_extreme, right_extreme + 1):
            diff = abs(arr[i] - x)
            if not maxheap or len(maxheap) < k:
                heapq.heappush(maxheap, (-1 * diff, arr[i]))
            else:
                if maxheap and maxheap[0][0] < -1 * diff:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap, (-1 * diff, arr[i]))

        res = [num for (diff, num) in maxheap]
        res.reverse()
        return res


if __name__ == '__main__':
    s = Solution()
    ans = s.findClosestElements([4,6,8,10,11,14], 4, 7)
    print(ans)