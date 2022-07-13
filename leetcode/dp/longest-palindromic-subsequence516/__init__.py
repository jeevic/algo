"""
516. 最长回文子序列
@see https://leetcode.cn/problems/longest-palindromic-subsequence/
"""


class Solution:


    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] 代表i...j的最长子序列长度
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        for i in range(len(s)+1):
            dp[i][i] = 1

        #base case
        i = len(s) - 1
        while i >= 0:
            j = i + 1
            while j < len(s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j - 1], dp[i -1][j-1])
                j += 1
            i -= 1
        return dp[0][len(s)-1]

