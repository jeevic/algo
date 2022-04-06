from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        last = 0
        length = len(nums)

        while last < length:
            if nums[last] != 0:
                if last - head > 1:
                    nums[head] = nums[last]
                head = head + 1
            last = last + 1

        while head < length:
            nums[head] = 0
            head = head + 1
        return None
