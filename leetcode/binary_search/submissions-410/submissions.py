# 410. 分割数组的最大值

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if len(nums) < 1:
            return -1

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if self.splitCount(nums, mid) <= m:
                right = mid
            elif self.splitCount(nums, mid) > m:
                left = mid + 1
        return left

    def splitCount(self, nums, mid):
        cnt = 0
        sums = 0
        for val in nums:
            if sums + val > mid:
                cnt += 1
                sums = val
            elif sums + val == mid:
                cnt += 1
                sums = 0
            else:
                sums += val
        if sums > 0:
            cnt += 1
        return cnt
