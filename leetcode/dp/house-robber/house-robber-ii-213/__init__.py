"""
 打家劫舍2
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        # 第一个不偷的情况下
        dp_0 = [0 for _ in range(length + 1)]
        # 第一个偷的情况下
        dp_1 = [0 for _ in range(length + 1)]
        dp_0[2] = nums[1]
        dp_1[1] = nums[0]

        for i in range(2, length):
            dp_1[i] = max(dp_1[i - 2] + nums[i - 1], dp_1[i - 1])

        for i in range(2, length + 1):
            dp_0[i] = max(dp_0[i - 2] + nums[i - 1], dp_0[i - 1])

        return max(dp_1[length - 1], dp_0[length])
