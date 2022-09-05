"""
698. 划分为k个相等的子集
@see https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
@see https://labuladong.github.io/algo/4/31/106/
"""
from typing import List

"""
按照桶的视角进行回溯选择
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n_sum = sum(nums)
        if n_sum % k != 0:
            return False
        # 排不排序都不重要
        nums.sort(reverse=True)
        self.mem = {}
        target = n_sum / k
        bucket = [0 for i in range(k)]
        used = 0
        return self.backtrace(k, 0, nums, 0, used, target)

    mem = {}

    def backtrace(self, k, bucket, nums, start, used, target):
        if k == 0:
            # all bucket is full
            return True
            # bucket equal target
        if bucket == target:
            res = self.backtrace(k - 1, 0, nums, 0, used, target)
            self.mem[used] = res
            return res

        if self.mem.get(used, False):
            return self.mem.get(used, False)

        for i in range(start, len(nums)):
            if used >> i & 1 == 1:
                continue
            if nums[i] + bucket > target:
                continue
            used |= 1 << i
            bucket += nums[i]
            if self.backtrace(k, bucket, nums, i + 1, used, target):
                return True
            used ^= 1 << i
            bucket -= nums[i]
        return False


"""
已nums视角选择桶插入
"""


class Solution2:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 按照nums视角进行遍历
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        nums.sort(reverse=False)
        target = sum_nums / k
        bucket = [0 for i in range(k)]
        if self.backtrace(nums, 0, bucket, target):
            return True
        return False

    # 回溯算法
    def backtrace(self, nums, start, bucket, target):
        if start >= len(nums):
            for v in bucket:
                if v != target:
                    return False
            return True

        for k, v in enumerate(bucket):
            if bucket[k] + nums[start] > target:
                continue
            bucket[k] += nums[start]
            if self.backtrace(nums, start + 1, bucket, target):
                return True
            bucket[k] -= nums[start]
            if bucket[k] == 0:
                break

        return False