"""
309. 最佳买卖股票时机含冷冻期
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0

        dp = [[0, 0] for _ in range(length)]
        for i in range(length):
            if i - 2 == -2:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[length - 1][0]
