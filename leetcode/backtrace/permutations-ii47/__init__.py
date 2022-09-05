"""
47. 全排列 II
@see https://leetcode.cn/problems/permutations-ii/
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrace([], len(nums), nums)
        return self.result

    result = []

    def backtrace(self, choices, n, nums):
        if len(choices) == n:
            if choices not in self.result:
                self.result.append(choices.copy())
                return True

        for k, v in enumerate(nums):
            choices.append(v)
            p = nums.copy()
            p.pop(k)
            self.backtrace(choices, n, p)
            choices.pop()
        return True
