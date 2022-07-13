
"""
  暴力法
  双循环  超时
"""

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        for k, v in enumerate(nums):
            i = 0
            while i <= k:
                max_num = max(max_num, sum(nums[i:k+1]))
                i += 1
        return max_num


"""
备忘录
    超时
"""


class Solution1:


    def maxSubArray(self, nums: List[int]) -> int:
        dp = {}
        dp[(0, 0)] = nums[0]
        max_nums = dp[(0, 0)]
        i = 1
        while i < len(nums):
            dp[(0, i)] = dp[(0, i - 1)] + nums[i]
            max_nums = max(dp[(0, i)], max_nums)
            j = 1
            while j <= i:
                dp[(j, i)] = dp[(0, i)] - dp[(0, j - 1)]
                max_nums = max(dp[(j, i)], max_nums)
                j += 1
            i += 1

        return max_nums

"""
 动态规划
 dp[i]代表包含 nums[i]的连续序列
 dp[i] = max(dp[i-1] + nums[i], nums[i])
"""


class Solution2:


    def maxSubArray(self, nums: List[int]) -> int:
        dp_i_0 = nums[0]
        max_nums = dp_i_0
        i = 1
        while i < len(nums):
            dp_i_1 = max(dp_i_0 + nums[i], nums[i])
            max_nums = max(dp_i_1, max_nums)
            dp_i_0 =dp_i_1
            i += 1
        return max_nums

"""
 前缀和
 
 res = max(preSum[i] - min(preSum[0..i-1]))
"""


class Solution3:
    
    def maxSubArray(self, nums: List[int]) -> int:
        preSum = [0 for i in range(len(nums) + 1)]
        preSum[0] = 0

        i = 1
        while i <= len(nums):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            i += 1

        min_val = sys.maxsize
        res = preSum[1]
        i = 0
        while i < len(nums):
            min_val = min(min_val, preSum[i])
            res = max(res, preSum[i + 1] - min_val)
            i += 1
        return res
