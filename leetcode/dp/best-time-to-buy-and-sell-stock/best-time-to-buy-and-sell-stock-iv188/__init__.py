"""
188. 买卖股票的最佳时机 IV
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        max_k = k
        dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(length)]

        for i in range(length):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')

        for i in range(length):
            for j in range(1, max_k + 1):
                if i - 1 == -1:
                    dp[0][j][0] = 0
                    dp[0][j][1] = -prices[i]
                    continue

                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[length - 1][max_k][0]
