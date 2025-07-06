from collections import defaultdict
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        """
            [1,2,3] => [1,2,3]
            [1,2,1] => [1,2,1]
            [1,2,4,3,2,2,1, 1] => [1,2,3,1,1,2,1,1]
            [1,2,3,2              1] # First I can fill the extremre positions
        """


        n = len(ratings)
        if n < 1:
            return 0
        sum_candies = 1
        index = 1
        while index < n:

            if ratings[index] == ratings[index - 1]:
                sum_candies += 1
                index += 1
                continue
            # Assume there's an increasing slope
            upward_slope_peak = 1
            while index < n and ratings[index] > ratings[index - 1]:
                upward_slope_peak += 1
                sum_candies += upward_slope_peak
                index += 1

            downward_slope = 1
            while index < n and ratings[index] < ratings[index - 1]:
                sum_candies += downward_slope
                downward_slope += 1
                index += 1

            if downward_slope >= upward_slope_peak:
                sum_candies += (downward_slope - upward_slope_peak)

        return sum_candies

if __name__ == '__main__':
    sol = Solution()
    ans = sol.candy([1,0,2])
    print(ans)