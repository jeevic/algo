
"""
归并排序
merege进行计算处理
"""


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        i = 0
        self.temp = [0 for i in range(length)]
        while i < length:
            self.temp[i] = nums[i]
            i += 1
        self.counter = 0
        self.sorted(nums, 0, length - 1)
        return self.counter

    temp = []
    counter = 0

    def sorted(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2

        self.sorted(nums, lo, mid)
        self.sorted(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):

        i = lo
        while i <= hi:
            self.temp[i] = nums[i]
            i += 1
        i = lo
        end = mid + 1
        while i <= mid:
            while end <= hi and nums[i] > 2 * nums[end]:
                end += 1
            self.counter += end - mid - 1
            i += 1

        i = lo
        j = mid + 1
        p = lo
        while p <= hi:
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1
            p += 1
        return
