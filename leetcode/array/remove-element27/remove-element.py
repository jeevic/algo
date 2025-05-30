from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        q = 0
        length = len(nums)
        while q < length:
            if nums[q] != val:
                if p != q:
                    nums[p] = nums[q]
                p = p + 1
            q = q + 1
        return p
