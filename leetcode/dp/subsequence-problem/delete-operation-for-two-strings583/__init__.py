
"""
动态规划 雷同最长子序列

"""

class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        i = 1
        while i <= len(word1):
            j = 1
            while j <= len(word2):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 2
                    )
                j += 1
            i += 1
        return dp[len(word1)][len(word2)]
