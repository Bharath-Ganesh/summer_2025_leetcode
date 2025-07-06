from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        slow, fast = nums[slow], nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break

        return slow

if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([1,3,4,2,2]))
