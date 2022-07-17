
class Solution:

    '''
        凑出amount总金额最多需要amount个硬币(因为硬币最小面值1元)
        dp[i][j]表示用i个硬币凑出总金额为j的种类有多少
        dp[i][j] += dp[i-1][i-c](c -> coins)
        则结果为:
        res += dp[1...amount+1][amount]
        即:1到amount+1个硬币凑出amount的总和
    '''

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(amount + 1)]
        for i in range(amount + 1):
            dp[0][i] = 0
        for j in range(amount + 1):
            dp[j][0] = 0
        for c in coins:
            dp[1][c] = 1

        for i in range(amount + 1):
            for j in range(amount + 1):
                for c in coins:
                    if j - c < 0:
                        continue
                    else:
                        dp[i][j] += dp[i - 1][j - c]
        res = 0
        for i in range(amount + 1):
            res += dp[i][amount]
        return res


