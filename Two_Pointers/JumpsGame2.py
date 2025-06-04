from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        """
            jumps += 1
                            L R
            nums = [2,[3,1][1,4],1,1,1,1]
        """
        n = len(nums)
        left, right = 0, 0
        jumps = 0
        while right < n - 1:
            max_distance = right
            # [0,1,2,3,4,5,6]
            # [3,4,3,2,5,4,3]
            # jumps = 1
            # left = 1
            # right = 3
            for pos in range(left, right + 1):
                max_distance = max(max_distance, pos + nums[pos])

            jumps += 1
            left = right + 1
            right = max_distance

        return jumps


if __name__ == '__main__':
    sol = Solution()
    ans = sol.jump([3,4,3,2,5,4,3])
    print(ans)