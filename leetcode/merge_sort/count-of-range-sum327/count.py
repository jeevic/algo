class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        length = len(nums)
        if length == 1:
            if nums[0] >= lower and nums[0] <= upper:
                return 1
        self.counter = 0
        presums = [0 for i in range(length + 1)]
        self.temp = [0 for i in range(length + 1)]
        presums[0] = nums[0]

        i = 0
        while i < length:
            presums[i + 1] = presums[i] + nums[i]
            i += 1
        self.sorted(presums, 0, length, lower, upper)
        return self.counter

    temp = []
    counter = 0

    def sorted(self, nums, lo, hi, lower, upper):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self.sorted(nums, lo, mid, lower, upper)
        self.sorted(nums, mid + 1, hi, lower, upper)
        self.merge(nums, lo, mid, hi, lower, upper)

    def merge(self, nums, lo, mid, hi, lower, upper):
        i = lo
        while i <= hi:
            self.temp[i] = nums[i]
            i += 1

        start = mid + 1
        end = mid + 1
        i = lo
        while i <= mid:
            while start <= hi and self.temp[start] - self.temp[i] < lower:
                start += 1
            while end <= hi and self.temp[end] - self.temp[i] <= upper:
                end += 1
            self.counter += end - start
            i += 1

        i = lo
        j = mid + 1
        p = mid
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
