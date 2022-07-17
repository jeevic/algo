"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n_sums = sum(nums)
        if n_sums % 2 != 0:
            return False
        half_sum = n_sums // 2

        # dp[i][j] == 最大值
        dp = [[0 for _ in range(half_sum + 1)] for _ in range(len(nums) + 1)]
        for j in range(half_sum + 1):
            dp[0][j] = 0

        for i in range(len(nums) + 1):
            dp[i][0] = 0

        for i in range(1, len(nums) + 1):
            for j in range(1, half_sum + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j - nums[i - 1]] + nums[i - 1],
                        dp[i - 1][j]
                    )
        if dp[len(nums)][half_sum] == half_sum:
            return True
        return False
