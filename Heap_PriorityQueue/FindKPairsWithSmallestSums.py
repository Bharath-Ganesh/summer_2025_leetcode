import heapq
from typing import List

"""
nums1   =   [1, 7, 11], 
nums2   =   [2, 4, 6]

(0,1), (0,2)
"""
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        minheap = []
        heapq.heappush(minheap, (nums1[0] + nums2[0], 0, 0))
        visited = set()
        visited.add((0, 0))
        res = []
        while minheap and k:
            k -= 1
            _, i, j = heapq.heappop(minheap)
            res.append([nums1[i], nums2[j]])
            if k == 0:
                break
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                curr_sum = nums1[i + 1] + nums2[j]
                visited.add((i + 1, j))
                heapq.heappush(minheap, (curr_sum, i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                curr_sum = nums1[i] + nums2[j + 1]
                visited.add((i, j + 1))
                heapq.heappush(minheap, (curr_sum, i, j + 1))
        return res


if __name__ == '__main__':
    s = Solution()
    ans = s.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k= 3)
    print(ans)
