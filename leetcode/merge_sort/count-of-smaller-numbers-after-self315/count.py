class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 1:
            return [0]

        self.temp = [[0, 0] for i in range(length)]
        self.counter = [0 for i in range(length)]

        arr = [[0, 0] for i in range(length)]
        for k, v in enumerate(nums):
            arr[k] = [k, v]

        self.sorted(arr, 0, length - 1)
        return self.counter

    temp = []
    counter = []

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
        j = mid + 1
        p = lo
        while p <= hi:
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.temp[i]
                self.counter[nums[p][0]] += j - mid - 1
                i += 1
            elif self.temp[i][1] > self.temp[j][1]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                self.counter[nums[p][0]] += j - mid - 1
                i += 1
            p += 1
        return

