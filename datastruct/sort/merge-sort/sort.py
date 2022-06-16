
"""
 归并排序
"""


class MergeSort:

    temp = []

    def sort(self, nums):
        length = len(nums)
        if length <= 1:
            return nums

        self.temp = [0 for i in range(len(nums))]
        self.sorted(nums, 0, length - 1)
        return nums

    def sorted(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2

        self.sorted(nums, lo, mid)
        self.sorted(nums, mid+1, hi)
        self.merge(nums, lo, mid, hi)

        return

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
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1
            p += 1
        return


if __name__ == '__main__':
    arr = [1, 3, 4, 2, 6, 7, 9]

    print(MergeSort().sort(arr))
