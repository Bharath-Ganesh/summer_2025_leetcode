from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        """
        [0,4,3,0,4]
         0 1 2 3 4
        [0,0,3,4,4]
        """

        nums.sort()

        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            nums_left = len(nums) - mid
            if nums[mid] >= nums_left:
                if mid == 0 or nums[mid] - 1 < nums_left:
                    return nums_left
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.specialArray([0,4,3,0,4]))