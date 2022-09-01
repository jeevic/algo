"""
 暴力法
 自顶而下:
    w1 转到 w2 每步无非是替换、删除、新增
    求这个三个最小
"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, len(word1) - 1, word2, len(word2) - 1)

    def dp(self, word1, i, word2, j):
        if j == 0:
            return i + 1
        if i == 0:
            return j + 1

        if word1[i] == word2[j]:
            return self.dp(word1, i - 1, word2, j - 1)

        return min(
            # 替换
            self.dp(word1, i - 1, word2, j - 1),
            # 插入
            self.dp(word1, i, word2, j - 1),
            # 删除
            self.dp(word1, i - 1, word2, j)
        ) + 1


"""
备忘录法 消除重复
自低而上

"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        self.mem = {}
        return self.dp(word1, 0, word2, 0)

    mem = {}

    def dp(self, word1, i, word2, j):
        if j == len(word2):
            return len(word1) - i
        if i == len(word1):
            return len(word2) - j

        if self.mem.get((i, j), None) is not None:
            return self.mem.get((i, j))

        if word1[i] == word2[j]:
            self.mem[(i, j)] = self.dp(word1, i + 1, word2, j + 1)
        else:
            self.mem[(i, j)] = min(
                # 替换
                self.dp(word1, i + 1, word2, j + 1),
                # 插入
                self.dp(word1, i, word2, j + 1),
                # 删除
                self.dp(word1, i + 1, word2, j)
            ) + 1
        return self.mem[(i, j)]


"""
自底而上 动态规划

"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        lw1 = len(word1)
        lw2 = len(word2)

        dp = [[0 for i in range(lw2 + 1)] for j in range(lw1 + 1)]

        # dp[x][y] 代表 word1 前x位到 word2 y位置的操作数
        for i in range(1, lw1 + 1):
            dp[i][0] = i

        for j in range(1, lw2 + 1):
            dp[0][j] = j

        i = 1
        while i <= lw1:
            j = 1
            while j <= lw2:
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        # 替换
                        dp[i - 1][j - 1] + 1,
                        # 删除
                        dp[i - 1][j] + 1,
                        # 新增
                        dp[i][j - 1] + 1
                    )
                j += 1
            i += 1
        return dp[lw1][lw2]
