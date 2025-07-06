from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []

        def twoSum(rest: int, left: int, right: int, temp: List[int]):
            while left < right:
                s = nums[left] + nums[right]
                if s == rest:
                    res.append(temp + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates after finding a pair
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < rest:
                    left += 1
                else:
                    right -= 1

        def k_sum(start: int, k: int, curr_sum: int, temp: List[int]):
            if k == 2:
                twoSum(-curr_sum, start, len(nums) - 1, temp)
                return

            for idx in range(start, len(nums) - k + 1):
                # skip duplicates at this level
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue
                temp.append(nums[idx])
                k_sum(idx + 1, k - 1, curr_sum - nums[idx], temp)
                temp.pop()

        k_sum(0, 4, target, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, 2], 0))
    # ➞ [[-1, 0, 0, 1]]
    print(s.fourSum([1, 0, -1, 0, 2, -2], 0))
    # ➞ [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
