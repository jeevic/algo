class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 1:
            return nums
        self.sorted(nums, 0, length - 1)
        return nums

    def sorted(self, nums, lo, hi):
        if lo >= hi:
            return
        p = self.partition(nums, lo, hi)
        self.sorted(nums, lo, p - 1)
        self.sorted(nums, p + 1, hi)

    def partition(self, nums, lo, hi):
        p = lo + (hi - lo)// 2
        lc = 0
        i = lo
        while i <= hi:
            if nums[i] <= nums[p]:
                lc += 1
            i += 1
        newp = lo + lc - 1
        nums[p], nums[newp] = nums[newp], nums[p]

        p = newp
        start = lo
        end = hi
        while start < p:
            if nums[start] > nums[p]:
                while nums[end] > nums[p]:
                    end -= 1
                nums[start], nums[end] = nums[end], nums[start]
            start += 1
        return p


"""
归并排序写法
"""
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums)
        return nums

    temp = []

    def sort(self, nums):
        length = len(nums)
        if length <= 1:
            return nums
        self.temp = [0 for i in range(length)]
        self.sorted(nums, 0, length - 1)

    def sorted(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self.sorted(nums, lo, mid)
        self.sorted(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        if lo == hi:
            return
        i = lo
        while i <= hi:
            self.temp[i] = nums[i]
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