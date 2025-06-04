class Solution:
    def convert(self, s: str, rows: int) -> str:

        """
            0  1  2  3  4  5  6
        0   P        I        N
        1   A     L  S     I  G
        2   Y  A     H  R
        3   L        I
        How do we compute
        1. row -> 0 -> numRows
        2. rows - 1, col + 1
        """
        row = 0
        col = 0
        total_words = len(s)
        count = 0
        cols = self.findCol(s, rows)
        res = [[' '] * cols for _ in range(rows)]
        while count < total_words:

            while count < total_words and row < rows:
                res[row][col] = s[count]
                count += 1
                row += 1

            row = rows - 1
            while count < total_words and row > 1:
                row -= 1
                col += 1
                res[row][col] = s[count]
                count += 1

            col += 1
            row = 0

        return res
    def findCol(self, s, rows: int):
        col = 0
        total_words = len(s)
        while total_words > 0:

            if total_words > rows:
                col += 1
                total_words -= rows

            min_word = min(total_words, rows - 2)
            col += min_word
            total_words -= min_word
        return col

if __name__ == '__main__':
    sol = Solution()
    ans = sol.convert("PAYPALISHIRING", 4)
    print(ans)

