"""
55. 跳跃游戏

"""

"""
思路逻辑:
  遍历所有的点, 看每个下标最远的距离  当距离小于等于当前下表 说明跳不过去
  最后比较 最远下标是否大于目标值即可
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)

        farther = 0
        for i in range(length - 1):
            farther = max(farther, nums[i] + i)
            if farther <= i:
                return False

        return True if farther >= length - 1 else False
