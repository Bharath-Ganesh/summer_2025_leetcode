from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        low = min, high = sum()
            [7,2,5,10,8] ; k = 2

        """

        low, high =  float("-inf"), 0
        for num in nums:
            low = max(low, num)
            high += num

        ans = -1
        while low <= high:
            split_sum = (low + high) // 2
            if self.isSumPossible( nums, k, split_sum):
                ans = split_sum
                high = split_sum - 1
            else:
                low = split_sum + 1
        return ans

    def isSumPossible(self, nums, k, split_sum):

        total_sum = 0
        total_count = 0
        for num in nums:
            if total_sum + num > split_sum:
                total_count += 1
                total_sum = num
            else:
                total_sum += num
        if total_sum:
            total_count += 1
        return total_count <= k


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray(nums=[7, 2, 5, 10, 8], k=2))
