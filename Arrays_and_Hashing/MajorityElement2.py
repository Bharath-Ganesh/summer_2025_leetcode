from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Find all elements appearing more than ⌊n/3⌋ times.
        Uses Boyer–Moore variant: two candidates, two passes.

        Time:  O(n)
        Space: O(1)
        """
        if not nums:
            return []

        # 1) Candidate selection
        cand1 = cand2 = None
        count1 = count2 = 0
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # 2) Verification pass
        res = []
        threshold = len(nums) // 3
        # reset counts
        count1 = count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        if count1 > threshold:
            res.append(cand1)
        if count2 > threshold:
            res.append(cand2)

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 3, 3,3,3,3,3]))  # [3]
