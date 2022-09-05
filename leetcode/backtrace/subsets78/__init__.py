"""
78. 子集
@see https://leetcode.cn/problems/subsets/
"""
from typing import List


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.result = []
        self.result.append([])

        for i in range(1, n + 1):
            self.backtrace(nums, [], 0, i)

        return self.result

    result = []

    def backtrace(self, nums, bucket, start, n):
        if len(bucket) == n:
            self.result.append(bucket.copy())
            return True
        if start >= len(nums):
            return False

        for i in range(start, len(nums)):
            bucket.append(nums[i])
            self.backtrace(nums, bucket, i + 1, n)
            bucket.pop()
        return True
