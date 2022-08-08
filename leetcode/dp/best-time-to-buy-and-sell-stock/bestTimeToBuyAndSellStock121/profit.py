class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = min(prices[i], dp[i-1][0])
            dp[i][1] = max(0, dp[i-1][1], prices[i] - dp[i-1][0])
        return dp[len(prices) - 1][1]