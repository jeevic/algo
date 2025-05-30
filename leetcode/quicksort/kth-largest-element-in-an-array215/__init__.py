
from typing import List


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if length <= 0:
            return 0

        lo = 0
        hi = length - 1
        ps = length - k
        while lo <= hi:
            p = self.partition(nums, lo, hi)
            if p == ps:
                return nums[p]
            elif p > ps:
                hi = p - 1
            elif p < ps:
                lo = p + 1
        return 0

    def partition(self, nums, lo, hi):
        mid = lo + (hi - lo) // 2
        i = lo
        lc = 0
        while i <= hi:
            if nums[mid] >= nums[i]:
                lc += 1
            i += 1
        new_mid = lo + lc - 1
        nums[new_mid], nums[mid] = nums[mid], nums[new_mid]
        mid = new_mid

        start = lo
        end = hi
        while start < new_mid:
            if nums[start] > nums[new_mid]:
                while nums[end] > nums[new_mid]:
                    end -= 1
                nums[start], nums[end] = nums[end], nums[start]
            start += 1
        return mid
