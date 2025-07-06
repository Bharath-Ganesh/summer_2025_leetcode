from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        max_length_index = 0
        max_length = -1
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] != 0 and nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                    if dp[i] > max_length:
                        max_length = dp[i]
                        max_length_index = i

        res = []
        while max_length_index != parent[max_length_index]:
            res.append(nums[max_length_index])
            max_length_index = parent[max_length_index]
        res.append(nums[max_length_index])
        res.reverse()
        return res



if __name__ == "__main__":
    s = Solution()
    ans = s.largestDivisibleSubset([1,2,4,8])
    print(ans)