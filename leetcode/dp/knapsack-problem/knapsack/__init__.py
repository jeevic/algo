"""
背包问题
问题描述:
给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？

N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]

"""


def knapsack(W, N, wt, val):
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 0
    for j in range(W + 1):
        dp[0][j] = 0

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if j - wt[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - wt[i - 1]] + val[i - 1], dp[i - 1][j])
    return dp[N][W]


if __name__ == '__main__':
    N = 3
    W = 4
    wt = [2, 1, 3]
    val = [4, 2, 3]

    value = knapsack(W, N, wt, val)
    print(value)
