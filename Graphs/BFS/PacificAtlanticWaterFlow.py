from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # pacific

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(row, col, prev_value, isAtlantic):
            if row < 0 or col < 0 or row >= rows or col >= cols or heights[row][col] < prev_value:
                return
            if isAtlantic:
                if atlantic[row][col]:
                    return
                atlantic[row][col] = True
            else:
                if pacific[row][col]:
                    return
                pacific[row][col] = True

            dfs(row + 1, col, heights[row][col], isAtlantic)
            dfs(row, col + 1, heights[row][col], isAtlantic)
            dfs(row - 1, col, heights[row][col], isAtlantic)
            dfs(row, col - 1, heights[row][col], isAtlantic)

        # pacific and atlantic: col-wise
        for row in range(rows):
            dfs(row, cols - 1, -1,True)  # atlantic
            dfs(row, 0, -1,False)  # pacific

        # pacific and atlantic: row-wise
        for col in range(cols):
            dfs(rows - 1, col, -1, True)  # atlantic
            dfs(0, col, -1,False)  # pacific

        res = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res


if __name__ == '__main__':
    sol = Solution()
    ans = sol.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    print(ans)