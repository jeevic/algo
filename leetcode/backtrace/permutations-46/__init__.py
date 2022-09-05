"""
46. 全排列
@see https://leetcode.cn/problems/permutations/
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrace([], len(nums), nums)
        return self.result

    result = []
    def backtrace(self, chioces, n, nums):
        if len(chioces) == n:
            self.result.append(chioces.copy())
            return

        for k, v in enumerate(nums):
            c = chioces.copy()
            c.append(v)
            least = nums.copy()
            least.pop(k)
            self.backtrace(c, n, least)
            c.pop()