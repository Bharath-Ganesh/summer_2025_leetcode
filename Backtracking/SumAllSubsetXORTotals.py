from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Find all the subsequence
        # XOR it
        n = len(nums)
        subsets = []

        def back_track(index, temp):

            if index == n:
                subsets.append(temp.copy())
                return

            temp.append(nums[index])
            back_track(index + 1, temp)
            temp.pop()
            back_track(index + 1, temp)

        back_track(0, [])
        XOR_sum = 0
        for subset in subsets:
            temp = 0
            for element in subset:
                temp = temp ^ element
            XOR_sum += temp
        return XOR_sum
    

if __name__ == '__main__':
    s = Solution()
    ans = s.subsetXORSum([5,1,6])
    print(ans)
