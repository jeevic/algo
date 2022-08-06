"""
 打家劫舍
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        dp = [0 for _ in range(length + 1)]
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, length + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[length]