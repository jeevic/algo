class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0

        i = 1
        while i <= amount:
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
            i += 1
        return dp[amount] if dp[amount] != amount + 1 else -1
