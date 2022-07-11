
"""
动态规划
自底而上求解

"""


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1 for i in range(length)]

        index = 1
        while index < length:
            j = 0
            while j < index:
                if nums[j] >= nums[index]:
                    j += 1
                    continue
                dp[index] = max(dp[index], dp[j] + 1)
                j += 1
            index += 1
        return max(dp)





"""
暴力法进行求解

"""


class Solution1:

    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1 for i in range(len(nums))]
        self.mem = {}
        for i in range(len(nums)):
            res[i] = self.dp(nums, i)
        return max(res)

    mem = {}

    def dp(self, nums, index):
        if index < 0:
            return 0
        if index == 0:
            return 1

        if self.mem.get(index, None) is not None:
            return self.mem.get(index)

        i = 0
        res = 1
        while i < index:
            if nums[i] >= nums[index]:
                i += 1
                continue
            else:
                res = max(res, self.dp(nums, i) + 1)
            i += 1
        self.mem[index] = res
        return res

