from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
            [8]
            side_length = 2
            [2,2,2,2]
            [2,2,1,1,1,1]
        """
        perimeter, max_side_length = 0, 0
        for matchstick in matchsticks:
            perimeter += matchstick
            max_side_length = max(max_side_length, matchstick)
        side_length = perimeter // 4
        if perimeter % 4 != 0.0 or side_length < max_side_length:
            return False

        matchsticks.sort()
        def count_subsequence_with_sum_as_side_length(idx, side, temp):
            if side == 0:
                return 1
            if side < 0 or idx == len(matchsticks):
                return 0

            total_count = 0
            for i in range(idx, len(matchsticks)):
                if i == idx or matchsticks[i] == matchsticks[i - 1]:
                    temp.append(matchsticks[i])
                    total_count += count_subsequence_with_sum_as_side_length(i + 1, temp)
                    temp.pop()

            return total_count

        count = count_subsequence_with_sum_as_side_length(0, side_length, [])
        return True if count == 4 else False




if __name__ == '__main__':
    solution = Solution()
    print(solution.makesquare([1,1,2,2,2]))