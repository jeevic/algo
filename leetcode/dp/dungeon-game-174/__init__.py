"""
 174. 地下城游戏
 动态规划 自顶而下写法
"""


class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.mem = {}
        return self.dp(dungeon, 0, 0)

    mem = {}

    def dp(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        if self.mem.get((i, j), None) is not None:
            return self.mem.get((i, j), None)
        if i == m - 1 and j == n - 1:
            return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
        if i == m or j == n:
            return sys.maxsize
        res = min(self.dp(grid, i + 1, j), self.dp(grid, i, j + 1)) - grid[i][j]
        res = res if res > 0 else 1
        self.mem[(i, j)] = res
        return res


"""
自顶而下 动态规划
"""


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[m - 1][n - 1] = 1 if dungeon[m - 1][n - 1] > 0 else -dungeon[m - 1][n - 1] + 1
        for i in range(m - 2, -1, -1):
            res = dp[i + 1][n - 1] - dungeon[i][n - 1]
            dp[i][n - 1] = res if res > 0 else 1
        for j in range(n - 2, -1, -1):
            res = dp[m - 1][j + 1] - dungeon[m - 1][j]
            dp[m - 1][j] = res if res > 0 else 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                res = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = res if res > 0 else 1
        return dp[0][0]
