from typing import List


class Solution:

    def matrix_chain_multiplication_diagonal(self, arr: List[int]) -> int:
        """
        Bottom-up dynamic programming solution for the Matrix Chain Multiplication problem.
        arr: list of matrix dimensions of length n,
             where matrix M_i has dimensions arr[i-1] x arr[i].
        Returns the minimum number of scalar multiplications needed to multiply the chain.
        """
        n = len(arr)
        # dp[i][j] = minimum cost to compute M_i x ... x M_j
        # We only need indices 1..n-1 for i and j, but allocate n x n for simplicity.
        dp = [[0] * n for _ in range(n)]

        # l is chain length (number of matrices in subproblem)
        # we start from l = 2 (two matrices => one multiplication) up to n-1
        for l in range(2, n):
            for i in range(1, n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                # try every possible split point k
                for k in range(i, j):
                    cost = (
                            dp[i][k]  # cost to compute M_i..M_k
                            + dp[k + 1][j]  # cost to compute M_{k+1}..M_j
                            + arr[i - 1] * arr[k] * arr[j]  # cost to multiply the two results
                    )
                    if cost < dp[i][j]:
                        dp[i][j] = cost

        # answer is the cost to multiply M_1 through M_{n-1}
        return dp[1][n - 1]


def matrix_chain_multiplication_tabulation(self, arr: List[int]) -> int:
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            min_cost = float('inf')
            for k in range(i, j):
                cost = (arr[i - 1] * arr[k] * arr[j]) + dp[i][k] + dp[k + 1][j]
                if cost < min_cost:
                    min_cost = cost

            dp[i][j] = min_cost
    return dp[1][n - 1]


def matrix_chain_multiplication(self, arr: List[int]) -> int:
    n = len(arr)
    dp = [[-1] * n for _ in range(n)]

    def dfs(i, j):

        if i == j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        min_cost = float('inf')
        for k in range(i, j):
            cost = (arr[i - 1] * arr[k] * arr[j]) + dfs(i, k) + dfs(k + 1, j)
            if cost < min_cost:
                min_cost = cost

        dp[i][j] = min_cost
        return min_cost  #

    return dfs(1, n - 1)


if __name__ == '__main__':
    s = Solution()
    arr = [5, 4, 6, 2, 7]
    ans = s.matrix_chain_multiplication_diagonal(arr)
    print(ans)
