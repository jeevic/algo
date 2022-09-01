"""
64. 最小路径和

"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, 1 + m):
            for j in range(1, 1 + n):
                min_pre = 0
                if i - 1 > 0 and j - 1 > 0:
                    min_pre = min(dp[i - 1][j], dp[i][j - 1])
                elif i - 1 == 0:
                    min_pre = dp[i][j - 1]
                else:
                    min_pre = dp[i - 1][j]

                dp[i][j] = grid[i - 1][j - 1] + min_pre
        return dp[m][n]
