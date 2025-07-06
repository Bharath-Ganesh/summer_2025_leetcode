from typing import List

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            nums = [10,1,2,7,6,1,5]
            nums = [1,1,2,5,6,7,10]

        """
        res = []
        curr = []
        candidates.sort(key=lambda x: x)

        def back_track(index, target_sum):
            if target_sum == 0:
                res.append(curr.copy())
                return

            if target_sum < 0 or index == len(candidates):
                return

            for ind in range(index, len(candidates)):
                if ind == index or candidates[ind] != candidates[ind - 1]:
                    if target_sum >= candidates[ind]:
                        curr.append(candidates[ind])
                        back_track(ind + 1, target_sum - candidates[ind])
                        curr.pop()

        back_track(0, target)
        return res

if __name__ == '__main__':
    s = Solution()
    ans = s.combinationSum2([1, 1,2,6,5], 7)
    print(ans)