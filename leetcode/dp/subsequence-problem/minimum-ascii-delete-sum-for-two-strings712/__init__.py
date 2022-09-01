"""
712. 两个字符串的最小ASCII删除和
动态规划思路
"""


class Solution:

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        res = 0
        for j in range(len(s2) + 1):
            if j == 0:
                pass
            else:
                res += ord(s2[j - 1])
            dp[0][j] = res

        res = 0
        for i in range(len(s1) + 1):
            if i == 0:
                pass
            else:
                res += ord(s1[i - 1])
            dp[i][0] = res

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1]),
                        dp[i - 1][j - 1] + ord(s1[i - 1]) + ord(s2[j - 1])
                    )

        return dp[len(s1)][len(s2)]
