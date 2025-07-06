from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            2 3 4
            ["abc"] ["def"] ["ghi"]
            visited =
                   f()
           /        |         \
          f(2,[a])     f(3)       f(4)
        """
        visited = set()
        look_up = { '2' : "abc",
                    '3' : "def",
                    '4' : "ghi",
                    '5' : "jkl",
                    '6' : "mno",
                    '7' : "pqrs",
                    '8' : "tuv",
                    '9' : "wxyz"
                }

        res = []

        def backtrack(idx, temp):
            if len(temp) == len(digits):
                res.append("".join(temp.copy()))
                return

            value = look_up[digits[idx]]
            for ch in value:
                temp.append(ch)
                backtrack(idx + 1, temp)
                temp.pop()

        backtrack(0, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))