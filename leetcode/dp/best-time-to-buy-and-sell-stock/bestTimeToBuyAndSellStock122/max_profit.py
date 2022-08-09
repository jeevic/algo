"""
122. 买卖股票的最佳时机 II
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 0:
            return 0
        dp = [[0, 0] for _ in range(length)]

        '''
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        '''
        for i, p in enumerate(prices):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[length - 1][0]


"""
 优化版本
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 0:
            return 0
        # dp = [[0,0] for _ in range(length)]

        '''
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        '''
        dp_00 = 0
        dp_01 = float('-inf')
        for i, p in enumerate(prices):
            if i - 1 == -1:
                dp_00 = 0
                dp_01 = -prices[i]
                continue
            temp = dp_00
            dp_00 = max(dp_00, dp_01 + prices[i])
            dp_01 = max(dp_01, temp - prices[i])

        return dp_00
