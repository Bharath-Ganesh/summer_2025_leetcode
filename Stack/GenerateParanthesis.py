from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def back_track(open_brackets, close, temp):
            if open_brackets == n and close == n:
                res.append(''.join(temp))
                return
            if open_brackets > n or close > open_brackets:
                return

            if close < open_brackets:
                temp.append(')')
                back_track(open_brackets, close + 1, temp)
                temp.pop()
                temp.append('(')
                back_track(open_brackets + 1, close, temp)
                temp.pop()
            else:
                temp.append('(')
                back_track(open_brackets + 1, close, temp)
                temp.pop()

        back_track(0, 0, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))