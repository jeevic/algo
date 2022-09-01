"""
714. 买卖股票的最佳时机含手续费
"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        if length <= 0:
            return 0

        dp = [[0, 0] for _ in range(length)]
        for i in range(length):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i] - fee
                continue

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)

        return dp[length - 1][0]
