"""
77. 组合
https://leetcode.cn/problems/combinations/
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        self.result = []
        self.backtrace(nums, 0, [], k)
        return self.result

    result = []

    def backtrace(self, nums, start, bucket, k):
        if len(bucket) == k:
            self.result.append(bucket.copy())
            return True
        if start >= len(nums):
            return False
        for i in range(start, len(nums)):
            bucket.append(nums[i])
            self.backtrace(nums, i+1, bucket, k)
            bucket.pop()

        return True
