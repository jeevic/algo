"""
45. 跳跃游戏 II
"""
import sys
from typing import List

"""
动态规划
dp[i] = min(dp[j] + 1)  j=[0...i-1]  j+num[j] > i
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] + [sys.maxsize] * (len(nums) - 1)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[len(nums) - 1]


"""
 贪心算法 
 0..i 可以跳到father远 则在i..father区间就是i..father之间最大值
 
"""


class Solution1:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        farther = 0
        bound = 0
        res = 0
        for i in range(0, n - 1):
            farther = max(farther, i + nums[i])
            if bound == i:
                bound = farther
                res += 1
        return res
