from typing import List


class Solution:
    """
        1st case
        10
        [3, 6, 8, 9, 11]        => 5
        [1, 2, 4, 6, 10]        => 5
        3,6,   | 8,9,11
        1,2,4  | 6,10  // min

        0   1  2  3  4  5  6  7  8   9
        [1, 2, 3, 4, 6, 6, 8, 9, 10, 11]


        [3, 6, 8]                      => 3
        [1, 2, 4, 6, 9, 10, 11]        => 5

        0   1  2  3  4  5  6  7  8   9
        [1, 2, 3, 4, 6, 6, 8, 9, 10, 11]

        [3, 6, 8]                       => 3
        [1, 2, 4, 6, 9, 10]             => 6
        3 , 6, 8         |  max
        1, 2             |  4, 6, 9, 10
        0   1  2  3  4  5  6  7  8
        [1, 2, 3, 4, 6, 6, 8, 9, 10]
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 or not nums2:
            return -1

        n1 = len(nums1)
        n2 = len(nums2)
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        low, high = 0, n1
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = ((n1 + n2 + 1) // 2) - cut1

            left1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]  # 1
            right1 = float("inf") if cut1 == n1 else nums1[cut1]  # 2
            left2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]  # 3
            right2 = float("inf") if cut2 == n2 else nums2[cut2]  # 4

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2 == 0:  # even
                    return (max(left1, left2) + min(right2, right1)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
















