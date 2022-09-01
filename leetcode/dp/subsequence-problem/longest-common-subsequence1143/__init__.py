"""
最长子序列
"""

"""
暴力法+备忘录
两个指针游走s1，s2  i, j 代表在 i,j 处情况 

"""


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.mem = {}
        return self.dp(text1, 0, text2, 0)

    mem = {}

    def dp(self, text1, i, text2, j):
        if i == len(text1):
            return 0
        if j == len(text2):
            return 0
        if self.mem.get((i, j), None) is not None:
            return self.mem[(i, j)]
        if text1[i] == text2[j]:
            self.mem[(i, j)] = 1 + self.dp(text1, i + 1, text2, j + 1)
        else:
            self.mem[(i, j)] = max(
                self.dp(text1, i + 1, text2, j),
                self.dp(text1, i, text2, j + 1)
            )
        return self.mem[(i, j)]


"""
  动态规划写法
  自底而上 
  
"""


class Solution1:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1) + 1):
            dp[i][0] = 0
        for j in range(len(text2) + 1):
            dp[0][j] = 0

        i = 1
        res = 0
        while i < len(text1) + 1:
            j = 1
            while j < len(text2) + 1:
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                res = max(res, dp[i][j])
                j += 1
            i += 1
        return res
