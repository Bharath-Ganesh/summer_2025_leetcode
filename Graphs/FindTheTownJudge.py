from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(n)]

        for x, y in trust:
            dp[x - 1][y - 1] = 1

        secret_judge_stack = []
        for num in range(n):
            secret_judge_stack.append(num)

        while secret_judge_stack and len(secret_judge_stack) > 1:
            x = secret_judge_stack.pop()
            y = secret_judge_stack.pop()
            # if x trusts y, it means x can't be a judge
            if dp[x][y] == 1:
                secret_judge_stack.append(y)
            else:
                secret_judge_stack.append(x)

        if len(secret_judge_stack) == 0:
            return -1

        curr_col =  secret_judge_stack[0]
        for row in range(n):
            if curr_col == row:
                continue
            if dp[row][curr_col] == 0:
                return -1

        curr_row = secret_judge_stack[0]
        for col in range(n):
            if dp[curr_row][col] == 1:
                return -1
        return curr_row + 1







if __name__ == '__main__':
    s = Solution()
    ans = s.findJudge(3, [[1,2],[2,3]])
    print(ans)