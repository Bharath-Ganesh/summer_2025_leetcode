from typing import List


class Solution:
    def length_of_lis_binarysearch(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        temp = [nums[0]]

        for i in range(1, n):
            if nums[i] > temp[len(temp) - 1]:
                temp.append(nums[i])
            else:
                index = self.binary_search(nums[i], temp, 0, len(temp) - 1)
                temp[index] = nums[i]
        ans = len(temp)
        return ans

    def binary_search(self,  num,  arr,low, high):
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] >= num:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = {}

        def dfs(prev_max, ind):

            if ind == n - 1:
                return 1 if nums[ind] > prev_max else 0

            key = (prev_max, ind)
            if key in dp:
                return dp[key]

            # take
            pick, not_pick = 0, 0
            if nums[ind] > prev_max:
                pick = max(1 + dfs(nums[ind], ind + 1),
                           dfs(prev_max, ind + 1)
                        )
            # not take
            else:
                not_pick = dfs(prev_max, ind + 1)
            dp[key] = max(not_pick, pick)
            return dp[key]

        curr_max = float('-inf')
        return dfs(curr_max, 0)

if __name__ == '__main__':
    s = Solution()
    print(s.length_of_lis_binarysearch([10,9,2,5,3,7,101,18]))
